# scripts/

Tools that are still part of how the project is built, checked or run. One-shot
content generators and repair scripts that have already done their job live in
[`archive/`](archive/).

Run everything from the repository root (`python scripts/<name>.py`).

## Checks (run before committing content)

| Script | Purpose |
|---|---|
| `validate-content.py` | Validates every content file against its course's schemas and the exercise-metadata rules. `--changed` checks only what git says changed. Run by the pre-push hook and CI. |
| `audit-lesson.py` | Cross-file lesson checks against the content spec (counts, structure, teaching order). |
| `audit-lesson-hu.py` | The Hungarian teaching-order check. |
| `triage-teaching-order.py`, `triage-teaching-order-hu.py` | Split the audit's teaching-order flags into real gaps versus noise. |
| `audit-reading-quality.py` | Paragraph typing, dialogue speakers and other reading-quality rules. |
| `audit_exercise_metadata.py` | Per-course, per-level report of missing `category` / `teaches`. |
| `resolve_skill_aliases.py` | After an approved skill merge or rename in `skills/<lang>.json`, rewrites alias slugs to the canonical skill in exercises (`teaches`, `distractor_skills`), tests, `targetSkills` and `verb-tense-skills.json`, keeping each file's formatting. `--dry` counts only. |
| `lock_tags.py` | Locks a read and reviewed unit's exercise tags in `indexes/tags.lock.json` (`lock_tags.py <course> <level>/<unit id> --reason "..."`); refuses a unit that still breaks a tagging rule. ROADMAP 125. |
| `apply_tags.py` | Applies a unit's read-through decisions (`apply_tags.py <course> <level> <decisions.json>`, one `{"teaches", "category", "ds"}` entry per exercise id) to `teaches`, `category` and `distractor_skills`; refuses a file with an exercise left undecided. Lock the unit with `lock_tags.py` afterwards. ROADMAP 125. |
| `fill-dictionary-gaps.py` | Fills the gaps the audit finds without spending tokens: `export hu\|es` writes batches for ChatGPT to `imports/dictionary/gap-batches/` (default: words seen 3+ times; `--dry-run` counts), `import <reply.txt> hu\|es` validates the reply and merges it into the dictionary via `imports/dictionary/additions-<lang>.json`, `merge` re-applies the additions after a dictionary re-import (Spanish verbs that share a headword with an adjective go to `spanish-verb-homographs.json`). Words ChatGPT calls non-words are remembered in `coverage-ignore.json`. `pull-ai hu\|es` downloads the Reader's cached AI glosses for review (see `docs/SERVICES.md`, "Word gloss"). |
| `audit-reader-coverage.js` | Runs every story word through the Reader's own `Lexicon.lookup()` (headless) and reports the words that would show "Not in the dictionary yet", plus any that make the lookup throw. `node scripts/audit-reader-coverage.js [hu\|es-es\|es-latam\|all] [--out report.json] [--markdown summary.md]`. Takes seconds. Runs in CI as a report only (`.github/workflows/reader-coverage.yml`); words to skip go in `imports/dictionary/coverage-ignore.json` (`all`, `hu`, `es`). |

## Generated indexes (also rebuilt by CI, `sync-generated-content.yml`)

`build-manifest.py` in the repository root builds `curriculum.json`, `decks.json`
and the story manifests. These scripts build the indexes the engine reads:

| Script | Output feeds |
|---|---|
| `build_skill_registry.py` | Each course's `skill-registry.json`, `grammar-titles.json` and `skill-prereqs.json`, from the source `skills/<lang>.json` (never edit the outputs by hand). `--check` exits 1 if they're out of date. |
| `build_grammar_guide_index.py` | Grammar Guide global search |
| `build_grammar_index.py` | Workshop Grammar Driller (skill to exercise lookup) |
| `build_translation_index.py` | Translation Driller and Vocabulary Driller context mode |
| `build_verb_index.py`, `build_verb_list.py` | Reader tap-to-translate and verb drillers |
| `build_word_index.py` | Non-verb inflected form to lemma |
| `build_word_lesson_index.py` | "Which lesson taught this word?" cross-links |
| `build_frequency.py`, `build_hu_frequency.py` | Lemma frequency ranking for word lookups |
| `build_competencies_index.py` | My Journey's Can-Do Passport |

## Imports (external data, run rarely)

`import_dictionary.py` (Spanish), `import_hu_dictionary.py` (Hungarian) and
`import_cefr_exam_prompts.py`. Raw download caches they use are gitignored and
regenerable.

## Content tooling

| Script | Purpose |
|---|---|
| `check-content.py` | Every mechanical content check in one pass (give-aways, hints, blanks, copies, teaching order, new-course shape); `--changed` gates new findings at pre-push. |
| `render_lesson.js` | Prints a lesson screen by screen as the app builds it (real `buildSteps()`), including the generated speaking steps and challenge, and flags missing files: `node scripts/render_lesson.js hu a1-01`. |
| `freeze_unit.py` | Freezes a finished unit (no findings left except accepted ones, each with a reason) in `content/<course>/frozen-units.json`; `--status` counts frozen units; `check-content.py --changed` then blocks edits to it (ROADMAP 153). |
| `migrate_fillblank_hints.py` | Moved fill-blank hints out of `sentence` into the `hint` field (ROADMAP 149); rerun it on imported content that still writes them into the sentence. |
| `export_missing_vocab_sentences.py` | Exports words lacking example sentences as prompt files for LLM backfill. |
| `generate_scenarios.py`, `generate_writing_exchanges.py` | Regenerate the conversation scenarios and written exchanges. |
| `stitch_track_unit_stories.py` | Stitches an elective-track unit's five readings into its consolidated Library reading. |
| `scaffold_es_es.py` | Example of scaffolding a course from another; see AGENTS.md "Adding a new course". |
| `narrate-story.py` | Story narration and annotation metadata. Audio plays through ParlourTTS. |

## Dev and deploy

`dev-server.py` is a static server that never lets the browser cache (launched by
`.claude/launch.json`). `stamp-assets.py` stamps a version onto `index.html`'s
local CSS and JS URLs.
