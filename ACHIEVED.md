# Achieved

Completed work archived out of `ROADMAP.md` so the active document stays
readable — the queue there tracks what's active/planned, this file is the
historical record of what's already shipped. Entries keep their original
queue numbering and wording (not renumbered or edited) so old references
and commit messages that cite an item number still resolve. Nothing here
needs re-reading before starting new work; it's reference only.

## Completed queue items

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
