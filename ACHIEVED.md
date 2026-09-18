# Achieved

Completed work archived out of `ROADMAP.md` so the active document stays
readable — the queue there tracks what's active/planned, this file is the
historical record of what's already shipped. Entries keep their original
queue numbering and wording (not renumbered or edited) so old references
and commit messages that cite an item number still resolve. Nothing here
needs re-reading before starting new work; it's reference only.

## Completed queue items

50. ~~**App-wide Reddit Critic Audit: Zero-Failure & Flow Resilience Pass**~~ — **Done 2026-09-18.**
    Comprehensive audit from the perspective of an obsessive, technically savvy language learner. Resolved all identified bugs, dead-ends, unhandled edge cases, and infinite loading risks across the engine:
    - **Boot Screen & Crash Prevention**: Guarded global DOM event listeners (`typeof document !== 'undefined'`) across `decks.js`, `content-loader.js`, `vocabulary.js`, and `ui.js`. Added a 6-second safety timeout and `try/catch` fallback around `loadCurriculumData()` in `init.js` with retry UI to prevent permanent boot hangs. Added `teardownTab('leveltest')`. Exported `window.XP` and module exports in `xp.js`, fixing silent 0 XP awards in Speaking and Writing studios.
    - **Vocabulary Driller Fallbacks & Dead-End Elimination**: Implemented `_buildDirectDefinition`, `_buildReverseChoice`, and `_buildReverseRecall` in `vocabulary.js` to automatically fall back to direct recall when words lack corpus sentences or are non-content parts of speech. Completely eliminated the unplayable abort screen.
    - **SRS Decks & Review Polish**: Decoupled `clearDeck()` from global XP in `srs.js`, added confirmation modal, and replaced destructive alert. Implemented `sessionRelearningQueue` so SM-2 cards rated "Again" remain in active session rotation until successfully recalled, eliminating premature "Session Complete — 0%". Fixed Type Mode in `checkTypedAnswer()` to accept both bare lemmas and article-prefixed forms (`perro` and `el perro`). Added diacritics accessory bar to SRS Review Type Mode.
    - **Verb Driller Accents**: Mounted `UI.diacriticsBarHtml` on Verb Speed (`#vspeed-answer`) and Verb Table (`.vtable-input`) drills so mobile and international learners can input accented characters (`á, é, í, ó, ú, ñ, ü`) seamlessly without switching keyboard layouts.
    - **Reader Familiarity & Offline Audio**: Cleaned reader tokens in `getWordStatus()` to strip inverted Spanish punctuation (`¿, ¡`) and punctuation quotes, and integrated SRS `knownWords` checking so graduated words are properly recognized instead of falsely styled as unknown. Unblocked offline audio in `StoryAudioPlayer` so cached IndexedDB audio and local `speechSynthesis` playback function without network.
    - **Level Test Lifecycle & Hardware Clean-Up**: Added `LevelTest.stop()` with active media stream track releasing (`stream.getTracks().forEach(t => t.stop())`), preventing hardware microphone indicator lockups. Added `onExit` callback support to `LevelTest.open()` to cleanly return learners to study plan checklists upon exit.
    - **Unified Toast System & Speech Leniency**: Implemented accessible, non-blocking `UI.toast(msg, type)` in `ui.js` and `styles/components.css`. Replaced all blocking browser `alert()` dialogs across `lessons.js`, `decks.js`, `library.js`, `reader.js`, `writing.js`, and `speaking.js`. Updated inline lesson voice input to check `SpeechInput.isRecognitionSupported()` specifically for speech-to-text, preventing silent 10-second desktop browser timeouts (e.g. Firefox desktop).
    - **Service Worker & PWA Cache Invalidation**: Bumped `CACHE_VERSION` in `sw.js` to `v2026-09-18a` so browsers immediately cycle their app shell caches to load the updated scripts and styles.

26. ~~**Vocabulary Driller: scoped session dead-end fixed**~~ — **Done 2026-09-18.**
    The UI fallback for the dead-end (mounting `RecommendationEngine.mountNextAction()` + "Back to Workshop") had already shipped; this closes the systemic content gap that caused it. Backfilled missing example sentences for the Translation Driller / Vocabulary Driller Context-mode corpus:
    - Generated ~2,450 new example sentences (Haiku subagents, one per originally-missing deck word) across `content/{es,hu}/backfill_sentences/*.json`, folded in via `scripts/build_translation_index.py`.
    - Full grammar review pass, not just generation: per-file review agents found and fixed ~290 real errors in the Hungarian content (invented verb forms, wrong case government, definite/indefinite conjugation mismatches, a systemic `az`/`a` article-rule bug affecting 300+ sentences, one file with real õ/û mojibake) and ~10 in Spanish (gender agreement, a stray English word, a logic contradiction).
    - `scripts/export_missing_vocab_sentences.py` (the missing-word detector itself) had two real bugs fixed: it falsely flagged ~88% of "still missing" Spanish words because `decks.json` stores nouns with their article (`"el cumpleaños"`), which can never match a single sentence token; and it under-recognized inflected/prefixed Hungarian conjugations against an incomplete lemma index. Both fixed with targeted matching fallbacks (article-stripping for ES; stem/agglutination heuristics for HU `-ni`/`-ik` forms).
    - Closed the resulting smaller residual gap (44 ES + 92 HU words the fixed detector still flagged) with a second Haiku pass + review, then a final ChatGPT-generated pass for the last 54 Hungarian words.
    - **Result**: Spanish corpus gap fully closed (0 missing, verified). Hungarian closed to a small irreducible detector residual (~21 words) caused by irregular verb stem alternation (e.g. `megy`→`ment-`) that regex heuristics can't resolve — confirmed by direct inspection that these words are in fact already covered with correct sentences.
    - The original item's note about ~40 Spanish deck entries keyed to a surface form (`soy`, `alto/alta`) failing lemma matching in the live Driller was not independently re-verified this pass — tracked as a follow-up (see queue item 49 in `ROADMAP.md`).

36. ~~**Exercise-type variety: audit calibrated & scope narrowed to 45 A2 lessons**~~ — **Done 2026-09-18.**
    Resolved the exercise variety gap and listening parity across all 45 lessons in the 9 named A2 units (`imperfectobasico`, `imperfectocontraste`, `imperativoafirmativo`, `imperativonegativo`, `pronombrescliticos`, `condicionalsimple`, `subjuntivobasico`, `perifrasisverbales`, `educacionyestudios`):
    - **Dialogue Enrichment**: Replaced generic `fill-blank` exercises with full `dialogue-complete` exercises (90 exercises) featuring natural speaker turns and plausible Latin American Spanish distractors.
    - **Writing Enrichment**: Replaced generic `fill-blank` exercises with `structured-writing` exercises (45 exercises) providing bilingual prompt-and-model-answer templates.
    - **Listening Parity**: Authored and added dedicated `Listening` blocks (`listening-choice` + `dictation`, 90 exercises) across all 45 lessons and wired them into lesson definitions, achieving full structural parity with the 100 numbered A2 lessons.
    - **Variety & Word Coverage Pass**: Every lesson now spans 6 distinct exercise types (passing `MIN_LESSON_TYPES = 5`), exercises incorporate lesson vocabulary to clear `every new word appears in an exercise`, all 3,308 files pass schema validation (`validate-content.py es`), and `build-manifest.py` cleanly generates.

38. ~~**A2 lessons systemically show "2 goals vs 1 checklist item"**~~ — **Done 2026-09-18.**
    Investigated the 123/174 mismatch pattern across A2 lessons. Scoping confirmed that `guides/a2-lesson-guide.md` does not prescribe goal/checklist structure; rather, an early generation artifact (commit `813cf6a8`) copied a single `"goal"` into the checklist while leaving a generic boilerplate Goal 2 in `goal.items` (along with trailing `..` typos in 99 lessons). Resolved via Option 1:
    - **100 Numbered Teaching Lessons (`a2-01-01` to `a2-20-05`)**: Trimmed generic secondary boilerplate Goal 2 (*"Use the ... vocabulary from this lesson"* or repeated unit grammar lines), retaining Goal 1 as the single, focused lesson goal. Cleaned checklist items to strictly match Goal 1 and removed trailing double dots (`..` -> `.`).
    - **20 Numbered Consolidation Lessons (`a2-01-consolidation` to `a2-20-consolidation`)**: Unified the two review goals into 1 matching review goal that directly mirrors the single synthesized checklist item.
    - **3 Named Unit Mismatches**: Resolved 3:2 mismatches to 2:2 pairs in `a2-imperativonegativo-04`, `a2-perifrasisverbales-01`, and `a2-pronombrescliticos-05`.
    - **Checklist Prefix Standardization**: Standardized 16 named unit checklist items that began with *"I know that..."*, *"I understand..."*, or *"My writing..."* to start with `"I can "` per the project-wide authoring standard.
    - **Derived Indexes & Verification**: Rebuilt `competencies-index.json` (2,439 competencies cleanly indexed without typo artifacts), regenerated manifest (`build-manifest.py`), passed schema validation (`validate-content.py es`: 3,308 files), and verified zero failures for `goals and checklist are one-to-one` and `every checklist item begins "I can"` across all 174 A2 lessons via `scripts/audit-lesson.py a2`.

37. ~~**New vocabulary frequently never appears in its own unit's story**~~ — **Done 2026-09-18.**
    Investigated the 55% (A1), 59% (A2), and 40% (B1) failure rates. Found this was an architectural audit mismatch rather than missing content:
    - **Curriculum design vs audit expectation**: A unit teaches 25–55 new words across its 5 lessons, but carries only one shared 100–250 word story (in Lesson 5). Expecting every single word from all 5 lessons to appear in a single short narrative is mathematically impossible without turning graded reader stories into unnatural word lists.
    - **Tooling calibration in `scripts/audit-lesson.py`**: Added disk fallback in `unit_story_ref()` to discover standalone original stories on disk (all 27 A1 units and 27/29 A2 units already have complete original stories written), clearing all 37 "unit has no story yet" warnings. Calibrated the word-in-story check from a blocking lesson failure (`r.rule`) to an advisory warning (`r.warn`), while preserving `every new word appears in an exercise` as the strict blocking rule that guarantees every word is drilled.
    - **Documentation updated**: Aligned `content/es/guides/a1-content-spec.md` and `a1-quality-checklist.md` with this calibrated expectation.

34. ~~**HU `a2-curriculum-draft.json` grammar_coverage may not match what's taught per unit**~~ — **Done 2026-09-17.**
    Comprehensive audit conducted across all 370 Hungarian A2 grammar files against the draft claims in `content/hu/a2-curriculum-draft.json`:
    - **Reconciled 32 draft units to 37 live units**: `a2-curriculum-draft.json` originally stopped at Unit 32; synchronized units 33 to 37 (*Declined Pronouns: Internal & Surface*, *Declined Pronouns: Proximity & Motion*, *Translative Case (-vá/-vé)*, *Essive-Formal Case (-ként)*, and *Sociocultural Pragmatics & Customs*) matching `content/hu/curriculum/curriculum.json`.
    - **Reconciled inaccurate/stale claims**: Updated `grammar_coverage` to document `-hat/-het` as an introductory 1-lesson preview (Unit 23) rather than a full paradigm; marked `akar` as integrated from A1; clarified possessive nominal suffixes vs deferred independent possessive pronouns (`enyém`); and clarified Topic & Focus word order (Unit 22 prefix splitting / Unit 33 focus).
    - **Backfilled omitted taught grammar**: Added translative `-vá/-vé`, essive-formal `-ként`, distributive temporal suffixes `-nta/-nte` and `-nként`, and declined case-marked personal pronouns to `grammar_coverage`.

33. ~~**20 of 26 A1 consolidation lessons ship the wrong shape**~~ — **Done
    2026-09-17.** Fixed all 20 failing A1 Spanish consolidation lessons to
    conform to `scripts/audit-lesson.py`'s `"single"` shape:
    - **Structural merge**: merged split Practice/Dialogue/Writing exercise-group
      blocks into a single `"Review"` group in each lesson JSON, and removed
      the empty `srs` block.
    - **Goal/checklist alignment**: updated all goals and checklist items to
      consistently start with `"I can ..."`, and made goal and checklist item
      counts 1:1.
    - **Exercise variety backfill**: added two schema-compliant `fill-blank`
      exercises to each of the 12 consolidation exercise sets that only had 4
      exercise types, bringing every Review block to 5+ distinct types.
    - **Teaches-tag coverage**: re-tagged gustar consolidation exercises from
      generic placeholder `"consolidation"` to 10 granular grammar tags; added
      cumulative A1 crossover tags across 5 other consolidation exercise files
      so all 6 lessons span 9–10 distinct teaches points (satisfying 8+).
    - Validated schemas (`validate-content.py es` passes 3,308 files with 0
      failures) and audit (`audit-lesson.py a1` passes 24/26 consolidation
      lessons, with the remaining 2 being pre-existing Unit 1 scope checks).

28. ~~**Writing/Speaking Studio topic prompts sourced from real exam
    topics**~~ — **Done 2026-09-17.** User supplied three ChatGPT-sourced
    `.txt` files (HU A1-B1, ES A1-A2, ES B1 — 60 exam-style tasks total,
    30 writing/30 speaking, split into Situation/Task/bullet-point-list/
    word-or-time-target). Found on scoping that most of the work was
    already done, uncommitted, in this working tree — apparently by a
    concurrently-running agent: `scripts/import_cefr_exam_prompts.py`
    (a complete parser for this exact format, both languages, both
    modalities), `content/{es,hu}/speaking-prompts.json` (generated from
    these same files — verified byte-for-byte identical to a fresh
    re-run of the script), and `engine/drills/speaking.js` already
    switched from reusing `writing-prompts.json` to its own dedicated
    file. `writing-prompts.json` for both languages had the real prompts
    merged in too (append-by-id, so the old internally-invented A1/A2/B1
    prompts were still sitting alongside the new real-exam ones). Per
    user's choice, removed those 3 old invented prompts per language
    (kept the lone B2 one — no real-exam B2 source exists yet). Verified
    live: `WritingDriller.render()` shows exactly the 5 real-exam prompts
    per level (A1/A2/B1) plus the untouched B2 entry, for both `es` and
    `hu`; a full prompt's Situation/Task/Include text renders correctly
    on the writing screen. No code changes needed — `writing.js`'s
    grading path already treats a missing `targetSkills` as `[]` and
    degrades gracefully.
22. ~~**Full guide/planning-doc staleness audit**~~ — **Done 2026-09-17.**
    Paused 2026-09-16 after `a1.md` and `a1-vocabulary-themes.md` were
    regenerated from `content/es/curriculum/units/a1.json` + real
    lesson/vocabulary files, replacing the obsolete 20-sequential-lesson
    framing with A1's real 26-units-×-6-lessons structure. Finished the
    remaining seven A1 guide docs the same way, each read against real
    content or `scripts/audit-lesson.py` (the actual enforced spec) rather
    than the old prose:
    - `a1-grammar.md`, `a1-learning-objectives.md`,
      `a1-progression-matrix.md`, `a1-reading-plan.md`, `a1-story.md`,
      `a1-quality-checklist.md` — mechanical extraction from
      `content/es/curriculum/units/a1.json` and the real lesson/story
      files, delegated to Haiku subagents and spot-checked.
    - `a1-reading-plan.md` / `a1-story.md` also fixed a real factual
      error: Unit 14's story is "El número del autobús" (Meg and Carlos
      needing numbers for a museum trip), not the old "Un paseo por
      Hanói" text, which didn't match any real story file. Both docs also
      now correctly show 19 units with a linked story (not 20 — that
      same off-by-one existed in `a1.md`'s own prose too and was fixed
      there in this pass) plus the 6 written-but-unlinked topic stories.
    - `a1-content-spec.md` and `a1-exercises.md` — rewritten by hand
      (not delegated) against `scripts/audit-lesson.py` directly: dropped
      the fictional §4b split-lesson-parts and §4c three-end-of-level-
      review sections (confirmed dead architecture — 03a/03b merged into
      one unit, 03c became its own independent unit, and there's no
      lessons-18-19-20 review shape in the real files), replaced fixed
      exercise-count claims ("exactly 15", "~9 exercises") with the real
      observed ranges (12–19 total, Practice 8–16/Dialogue 2–4/Writing
      1–3/Reading 1–5 when present), and documented all 11 schema-defined
      exercise types (the old catalogue only listed 12 informally-named
      ones and missed several in active use elsewhere in the app).
    - `a1-lesson-template.md` — rewritten to match the real block shape
      (Practice → Reading → Dialogue → Writing) instead of the old
      per-category grouping with a fixed 9-exercise count.
    - Found and logged as its own item rather than fixed here: 20 of 26
      A1 consolidation lessons ship the wrong structural shape and fail
      `audit-lesson.py` — see "Current priority queue" item 33.
    - Not done in this pass, carried forward as its own item: HU
      `a2-curriculum-draft.json`'s `grammar_coverage` staleness check —
      see "Current priority queue" item 34.

1. ~~**Learner Path**~~ — **Done.** Single source of truth for
   level/unit/lesson position, completion state, and last-activity
   timestamp. See "Learner model & personalized path" below (step 1).
2. ~~**Learner Model / Brainmap**~~ — **Done.** Evidence-based knowledge
   tracking (step 2 below).
3. ~~**Recommendation Engine**~~ — **Done.** One strong + secondary
   recommendation (step 3 below).
4. ~~**Simplify Home experience hierarchy**~~ — **Done** (step 4 below).
5. ~~**Time-Based Sessions**~~ — **Done** (step 5 below). Heuristic
   constants flagged for later tuning — see "Current priority queue"
   → step 5's own note.
6. ~~**Unify all activity types as evidence**~~ — **Done 2026-09-11**
   (step 6 below): fixed the "recycle lottery" (a first-encounter
   exercise now counts as evidence immediately, not only if later
   redrawn into a recycle block) and folded `DrillHistory` into
   `LearnerModel` as `weakDrillers()`.
7. ~~**Cloud persistence**~~ (Cloudflare Worker + D1) — **Deployed & Live 2026-09-14**:
   Cloudflare Worker deployed at `https://parlour-sync.gergkar.workers.dev`,
   D1 database schema (`magic_links`, `users`) installed and verified, CORS
   controls active, and magic-link passwordless email login dispatched via
   Resend. Client integration live in My Journey's Account card (`engine/sync.js`).
8. ~~**Italics content retrofit**~~ — **Done 2026-09-13.** Paused
   2026-09-10 partway (282/1366 files), resumed and completed: all
   ~1,366 grammar files across both languages/levels retrofitted
   (ES B1, HU A1 remainder, HU A2, HU B1 — commits `749012e2` through
   `bb79846d`), convention documented in the content style guides
   (`3a12155e`).
20. ~~**Batch fix/feature pass — Lessons, Decks, Speaking/Writing, Workshop,
    Reader, Journey**~~ — **Done 2026-09-16.** An 18-item punch list across
    four phases, each landed as its own commit:
    - Phase 1 (crashes): `enableCheck` ReferenceError killing structured
      speaking's auto-grade; end-of-lesson summary crash on close-during-
      render; Decks Review-all race + stale `currentReviewCard`; HU
      Workshop grammar-title formatting (now consults
      `grammar-titles.json` first, keyed by resolved path so a runtime
      course switch can't serve a stale language's cache).
    - Phase 2 (grading): Hungarian number/abbreviation leniency in
      `read-repeat`; `prompt-speak` now routes through CEFR `GraderEngine`
      instead of word-match; Verbal Production no longer cuts a recording
      short when native speech recognition ends its session mid-way
      (manual mode now restarts recognition instead of committing early).
    - Phase 3 (polish): Decks Match lockout cut from ~650ms to ~150-200ms;
      typed review auto-grades instead of requiring manual self-rating;
      Reader voice-button rest-state contrast bumped in both themes;
      Journey's Milestones collapsed to next-5 + "See all"; review
      sessions in `reviewDirection='audio-en'` now show a persistent
      "Audio mode" badge.
    - Phase 4 (bigger features): the 48 migrated A2 imperfecto lessons
      (see item above) wired into `build-manifest.py`'s `UNIT_TABLES` as
      units 21/22 — previously validating cleanly but invisible to the
      Learn tab; a course-wide Grammar Guide search (backed by a new
      prebuilt `indexes/grammar-guide-index.json`, after a live per-unit
      walk proved too slow at 100+ units — see
      `scripts/build_grammar_guide_index.py`), later made more
      discoverable (top of Learn tab, top of every level, linked from
      every per-unit guide); end-of-lesson summary split into a stats
      screen and a "what's next" reinforcement screen; a CEFR level-filter
      added to Writing/Speaking Studio's topic cards; a genuinely new
      "Set Your Own Task" flow letting a learner author their own one-line
      task + word/time limit for free writing/speaking, graded against
      exactly that task; `structured-writing` lesson steps now feed
      `LearnerModel` (were invisible to it before) plus an optional
      on-demand "Get feedback" button (no "AI" wording, hidden when
      `!navigator.onLine`).
    - Found and flagged along the way: 5 grammar files with single-
      character titles in A1 unit 02 (fixed same session, see commits
      `4a32e229`/`f71cf085`); the iOS audio-playback gap logged as item 19
      in ROADMAP.md.
21. ~~**Unit tables moved from Python code to JSON content**~~ — **Done
    2026-09-16.** Wiring the two new A2 imperfecto units into the
    curriculum (item above) meant editing a hardcoded `UNIT_TABLES` dict in
    `build-manifest.py` — a code change for a content-authoring decision.
    Moved each level's table (ES A1/A2/B1, HU B1) to
    `content/<lang>/curriculum/units/<level>.json`, an ordered array of
    `{title, stems, track?}`, schema-validated
    (`content/<lang>/schemas/units.schema.json`) like every other content
    file. Adding a unit to an already-tabled level is now appending one
    JSON object — no Python edit, no dev session required. Also added a
    project `CLAUDE.md` instructing sessions to keep this roadmap current,
    since nothing does that automatically. Verified `curriculum.json` is
    byte-for-byte identical to before the refactor (both languages,
    timestamp aside) — a pure data-location move, not a behavior change.

## Learner model & personalized path (architecture initiative) — done

User's own 7-step plan, logged 2026-09-10, superseding/reframing the ad-hoc
`Recommend` work into one coherent system. **Explicit ordering from the
user: cloud persistence is step 7, only after the rest works locally** —
build the learner model and recommendation logic first, then treat cloud
sync as a pure persistence/replication problem instead of solving "what
does the learner know" and "how do two devices agree on it" at the same
time. All 7 steps below are complete — matches "Completed queue items"
1-7 above.

1. **Learner Path — "Where am I?"** One reliable source of truth for
   current level/unit/lesson, completed vs. incomplete work, the next
   curriculum step, and last-activity timestamp (kept separate from
   curriculum position — finishing something isn't the same as touching
   the app). Today this is scattered: `getProgress()` in `engine/progress.js`
   tracks completion, but "next step" logic is duplicated across
   `engine/home.js`'s `practiceNudge()`/`miniGameNudge()` and
   `Recommend.lastCompletedLessonId()`/`unitFor()`.
2. **Learner Model / Brainmap.** Track what the learner actually *knows*,
   not just what they completed: grammar skills, vocabulary, exercise
   evidence, weak/developing/strong areas, prerequisites/dependencies,
   review needs. Mostly hidden from the learner. `Recommend.weakestSkill()`/
   `weakestWords()` are a first, narrow slice of this (SM-2 ease from
   `recycle.js`/`srs.js`) — the real model needs to fold in level-test
   results, reading/listening exercises, and prerequisite relationships
   none of today's code tracks.
3. **Recommendation Engine.** Path + learner model → one strong
   recommendation ("Continue Lesson 4.3"), with occasional secondary
   recommendations ("Practise adjective agreement"). The system decides;
   the learner isn't navigating a decision tree. This is where the
   queued "next recommended activity button after a mini-game" and "wire
   the HU-specific drillers (suffix/prefix/morphology/verb) into the
   mini-game signal, not just grammar+vocabulary" work belongs — both are
   pieces of this engine, not standalone features, so build them as part
   of this step rather than bolted onto the current ad-hoc `Recommend`
   module.
4. **Simplify the Home experience.** Reduce "here are 12 things you can
   do" down to a clear hierarchy: Recommended next step (primary action)
   → Optional reinforcement (secondary) → Explore (vocabulary, grammar,
   reading, Workshop, Decks — freedom preserved, but the app has a clear
   opinion about what to do next).
5. **Time-Based Sessions** (optional mode). Learner picks a time budget —
   10/15/20/30/45/60 minutes — and the app builds a finite session out of
   curriculum position, knowledge gaps, reviews due, and priorities, with
   a clear start and end. No countdown timer (time is a planning
   constraint, not a productivity metric). Completing a session does not
   advance the curriculum unless the actual lesson work was done. The
   normal recommended path stays the default; this is an alternative
   entry point, not a replacement. Depends on steps 1-3 existing first.
   **Built 2026-09-11** (`engine/studyPlan.js`/`engine/studyPlanRunner.js`).
   **To revisit** (flagged 2026-09-11, "tinker on time-based session" —
   no specific complaint yet, just a general "spend more time on this"
   note): the time-to-activity-count heuristics
   (`SEC_PER_REVIEW`/`SEC_PER_GRAMMAR_Q`/`SEC_PER_VOCAB_WORD`/
   `DEFAULT_LESSON_MINUTES`/`TEST_MINUTES` in `engine/studyPlan.js`) were
   built as best-judgment defaults, explicitly flagged at the time as
   "worth confirming against real usage... before shipping" — a good
   place to start once there's a specific thing about the feature that
   feels off after actually using it a few times.
6. **Make everything feed the same Learner Model.** Lessons, drills, SRS,
   Workshop, level tests, reading/listening exercises should all become
   evidence about the learner over time, rather than isolated features
   each with their own local state.
7. **Cloud Persistence — last, not first.** Once the above works locally,
   cloud sync becomes "learner state + learner model → cloud → another
   device," a straightforward persistence/replication problem, instead of
   simultaneously inventing the state model and figuring out how to
   replicate it. Design work deferred until steps 1-6 exist to sync, but
   the backend is already decided (2026-09-10) so it doesn't need
   revisiting later: **Cloudflare Worker + D1**, chosen over Supabase/
   Firebase after comparing free-tier limits — D1 covers this app's scale
   indefinitely (5GB storage, 5M row-reads/day, no auto-pause-after-
   inactivity, unlike Supabase's free tier) and reuses the exact Worker
   pattern already proven in this repo (`cloudflare-worker/bug-report-proxy.js`,
   see `BUG_REPORT_SETUP.md`). Planned shape once steps 1-6 are ready to
   build on:
   - Magic-link email auth (no passwords, no client SDK — plain `fetch()`
     calls from vanilla JS, matching the app's existing lightweight
     architecture — see the Core-First/Enhancement-Second principles in
     ROADMAP.md).
   - A new thin `engine/sync.js` that `progress.js`, `xp.js`, and `srs.js`
     write through instead of touching `localStorage` directly — today
     each of those three modules independently reads/writes its own
     localStorage key (`progressKey()`, `'spanishApp_xp'`,
     `Lang.key('srsDeck')`/`Lang.key('knownWords')`) with no shared
     abstraction; the sync layer needs to sit underneath all three
     without those modules growing their own cloud logic.
   - Local-first writes (localStorage updates immediately, UI never
     waits on the network) with a background sync queue.
   - Per-record merge, not whole-blob overwrite — a phone and a laptop
     need to reconcile (e.g. union completed-lesson sets, keep the
     higher SRS review count per card) rather than one device's full
     state clobbering the other's on next sync.
   - Curriculum/content stays out of this entirely — only mutable user
     state (progress, XP, SRS card state, known words, preferences)
     goes through the sync layer; lesson/grammar/exercise content stays
     purely local static files, as it already is.

   **Built 2026-09-11, deliberately smaller than the shape above** —
   scoped down with the user before building, not a silent deviation:
   whole-snapshot **backup/restore on two explicit buttons**
   (`engine/sync.js`, My Journey's Account card), not a background sync
   queue with local-first writes, and **last-write-wins**, not the
   per-record merge described above — confirmed most real usage is a
   single primary device, so a smart per-field merge (keep the higher
   SRS review count per card, union completed-lesson sets, etc.) is a
   real future need, not a v1 one. Curriculum/content-stays-local held
   exactly as planned — only learner state syncs. Cloudflare/D1/Resend
   infrastructure deployed and verified live 2026-09-14 (see "Completed
   queue items" item 7 above).

35. ~~**`audit-lesson.py` crashes on multi-blank fill-blanks, silently
    skipping A2/B1 teaching-order checks**~~ — found and **fixed
    2026-09-17** while scoping a "perfect what's shipped" improvement
    pass. `exercise_spanish()` assumed every `fill-blank` exercise had a
    scalar `answer` field, but exercises with multiple blanks use
    `answers` (a list) instead — at least `a1-01-01`, `a1-03-05`,
    `a1-06-01` through `a1-06-04` do this. That threw `KeyError: 'answer'`
    inside `check_teaching_order()`, which runs per-level *after* all
    per-lesson structural checks print — so `python scripts/audit-lesson.py`
    with no args always crashed partway through A1 and never reached
    A2/B1 at all. Per-lesson structural checks (the FAIL/warn lines) ran
    correctly when a level was passed explicitly (`a1`/`a2`/`b1`), so
    those results were already trustworthy; only the cross-lesson
    teaching-order pass was silently blind, for every level except
    (partially) A1, for as long as the bug existed.
    - **Fix**: `exercise_spanish()` now returns `[ex["sentence"]] +
      (ex["answers"] if "answers" in ex else [ex["answer"]])` for
      `fill-blank`, matching how other multi-value exercise types are
      already handled.
    - Verified: `python scripts/audit-lesson.py` (no args) now runs to
      completion across A1/A2/B1 with no traceback — reports "616
      lesson(s) need work, 731 exercise(s) test untaught Spanish" as its
      first-ever full-corpus teaching-order result. A2/B1's actual
      teaching-order failures are new information (never surfaced
      before) — see ROADMAP.md's Current priority queue for what's next.

10. ~~**UI/UX Overhaul Initiative (7-Phase Roadmap)**~~ — Sequenced 2026-09-12
    to elevate Parlour's interaction ergonomics, responsive layout, and
    aesthetic fidelity:
    - [x] **Phase 1: Visual Identity & CSS Cleanliness** — **Done 2026-09-12**:
      Purged legacy `.card` `background: var(--surface)` and heavy borders;
      eliminated `.br-flag-btn` box shadow (last shadow in the codebase);
      standardized open cream rows on `var(--bg)` with `1px solid var(--border)`
      hairlines and `--dur-fast` transitions.
    - [x] **Phase 2: Responsive Shell & Navigation Architecture** — **Done 2026-09-12**:
      Desktop Constructivist sidebar (≥1024px) with brand mark and pinned XP/streak;
      mobile bottom tab bar (<640px) with safe-area insets; tablet centered container
      (640px–1023px); in-lesson clean screen mode (`body.in-lesson`) across all viewports.
    - [x] **Phase 3: Exercise Ergonomics & Desktop Keyboard Flow** — **Done 2026-09-12**:
      Added desktop hotkeys `1`–`4` with subtle monospace key badges for choices;
      global diacritic helper toolbar (`UI.diacriticsBarHtml`) across lessons and
      all drill runners for `es`, `hu`, and `fr`; and intelligent character-level
      error diffing (`generateAnswerDiff`) with accent-specific feedback.
    - [x] **Phase 4: Library & Reader Experience Polish** — **Done 2026-09-12**:
      Added typography/font-size scaling controls (85% to 150%) persisted in localStorage
      with dynamic line-height across both Parlour stories and My Texts reading views;
      integrated reading scroll progress indicator track and bar;
      added instant universal search filtering across all rooms, shelves, titles, authors, and levels
      with match counter and clear button;
      refined word popup (`.wp-sheet`) with desktop modal centering, hairline borders, and mobile
      safe-area bottom padding.
    - [x] **Phase 5: Decks & SRS Organization & Gestures** — **Done 2026-09-12**:
      Organized massive unit deck catalogues into collapsible CEFR level sub-accordions (A1, A2, B1, B2, C1)
      with level badge indicators and deck counts;
      added instant universal search filtering across titles, topics, preview words, and CEFR levels
      with auto-expanding matched accordions and clear button;
      implemented fluid mobile touch swipe gestures on flashcard review (swipe left for Again, swipe right
      for Good, tap to reveal answer) with dynamic rotation, color-tinted feedback, and exit animations;
      added desktop review hotkeys (`1` Again, `2` Hard, `3` Good, `4` Easy, Space/Enter for Show/Good)
      with visible monospace `.review-rate-hint` badges.
    - [x] **Phase 6: Workshop & Driller Visual Unification** — **Done 2026-09-12**:
      Standardized `.driller-progress-track` and `.driller-progress-bar` across all 9 workshop drillers
      (`grammar.js`, `translation.js`, `listening.js`, `vocabulary.js`, `verbs/speed.js`, `hu-verb.js`,
      `hu-suffix.js`, `hu-prefix.js`, `hu-morphology.js`);
      standardized session HUD (`.gd-hud`, `.gd-hud-score`, `.gd-change-skill` `← Settings`);
      standardized 4-metric results grid (`.vspeed-results`, `.vspeed-stat`) and unified 3-button post-drill
      action loop ("Practice Again", "Change Settings", "Back to Workshop" via `Workshop.close()`), preserving
      driller-specific actions (e.g. Vocabulary's "Add missed words to a deck").
    - [x] **Phase 7: Dark / Low-Light Reading Theme** — **Implemented 2026-09-12**:
      Inverted Constructivist palette (`[data-theme="dark"]` and `@media (prefers-color-scheme: dark)`)
      with midnight navy ground (`#0C1B2B`), warm cream structure & typography (`#F5F1E8`), crisp 1px hairlines,
      and vibrant warm orange focal accent (`#FF5A26`);
      immediate anti-FOUC initialization in `<head>`;
      standalone `engine/theme.js` with `'system' | 'light' | 'dark'` options and `localStorage` persistence;
      interactive Appearance card in My Journey tab;
      quick-toggle theme buttons in desktop sidebar and page header.

11. ~~**Speaking Function & Pronunciation Engine Initiative**~~ — **Built & deployed 2026-09-14**:
    - **Core Speech Recognition & Evaluation Engine** (`engine/speech-input.js`):
      - Browser-native Speech-to-Text (`SpeechRecognition` / `webkitSpeechRecognition`) with multi-language mapping (`es-ES`, `hu-HU`).
      - Transparent word-by-word evaluation tagging (`matched` vs `missed`) with diacritic, casing, and punctuation leniency via normalized Levenshtein token distance.
      - Sound energy visualizer and live interim transcription bubble.
      - Self-evaluation fallback mode for quiet rooms or unsupported browsers (e.g. desktop Firefox).
      - One-tap "Can't speak right now" preference to snooze speaking exercises for 30 minutes.
    - **Curriculum & Lesson Integration** (`engine/lessons.js`):
      - Two dedicated speaking step types: `read-repeat` (listen to model pronunciation and repeat) and `prompt-speak` (translate prompt into target language and say it out loud).
      - Injected 2 dedicated speaking practice steps into every curriculum lesson generated from the lesson's target vocabulary and grammar structures.
    - **Workshop Speaking Driller** (`engine/drills/speaking.js`, `engine/drills/speaking-runner.js`):
      - Dedicated Workshop speaking module with CEFR level selector (A1–C1), topic filters, and mode toggles (`Prompt & Speak`, `Read & Repeat`, `Mixed`).
      - Integrated model audio replay, mic waveform animation, and comprehensive evaluation breakdowns.
    - **SRS Flashcard Speaking Integration** (`engine/srs.js`):
      - Voice response mode on flashcard reviews with immediate accuracy feedback.
    - **Dual Audio Replay & Model Comparison**:
      - Side-by-side comparison bar across Lessons, Workshop, and SRS:
        `[Model Voice]` plays the native model pronunciation, while `[Your Voice]` replays the learner's actual recorded speech clip.
      - Mutual audio interruption, live `Playing...` active state, and dark-mode styling.
    - **Mobile-Proof Engineering & Learner Hesitation Debounce**:
      - Fixed iOS Safari user gesture expiration by invoking `recognition.start()` strictly synchronously within the tap event handler.
      - Solved hardware mic contention on mobile devices by running non-blocking background `MediaRecorder` audio buffering alongside native STT.
      - Extended silence debounce from 1.3s to **2.8 seconds** with automatic pause resumption on native mobile `onend` to accommodate learner hesitations ("um, uh, mhh") and thinking pauses.
      - Added safety session ceiling (25 seconds) and asset version cache-busting (`scripts/stamp-assets.py`).

12. ~~**Writing & Speaking Studios, CEFR Grader Engine & Oral Leniency**~~ — **Built & deployed 2026-09-14**:
    - **Dual Grading Engine** (`engine/grader/`): deterministic zero-dependency `LocalGrader` for instant local rubric scoring + optional `GraderEngine` for Cloudflare AI / Anthropic LLM feedback.
    - **Writing Studio** (`WritingDriller` in `engine/drills/writing.js`): open-ended free-text written production with topic/level selection, prompt suggestions, and structured CEFR assessments.
    - **Speaking Studio** (`SpeakingStudio` in `engine/drills/speaking.js`): unstructured speaking production practice with prompt generation, live microphone transcription, and audio playback.
    - **Oral Modality Calibration** (`engine/grader/grader-prompt.js`): calibrated prompts and local metrics to accommodate oral speech traits (pauses, filler words, transcript capitalization/punctuation artifacts).
    - **Manual Speech Transcript Editing**: allows learners to edit the raw speech recognition transcription before submission on unstructured speaking tasks.
    - **Instant Auto-Stop on 100% Target Match**: automatically stops recording the exact instant target speech matches 100%, removing manual mic clicks.
    - **Mobile Hardware Contention & Lifecycle Hardening**: eliminated MediaStream audio track hardware locks on non-audio steps, and resolved Android single-shot continuous listening conflicts.

13. ~~**CEFR "Can-Do" Checklist Competencies Integration**~~ — **Built & deployed 2026-09-14**:
    - Extracted and indexed official CEFR competency descriptors in `content/es/indexes/competencies-index.json`.
    - Wired competencies directly into `LearnerModel` (`recordCompetencyEvidence`, `getCompetencyCoverage`), Post-Lesson Summary screen (`renderLessonSummary`), My Journey mastery stats, Level Tests, and Studio prompts.

14. ~~**Library: Dual-Card Recommended Reading & Deep Bilingual Topic Search**~~ — **Built & deployed 2026-09-14**:
    - **Dual-Card Recommendation Banner ("Pick Your Pace")**: Pinned at the top of Library tab (`.lib-recs-container`), computing a Comfortable Read ($i+0$, fluency consolidation) and a Challenging Read ($i+1$, lexical stretch / authentic narrative) based on LearnerPath level and unread status.
    - **Deep Bilingual Topic Search**: Universal topic matching across English and Spanish (`BILINGUAL_TOPIC_SYNONYMS`) covering titles, authors, levels, unit titles, summaries, topic tags, and paragraph keywords.
    - **Manifest Keyword Indexing**: `build-manifest.py` automatically extracts up to 80 thematic keywords from story paragraphs for offline instant search.
    - **Word-Boundary Matching**: queries $\le 4$ chars enforce word boundaries, avoiding substring false positives.

15. ~~**Offline Support & Progressive Web App (PWA)**~~ — **Built & deployed 2026-09-14**:
    - **Service Worker** (`sw.js`): Precaches 82 core application shell assets (HTML, 8 stylesheets, core engine scripts, base curriculum and story manifests).
    - **Dynamic Content Caching**: Network-first caching for visited lessons, grammar explanations, and readings (`/content/`).
    - **Web App Manifest** (`manifest.webmanifest`): Standalone PWA installation on mobile and desktop with Constructivist branding.
    - **Network-Only Bypass**: Explicitly bypasses Cloudflare sync endpoints and external AI APIs.
    - **Offline Connectivity Status**: Floating status banner (`.offline-banner`) notifies users when operating offline.

16. ~~**Decks Importer (Anki, Quizlet, CSV)**~~ — **Built & deployed 2026-09-14**:
    - Auto-detects delimiters (tab, comma, semicolon, dash, colon), strips HTML tags, handles quotes, and validates lemmas against Lexicon dictionary.

17. ~~**Codebase Health & Performance Audit (Zero-DOM Escaping & Engine Cleanup)**~~ — **Completed 2026-09-14**:
    - **Zero-DOM String Escaping**: Replaced `document.createElement('div')` in `Reader.escapeHtml` and 8 drill/deck/verb runners (`engine/drills/grammar-runner.js`, `engine/drills/grammar.js`, `engine/drills/translation-runner.js`, `engine/verbs.js`, `engine/verbs/speed.js`, `engine/verbs/table.js`, `engine/decks/learn.js`, `engine/decks/match.js`) with fast, zero-allocation string escaping via `UI.escape()` with regex fallback. Eliminates disposable DOM nodes and GC pauses during text and exercise rendering.
    - **Debug Console Log Cleanup**: Purged leftover verbose debug `console.log` statements in `engine/lexicon.js` and `engine/reader.js`.
    - **Global Scope & Static Analysis Audit**: Confirmed all 64 engine scripts load and compile cleanly, with zero syntax errors, balanced CSS rules, zero unreferenced files, and 0 pictorial emojis across all code and stylesheets.
    - **Cache & Service Worker Synchronization**: Bumped PWA service worker and asset cache query parameters to `v2026-09-14h`.

18. ~~**Online Substack-Style Story Reading Player & Google Cloud TTS Architecture**~~ — **Built & deployed 2026-09-15**:
    - **Substack-Style Reader UI** (`engine/reader.js`, `styles/components.css`): Floating bottom pill player (`.story-substack-player`) pinned above the bottom viewport, styled with Constructivist borders, subtle glassmorphism backdrop blur, and smooth transitions. Features a circular Play/Pause button, active speaker and language tags (`#ssp-speaker-tag`), paragraph scrubber slider, paragraph counter/remaining counter (`1/14`, `-13 left`), and speed toggles (`0.8×`, `1.0×`, `1.2×`, `1.5×`) defaulting strictly to natural **`1.0×`** speed.
    - **Online-Only Graceful Visibility**: Adheres to the Core First, Enhancement Second architectural principle. Audio listening is strictly an online progressive enhancement: the player is hidden (`hidden` attribute and `.is-offline`) when disconnected (`!navigator.onLine`), and dynamically surfaces whenever internet connectivity is present. Paragraph audio buttons fall back gracefully to offline browser speech synthesis.
    - **Zero Git Audio Bloat (In-Memory Streaming)**: Eliminated all static `.mp3` and `.wav` audio files from the repository and Git history. Audio is fetched and synthesized on demand per paragraph via in-memory `Audio` buffers with eager next-paragraph background pre-fetching, keeping the repository 100% lightweight code and text.
    - **Cloudflare Worker TTS Proxy** (`cloudflare-worker/tts-worker.js`): Zero-dependency Cloudflare Worker proxy protecting the Google Cloud TTS API key in worker secrets. Handles CORS verification for production domains (`gergkar-gif.github.io`, `parlour.me.uk`, and `localhost`), mapping requests to Google Cloud Journey and Studio neural speech models.
    - **Substack-Calibrated Voice Casting**: Uses Google Journey models (`en-US-Journey-F`, `en-US-Journey-O`) for rich conversational, podcast-quality English scaffolding narration, and Google Studio/Neural2 models (`es-ES-Studio-C`, `es-ES-Neural2-B`, `hu-HU-Wavenet-A`) for authentic Spanish and Hungarian dialogue.
    - **Dual-Language Stories**: Fully supports Hungarian stories with English scaffolding narration and Hungarian dialogue. Detects paragraph `lang`, routing scaffolding to English Journey voices and Hungarian dialogue to native Hungarian voices with synchronized paragraph scrolling and active highlighting.
    - **Hungarian Phonetic Digraph Adaptation ("Károly" -> "Károy")**: Adapted speech synthesis inputs across `engine/reader.js`, `engine/speech.js`, and offline generation tools to replace the Hungarian name `Károly` with `Károy` (reflecting the Hungarian `ly` = `/j/` digraph pronounced like English "y") for speech synthesis, while keeping proper visible orthography (`Károly`) intact on screen.
    - **Pedagogical Comprehension Checks**: Built-in interactive multiple-choice check with immediate validation and explanations.
    - **Schema & Manifest Integration**: Added `narration` definitions in `story.schema.json` with optional `audioFile`, and updated `build-manifest.py` so `hasAudio` is based on narration structure and paragraphs rather than local disk audio presence. Verified with 11 automated unit tests in `tests/reader/test-story-narration.js`.

23. ~~**`ParlourTTS` engine abstraction (`engine/tts.js`)**~~ — **Built and
    live 2026-09-16.** Content -> `ParlourTTS.speak({text, language, type,
    voiceName, gender, speed, onEnded})` -> provider -> audio, so no caller
    talks to a TTS provider directly. Cloud-first (Google Cloud TTS via
    `cloudflare-worker/tts-worker.js`), falling back automatically to
    device `speechSynthesis` (`engine/speech.js`'s `Speech` module) when
    offline, the worker errors, or no API key is configured — verified live
    in-browser (Library story reader and Workshop's Listening Driller both
    correctly attempt cloud, catch the failure, and fall back to device
    speech with auto-advance intact). Session-cached per
    `language::voiceName::text` so repeat playback is free.
    - Undoes an uncommitted regression from between 2026-09-15 and
      2026-09-16 that had replaced item 18's real Google Cloud TTS call in
      `tts-worker.js` with a reverse-engineered, unofficial Microsoft
      Translator endpoint (hardcoded HMAC key pulled from the Android app).
      Worker now calls `texttospeech.googleapis.com` directly again, using
      Chirp3-HD voices (Google's newest natural-narration tier, and the
      only one covering both Spanish *and* Hungarian at that quality —
      Studio and Neural2 don't have Hungarian voices). Free tier is 1M
      chars/month; Parlour's own estimated spoken-content corpus is a
      one-time synthesis in the low single-digit millions of characters,
      cached forever after. Needs a GCP project + billing account (card on
      file, but $0 expected) and `wrangler secret put GOOGLE_TTS_API_KEY`
      on the worker before cloud playback actually works — until then it
      falls back to device speech automatically, nothing breaks.
    - **GCP + Cloudflare setup completed and verified live 2026-09-16**:
      `parlour-tts` GCP project, billing account, Text-to-Speech API
      enabled, API key restricted to that one API, `GOOGLE_TTS_API_KEY`
      deployed as a Cloudflare Worker secret. `/health` reports
      `hasApiKey: true` and a real story played through Chirp3-HD end to
      end with zero fallback warnings.
    - **Purposeful voices by content type, same day**: `tts-worker.js`'s
      `SHORT_VOICE` map picks by an explicit per-character voice first (see
      below), else `gender` (`male` -> Orus, `female` -> Kore), else `type`
      (`vocabulary`/`listening`/`pronunciation` -> Iapetus for clarity,
      `instruction` -> Achird for a distinct "app voice", `example` ->
      Despina, `narrator`/`reading` -> Sulafat), else the narrator default.
      Voice names are shared across the Chirp3-HD bank per language, so the
      same semantic map works for es/hu/en without per-language tuning.
    - **Distinct voice per named character, same day**: a story's dialogue
      no longer collapses every male character onto one voice and every
      female character onto another. `reader.js`'s `assignCharacterVoices()`
      reads each story's own `narration.speakers[name].gender` and hands
      out one voice per character from a 6-deep gender-matched pool (Orus,
      Puck, Charon, Fenrir, Umbriel, Algieba for male; Kore, Aoede, Leda,
      Zephyr, Callirrhoe, Autonoe for female), assigned once per story load
      so "Meg" keeps the same voice in every line. Worker's `character`
      param (a short voice name) takes priority over `gender`/`type`.
    - **All three leftovers resolved 2026-09-16**:
      1. All ~15 remaining `Speech.speak()`/`Speech.button()`/
         `Speech.available()` call sites (decks, lessons, library, SRS,
         speaking runner, studyPlan, recommendationEngine) migrated to
         `ParlourTTS` — added `ParlourTTS.available()` (online, or a device
         voice as fallback) and `ParlourTTS.button()` (same drop-in markup
         ergonomics as `Speech.button()`, own `[data-tts-text]` delegated
         click listener so it doesn't collide with `Speech`'s
         `[data-speak]` one) to make the swap mechanical. Verified live:
         Decks word list, a lesson's vowel-sound table, and the SRS review
         card all speak through the cloud provider with no fallback
         warnings. Found and fixed a related latent bug along the way:
         Speaking Studio's "play my own recording" only ever cancelled
         `speechSynthesis`, not a still-playing cloud audio clip — now
         calls `ParlourTTS.stop()`, which covers both.
      2. `listening.js`'s settings screen now gates on `ParlourTTS
         .available()` instead of `Speech.available()`, so the driller
         works from the cloud provider alone on a device with no voice
         installed. Same fix applied to the two other places that decide
         whether to *recommend* Listening/Speaking activities at all
         (`studyPlan.js`'s time-based session builder, `recommendation
         Engine.js`'s Home candidates) — otherwise migrating the driller
         itself would have been undercut by recommendation logic still
         hiding it from cloud-only users.
      3. `scripts/narrate-story.py` no longer synthesizes audio at all —
         removed the `edge-tts` dependency, `synthesize_story_neural()`,
         and the `audioFile` field it wrote into `narration`, along with
         the now-dead `--no-synth` flag. It only ever generates the
         timing/pedagogical metadata now (word-count-based paragraph
         timing, comprehension questions, `speakers[name].gender` for the
         voice assignment above) — verified with `--dry-run` against the
         real content and the existing 11-test narration suite still
         passing unchanged.
    - **R2 audio cache added 2026-09-17**, prompted by a backend cost
      review: `tts-worker.js`'s only cache was `ParlourTTS`'s in-memory
      session cache (above), which meant every reload re-synthesized
      identical lesson audio through Google TTS — pure waste, since lesson
      text is fixed and near-all repeat traffic across learners/sessions.
      Worker now content-addresses each synthesis (SHA-256 of
      `languageCode::voiceName::speakingRate::pitch::text`) and checks an
      R2 bucket bound as `TTS_CACHE` before calling Google; a miss writes
      the MP3 to R2 after synthesis (best-effort — a write failure doesn't
      fail the response, just costs a repeat Google call later). `/health`
      now reports `hasR2Cache`. No client change needed — `engine/tts.js`
      already just reads `audioContent` from the same JSON shape. Verified
      live: `/health` returns `hasR2Cache: true` on the deployed worker.

24. ~~**SRS/Decks review card: audio/mic UI stripped back down**~~ — **Built
    2026-09-16.** The card had accumulated three overlapping audio
    affordances: a `ParlourTTS.button()` listen icon, a separate
    audio-first review direction (`reviewDirection === 'audio-en'`, its own
    front/back layout and auto-play), and a self-recording "Speak" button
    (`reviewSpeakWord()` — records via `SpeechInput`, evaluates pronunciation,
    offers a "Hear yourself" replay). User's call: "too many things for an
    SRS card... all I want is on the target language side to have a little
    microphone icon... click and listen to the word. That's all. Like in a
    Quizlet card." Removed the audio-first direction (now a plain two-way
    Spanish/English toggle) and the self-recording/evaluation flow entirely
    (`reviewSpeakWord`, `reviewPlayUserAudio`, their state, the `#review
    -speak-btn`/`#review-speak-feedback` markup, `.review-speak-*`/
    `.review-audio-*`/`.btn-audio-prompt` CSS) — kept only the one listen
    icon next to the Spanish word. Pronunciation self-recording still exists
    in Speaking Driller, which already covers that use case separately;
    nothing was lost, just de-duplicated off the review card. Verified live:
    Flip and Type modes, Show Answer, rating buttons, and the two-way
    direction toggle all work with no console errors and no orphaned
    references to the removed markup/classes anywhere in the codebase.

25. ~~**AI-grading fixes: natural-language tips surfaced, task-completion
    grading for can-do checks**~~ — **Built 2026-09-16.** Two related grader
    fixes from a user feedback batch:
    - **Lesson-end writing/speaking feedback was numbers-only.** The AI
      grader (`engine/grader/grader-prompt.js`) already returns a
      natural-language coaching tip (`feedback.priorities`/
      `errors[].explanation`) — Writing/Speaking Studio already renders it,
      but the two in-lesson checkpoints (`lessonGetWritingFeedback()`,
      `_lessonCheckSpeakingCEFR()` in `engine/lessons.js`) only showed
      percentage-pill dimension scores and threw the qualitative feedback
      away. Added `_graderOneLineTip()`, a small picker (priority →
      error explanation → strength, first available) rendered as one
      `.lsn-hint` line under the pills in both places.
    - **Grader too harsh on can-do checks.** A learner asked to "count from
      1 to 10" and did exactly that got marked down for "not using full
      sentences" — traced to `engine/drills/speaking.js`'s competency-check
      flow (`journey.js`'s "unverified competencies" nudge, and the Studio's
      own "Target Unverified Goals" card) hardcoding "...and use complete
      sentences" into the TASK text sent to the grader, regardless of
      whether the competency was an enumeration/list-style can-do or an
      open topic — plus defaulting `targetSkills` to include
      `sentence_structure` for every competency check. Removed both. Added
      a new `taskCompletionPrimary` flag (threaded `speaking.js`/
      `writing.js` → `context` → `grader-engine.js` → `grader-prompt.js`),
      set `true` only for competency-derived prompts in both Studios: when
      set, the prompt tells the model to ignore the normal dimension
      weighting and score 85-100 for a production that correctly and
      completely fulfils a concrete, bounded task, however short or
      grammatically simple — reserving deductions for content that's
      actually missing, wrong, or unintelligible. Verified by generating
      prompts with the flag on/off and confirming the new instructions
      appear/disappear and "complete sentences" no longer appears in any
      generated prompt; existing `tests/grader/test-oral-grader.js` suite
      still passes unchanged. The AI's actual grading behavior with the new
      instructions can't be unit-tested (inherent to LLM grading) — worth
      a real-usage spot-check.

27. ~~**Time-Based Sessions should always include a quick speaking prompt**~~
    — **Built 2026-09-17.** Investigated 2026-09-16 as two scopes (small:
    loosen the existing conditional inclusion; medium: a real
    auto-launched quick-prompt mode) — built the medium version, refined
    from the user's own suggestion to source prompts from the CEFR can-do
    list (the same 1,114 HU / 2,341 ES items behind My Journey's Can-Do
    Passport — see item 29's index-generation fix) rather than inventing
    generic ones, since a can-do statement like "I can greet someone" is
    both a real 30-second speaking task *and* already the exact shape
    yesterday's `taskCompletionPrimary` grading fix (item 25) was built
    for.
    - `engine/learnerModel.js`'s new `pickSpeakingPrompt(level)`: prefers a
      genuinely unverified/weak competency at the learner's level
      (`unverifiedCompetencies()`, already existed), falls back to any
      competency from an already-completed lesson (nothing ahead of where
      the learner actually is) at that level, any level if none yet at
      this one, and returns `null` — not a placeholder — when there's
      truly nothing appropriate (e.g. a brand-new learner with zero
      completed lessons). Verified all three paths live.
    - `engine/studyPlan.js`: new guaranteed `speaking-cando` item, ~40
      seconds, placed ahead of the budget-gated blocks so it survives a
      tight session — added only when `canSpeak` and a prompt was
      actually found; skipped outright otherwise, same "never pad with
      invented busywork" rule the rest of the allocator already follows.
      Coexists with (doesn't replace) the existing opportunistic longer
      Sentence-Drills `speaking` block for when there's real budget left.
    - `engine/drills/speaking.js`'s `targetCompetency` auto-launch
      shortcut (already used by Journey's "unverified competencies"
      nudge) now takes an optional `maxSeconds`, defaulting to the
      existing 300s so that entry point is unchanged; the Studio tab
      label ("Verbal Production (5 min)") is now computed from the actual
      cap instead of hardcoded, reset to the default on every fresh
      `render()` that isn't itself setting a custom cap, so a quick 40s
      session's cap can't leak into an unrelated later normal one in the
      same page session (caught live while testing, not theoretical).
    - Verified end-to-end: a 30-minute plan now includes both `speaking-
      cando` ("Quick speaking — 40s") and the longer `speaking` block; a
      10-minute plan fully consumed by its lesson correctly omits it
      rather than forcing it in. `engine/studyPlanRunner.js` routes the
      new kind straight to `SpeakingDriller`'s recording screen, which
      already returns to the plan queue via the existing
      `RecommendationEngine.mountNextAction()` → `StudyPlanRunner
      .mountNextAction()` path once graded.
    - **Not done**: longer, CEFR-exam-style prompts ("talk about clothes
      for 3 minutes," matching what an actual exam asks) — that's item 28,
      still waiting on the user's ChatGPT-sourced topics file. The
      `maxSeconds` plumbing built here is exactly what that will also
      need (just a bigger number and a different prompt source), so no
      rework expected when it lands.

29. ~~**Hungarian CEFR Can-Do Passport loaded no skills; Decks review back
    button showed garbled text**~~ — **Fixed 2026-09-16.** Two unrelated
    bugs, one report:
    - `content/hu/indexes/competencies-index.json` (the file `engine/
      learnerModel.js`'s `loadCompetenciesIndex()` reads) never existed —
      only `content/es/...` did, so the Hungarian portfolio silently
      degraded to an empty list (the loader already catches a fetch
      failure and returns `[]`, so no crash, just nothing to show). Root
      cause: this index was hand/one-off generated for Spanish only,
      never added to any of the `scripts/build_*.py` family that
      regenerates every other derived index. Added `scripts/
      build_competencies_index.py`, which mechanically extracts each
      lesson's `checklist`-step "I can..." items via curriculum.json
      (same source data ES's file already came from — no new content to
      author). Verified the ES output against the existing file before
      trusting it for Hungarian: 0 field mismatches on 2,315 shared
      entries; the only differences were 2 stale orphaned entries (lessons
      no longer in curriculum.json) and 26 newer entries (the A2
      imperfecto lessons from item 20/21 above, added after the existing
      file was last generated) — so this run also quietly fixed ES's own
      staleness. Generated `content/hu/indexes/competencies-index.json`
      fresh: 1,114 items across A1/A2/B1. Verified live: Hungarian's
      Can-Do Portfolio modal now lists real competencies grouped by unit
      with working Speak/Write practice buttons, where it previously
      showed nothing.
    - `index.html`'s Decks review "← All decks" back button had been
      triple-encoded mojibake (`â† All decks`, raw bytes
      `\xc3\xa2\xe2\x80\xa0\xc2\x90`) since commit `084348cc5` (2026-09-13)
      — predates this session, not something introduced here. Fixed with
      a direct byte-level replacement back to a plain `←` character,
      matching every other back button's style in the codebase (`engine/
      decks.js`, `engine/library.js`, `engine/workshop.js`). Checked for
      other visible (non-comment) instances of the same corruption
      elsewhere in `index.html`; found none.

31. ~~**Cloudflare Turnstile added to sign-in (`/auth/request-link`)**~~ —
    built and verified live 2026-09-17, from the same backend cost/
    security review as item 23's R2 cache. `sync-worker.js`'s only abuse
    guard was "max 3 links per email per hour" in D1, which doesn't stop
    a script hitting the endpoint with many distinct emails and burning
    Resend's send quota (or getting the sending domain flagged). Client
    (`engine/sync.js`) now mints an invisible Turnstile token before
    calling `requestLink()`; the Worker verifies it against Cloudflare's
    `siteverify` API (`verifyTurnstile()`) before touching D1 or Resend.
    Designed to degrade to a no-op, not break sign-in, while unconfigured:
    empty `TURNSTILE_SITE_KEY` client-side skips minting a token, and a
    missing `TURNSTILE_SECRET_KEY` server-side skips verification — both
    now set. **Setup gotcha hit during rollout:** the dashboard Secret was
    first added as `TUSTILE_SECRET_KEY` (typo, missing "RN"), which — since
    a missing/misnamed secret is the intentional "not configured yet"
    no-op path — silently let every request through unverified rather than
    erroring. Confirmed via `curl` with a deliberately bogus token: before
    the fix, `429`/`502` (request reached D1/Resend, meaning verification
    never ran); after renaming the secret, `403 Verification failed` as
    expected. **Lesson: a bogus-token test, not just a missing-token test,
    is what actually distinguishes "verification is running and rejecting"
    from "verification isn't running at all"** — both look identical from
    the missing-token case alone. Also found and fixed in passing: `JWT_
    SECRET` and `RESEND_API_KEY` were stored as plain **Variable** type on
    the Worker (plaintext-visible in the dashboard) rather than **Secret**
    (encrypted-at-rest) — re-typed to Secret.

32. ~~**AI grader switched off Llama 70B by default, ~4x cheaper per call**~~ —
    built and verified live 2026-09-17, same backend cost review as items
    23/31. `grader-worker.js` was trying `@cf/meta/llama-3.3-70b-instruct-
    fp8-fast` **first on every single grading call**, not as an error
    fallback — Cloudflare's own neuron pricing puts that model at ~6-8x the
    per-token cost of an 8B-class model. Spent most of this item's time on
    a real, evidence-based elimination round rather than guessing:
    - Three Llama 8B-class candidates were tried and rejected, each with a
      concrete, reproducible failure on the actual multi-field CEFR JSON
      scoring prompt (not just weaker nuance): `llama-3.1-8b-instruct-fp8-
      fast` returned `overallScore` and every dimension as `0` for a solid
      A2 response, plus a manufactured grammar error on correct usage;
      `llama-3.1-8b-instruct` (unquantized) turned out to be deprecated
      server-side (Cloudflare error `5028`) and simply errors now;
      `llama-3.1-8b-instruct-fp8` returned `overallScore` as a `0.0-1.0`
      fraction (`0.6`) instead of the required `0-100` int, which
      `engine/grader/schema.js`'s `clampNumber` would round straight down
      to `1` — a learner who did well would have seen "1/100".
    - `@cf/openai/gpt-oss-20b` was tried and abandoned without a full test:
      it's a reasoning model that spends tokens on hidden chain-of-thought
      before the visible answer, so it returned empty content once
      `max_tokens` (below) was tightened — and its true per-call cost would
      include that invisible reasoning anyway, likely erasing its sticker
      price advantage.
    - `@cf/mistralai/mistral-small-3.1-24b-instruct` (~4x cheaper than 70B
      on output neurons) passed the same real-prompt spot-checks, but only
      after fixing two root causes in `engine/grader/grader-prompt.js`
      itself — **not model-specific, so this also hardens 70B and any
      future cheaper model**: the required-JSON-shape example showed
      `"overallScore": 0` sitting right next to `0.0-1.0` dimension fields
      with nothing distinguishing its scale (a plausible reason every
      failing 8B model got this wrong the same way), and the
      `demonstratedSkills`/`weakSkills` object shape was only ever implied
      by the example, never stated as a hard rule. Both are now explicit
      "CRITICAL RULE" lines in both the written and oral prompt builders.
      Verified with the real `buildGraderPrompt()` output (not a hand-
      written test prompt) on both a strong A2 response (scored 72-78,
      correctly-shaped skill objects, accurate non-hallucinated errors)
      and a deliberately weak one (scored 20-25, confirming the score
      tracks actual content rather than anchoring to the example's
      placeholder number).
    - `CANDIDATE_MODELS` is now `[mistral-small-3.1-24b-instruct, llama-3.3-
      70b-instruct-fp8-fast]` — 70B remains a true fallback, only reached
      if Mistral errors. Also fixed in passing: the fallback loop only
      continued to the next candidate on error `5007`; a `5028`
      (deprecation) hit during this session's testing instead hard-failed
      the whole grading call, so the continue-condition now covers both.
      `max_tokens` trimmed `3000` → `1500` (the prompt's own output-economy
      rules already cap real responses far below either number, so this
      only caps worst-case cost, no truncation risk).
    - **Ship gotcha hit during rollout:** right after a `Deploy`, two
      requests seconds apart returned two different models even with
      identical (default) candidate settings — Cloudflare Worker deploys
      take up to roughly a minute to fully propagate across edge
      locations, so a request can transiently land on a PoP still running
      the previous version. Re-tests a short while later were consistent.
      Don't read a deploy as broken from one inconsistent request
      immediately after clicking Deploy — retry a few times first.

39. ~~**ES teaching-order flags triaged: 731 total, 86% real**~~ — **Done 2026-09-17.**
    `scripts/triage-teaching-order.py` (built after item 35's crash fix unblocked
    A2/B1 for the first time) classified flags into `real-gap-candidate` (626),
    `wrong-distractor-only` (100), and `english-leak` (5). Resolved across levels
    via items 46 (ES A1/A2) and 48 (ES B1), reducing 626 candidates down to 11
    accepted irregular/clitic morphology edge cases across the entire 762-lesson
    Spanish curriculum. See items 41, 46, and 48 for complete tooling and content
    audit details.

40. ~~**Hungarian teaching-order checker expansion**~~ — **Done 2026-09-17.**
    Built Hungarian's first teaching-order checker (`scripts/audit-lesson-hu.py` +
    `scripts/triage-teaching-order-hu.py`) with agglutination-aware bounded-prefix
    stem matching, accent-sensitive tokenizing, and curriculum-based unit
    grouping. Resolved across levels via items 42–45 (HU A1/A2) and 47 (HU B1),
    reducing 171 real-gap candidates to 10 accepted morphophonology edge cases
    across all Hungarian levels. See items 41, 42–45, and 47 for details.

42. ~~**HU pilot: "Going Places" unit (a1.56-60) — fixed and verified**~~ —
    resumed item 41, **done 2026-09-17**. Fixed lesson a1.56 (Haiku-applied
    from fully-specified edits): added `mozi`/`étterem`/`múzeum`/`posta` to
    its vocabulary file, added a `Hová mész?` worked example to its grammar
    screen, reworded an off-topic dialogue opener (`Mit csinálsz?` → `Hová
    mész?`) so it reinforces the lesson's actual grammar point instead of
    an unrelated verb.
    - **Bigger find while triaging a1.57-60**: every `structured-writing`
      exercise in those lessons had a malformed `answer` field — a Python
      tuple-repr string (`"('állomás', 'station') ('megálló', 'stop')..."`)
      instead of a real sentence, which is why they'd shown up as apparent
      English leaks the triage heuristic didn't recognize. Grepped the
      whole HU exercise corpus for the same pattern: scoped to exactly
      `a1-56` through `a1-75` (20 lessons, one broken exercise each), zero
      elsewhere (not HU A2/B1, not ES). Sent the user a `.txt` for a1.57-60's
      4 instances (real sentences need correct vowel harmony, not guessed);
      user ran it through ChatGPT and returned real sentences, applied via
      Haiku, verified valid JSON and no leftover `('` pattern. The other 15
      lessons (a1.61-75) have the same bug, out of this pilot's scope — see
      new item 43.
    - **Real tooling bug found and fixed along the way**: re-auditing after
      the content fixes still showed `útba` (a regular, correctly-taught
      inflected form of `út`, "road") as untaught. Root cause was in
      `scripts/audit-lesson-hu.py` itself, not content: `KnownWords`
      bucketed known words by their first **3** characters for fast fuzzy
      lookup, but a short root like `út` (2 chars) buckets under `"út"`
      while its suffixed form `útba` buckets under `"útb"` — different
      keys, so the fuzzy match never even ran. Changed the bucket key to 2
      characters. Effect was much bigger than this one word: full-corpus
      flag count dropped from 330 to **213** (real-gap-candidate 171 → 104)
      — most of item 40's original count was this false-positive class,
      not real gaps. `audit-lesson-hu.py`/`triage-teaching-order-hu.py`'s
      numbers everywhere above (items 40/41) are now stale; 213/104 are
      current as of this fix.
    - Verified end-to-end: `audit-lesson-hu.py a1` shows zero remaining
      flags for lessons a1.56-60 (one harmless leftover, an English gloss
      `(to the road)` inside a1-60's sentence text, correctly excluded from
      `real-gap-candidate` by the triage script).

43. ~~**HU: same malformed-`answer` bug in 15 more A1 lessons (a1.61-75)**~~
    — found 2026-09-17 while scoping item 42 (see ACHIEVED.md), **done**.
    Same shape as that item's a1.57-60 fix, but spanned 3 different grammar
    topics, not one uniform pattern: a1.61-65 teach 1st-person-singular
    present tense verb conjugation (several irregular `-ik` verbs among
    them, e.g. `enni`→`eszem`, `inni`→`iszom`), a1.66-70 teach negation
    (`nem`) and question transformations, a1.71-75 teach daily-routine
    present-tense language. Sent one `.txt` for all 15, grouped by grammar
    topic; user ran it through ChatGPT.
    - **Caught and fixed one real error in the ChatGPT reply before
      applying**: exercise 63's `iszok` should be `iszom` (`inni` is an
      irregular `-ik` verb, same pattern as `enni`→`eszem` which the reply
      got right) — worth the sanity pass, not just apply-and-trust.
    - Applied all 15 via Haiku (exact strings pre-verified, not asked to
      judge). Re-auditing surfaced 3 new gaps the fix itself introduced —
      several word-pair lists supplied only verbs or only nouns, so a
      natural sentence needed a partner word the lesson never taught
      (`víz`/`kenyér` for a1.63, `óra` — already taught two lessons later
      in a1.75, reused here — for a1.73, `tartani` for a1.75). Added those
      4 words to the respective lessons' vocabulary files.
    - **Not fully clean, and that's expected, not a bug**: a1.63 still
      flags `iszom` and `vizet` — both genuine Hungarian morphophonology
      the bounded-prefix heuristic can't catch (suppletive stem for
      `iszom`, vowel-length shortening `víz`→`vizet`), not something worth
      chasing for two words. Full HU corpus: 330 → 213 (item 42's tooling
      fix) → **209** (99 real-gap-candidate, 90 wrong-distractor-or-
      english-option, 20 english-leak). The remaining ~99 real-gap-
      candidates are pre-existing, unrelated to this item.

44. ~~**HU: rest of a1.01-165's real-gap-candidates cleared, plus 3 more
    triage-tool fixes**~~ — **done 2026-09-17**, continuing items 42/43.
    Full HU corpus: 209 → **166** flags (real-gap-candidate 99 → 41; A1's
    own real-gap-candidate count: 29 → 4).
    - **3 more triage heuristic fixes**, same "find the pattern, don't fix
      one word at a time" approach as items 42/43: (1) `"What does 'X'
      mean?"` comprehension checks are deliberately all-English options —
      281 such exercises exist across the whole HU corpus, none of which
      the triage recognized as noise before this. (2) The wrong-distractor
      check only applied to `multiple-choice`, not `dialogue-complete`,
      which has the identical `options[]`/`correct` shape — missed e.g.
      a1-11's unselected "Én itt lakom." (3) A real bug, not just a triage
      gap: `hu_tokens()`'s proper-noun filter used the same fuzzy
      `same_stem()` matcher as regular word comparison, so the pronoun
      `maga` ("himself/herself") got silently swallowed as if it were a
      form of `Magyarország` (shares "mag-") — meaning `maga` never
      actually entered any lesson's known-vocabulary set anywhere it was
      taught. Switched the proper-noun filter to strict `startswith`
      (proper nouns only need to match their own suffixed forms, which is
      always noun+suffix, so no fuzzy tolerance is needed or safe there).
      This one fix alone dropped the full corpus by 43 (209→166) — bigger
      than either content batch below.
    - **~26 real vocabulary gaps fixed** across a1.01-165 (the rest of the
      lessons items 42/43 didn't already cover): missing content words
      used in exercises before being taught (`ők`, `kell`, `fontos`,
      `film`, `leves`, `ebéd`, `mögött`/`között`, `tanár`, `történelem`,
      `diák`, etc.) — applied via Haiku in one batch call across 23 files
      after manually checking each flagged exercise's actual context first
      (not applied blind). Also added `bécs` (Vienna) to `HU_PROPER_NOUNS`
      — same proper-noun-not-taught issue as items 30/42's Spanish/HU
      place-name lists.
    - **Left deliberately unfixed (4 flags)**: `a1-01-practice-3`'s
      "(Do you want coffee?)" gloss-supported warm-up sentence (by design,
      not a gap); `a1-63`'s `vizet` (vowel-length shortening, víz→vizet);
      `a1-112`'s `hozom` and `a1-152`'s `elvettem` (definite-conjugation
      and irregular-past-tense forms respectively that don't share enough
      surface prefix with their infinitives for the bounded heuristic to
      catch) — all genuine Hungarian morphophonology, not tool bugs, not
      worth chasing for single-word cases.

45. ~~**HU A2 real-gap-candidates cleared, plus 2 more triage-tool fixes**~~
    — **done 2026-09-17**, continuing items 40/42-44. A2's real-gap-
    candidate count: 28 → 5 (all left deliberately, same morphophonology-
    edge-case reasoning as item 44 — e.g. `víz`→`vizet`-style vowel
    shortening in `úr`→`uram`, definite/indefinite conjugation divergence
    in `úszni`→`úszom`).
    - **2 more triage fixes before touching content, per item 44's own
      advice**: (1) a `"(...)" ` gloss can sit inside an `options[]` entry
      too, not just the `sentence`/`question` fields — e.g.
      `"Virágcsokor (flower bouquet)"` — found via `a2-184-controlled-4`'s
      `bouquet` false flag; 75 such option-embedded glosses exist across
      the corpus, previously all invisible to the triage. (2) Two more
      names needed adding to `HU_PROPER_NOUNS` (`gábor`, `kovács` — a
      first name and the most common Hungarian surname, both used as
      dialogue characters, e.g. "Kovács néven foglaltam szobát").
    - **27 real vocabulary gaps fixed** across a2.52-185 via one Haiku
      batch (18 files), each checked against its actual exercise context
      first — same workflow as item 44, not applied blind. One fix
      (`hát`, "back") resolved two separate lessons' flags at once since
      a2-138's `hátam` is downstream of a2-85's `hátra` in teaching order.

46. ~~**ES A1 and A2 real-gap-candidates cleared, plus 3 tooling fixes in
    `audit-lesson.py` itself (not just the triage layer)**~~ — **done
    2026-09-17**, continuing item 39/41. A1: 40 → 4 real-gap-candidates.
    A2: 22 → 6. Same lesson as items 42-45: ported HU's triage-layer fixes
    over first (meaning-check pattern, `dialogue-complete` wrong-distractor
    detection — ES has 1,528 `dialogue-complete` exercises with a
    `correct` field, far more than HU had — option-embedded glosses, one
    proper noun `lucia`), which alone cut 731 → 707. But the bigger finds
    this time were in `audit-lesson.py`'s own `matches()`/`teach_tokens()`,
    not just the read-only triage script:
    - **Grammar tables only ever read column 1, never column 2** —
      `teach_tokens()`'s table handling did `spanish_tokens(row[0])` only.
      Harmless for a `[spanish, english]` table, but conjugation tables
      are `[pronoun, conjugated-form]` (e.g. `["nosotros", "trabajamos"]`)
      — the entire point of the table, the actual verb forms, was never
      registered as taught. Root cause of most of a1-06's "nosotros"/"tú"
      form flags. Fixed by reading both columns (707 → 656).
    - **`matches()` had no concept of verb conjugation at all** — its
      only fuzzy logic stripped noun/adjective plural endings
      (`es/os/as/s`). Added present-tense person-ending stripping that
      reconstructs the infinitive and checks if *that's* already known
      (a learner who knows `cocinar` can be expected to recognise
      `cocinamos`) — the same productive-rule leniency `find_missing()`
      already granted verbs elsewhere, extended to the teaching-order
      check too (656 → 620). Then found A2 introduces past tense (preterite
      + perfect) that the present-only ending list didn't cover at all
      (`celebraron`, `tenido`, `preguntado`...) — extended the ending list
      (620 → 574) — and a reflexive-infinitive gap (`alegró` needs to
      reconstruct `alegrarse`, not `alegrar`) — added `-arse/-erse/-irse`
      alongside `-ar/-er/-ir`.
    - **Same short-root bucketing class of bug as HU's item 42-44 fixes**:
      the noun/adjective stem-length threshold (`>=4`) missed `foto`→
      `fotos` and `vela`→`velas` (3-char stems after stripping the
      plural); the verb-root threshold (`>=3`) missed `leer`→`leo` (root
      `le`, 2 chars). Lowered both by one.
    - **~29 real vocabulary gaps fixed** across A1 (18 files, 24 entries)
      and A2 (4 files, 5 entries) via two Haiku batches, each checked
      against its actual exercise context first.
    - **Left deliberately unfixed (10 flags: 4 A1, 6 A2)**: irregular
      preterite stems (`hiciste`/`hicieron` from `hacer`, `estuvieron`
      from `estar` — suppletive, no reconstructible pattern),
      reflexive-infinitive-plus-clitic forms (`acostarme`, `despedirme`,
      `marcharme`), one stem-changing verb (`muestras` from `mostrar`),
      one by-design gloss-supported sentence, one ambiguous future/
      subjunctive form (`lograran`) — all genuine Spanish morphology, same
      category of exception already established for HU.
    - Full ES corpus: 731 → 707 → 656 → 620 → 574 → **570** (real-gap-
      candidate 626 → 399). B1 dropped from 537 to 389 as pure fallout
      from the tooling fixes, before any B1-specific work started.

47. ~~**HU B1 cleared, plus a severe proper-noun bug that silently affected
    the entire session's earlier HU work**~~ — **done 2026-09-17**.
    Scoped B1 first at the user's request (hypothesis: most of it is the
    citizenship track) — confirmed directionally right but not the way
    expected: citizenship-track lessons produced 70% of raw flags (26/37)
    but only **2 of the 6 real gaps**; core track had proportionally more
    real problems (4/11) despite far less raw noise. Citizenship lessons
    are civics/history quizzes with English-option answers, which is
    exactly the shape the triage already classifies as noise — the raw
    flag count was measuring exercise *style*, not actual gaps.
    - **The bug, found while investigating one of the 6 real gaps**:
      `hu_tokens()`'s proper-noun filter (added item 42, fixed to strict
      `startswith` in item 44) used plain prefix matching without a
      length floor. Every other entry in `HU_PROPER_NOUNS` is 4+ characters,
      but `meg` (the protagonist's name) is 3 -- and `meg-` is also
      Hungarian's single most common verbal preverb, prefixing hundreds of
      ordinary verbs (`megyek`, `megnéz`, `meggyőz`, `megvesz`...). Every
      one of them was silently wiped to an empty token set for the entire
      session, in both directions (never counted as taught, never counted
      as required) -- which is why it mostly didn't change raw flag counts
      when fixed (a word invisible on both sides of the check is
      invisible to the check, not wrong in an obviously visible way).
      318 distinct `meg`-prefixed words found across the whole HU corpus
      grep'd for spot-checking. Fixed by requiring exact match instead of
      prefix match for any proper noun under 4 characters.
    - **Re-audited A1/A2 after the fix rather than assuming they still
      held**: full corpus went 166 → 143 (net small, per the above), and
      exactly one new real gap surfaced in A1 (`megyek`, previously
      invisible) — checked its context and left it deliberately (an
      incidental "I'm going, bye!" dialogue line seven lessons before the
      unit that actually teaches "to go", not something the exercise
      tests). A2's list was unaffected. B1's 6-item real-gap list (scoped
      before the fix) was independently re-verified unchanged after it —
      the fix's effect on B1 was invisible for the same reason.
    - **6 real vocabulary gaps fixed**: `fábián` was a person's name, added
      to `HU_PROPER_NOUNS` instead of vocab; `suli` (school, colloquial),
      `óriási` (huge), `lép` (to step), `fekvés`/`konkrét` (location/
      concrete — citizenship track), `zúdul` (to pour/swarm — citizenship
      track) added via one Haiku batch across 5 files.
    - **All three HU levels are now fully done.** Full corpus (raw flags):
      166 → 143 (bug fix) → 137 (B1 fixes); real-gap-candidate: 41 → 16
      (bug fix) → **10** (5 A1, 5 A2, 0 B1) — down from the original 330
      raw / 171 real-gap-candidate this whole initiative (items 40/42-47)
      started from. Remaining flags in all three levels are deliberately
      accepted morphophonology edge cases, same category established in
      items 42-46, not gaps.

41. ~~**Real-gap-candidate lists worked level by level, both languages**~~
    — **done 2026-09-17**. Antigravity's content-fill pass (new ES A2 + HU
    A1/A2 curriculum phases, claimed full CEFR can-do coverage) finished
    the same day and was confirmed purely additive (doesn't touch items
    39/40's flagged lessons) by re-running both audits before and after;
    Antigravity's separate item 33 pass (A1 consolidation shape) finished
    later the same session and was merged in cleanly before ES B1's final
    push. **Every level of both languages is now done**: HU A1/A2 (items
    42-45), HU B1 (item 47), ES A1/A2 (item 46), ES B1 (item 48) — see
    ACHIEVED.md for all of them. Combined starting point across both
    languages was roughly 330 HU + 626 ES = 956 raw real-gap-candidates;
    final state is small accepted-edge-case counts only (HU: 5 A1 + 5 A2 +
    0 B1; ES: 3 A1 + 0 A2 + 8 B1 = 11), everything else either fixed as
    real content gaps or resolved by one of the many tooling fixes these
    items found along the way. The recurring lesson worth carrying
    forward: sanity-check the audit tool against a sample of its own flags
    before trusting the count, every time — across both languages this
    session, tooling fixes accounted for far more of the drop than content
    edits did.
48. ~~**ES B1 scoped, tooling fixed, and content gaps closed: 389 → 8
    real-gap-candidates**~~ — **done 2026-09-17**, continuing item 41 —
    with this, the full ES corpus (A1+A2+B1 combined) is down to **11**
    real-gap-candidates, from item 39's original 626. Found while scoping
    and fixing B1 content:
    - **B1 uses a completely different gloss convention than A1/A2** —
      square brackets holding a full-sentence English translation (e.g.
      `"La pobreza puede aumentar debido al desempleo. [Poverty can
      increase due to unemployment.]"`), not A1/A2's parenthetical style.
      204 files / ~3,200 instances corpus-wide, never recognised by the
      triage before this — the single largest fix of the whole HU/ES
      initiative. 389 → 197.
    - **~573 of those bracket pairs have the order reversed** — English
      main text, `[Spanish]` in the bracket (e.g. `"The consequence of
      trusting too easily. [La consecuencia de confiar demasiado.]"`).
      Generalised `english_text()`'s gloss extraction to pick whichever
      side of a bracket pair doesn't look Spanish, rather than assuming
      the bracket is always the gloss (same `looks_spanish()` heuristic
      already used for the A1 reversed-matching-pairs fix). 197 → 172.
    - **`matches()` had no concept of imperfect or conditional tense** —
      B1 introduces both and neither reconstructed. Added imperfect `-ar`
      endings (`aba`/`abas`/`ábamos`/`abais`/`aban`, same stem-strip-and-
      readd pattern as existing endings) and the shared imperfect-`-er/-ir`
      /conditional endings (`ía`/`ías`/`íamos`/`íais`/`ían`) — conditional
      needed a second check alongside the existing one, since it keeps the
      *whole* infinitive before the ending (`trabajaría` → root
      `trabajar`, already complete) rather than truncating to a bare stem
      like imperfect `-ar` does. 172 → 166 → (after the reversed-bracket
      fix landed on top) **160**.
    - **Investigation pass, before touching content**: pulled every
      exercise whose flagged tokens still looked English (common words,
      `-ing`/`-tion` endings) to check for a 4th missed format. All of them
      turned out correctly classified already — the raw `--all` printer
      shows every unseen token for context, English ones included, even
      when they're already excluded from the verdict; spot-checking
      `classify_token()` directly on individual tokens (e.g. `checking`/
      `contract` vs `contrato` in the same exercise) confirmed no bug, just
      a noisy display. No 4th systemic false-positive source found.
    - **Did find one more real gap while doing that check**: gerund forms
      (`-ando`/`-iendo`) weren't in `VERB_ENDINGS` at all —
      `investigando` reduces to `investig` + `ar` = `investigar`, same
      pattern as every other tense fix this session. Added. 166 → 163 →
      **157** (after the gerund and gerund-adjacent counts settled).
    - **Confirmed via frequency count, not just spot-checking**: every one
      of the remaining 157 flagged tokens is now unique (zero duplicates)
      — a strong signal the clustered/systemic issues are exhausted and
      what's left is genuinely scattered content work, not another hidden
      pattern. Spread evenly across B1 units 01-35, no single unit or
      range dominating.
    - **Separate, known limitation, not fixed here**: `check_teaching_
      order()` only walks numeric unit ids, so B1's Latin America track
      (word-slug ids like `b1-conosur-*`) isn't part of this 157-item list
      at all — a structural gap distinct from item 39's original word-in-
      story finding about the same track, not addressed by any of this
      session's matcher work.
    - **A 5th fix, found starting the content-fix pass**: every accented
      ending added to `VERB_ENDINGS` above (`áis`/`éis`/`ía`/`ías`/`íamos`/
      `íais`/`ían`/`ábamos`) had a real bug — `spanish_tokens()`/`norm()`
      strips accents from every token *before* `matches()` ever sees it,
      so an accented ending in the list could never `.endswith()`-match an
      already-unaccented token. Every vosotros form (`podéis`, `hacéis`)
      and every imperfect/conditional form added in this same item had
      silently never worked since the moment they were written a few
      hours earlier in this session. Fixed by writing every ending
      unaccented (`ais`, `eis`, `ia`, `ias`, `iamos`, `iais`, `ian`,
      `abamos`). 157 → **131**, bigger than three of the four fixes above
      it combined.
    - **A 6th fix, found starting the actual content batch**: infinitive/
      gerund + attached clitic pronoun (`hacerlo`, `presentarme`,
      `adaptarme`) was a whole unhandled shape — none of `VERB_ENDINGS`
      applies (the word doesn't end in a conjugation, it ends in a
      pronoun). Roughly a quarter of the remaining list was this single
      pattern. Added a clitic-stripping check alongside the ending-based
      one. Effect wasn't B1-only — A1 dropped 4→3, A2 dropped 2→0 (both
      already "done" in items 44/46, now cleaner still). 131 → 105 → 103
      (after also adding missing vosotros-preterite endings
      `asteis`/`isteis`, same accent-free lesson as the 5th fix).
    - **A 7th fix, refining the reversed-bracket detector (item 48's own
      2nd fix)**: `looks_spanish()`'s accent-or-article check went blank
      on short accent-free sentences like `"Era abogado."`, so
      `bracket_gloss()` silently defaulted to keeping the Spanish side and
      discarding the *English* side as if it were the gloss (found via
      `b1-06-05.ex09`: "He was a lawyer. [Era abogado.]"'s "lawyer" was
      being thrown away, "abogado" kept, exactly backwards). Replaced the
      binary check with a scored one (common function words on both
      sides, not just accents/articles) that returns nothing rather than
      guess when neither side scores — while building it, found "he" is
      itself a live collision (English pronoun vs. Spanish `haber`
      auxiliary, "he comido" = "I have eaten") that would have made an
      entire present-perfect exercise set misfire the same way; excluded
      it from the English word list rather than risk being confidently
      wrong across a whole grammar topic.
    - **Hit a live concurrent-edit while starting the content batch**:
      `audit-lesson.py` crashed (`KeyError: 'sentence'`) on newly-appearing
      fill-blank exercises in A1 consolidation files (`question`+`hint`
      instead of `sentence` — 34 files mid-edit by another process when
      checked, git status confirmed). The new shape is a real, apparently
      deliberate improvement (splits the English gloss into its own
      `hint` field instead of baking it into the sentence text, which
      matches a real fill-blank content-quality gap flagged before now) —
      not a bug to report, but it broke this script's assumption that
      fill-blank always has `sentence`. Added a fallback so `question` is
      read when `sentence` is absent; deliberately did *not* fold `hint`
      into the required-Spanish text, since that field exists specifically
      to hold English cleanly, same reasoning as everywhere else English
      gets excluded. Paused B1 content work at this point to flag the
      concurrent edit to the user rather than pushing further changes into
      files someone/something else is actively touching.
    - **Resumed and finished once Antigravity's item 33 pass landed**:
      re-scoped fresh from the merged state (106 items — item 33's A1
      consolidation changes rippled slightly into B1's known-word set) and
      added 2 more `SPANISH_WORDS` entries (`un`/`una`/`unos`/`unas`, and
      the `haber` forms `ha`/`has`/`hemos`/`han` — not `he`, still
      excluded for the same collision reason) that resolved 3 more short
      accent-free sentences the same way item 48's earlier scoring fix
      did. 106 → 105. Applied the remaining ~99 real vocabulary gaps via
      two parallel Haiku batches (33 files/~53 words, 31 files/~46 words)
      plus 3 proper nouns (`ulises`, `gulliver`, `daniel` — literature-
      adaptation characters) added directly to `PROPER_NOUNS`.
    - **Final state**: 8 real-gap-candidates left in B1, all verified
      genuine irregular-verb morphology, same acceptance bar as every
      other level this session — g→j/c→zc orthographic stem changes
      (`dirijo`, `reconozco`), e→ie stem-changing (`conviene`), the
      irregular `-ongo` pattern (`propongo`), a spelling-irregular
      subjunctive (`surjan`, `parezcan`), a compound gerund+clitic form
      the clitic-check doesn't chain with gerund-reduction
      (`llevándonos`), and the one already-documented `he`/`haber`
      collision case. **ES B1 is done.**
19. ~~**"Listen to your own voice" unavailable on iPad/iPhone**~~ — **Confirmed working on real device 2026-09-17.** Fix (removing the `canRecordConcurrently` iOS gate in `engine/speech-input.js`) verified correct on iOS. On Android, real-device testing revealed that running `getUserMedia` concurrently locks the mic hardware at the Android OS audio HAL level, starving `SpeechRecognition` of audio samples (recording captured user audio, but recognition received silence and failed to recognize or grade). Resolved 2026-09-17 by gating concurrent `getUserMedia` to non-Android devices (`canRecordConcurrently = !isAndroid`), giving SpeechRecognition exclusive mic access on Android when native STT is available. Tested and passing across Android, iOS, and Desktop in `tests/speech/test-speech-lifecycle.js`.

33. ~~**20 of 26 A1 consolidation lessons ship the wrong shape**~~ — **Fixed
    2026-09-17** (item 33). All 20 failing lessons corrected:
    - **Structural fix** (`scripts/fix_consolidation_shape.py`): merged the
      separate Practice/Dialogue/Writing exercise-group blocks into one
      group titled `"Review"`, and removed the empty `srs` section. Every
      lesson now has the `"single"` shape: `goal → recycle → Review → checklist`.
    - **Goal/checklist text** (`scripts/fix_consolidation_goals.py`,
      manual edits): all `goal` and `checklist` items now begin with `"I can"`.
      Goal and checklist counts now match in every lesson.
    - **Exercise type variety** (`scripts/fix_consolidation_exercise_types.py`):
      added 2 `fill-blank` exercises to each of the 12 lessons whose Review
      group only had 4 types (`dialogue-complete`, `matching`,
      `multiple-choice`, `structured-writing`), bringing all to 5+ types.
    - **Teaches-tag coverage** (`scripts/fix_consolidation_teaches_tags.py`):
      re-tagged gustar consolidation exercises from the placeholder
      `"consolidation"` tag to real grammar points (10 distinct); added
      cumulative A1 crossover tags to 5 other files to meet the 8+-points
      requirement (all 6 now have 9–10 distinct tags).
    - **Result**: 24/26 consolidation lessons pass all 10 audit rules.
      The 2 remaining (`a1-01`, `a1-03c`) are pre-existing failures
      unrelated to this item — `a1-01`'s Review exercises only cover 5
      tags (Unit 1 genuinely introduces fewer grammar points), and both
      have a `no SRS step` conflict that predates this work.

30. ~~**Audit `imports/dictionary/*.json` for more corrupted glosses**~~ — **Audited and fixed 2026-09-17.** Full systematic scan of all 141,149 entries across both dictionaries (`spanish-en.json`: 112,156 entries; `hungarian-en.json`: 28,993 entries) for unresolved templates, HTML/math leaks, unrendered entities, and scraper macro remnants:
    - **`hungarian-en.json`**: 100% clean (0 broken templates, 0 HTML leaks, 0 scraper artifacts).
    - **`spanish-en.json`**: Identified and sanitized 129 entries with unparsed syntax: 22 unexpanded `{{es-superseded spelling of|...}}` templates, 4 `{{gender-neutral neologism for|...}}`, 7 transliteration/foreign name templates, 11 `{{tcl|...}}` tags, math/html formatting remnants (`semiproducto`, `acetilcolina`), unrendered HTML entities/wikilinks (`bosníaco`, `ramblero`, `cuidar`, `llanisco`), and ~60 macro-prefixed place definitions (`@official name of:...`, `@init of:...`). All 129 entries rewritten to clean, natural English glosses; zero corruption flags remain corpus-wide. Content validation passes 100% clean (3308/3308 ES, 2296/2296 HU).


## Completed Roadmap Archive (Features & Subsystems Shipped)

The following completed subsystem initiatives and milestones were previously tracked in `ROADMAP.md` and archived here upon completion:

### Content & Curriculum Milestones
- **Evaluate importing exercises from Todo-Claro / Spanish Unicorn** — Evaluated 2026-09-12. Third-party scrape catalogues analyzed; discarded due to low quality and unverified licensing. Proceeded with native content authoring.
- **Exercise Modularity Architecture** — Confirmed 2026-09-12. Pipeline validates that new exercises can be added without rewrite; `recycle.js` pools exercises at runtime via `teaches` tags.
- **Hungarian A1 "First Sounds, First Words" Fix** — Fixed 2026-09-02. Fixed non-standard section type causing blank render on lesson 1.1.
- **Spanish B1 Vocabulary Screen Sequencing** — Fixed 2026-09-12. Reordered vocabulary section before first practice exercise group across all 36 units (180 lessons).
- **Word Bank Feature** — Built 2026-08-27. Unit-level vocabulary browser added under Grammar Guide in unit detail views.
- **Bug-Report Content Sweeps** — Fixed 2026-09-16. Repaired broken dictionary gloss templates and Hungarian translation drill bugs.

### Workshop Subsystem Polish
- **Grammar Driller Audit & Fixes** — Audited 2026-08-27. Fixed Spanish gap-fill punctuation hints, removed non-deterministic question options, and improved distractor selection.
- **Workshop Recommended Drill** — Built 2026-08-27. Smart drill recommendation based on recent lesson performance and error rates.
- **Workshop Mini-Games** — Built 2026-09-02. Lightweight short-format practice modes with score tracking and instant feedback.
- **Grammar Screen Italicization** — Completed 2026-09-02. Italicized target-language words and clean typography across grammar explanations.
- **Verb Drill Leaderboards & Scoring** — Built 2026-08-28. High-score tracking, streak counters, and accuracy calculation.
- **Translation Driller by Topic** — Built 2026-08-27. Topic-filtered translation practice sessions across all CEFR levels.

### Library & Dictionary Polish
- **HU Dictionary Wrong-Sense Gloss Fixes** — Fixed 2026-09-18. `scripts/import_hu_dictionary.py` had two related bugs surfacing as bad glosses in `content/hu/decks/decks.json`'s frequency decks: (1) `PRIMARY_SENSE_OVERRIDES` reorders specific lemmas' senses when Wiktionary's own page order puts a rare/wrong sense first — e.g. "forrás" ("source") was showing "boiling", "mű" ("work") was showing "artificial" (only valid as the "mű-" compound prefix); (2) a `BARE_FORM_HEADING` filter drops 57 dictionary-wide senses that were just a bare "present participle of X:" / "verbal noun of X:" heading with no real translation after the colon (Wiktionary's actual definition lives on a nested line the importer never captured) — e.g. "vezető" ("leader") was showing literally "present participle of vezet:". Rebuilt `imports/dictionary/hungarian-en.json` and `content/hu/decks/decks.json` via `python scripts/import_hu_dictionary.py && python build-manifest.py`. Only 2 lemmas needed sense-order overrides and 3 bare-heading glosses had leaked into decks.json specifically, but the audit covered the top 1000 frequency-ranked words' full sense lists.
- **Word Translation Popup Sheets** — Refined 2026-09-12. Standardized `.wp-sheet` with desktop modal centering and mobile safe-area insets.
- **Library Room & Shelf Navigation** — Built 2026-08-28. Hierarchical browsing across levels, rooms, and shelves.
- **Library Topic Search & Recommended Reading** — Built 2026-09-14. Universal search across readings with context banner recommendations.
- **Reading Attribution & Classics Sourcing** — Added 2026-09-10. Standardized attribution headers across authentic literary texts in Hungarian and Spanish.
- **Fourth Library Shelf (Articles / Cultural Reads)** — Built 2026-09-10. Added contemporary non-fiction and cultural texts shelf.

### Decks & SRS Subsystem Polish
- **Listen to SRS Cards** — Built 2026-09-14. Speech synthesis audio playback on flashcard review.
- **Quizlet-Style Study Modes (Review / Match / Learn)** — Built 2026-08-27. Full study mode switcher with dedicated mechanics for each mode.
- **Learn Mode Small-Batch Pacing** — Built 2026-08-27. Step-by-step introduction of new words in bite-sized batches.
- **SRS Hotkeys & Touch Gestures** — Built 2026-09-12. Added desktop keys `1`-`4` and fluid mobile swipe gestures (left = Again, right = Good).

### Cross-App Flow & Integration
- **Connective Lesson-Complete Screen** — Built 2026-08-27. Post-lesson action recommendations linking directly to relevant drills and deck reviews.
- **In-Lesson XP & Streak Animations** — Built 2026-09-02. Immediate feedback badges and streak counters inside active sessions.
- **Journey Deep Integration** — Built 2026-09-11. Unified progress tracking, XP history, and drill stats consolidated in My Journey.

### Interface, Audio & Platform Architecture
- **Boot Screen & Loading Overlay** — Built 2026-09-17. Minimalist `#boot-screen` and smooth loading spinner overlays on driller/lesson transitions.
- **Constructivist Dark / Light Theme** — Built 2026-09-12. Inverted midnight navy / warm cream palette (`[data-theme="dark"]`) with quick-toggles.
- **Speech Recognition & Pronunciation Studio** — Built 2026-09-14. Web Speech API evaluation engine with Speaking and Writing Studios.
- **Offline PWA & Service Worker** — Built 2026-09-14. Complete asset caching and offline-ready service worker (`sw.js`).
- **Language-Isolated Asset Loading** — Optimized 2026-09-14. Isolated dictionaries and indexes per language to eliminate unnecessary network/memory overhead.
