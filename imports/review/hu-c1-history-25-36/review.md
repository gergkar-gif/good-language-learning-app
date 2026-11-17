# HU C1 culture history rewrite, round 1: Culture Units 25–30 (2026-11-17)

User's decision (2026-11-17): Units 25–36 are rewritten as history of 2010 to spring 2026. Round 1: constitutional-breakdown, media-capture, healthcare-crisis (agent A); railway-decay, cultural-policy, pendulum-politics (agent B). Brief `scripts/templates/edit-hungarian-c1-history.txt`, prompts here.

- Agents (Sonnet, edit in place, three units each): A 410,757 tokens on its resumed run (its first run, stopped by the 5-hour limit, was not reported); B 321,117 (18.5 min). Both stopped by the usage limit once; A resumed with SendMessage after the reset.
- Every text, screen, item, goal and challenge rewritten; new neutral dated unit, lesson and story titles (unit ids and skill slugs unchanged). check-content 0 errors / 0 suspects in all six before freezing (3 accepted `vocab-unused` later), `check_c1_forms` 0, `validate-content` passes. 36 challenges, 42 glosses.
- Reviewer's fact changes (`reviewer-facts.md`): branch lines (10 lines from 1 Aug 2023, MÁV, not "the ministry"); motorway concession (May 2022, ~1,200 km, most of the network); Budapest–Belgrade dates softened, "Serbian section" narrowed to Belgrade–Novi Sad; PKÜ founding softened; EP 2022 "electoral autocracy"; removed as unconfirmed: Semjén as sponsor of the 2023 chamber law, the hospital-debt figures (53 hospitals, 35 suppliers, 98.4bn), the Klubrádió year, the 37 % and 70 % targets, the nurse survey and emigration figures, the 700bn programme cost; the items, goals and challenges that repeated them rewritten. Backticks in screens replaced by italics (47).
- The combined unit readings of all six restitched, with neutral Hungarian titles and summaries (the agents were told not to touch them; the reviewer missed this for 28–30 at first and caught it at round A's report).
- Walked 84/84 (with Culture Units 1–8): the first run failed 6 lessons because a one-time Guide note under a short story covers the Continue button (`engine/guide.js`, `lesson-tap-word`); the walk now closes it like a learner would. **For the user:** the note covering Continue is a small real UI defect.

## Open
- **For the user:** the vocabulary skills of these units keep one-sided titles in `skills/hu.json` (`c1-constitutional-breakdown-vocab`, `c1-media-capture-vocab`, `c1-healthcare-crisis-vocab` …); the skill list is frozen, so retitling needs your sign-off.
- Round 2: Culture Units 31–36 (historical-revisionism, judicial-independence, literary-canon, mta-ceu, pegasus-scandal, civil-society).
