# Unit pipeline: prompts, measurements, process reviews

How the reviewer (Claude) runs units through Sonnet agents, what each step
costs, and what changed at each review. **Every 2 finished units, the
reviewer reviews the process** (decided by the user 2026-10-13, under
time and usage pressure): add the units' numbers to the table, compare
with the previous rows, pick one or two changes that cut tokens or
reviewer work without losing defects, record them below, and apply them
to the next units. Repeated defects go into `docs/unit-agent-rules.md`
§ 6 at once; a recurring problem gets a script (§ "Script recurring
problems").

## Pipeline (current, as HU A1 was finished 2026-10-13/14)

Read this before working on any unit. Agents read only
`docs/unit-agent-rules.md`; the reviewer (Claude) runs the steps below.

0. **Knowledge sheet** for each unit (from 2026-10-14):
   `python scripts/prior_knowledge.py <course> <level> <unit id> --out
   <worktree>/prior-<unit id>.md`: known grammar and words by unit, every
   earlier screen title, what this unit teaches, what comes later. Give
   its path to the regenerating and the reading agent instead of "read the
   earlier units" (~7k tokens a unit).
1. **Regenerate two units per Sonnet agent** (a pair costs ~119k a unit
   against 160–267k single; the second unit re-teaches the first's
   material more often, so the prompt points at both units' sheets and
   says "recap, never new"). Real, decent content can go read-first
   instead (step 2, then decide). Each agent works in its own worktree:
   `git worktree add --detach /home/user/parlour-<job> HEAD`, removed after.
2. **Take each commit:** `python scripts/take_unit_commit.py hu a1 <unit
   id> <commit>` (cherry-picks, resolves the `challenges.json` and
   `word-lesson-index.json` conflicts, runs the checks).
3. **Paired blind read** by one Sonnet agent (report only, ~83–108k a
   unit). From 2026-10-14 the reader also writes its fixes as JSON, one
   file per unit (`<worktree>/fixes-<unit id>.json`, format in
   `scripts/apply_replacements.py`: exact `old`/`new` text or an `id` with
   `set` fields; every fix carries the exercise `id`, `"kind":
   "hungarian"` when it changes Hungarian, `"sure": false` when unsure).
4. **Check the fixes by script:** `python scripts/check_fixes.py <course>
   <level> <unit id> <fixes.json>` applies them to a scratch state, runs
   check-content, restores the files, and splits them into rejected (no
   exact match, or a new finding on its exercise), review (Hungarian or
   unsure) and auto. **Read only the review list and the report's
   non-fix notes**; readers propose wrong Hungarian a few times per level
   (*Nem van tej*, *szürkét*). Record the outcome in
   `imports/review/sonnet-reads/<course>-<level>-<unit id>.md` (Applied /
   Not taken with reasons).
5. **Apply:** `python scripts/apply_replacements.py <fixes>.auto.json`,
   then the review file after deleting what you don't take. No Haiku
   fixer needed when the reader's JSON is good; for a list without JSON,
   write the JSON yourself (short lists) or give it to Haiku (long ones).
6. **Check after every hand edit**, not only at freeze:
   `python scripts/check-content.py <course> <level> <unit id>`; then
   `lock_tags.py --update`, `freeze_unit.py` (`--accept
   "<check>:<id>:<reason>"` for deliberate suspects), commit, push.
   Refreezing a frozen unit keeps its earlier reason and accepted
   findings.
7. **Every 2 units:** process review below; a repeated defect goes into
   `docs/unit-agent-rules.md` § 6 the same day, and anything recurring
   gets a script (below).

At most 2 agents at once (CLAUDE.md). Never let an agent bypass hooks.

### Script recurring problems (user, 2026-10-13)

When an issue shows up a second time, stop fixing it by hand or by prompt
and write a Python script, in the same session:

- **A recurring content defect → a check** in `scripts/check-content.py`:
  an error when the rule is certain (`ik-first-person`, `vocab-duplicate`,
  `ds-on-answer`), a suspect when it needs a reader's eye
  (`consolidation-copy`, `reported-question`, `glued-blank`,
  `article-blank`, `take-gloss`). Run it over the whole course at once:
  that is how hits in already-frozen units were found. Add the rule to
  `docs/unit-agent-rules.md` § 6 and AGENTS.md's checker list.
- **A mechanical fix that is always the same → a fixer script**, never a
  prompt. It must refuse rather than guess: write nothing unless every
  change matches exactly (`apply_replacements.py`), and run the checker
  after.
- **A recurring chore or conflict → a script**: `take_unit_commit.py`
  (cherry-pick + the two conflicts every parallel unit causes),
  `merge_challenges.py`, `freeze_unit.py` (refreeze keeps history),
  `walk_lessons.js` (play every lesson), `fill-dictionary-gaps.py merge`
  (dictionary additions survive rebuilds).
- Test a new check on the existing content before trusting it: look at
  its first hits, tighten it until they are real (false positives such as
  the B1/C1 *az* pronoun hits are noted in the process review), and record
  the count.

### Who does what: model choice (measured on HU A1)

(From 2026-10-14 the reader's JSON plus `check_fixes.py` replaces the
Haiku fixer for most lists; see Pipeline steps 3–5. Measure the first A2
pairs against the A1 rows before trusting the saving.)


| Job | Model | Why |
|---|---|---|
| Regenerate units (2 per agent) | **Sonnet** | Writes usable Hungarian; ~119k/unit paired. |
| Blind read (report only, 2 units per agent) | **Sonnet** | Finds ~10–25 real defects/unit; Haiku is too weak to find them. |
| Filter the read into a fix list | **Claude (main session)** | Readers propose wrong Hungarian a few times a level; only the filter catches it. Never delegate this. |
| Apply a filtered list, exact old → new | **Claude** with `apply_replacements.py` for short lists (≤ ~40 items); **Haiku** for long ones | Haiku applied 9/9, 11/11, 17/17, 19/19 exact items with no improvisation (74–131k); its only slips came from vague items in Claude's list ("only if that is the exact text"). Doing it directly is cheaper when the list is short. |
| Mechanical translation (e.g. story questions → English) | **Haiku** | 36 questions, 77k, 1 min, all right. Under ~10 items: Claude directly. |
| Build a tool (e.g. the walk test) | **Sonnet**, own worktree | 152k; review and rerun its output before taking it. |
| Judgement calls, registry/skill questions, anything for the user | **Claude**, ask the user | Never left to an agent. |

How to delegate:

- **At most 2 agents running at once** (CLAUDE.md); count before launching.
- Each agent gets its **own worktree** (`git worktree add --detach
  /home/user/parlour-<job> HEAD`) and the rulebook `docs/unit-agent-rules.md`
  only; the prompt templates below say the rest. Name exact files, stems,
  earlier units' ranges and what earlier units own.
- Every prompt says: never bypass hooks or change git/tool config; report
  only (reads); quote option text when naming an option; give fixes as
  exact old → new.
- An agent's report is a claim, not a result: check its Hungarian, rerun
  its commands, take its commit with `take_unit_commit.py`.
- **Usage limits:** a Sonnet weekly limit stops an agent within seconds
  ("resets <time>"). Tell the user and offer: wait, do it in the main
  session, or a weaker Haiku pass. Don't silently downgrade a read to
  Haiku.

### Before calling a level done

Count with the tools before giving the user any number, and say what is
not verified:

- `python scripts/freeze_unit.py --status`: every unit frozen.
- `python scripts/check-content.py <course> <level>`: 0 errors; every
  suspect fixed or accepted (copies, reported questions, glued blanks…).
- `python scripts/validate-content.py --warnings`: none for the level
  (`thin_ok` in `skills/<lang>.json` for a skill the user lets stay thin).
- `node scripts/walk_lessons.js <course> <level>` with
  `python scripts/dev-server.py 8131` running: every lesson plays to its
  summary with no console errors and no failed requests (TTS is stubbed;
  `--live-tts` and the live site can't be reached from the cloud
  container; the user checks audio).
- Not covered by any of this: speaking/challenge steps, wrong-answer
  paths, and a native speaker's eye (the user spot-checks).

## Prompt templates

Fill `<…>`. Each agent reads `docs/unit-agent-rules.md` and nothing else
by default. Reads end with "fix as an exact old → new replacement; quote
the option text whenever you name an option" and "Run ALL its § 5
commands"; regenerations get the unit's taught/not-yet-taught list
(verbs, cases, *is*, -ik, accusative) spelled out.

**Read.** "You are reviewing one unit of a Hungarian course (Parlour app)
for a learner who knows only English, to find everything wrong with it.
REPORT ONLY: edit, create or commit nothing; change no git or tool
config. Work only in `<folder>`. Unit `hu a1 <unit id>`: lessons
`<stems>`, story `<story stem>`; earlier units `<range>`. Read
`docs/unit-agent-rules.md` first; it is your rulebook (open other docs
only to settle a point it doesn't cover). Run its § 5 commands. Read
every exercise, screen, challenge, goal, checklist, speaking step and the
story, checking § 1–4 and every item of § 6. Skip what check-content
reports. Focus: `<unit-specific grammar to watch>`. Report grouped: 1.
Found by reading; 2. Metadata; 3. Challenges / goals / checklists; 4.
Doubtful. One line each: id, problem quoting the text, fix; mark
uncertain items (unsure). Don't pad. What the learner knows before this
unit is in `<prior sheet path>` (read it first; anything listed there
presented as new is a defect). Also write every fix you give as JSON in
`<fixes path>`, in the format at the top of
`scripts/apply_replacements.py`, each with its exercise or challenge
`id`, `\"kind\": \"hungarian\"` when it changes Hungarian text and
`\"sure\": false` when unsure; quote `old` exactly from the file (that
file is the only one you may create)."

**Regenerate.** "Regenerate hu a1 unit `<n>` `<unit id>` (`<stems>`) in
`<folder>`. Rulebook: `docs/unit-agent-rules.md`; shape:
`docs/course-generation-brief.md` § 2.2/2.3 (read only those). Rewrite
both screens per lesson, story, exercises, goals/checklists, challenges;
keep ids and stems. What the learner already knows is in `<prior sheet
path>`: use it instead of opening earlier units; anything in it is
presented as known (\"You know …\"), never as new. `<unit-specific points>`. Run § 5 checks, fix
everything, lock tags, don't freeze. Commit normally with start/finish
times; report the commit, per-lesson points, and Hungarian you are unsure
of."

**Fix.** "Apply the fix list `<file>` to hu a1 `<unit id>` in `<folder>`.
Rulebook: `docs/unit-agent-rules.md`. Apply every Applied item, nothing
under Not taken; re-lock; run § 5 checks; don't freeze; commit normally
listing each item."

**Read, paired (HU A2 pass, 2026-10-14; challenges added 2026-10-14; report file, same-family list, compound glosses and up to three units per reader added 2026-10-14).** Fill `{W}` (reader worktree), `{N}` (number of units: TWO or THREE), one `- hu a2 …` line per unit with its unit id, stems (space-separated) and story (`a2-unit-NN`), and `{REPORT}` (`report-<first unit>.md`); put the `prior-<unit>.md` sheets in `{W}` first. Afterwards: `check_fixes.py` per unit, read the review lists, then `merge_fixes.py` over all the filtered lists (it refuses when two readers fixed the same item differently), `apply_replacements.py` on the merged list, and the readers' compound glosses through `fill-dictionary-gaps.py import`.

```
You are reviewing {N} units of the Hungarian A2 course (Parlour app) for a learner who knows only English, to find everything wrong with them. REPORT ONLY: edit, create or commit nothing except the fixes, challenges and report files named below; change no git or tool config; never bypass hooks. Work only in `{W}` (absolute paths).

Units (read all; a later unit must not present an earlier one's material as new: recap, never new):
- `hu a2 {U1}`: lessons {S1}, story `{ST1}`. Knowledge sheet: `{W}/prior-{U1}.md`. Fixes file: `{W}/fixes-{U1}.json`. Challenges file: `{W}/challenges-{U1}.json`.
- `hu a2 {U2}`: (same pattern)
- `hu a2 {U3}`: (same pattern; omit this line for a pair)

Read `{W}/docs/unit-agent-rules.md` first; it is your rulebook (open other docs only to settle a point it doesn't cover; it says "a1" in command examples: use `a2`). Read each knowledge sheet before its unit: anything listed there presented as new is a defect, and anything in its "Same family … taught at B1" list that the unit presents or drills is a defect too (report it: either the lesson goes beyond A2 or the skill's level is wrong). Run its § 5 commands for every unit (`python scripts/check-content.py hu a2 <unit id>`, `node scripts/render_lesson.js hu <stems>`, `node scripts/audit-reader-coverage.js hu --story <story stem> --top 0`). Read every exercise, screen, goal, checklist, speaking step and the story as rendered, checking § 1–4 and every item of § 6. Also write a fix for every check-content ERROR (length give-aways: make the wrong options as long as the right one, or shorten the right one, with met words and one fault each; shared checklist lines: reword one). Suspects: fix unmet words in options/prompts with met words; leave consolidation copies and characters' names alone. Do NOT report: missing Listening groups or exercise counts below the brief's numbers (course-wide, parked); vocabulary lists re-listing earlier words; sentence-builder alternative orders.

Known false positives (don't report): *Szabad vagy foglalt vagy?* (natural); *ki* as a literary relative is acceptable Hungarian, so never propose it as a wrong option; a wrong option must never be a possible true answer (*szekrényen* for where clothes are); consolidation items reusing lesson items (the user wants replays). A2 focus: past tense and definite/indefinite conjugation used before taught (see `taught_in` in `skills/hu.json` and the sheet's "later" list); cases taught later (-hoz a2-31, -nál a2-13, -ra/-re a2-29, translative a2-171); plural possessed (-aim, -ai) before a2-13/a2-191; wrong `teaches` (a tested form → its grammar skill, a tested word → the unit vocabulary skill); `distractor_skills` on ungrammatical options; screens restating known A1 material as new.

Write one challenge per lesson of each unit, consolidation included (six per unit), to the unit's challenges file: a JSON object keyed by lesson stem, each entry with exactly the fields of the entries in `{W}/content/hu/curriculum/challenges.json` (`tier` "tier1", `level` "A2", `title` "Communicative Challenge: …", `scenario`, `prompt`, `cues`, `target`, `english`, `canDo`), following the rulebook § 4 (the story's people; cues say what to include, never the words; target 1–3 sentences of met words using the lesson's grammar; `canDo` = the lesson's first checklist line, copied after your own checklist fixes). Report grouped: 1. Found by reading; 2. Metadata; 3. Goals / checklists; 4. Doubtful. One line each: id, problem quoting the text, fix; mark uncertain items (unsure). Don't pad. Also write every fix as JSON in the unit's fixes file, in the format at the top of `scripts/apply_replacements.py`, each with its exercise id, `"kind": "hungarian"` when it changes Hungarian text and `"sure": false` when unsure; quote `old` exactly from the file; when naming an option, quote its text.

Write your full report (the four groups above, plus a 5. Dictionary group: every "literal compound guess" word from the audit as `word | lemma | pos | gloss |`, one per line) to `{W}/{REPORT}` before you finish, and end your reply with that path; your reply may be lost if the session restarts, the file is not. With three units, finish and write each unit's fixes and challenges files before starting the next unit.
```

**New unit (from scratch; written 2026-10-14 for HU A2 units 45–47).** Fill `{W}` (the agent's worktree), `{SHEET}` (`prior_knowledge.py` output), `{UID}`, `{TITLE}`, `{NUM}`, `{S1}`…`{S5}` (lesson stems), `{PLAN}` (from `docs/hu-a1-a2-cefr-gap-proposal.md`) and `{EXTRA}` (unit-specific notes). Add the unit's row to the unit table and its vocabulary skill to `skills/<lang>.json` / `frozen-<lang>.json` in the agent's worktree before it starts (the validator needs both, and they go in the same commit as the lessons).

```
You are writing ONE NEW unit of the Hungarian A2 course of the Parlour language app, from scratch. Work ONLY in `{W}` (a git worktree; absolute paths). DO NOT COMMIT (the main session collects your files). Never change git or tool config, never bypass hooks.

Read first, in this order, and nothing else unless needed to settle a point:
1. `{W}/docs/unit-agent-rules.md` (rulebook: met words, exercises, metadata, screens, challenges, known defects).
2. `{W}/docs/course-generation-brief.md` § 2 (shape), § 3 (screens), § 4 (vocabulary), § 5 (story), § 6 (exercises), § 7 (tags), § 9.1 (Hungarian).
3. The knowledge sheet `{W}/{SHEET}`: everything the learner knows (all of A1–A2 grammar and 1600 words). Every A2 grammar skill is known by now; anything on the sheet is presented as known ("You know …"), never as new.
4. As a JSON-shape model, the existing lesson `content/hu/lessons/a2/a2-160.json` with its screens, vocabulary, exercise file and story `content/hu/stories/original/a2/a2-unit-32.json`, and challenge entries in `content/hu/curriculum/challenges.json` (A1 entries show the format; key = lesson stem). Copy field names exactly; never invent fields.

The unit (already in `content/hu/curriculum/units/a2.json` and `skills/hu.json`):
- unit id `{UID}`, title "{TITLE}", unit number {NUM} (lesson field `"unit": {NUM}`), vocabulary skill `a2-{UID}-vocab`.
- lessons `a2-{S1}` … `a2-{S5}` and `a2-{S5}-consolidation` (lesson ids `lesson.a2.{S1}` …; files `content/hu/lessons/a2/<stem>.json`, screens `content/hu/grammar/a2/<stem>-a-gr.json` and `-b-gr.json`, vocabulary `content/hu/vocabulary/a2/<stem>-voc.json`, exercises `content/hu/exercises/a2/<stem>-ex.json`, story `content/hu/stories/original/a2/a2-unit-{NUM}.json` on lesson `a2-{S5}`, consolidation exercises `a2-{S5}-consolidation-ex.json`).
- Lesson plan (adjust if a better order emerges, keep the topic): {PLAN}

Rules specific to this job:
- The A2 skill list is CLOSED: no new grammar skills. Each lesson's two screens either (a) present the lesson's key words/phrases as a pattern table (like the existing A2 screen "híd, folyó, Duna: The River and the Bridge"), or (b) apply a known A2 grammar skill to the theme, saying "You know …". Exercises are tagged with the unit vocabulary skill (word meaning) or the existing grammar skill whose form a wrong answer shows (skill slugs from `skills/hu.json`; `taught_in` must be before this unit, which is true for all A1–A2 skills).
- About 20–25 new words over the unit (check each against the knowledge sheet: a known word is used, not re-listed), British English glosses, same `theme` label in all five vocabulary files.
- Exercise counts and section order per brief § 2.2 (A2: Introduce 2, Controlled 4, Practice 4, Listening 2 (`listening-choice`, `dictation`), Dialogue 2, Production 2, Check 2; lesson {S5} also has the story and a Reading group of 3), consolidation per § 2.3 (20 items, 4 groups of 5). Look at an existing A2 listening item shape in the HU B1 or Spanish A2 exercises if you need one (`grep -rl listening-choice content/*/exercises | head`).
- Story 120–200 Hungarian words, the course's A2 characters (see a2-unit-32: Meg, Károly and friends), 3 comprehension questions; Hungarian setting; facts only when certain.
- One challenge per teaching lesson (`a2-{S1}`…`a2-{S5}`) in `content/hu/curriculum/challenges.json`, `"level": "A2"`, tier as in the file, target 1–3 sentences using met words, `canDo` = the lesson's first checklist line.
- Characters' names and the story move forward naturally; this unit is not another unit with nouns swapped.
{EXTRA}

Then run from `{W}`: `python scripts/build_word_lesson_index.py hu`; `python scripts/check-content.py hu a2 {UID}` (fix EVERY error; fix or justify each suspect); `node scripts/render_lesson.js hu a2-{S1} a2-{S2} a2-{S3} a2-{S4} a2-{S5} a2-{S5}-consolidation` and read every screen and item as rendered (`!!` = error); `node scripts/audit-reader-coverage.js hu --story a2-unit-{NUM} --top 0`; `python scripts/validate-content.py --changed` (fix everything it reports); `python scripts/lock_tags.py hu a2/{UID} --update --reason "new unit (CEFR gap check, 2026-10-14)"`.

Report concisely: files created, word list, per-lesson topic and screens, check results, every Hungarian line or fact you are unsure of.
```

## Measurements

| Date | Unit | Route | Regen / fix (tok, min) | Read (tok, min) | Real defects in read | Notes |
|---|---|---|---|---|---|---|
| 10-10 | 8 plurals-quantities | Sonnet regen (pilot A) | 251k, 16 | 153k, 4.5 | ~21 | |
| 10-10 | 9 possession | read → fixer (pilot B) | 298k, 23 | 159k, 7.5 | ~14 | |
| 10-13 | 8 + 9 | pilot fix lists, one Sonnet fixer | 142k, 4.5 | | | both units in one agent |
| 10-13 | 11 where-things-are | Sonnet regen | 267k, 14 | 155k, 5.5 | 9 applied | frozen; agent bypassed hooks (now forbidden) |
| 10-13 | 10 foundations-review | Sonnet regen | 245k, 9 | 187k, 5 | ~15 to filter | |
| 10-13 | 8 (second read) | | | 161k, 5 | 8 applied | found a wrong pilot fix-list item |
| 10-13 | 9 (second read) | | | **123k, 3.5** (rules sheet) | 10 applied, 1 false | first read on the rules sheet |
| 10-13 | 8 + 10 fixes | **Haiku** applies filtered lists | 118k Haiku, 2.5 | | all 17 items right | the one slip was in Claude's list |
| 10-13 | 9 fixes | Claude directly | | | | short list |
| 10-13 | 12 going-places | Sonnet regen (rules sheet) | 171k, 9 | 125k, 4.5 | 9 applied | |
| 10-13 | 13 everyday-actions | Sonnet regen (rules sheet) | 204k, 11 | 106k, 2 | 8 applied | read skipped 2 commands |
| 10-13 | 12 + 13 fixes | Haiku | 115k Haiku, 3 | | 16/17; 1 skipped, 1 wrong | both caused by Claude's list |
| 10-13 | 14 questions-negation | regen + § 6 self-check | 171k, 9 | 113k, 2.5 | 9 applied | |
| 10-13 | 15 daily-routine | regen + § 6 self-check | 214k, 12 | 135k, 4 | 11 applied | |
| 10-13 | 14 fixes | Haiku, exact old → new list | 74k Haiku, 1 | | 9/9 | |
| 10-13 | 15 fixes | Haiku, exact old → new list | 83k Haiku, 3 | | 11/11 | |
| 10-13 | 16 time-dates | read first (real content) | | 132k, 4 | 40+ | → regenerate |
| 10-13 | 16 time-dates | Sonnet regen | 177k, 10 | 112k, 3 | 6 applied | Claude applied directly |
| 10-13 | 17 frequency-word-order | verdict-first read → regen | 181k, 9 | 90k + 121k | 9 applied | read caught a reversed answer key |
| 10-13 | A1 story questions ×12 | Haiku translation | 77k Haiku, 1 | | 36 questions | for the English toggle |
| 10-13 | 18 home | regen, no verdict read | 204k, 11 | 126k, 3.5 | 9 applied | |
| 10-13 | 19 food-drink | regen, no verdict read | 160k, 8 | 127k, 4.5 | 10 applied, 1 false | read claimed *Nem van tej.* is correct |
| 10-13 | 20 everyday-hungarian-review | regen (review unit) | 267k, 12 | 191k, 5 | 10 applied | review units cost ~40% more |
| 10-13 | 21 buying-food | regen | 213k, 11 | 137k, 4 | 9 applied | two-right-answer blanks via English "take" |
| 10-13 | 22 market | regen | 217k, 13 | 167k for 22+23 (**83k/unit**), 5.5 | 12 applied | paired read |
| 10-13 | 23 cafe | regen | 180k, 9.5 | (paired) | 7 applied | |
| 10-13 | 22 + 23 fixes | Haiku | 110k Haiku, 2.5 | | 19/19 | |
| 10-13 | 24–33 | paired regen + paired read | ~119k/unit | 83–108k/unit | ~25/unit | numbers in the process reviews below |
| 10-14 | walk test build | Sonnet | 152k, 10.5 | | | HU A1 198/198 in 4.5 min |
| 10-14 | HU A2 25–28 | paired read (2 units/reader) | | 235k + 235k, 10.5 | 128 applied of 132, 0 rejected | ~59k reader tokens/unit; 1 skill-level clash (a2-140) found only via the batch note |

Reads before unit 9's second read used the full docs (brief, AGENTS, spec, registry).

## Process reviews

### 2026-10-13 (after units 10, 11)

- Cost per finished unit ≈ 450k Sonnet tokens on either route; reads
  (150–190k) mostly re-read the same four docs. **Change:** this rules
  sheet replaces them for every agent; templates above replace hand-written
  prompts. Measure on unit 9's second read against the 155–187k reads.
- Reviewer's own cost: filtering by checking each claim in the files is
  where errors were caught (wrong pilot item, "Harminc éves" two-answer
  item), so it stays.
- Done: `check-content.py` `vocab-duplicate` (error); it also found
  *foto* twice in es-es/es-latam `a1-03-01-voc` (left for the Spanish A1 pass).
- Next candidates: a check for `distractor_skills` on non-word options (the Reader
  lexicon can tell a non-word); Haiku for applying an already-filtered
  fix list.

### 2026-10-13 (after units 8, 9, 10 frozen)

- **Rules sheet:** unit 9's read cost 123k / 3.5 min against 155–187k /
  5 min, with as many real findings (and one new class: challenge scenarios
  not naming the target's object). Keep it; every agent uses it.
- **Haiku for applying a filtered list:** 17/17 items right, 118k Haiku
  tokens, 2.5 min, no improvisation. Use Haiku for every fix list from now
  on; Sonnet only for regeneration and reads.
- **Reviewer slips found by the next step:** twice the reviewer's own list
  put `distractor_skills` on the wrong option (pilot a1-44 items; a1-38-check-2,
  where the option order differed). **Change:** a list item naming an option
  index must quote the option text, and the fixer checks the text matches
  before editing. Added to the rules sheet § 3.
- Reads still produce ~1 false claim each (*táskája* does not lengthen):
  filtering against the files stays.

### 2026-10-13 (after units 12, 13 frozen)

- **Cost per unit is down ~30%:** regeneration 171–204k (was 245–267k),
  read 106–125k (was 155–187k), Haiku fix ~58k Haiku. About 300k Sonnet +
  60k Haiku per stub unit, ~25 min wall time with two units in parallel.
  Projection for the 20 HU A1 units left: ~6–7M Sonnet tokens (was ~9M).
- **Remaining errors are the reviewer's fix lists:** a conditional item
  ("only if that is the exact text") made Haiku add *i, í* to a vowel list
  the screen's own tip contradicts; an item asked for `answers` next to
  `answer`, which the schema rejects (`answers` replaces `answer`).
  **Change:** fix-list items are exact old → new replacements, no
  conditionals; field shapes are checked against an existing item first.
- **Regenerators still write words whose meaning needs a form not yet
  taught** (*hallgat* alone = "is silent"). Added to rules § 6.
- **New checks (user: script every repeat defect):** `ds-on-answer`,
  `ds-own-skill` (0 hits course-wide: guards), `glued-blank` (HU suspect: a
  blank glued to a stem in *-a/-e* with a lengthening suffix as the answer;
  3 real hits in B1: b1-18-03.ex03, b1-26-05.ex02, b1-30-03.ex05; one false
  positive, a verb, b1-33-04.ex02).
- `unmet-word` now also scans challenge targets. (It briefly scanned
  stories too; the user ruled 2026-10-13 that stories may use unmet words.)
- **Next to try (units 14, 15):** have each regenerator run a self-check
  against rules § 6 and list what it checked, to see if the read finds
  fewer defects; keep two units in parallel.

### 2026-10-13 (after units 14, 15 frozen)

- **§ 6 self-check in regeneration: dropped.** Reads still found 9–11
  real defects per unit (same as without it) and regeneration cost the
  same or more (171k, 214k).
- **Reads propose exact old → new fixes: kept.** The fix list is then a
  near-copy, Haiku's pass fell to 74–83k / 1–3 min, all items right.
- **Real-content units: read first, then decide.** Unit 16's read found
  40+ defects (no challenges, generic checklists, forms taught later, an
  incoherent story): regenerate when a read finds more than ~30 or the
  challenges/checklists are missing or generic; else fix.
- **New checks this round:** `ds-on-answer`, `ds-own-skill`,
  `glued-blank`, and `unmet-word` over stories and challenge targets;
  `scripts/merge_challenges.py` for parallel-unit conflicts.
- Running cost per stub unit now ≈ 190k regen + 120k read Sonnet + 80k
  Haiku; ~4 units/hour with two agents.

### 2026-10-13 (after units 16, 17 frozen)

- **Verdict-first reads** on old units cost 90k (vs 130k) and decide
  regenerate/fix before anyone pays for a full defect list. Keep for every
  unit not yet read.
- **Regenerated units so far all needed regenerating** (8–17 except 9):
  units 18–33 are probably the same; verdict-first read stays as the gate.
- **Short fix lists (≤ ~8 text edits): the reviewer applies them directly**
  (unit 16, 17); Haiku only for longer lists — the agent's own setup
  (~50k) outweighs a few edits.
- **A read caught a reversed answer key** (a1-84-check-2) that every check
  passed. No script can tell which option is right; reads stay.
- **English toggle (user, 2026-10-13):** A1 comprehension questions in
  Hungarian with `questionEnglish`/`optionsEnglish`; done for units 1–7, 9,
  11–15, 17. The rest (units 8, 10, 16 need Hungarian questions; 18+ need
  English) is done by Sonnet once all units are finished (user).

### 2026-10-13 (planning units 18–33)

- A scripted survey of units 18–33 (check-content counts, challenge entries,
  distinct screens) finds every one with **no challenges** and 18–30 with
  generic checklists shared across lessons: the pattern that sent 16 and 17
  to regeneration. **Change:** regenerate them directly, no verdict read
  (saves ~90k Sonnet per unit, ~1.4M in all); each still gets one blind
  read after regeneration.

### 2026-10-13 (after units 18, 19 frozen)

- Direct regeneration (no verdict read) worked: 18 and 19 needed only
  short fix lists (9–10 items). Keep.
- `scripts/take_unit_commit.py` replaced the hand-written cherry-pick and
  conflict sequence.
- Reads keep producing ~1 false Hungarian claim per unit (*Nem van tej.*,
  *táskája*): filtering stays with the reviewer.
- Reviewer's own slips this round: none found by the next step.

### 2026-10-13 (after units 20, 21 frozen)

- Review units cost ~40% more (read every earlier unit): budget ~460k for
  unit 25 and the A1 end review.
- New repeat defect: English glosses that let two conjugations fit
  ("take" for *kérem*/*veszem*). Added to rules § 6.
- Units 21 and 22 overlap in topic (market lesson in 21): the regeneration
  prompt now names what the previous unit already covers.

### 2026-10-13 (after units 22, 23 frozen): two units per agent

- **Paired read** (one Sonnet agent, units 22 + 23): 167k = 83k per unit
  against 106–191k single, with as many real findings (12 + 7 applied) and
  a cross-unit catch (unit 23's price screen re-teaching unit 21). **Reads
  go in pairs from now on** (user: "double is ok").
- Triples considered and declined for now (user agreed): the fixed cost
  per read is ~40–50k, so a third unit saves only ~13k/unit more, while a
  ~250k-token context risks the detail checks late in the read.
- **Paired regeneration** (24 + 25): 238k = 119k/unit (single: 160–267k),
  14 min for both. But its read found ~16 real defects per unit (single:
  9–12), mostly in the second unit: re-teaching earlier units as new
  (colours from 22, the definite verb from 21) and repeated item shapes.
  Net still cheaper (the extra fixes are Haiku work), so pairs stay, with
  the prompt now listing what earlier units already teach.
- New check `take-gloss` (HU fill-blanks whose English "take" lets *kér-*
  and *vesz-* both fit): the defect recurred in 21, 22, 24, 25 despite the
  rules sheet; the check finds exactly the read's 4 typed items.

### 2026-10-13 (units 26, 27 read)

- The paired read found ~25 items per unit, mostly recap screens presenting
  earlier units as new (the 28+29 prompt already lists "recap, never new").
- New check `consolidation-copy` (suspect): a consolidation item identical
  to a lesson item. 317 hits course-wide, almost all in frozen units 2–7, 9
  (whose consolidations were built as replays; left as they are) and in the
  not-yet-regenerated 28–30; regenerated units have 1–5 each.
- Known `consolidation-copy` suspects in units frozen before the check
  (one each): a1-45-consolidation-10, a1-60-consolidation-4,
  a1-65-consolidation-17, a1-70-consolidation-1, a1-75-consolidation-17.
  Left: reopening five frozen units for one review item each isn't worth it;
  fold them into any later edit of those units.
- New check `reported-question` (suspect): "Anna asks Meg where she is
  going. Which question?" lets *Hová megy?* fit too. 9 hits in HU A1: 2 new
  ones in 28/29 sent to the fixer; a1-124/125 hits are formal *Ön* (3rd
  person is right there, accept); a1-113-practice-3 logged.
- New checks `hova-variant` and `article-blank` (suspects). First run:
  a1-153-controlled-1 (in the fixer's list), a1-151-practice-3 (in the
  list), and a real one in frozen unit 8: a1-36-practice-5 builds *A
  emberek* (fold into the next edit of unit 8); B1/B2 hits logged; the C1
  hits are *az* the pronoun (false positives).
- New check `ik-first-person` (error): *eszek/iszok/dolgozok…* as a right
  answer (the course teaches *eszem/iszom*; *-k* forms are its wrong
  options). One hit course-wide, unit 33 (fixed with its screen, a
  consolidation item and an a1-164 challenge, all *eszek/iszok* → *-m*).

### 2026-10-13 (units 32, 33 frozen): HU A1 complete

- Paired read 32+33: 202k, 10 min (first attempt stopped on the weekly
  Sonnet limit). ~35 items; I applied them myself with one exact-replacement
  script (each old string must match once, else nothing is written) plus a
  JSON pass for `ds`, retags and challenges. Cheaper than a Haiku pass for a
  list this size, and the script caught a double match the list missed
  (*Magyarul tanulsz.* in two items).
- Same pattern again: recap screens presenting earlier units as new
  (a1-158-b, a1-159-a, a1-160-a/b). The regeneration prompt's "recap, never
  new" line is not enough on its own; the reader catches it reliably, so
  keep the read.
- My own edits tripped `length-giveaway` and `unmet-word` once each;
  run check-content after every hand edit, not only before freezing.

### 2026-10-14: follow-ups after HU A1 (user's decisions)

- Consolidation copies: the count I first gave (five) was wrong; the
  frozen units 12–25 had 22 stray copies, units 2–9 are replays. The user
  chose to fix the strays and leave 2–9. 21 rewritten (a1-60, 65, 70, 75,
  80, 115, 120, 125) plus a1-113-practice-3 (reported question → quoted)
  and a1-36-practice-5 (*A emberek* → *Az*). Lesson: count with the
  checker before putting a number to the user.
- `freeze_unit.py` refreezing a frozen unit replaced its reason and lost
  its accepted findings (check-content hides them, so they weren't passed
  back). Fixed: a refreeze keeps the earlier accepted entries and reason.
- Accepted at refreeze: a1-57-introduce-1 (asks about the question form, not
  reported speech), a1-124-controlled-2, a1-124-practice-3,
  a1-125-practice-5 (formal *Ön*: third person is right).
- *hánykor* added through `imports/dictionary/additions-hu.json` (merge
  step, so a dictionary rebuild keeps it). Spanish a1-03-01 duplicate
  *foto* removed in both courses. B1 glued blanks (b1-18-03.ex03,
  b1-26-05.ex02, b1-30-03.ex05) stay parked with HU B1.
- Next, decided by the user: the gate-1 lesson walk test (ROADMAP 153(b))
  on HU A1 before starting HU A2.

### 2026-10-14: two efficiency methods built (for HU A2 onwards)

- **Knowledge sheet** (`scripts/prior_knowledge.py`): ~7k tokens a unit
  (61 known skills, 527 words, every earlier screen title before A1 unit
  32). Replaces agents opening earlier units; aimed at the most common
  read finding in units 24–33 (screens presenting earlier material as
  new). Expected: shorter reads and fix lists; measure on the first A2
  pair.
- **New suspect `recap-unmarked`** in check-content: a grammar screen that
  repeats 2+ example sentences of an earlier unit's screens with no "You
  know"-style wording. HU A1 21 hits (mostly review units 10 and 20, whose
  screens recap without saying so), A2 7, es-es A1 0. It would not have
  caught the unit 32 defects (those screens said "you know" for part and
  presented the rest as new), so it is a partial check; the sheet is the
  prevention.
- **Reader JSON + `scripts/check_fixes.py`**: the reader writes its fixes
  as JSON; the script applies them to the working tree, runs check-content
  on the unit, restores the files and sorts them into rejected / review /
  auto. Tested on a frozen unit with five planted fixes: the good one went
  to auto, the Hungarian and unsure ones to review, a non-matching text and
  a length give-away were rejected, files unchanged afterwards. The reviewer
  then reads only the review list. `apply_replacements.py` now also takes
  `{"file", "id", "set": {...}}` fixes (tags, `distractor_skills`,
  options, challenge fields; null deletes a field).
- Limit: the script knows only whether a fix applies cleanly and passes
  the checks, not whether its Hungarian is right; that stays the
  reviewer's job (the review list).
