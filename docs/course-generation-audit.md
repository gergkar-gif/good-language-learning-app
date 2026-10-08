# Course generation audit (ROADMAP 149)

Draft for the user's sign-off, 2026-10-08. Step 1 of item 149. It lists what a new-course run needs, every content rule learned so far, and whether anything enforces each one. It then proposes one generation brief and the checks that are missing. Nothing has been built yet. Section 6 lists the decisions that come first.

Sources read: AGENTS.md; `content/hu/HU_Content_Authoring_Template.md`; `content/es-latam/guides/a2-lesson-guide.md` and `editorial-style-guide.md`; the 17 archived guides in `docs/archive/guides/`; `docs/latam-stories-brief.md`; `docs/readthrough-brief.md` and `readthrough-process.md`; `docs/skill-tagging-spec.md`; every `imports/review/ANTIGRAVITY-*.md` brief and its review notes; the HU review feedback rounds 1–7; both review-questions files; and the "Content fixes" lines in ACHIEVED.md items 109–148. The checks are every script under `scripts/` and `imports/review/`, CI (`.github/workflows/sync-generated-content.yml`) and `.githooks/pre-push`.

## 1. Findings

1. **The rules are spread over about 25 files, and the generator would read the wrong ones.**
   - Most of the detailed shape rules sit in archived guides that still point at `content/es/`, a folder that no longer exists.
   - The only Hungarian guide (`HU_Content_Authoring_Template.md`) says of itself that it is historical and A1-only.
   - The defect lessons from reviews live mostly in ACHIEVED.md and in review notes at the bottom of briefs. A generator never reads either.
2. **Only one check is a gate.** `validate-content.py` runs in CI and in the pre-push hook. It covers:
   - schemas and wiring
   - tags and skills: one tag, frozen list, level, `taught_in`/`requires`
   - foreign-script characters and duplicate story ids

   Every check that catches *content* defects runs only by hand, or only inside a read-through:
   - `audit-lesson.py`: lesson shape and counts, Spanish only
   - `readthrough_check.py`: answer in the prompt, hint repeats the answer, taught later, missing person in a hint. It needs a read-through decisions file to run.
   - `check-hu-exercises.py`: Hungarian case errors, time-word give-aways, hint leaks
   - `check-slash-giveaway.py`: length and " / " give-aways
   - `check-es-b1-giveaways.py`
   - `dup_report.py`: lesson-to-lesson copies
   - `audit-reading-quality.py`

   New content never meets any of them. That's why give-aways came back after their review (item 148(a)), and why late units shipped with copied lesson templates.
3. **There is no single lesson shape.**
   - Spanish A1/A2/B1-core use Practice/Dialogue/Writing blocks, which `audit-lesson.py` checks.
   - Spanish B1 latam is reading-first: a story in every lesson, then one Practice group.
   - Hungarian uses staged groups: Introduce, Controlled, Practice, Dialogue, Production, Check. No script checks this shape. Live lessons don't match the "25 steps" in memory exactly (`a1-05` has a 6-item "Vowel Harmony" group).
   - Target numbers conflict between sources: words per unit (16, 20, 20–55), exercises per lesson (A2G 18–21, B1S 16/19/18) and story length (100–250, 150–350, 220–280).
4. **About 70 defect classes were found after generation and fixed by hand** (section 3). Roughly a third can be checked mechanically, a third partly, and a third need a read by a model or a person: second right answers, a correct option that doesn't answer its question, gloss accuracy, facts against the story, natural phrasing.
5. **Several parts of a course aren't covered by any authoring doc:**
   - audio: TTS voices per language and the recordings needed for sounds
   - Reader dictionary and morphology data
   - `challenges.json`
   - the per-language `engine/lang.js` profile

## 2. What a new-course run produces, in order

| Stage | Output | Rules now in | Checked by |
|---|---|---|---|
| 0. Course setup | `content/<code>/schemas/` (copied from es-es), `engine/lang.js` profile (orthography, speech locale, abbreviations), `curriculum/challenges.json` | AGENTS.md § Adding a new course | validator (schemas exist, registry exists); nothing checks `lang.js` or challenges |
| 1. Skill plan | unit tables `curriculum/units/<level>.json` (permanent ids), `skills/<lang>.json` (one vocab skill per unit, grammar skills with family, title, `taught_in`, `requires`), `skills/frozen-<lang>.json` | AGENTS.md, skill-tagging-spec.md | validator (full) |
| 2. Per unit: screens | one grammar file per concept | archived a1-authoring-guide, b1-content-spec, HU template | `audit-lesson.py` (ES only): ≤300 words, 3–5 examples |
| 3. Per unit: vocabulary | `-voc.json` per lesson | archived guides, HU template | `audit-lesson.py` (ES only): every word used in an exercise |
| 4. Per unit: story | one story per unit, or one per lesson (latam B1) | archived a1-story/b1-content-spec, latam-stories-brief | `audit-reading-quality.py` (by hand); validator for story ids |
| 5. Per unit: lessons | lesson files: sections, goal/checklist, exercise groups | archived guides, HU template | validator (schema); `audit-lesson.py` (ES only) |
| 6. Per unit: exercises | `-ex.json`, tagged and locked | AGENTS.md, readthrough-brief, review notes | validator (tags); everything else by hand (section 3) |
| 7. Wiring | unit-table entry, `build_skill_registry.py`, `build-manifest.py` | AGENTS.md § Wiring | validator, CI |
| 8. Audio | TTS works for any language with a Chirp3-HD voice; letter or sound tables need recordings (`tools/sound-recorder/`) | memory only (`hu-sound-recordings`) | nothing |
| 9. Reader/Lexicon | dictionary import (`import_dictionary.py` is Spanish-specific; HU has its own), word index, morphology | none | `audit-reader-coverage.js` (report only) |
| 10. Review | a read of every unit, then `lock_tags.py` | readthrough-process.md | `readthrough_check.py`, lock |

Stages 8 and 9 are per-language engineering, not content. They can't come out of a one-hour generation run and should be planned as separate items.

## 3. Rule inventory and what enforces it

**Gate** = `validate-content.py` (CI and pre-push). **Script** = exists but runs by hand. **None** = nothing checks it. **Read** = needs a model or a person.

### Structure and shape

| Rule | Enforced |
|---|---|
| Schemas per course, copied from es-es; six-value `category`; stage names in `stage` | Gate |
| Unit = 5 teaching lessons + 1 consolidation; permanent unit id; every lesson file in exactly one unit | Gate (unit table); orphan lessons: Script (coverage check in readthrough-process) |
| `goal.items` = `checklist.items` in count; checklist items start "I can" | Script (ES) |
| Consolidation: one "Review" group, no grammar/vocab/srs/story, ≥5 types (A1) / ≥6 (B1), ≥8 / ≥6 distinct tags | Script (ES) |
| Teaching lesson spans ≥5 types (A1/A2) / ≥6 (B1); Practice ≥4 / ≥6 | Script (ES) |
| Dialogue and Writing in every teaching lesson; Listening from A2 | Script (ES) |
| Only the 9 rendering exercise types in lessons (no `error-correction`) | None |
| `recycle` is `{"type":"recycle"}`, `srs` is `{"type":"srs"}`; lesson has `level` | Gate (schema) |
| Grammar screen: ≤300 words of prose, 3–5 examples, paradigm in a table, `external-link` last | Script (ES) for words/examples; tables: None |
| Italicise target-language words in `text`/`tip` prose | None |
| Exercise ids sequential and unique; `exerciseRefs` resolve | `build-manifest.py` (refs); duplicates: None |

### Vocabulary and stories

| Rule | Enforced |
|---|---|
| Lemma form, `pos` from the list, consistent `theme` | Gate (schema) for `pos`; rest None |
| Every new word used in an exercise of its own lesson | Script (ES) |
| Every word appears in the unit story (advisory) | Script (`audit-reading-quality.py`, ≥85%) |
| Story uses only taught grammar and words; advances the plot; one topic per story; no spliced templates | Read |
| Story length per level | None (sources conflict) |
| Reading questions answerable from the story, 3 per story, after the story | Read; order: partly Script |
| Facts verified (dates, names, numbers); no invented details about real people | Read |

### Exercises: wording and answers

| Rule | Enforced |
|---|---|
| Correct option answers exactly what is asked (*Hány* → number, *Miért* → reason) | Read; partly checkable by question word |
| Every option is the same answer type as the question; no *Igen/Sí* openers under open questions | partly Script-able (none yet) |
| Prompt understandable on its own; never "this exchange" without one shown | Script (`readthrough_check.py`, one pattern) |
| No repeated question line in adjacent steps | Script (item 109 audit, not kept) |
| Each lesson tests its own words and screen; no exact copy across lessons of a unit | Script (`dup_report.py`) |
| Stem doesn't contain the tested form; answer not printed in prompt, hint, English line or options | Script (`readthrough_check.py`) |
| Prompt person/tense/meaning match the answer; English line pins one answer | Read |
| Vocabulary item has exactly one fitting option; sibling items don't share a definition | Read |
| Every fill-blank and sentence-builder has `english` | Gate for ES fill-blank; HU fill-blank: None; builders: None |
| One blank per fill-blank, inside the sentence; answer doesn't repeat letters printed next to the blank | None |
| All natural variants in `answers`; builders with a natural second order use `solutions` | Read (builder plan parked, 148(b)) |
| Accept every grammatically valid alternative | Read |

### Distractors

| Rule | Enforced |
|---|---|
| Reply items: wrong options wrong in *form*, or self-contradictory; never another sensible reply | Read |
| Grammar items: a wrong option a native teacher would accept is a second right answer | Read; partly Script (adjacent-word swap, ES) |
| No time word only in wrong options | Script (`check-hu-exercises.py`, `check-es-b1-giveaways.py`) |
| No absolutes (*kizárólag, soha, nunca*) only in wrong options | None |
| No opener or marker (*Sajnos*, *Mert*, *Porque*) only on wrong options or only on the correct one | None |
| Options of similar length (correct ≤2× longest wrong, 15 chars) | Script (`check-slash-giveaway.py --length`) |
| No " / " shape give-away | Script (`check-slash-giveaway.py`) |
| Options identical apart from the tested element (punctuation, capitals, endings) | None |
| Options in the item's language; real forms, never non-words; only taught forms and words | None; taught forms: partly Script (`audit-lesson*.py` teaching order) |
| Fact items: wrong options are real, plausible, false facts of the same kind | Read |
| No duplicate options; `correct` a valid index | Script (`check-hu-exercises.py`) |

### Hints

| Rule | Enforced |
|---|---|
| Hint only when the blank is unrecoverable; gives lemma + grammar or English, never the inflected answer | Script (`check-hu-exercises.py` hint-leak, `readthrough_check.py`) |
| Person- or possessor-marked answer needs a person in the hint (HU); dropped subject needs one (ES) | Script (`readthrough_check.py`) |
| English-only hint → all synonyms in `answers` | Read |
| Function words and correlatives get a structural hint, not English | Read |

### Teaching order and tags

| Rule | Enforced |
|---|---|
| Never use a form before its `taught_in` screen, in options and examples too | Script (`audit-lesson.py`, `audit-lesson-hu.py`, coarse) |
| Exactly one `teaches`, by what a wrong answer shows; category follows the tag; matching = vocabulary; reading untagged | Gate for slug, level, one tag on locked units; category rules: Script (`readthrough_check.py`) |
| `distractor_skills` only for a real form of another grammar skill | Script (`readthrough_check.py`) |
| Vocab tag is the unit's own | Script (`readthrough_check.py`, ES) |
| ≥6 exercises per taught grammar skill | Gate (warning) |
| `taught_in` = the first screen that really teaches it | Gate (exists, prerequisite order); "first" is Read |

### Language-specific

| Rule | Enforced |
|---|---|
| HU: right case family per noun (-n/-ra vs -ba/-ban) | Script (noun list) |
| HU: definite/indefinite, harmony, `a/az`, focus position, natural frames (*Mennyibe kerül?*) | Read; native-speaker questions file |
| HU: no archaic *-tatik/-tetik* | None (blocklist would do) |
| Never TTS a bare letter; sound tables use recordings | None |
| ES latam: no *vosotros* outside the drill | None (regex would do) |
| ES: shared es-es/es-latam copies stay identical | Script (`readthrough_check.py`) |

## 4. Proposal: one generation brief

One file, `docs/course-generation-brief.md`, replaces the HU template and the archived guides as the thing a generator reads. The old files stay archived as history. Contents:

1. **Order of work**: stages 0–7 and 10 from section 2, with what to stop and show the user after each.
2. **The lesson shape**: one canonical teaching lesson and one consolidation, with fixed numbers per level (decision 1 and 2 below), and a worked example file.
3. **Screens, vocabulary, stories**: the rules from section 3 as short imperatives, each with one real bad/good pair taken from the review notes.
4. **Exercises**: per type, its fields and its rules. Then the distractor, hint and answer rules, each with a bad/good example.
5. **Tags**: a short pointer to skill-tagging-spec.md (already the reference).
6. **Self-check before handing back**: run the check script (section 5), then a read checklist for the rules a script can't catch. The read is done by a second model per unit, not by the generator. (Generating and checking your own output in one pass missed exactly these classes in the Antigravity blocks.)
7. **Language appendix**: one per language, holding only what differs (HU cases, harmony, articles; ES variants and *vosotros*). A new language gets a new appendix written at stage 1.

AGENTS.md and CLAUDE.md shrink to a pointer at the brief for content rules, so the rules live in one place.

## 5. Proposal: missing checks

One new script, `scripts/check-content.py <course> [level] [unit]`, that runs every mechanical content check in one pass. It folds in the existing ad-hoc scripts, so nothing has to be remembered:

- **Already written, gathered in:** time-word give-away, length and slash give-aways, hint leak, answer in prompt, "this exchange", person missing from hint, duplicate options, lesson-to-lesson copies, Hungarian case nouns, teaching order, es-es/es-latam copy match.
- **New, simple:**
  - absolutes only in wrong options
  - an opener or marker only on wrong options (or only on the correct one)
  - punctuation or capital-letter odd-one-out
  - an option in the wrong language
  - more than one blank, or the blank outside the sentence
  - the answer repeating letters printed next to the blank
  - repeated question lines in adjacent steps
  - question word vs answer type (*Miért*/*Por qué* → reason, *Hány*/*Cuántos* → number, a yes/no opener under an open question)
  - `english` on every fill-blank and builder
  - only rendering types in lessons
  - every vocabulary word used in an exercise
  - the lesson-shape and consolidation-shape rules for the chosen shape, for every course (porting the Spanish-only parts of `audit-lesson.py`)
  - per language: an archaic-form blocklist (HU) and *vosotros* in es-latam
- **Run as:** a gate on new courses, and on `--changed` files, through the pre-push hook next to the validator. A warning-only report everywhere else, because existing content would fail it. Lock status stays separate.

Calibration step before relying on it: run it over HU and ES A1–B1, which have all been read, so its hit rate there shows the false positives. Tune it until clean content passes.

## 6. Decisions needed *(sign-off)*

**Decided by the user 2026-10-08:** 1 yes (HU staged shape with the Spanish counts on top), 3 yes, 5 yes: the hint goes in exercise metadata, a typed `hint` field, never in `sentence`; 6 yes, 7 yes. 2 yes, with word counts as a guide that varies by level and topic (table in the brief § 2.1); 4: 1.3× for new content. All seven are decided; the brief is [course-generation-brief.md](course-generation-brief.md).

1. **One lesson shape for new courses.** I'd suggest the Hungarian staged groups (Introduce, Controlled, Practice, Dialogue, Production, Check). They build the recognise → manipulate → produce progression into the shape. The Spanish block rules (≥5 types, Dialogue and Writing present) would sit on top as counts. Existing Spanish and Hungarian lessons stay as they are.
2. **One number table per level:** new words per unit, exercises per lesson, story length, stories per unit. I'll propose values from what shipped lessons actually average, for you to adjust.
3. **Gate policy:** the new checks fail new courses and changed files only, and stay a report on existing content.
4. **Length give-away threshold for new content:** keep 2× / 15 characters, or tighten to the 1.3× the review notes recommend (there are about 3,600 milder cases at 1.5× in existing content).
5. **The typed `hint` field** (roadmapped, item on fill-blank hints): add it before Italian. Otherwise a new course adds another ~1,000 hints written into `sentence` that would have to be moved later.
6. **Who does the read:** a second model per unit, against the brief's read checklist, before locking. This is cheaper than the full read-throughs (~110k tokens per unit) because the checks clear the mechanical classes first.
7. **Scope of "one button":** content only (stages 0–7 and 10). Audio recordings, dictionary import and morphology are separate per-language items.

## 7. After sign-off

1. Write `docs/course-generation-brief.md` with the HU appendix, then the ES one.
2. Build `scripts/check-content.py`, run it on HU and ES A1–B1, and tune it to clean.
3. Pilot: one HU C1 unit, or the latam pilot `central-america-revolution-conflict` (148(p)). Generate under the brief, check, read, and compare the cost with a manual fix.
4. Then item 149's dry run on a small slice of Italian A1.
