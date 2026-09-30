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
| `fill-dictionary-gaps.py` | Fills the gaps the audit finds without spending tokens: `export hu\|es` writes batches for ChatGPT to `imports/dictionary/gap-batches/` (default: words seen 3+ times; `--dry-run` counts), `import <reply.txt> hu\|es` validates the reply and merges it into the dictionary via `imports/dictionary/additions-<lang>.json`, `merge` re-applies the additions after a dictionary re-import. |
| `audit-reader-coverage.js` | Runs every story word through the Reader's own `Lexicon.lookup()` (headless) and reports the words that would show "Not in the dictionary yet", plus any that make the lookup throw. `node scripts/audit-reader-coverage.js [hu\|es-es\|es-latam\|all] [--out report.json]`. Takes seconds. |

## Generated indexes (also rebuilt by CI, `sync-generated-content.yml`)

`build-manifest.py` in the repository root builds `curriculum.json`, `decks.json`
and the story manifests. These scripts build the indexes the engine reads:

| Script | Output feeds |
|---|---|
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
| `add_fillblank_hints.py` | Adds a parenthetical hint to fill-blanks that are unrecoverable without one. |
| `export_missing_vocab_sentences.py` | Exports words lacking example sentences as prompt files for LLM backfill. |
| `generate_scenarios.py`, `generate_writing_exchanges.py` | Regenerate the conversation scenarios and written exchanges. |
| `stitch_track_unit_stories.py` | Stitches an elective-track unit's five readings into its consolidated Library reading. |
| `scaffold_es_es.py` | Example of scaffolding a course from another; see AGENTS.md "Adding a new course". |
| `narrate-story.py` | Story narration and annotation metadata. Audio plays through ParlourTTS. |

## Dev and deploy

`dev-server.py` is a static server that never lets the browser cache (launched by
`.claude/launch.json`). `stamp-assets.py` stamps a version onto `index.html`'s
local CSS and JS URLs.
