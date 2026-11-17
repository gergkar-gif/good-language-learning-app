# New Language Scaffolding Guide (Pre-Lesson Infrastructure)

Checklist and pitfalls for adding a new language (`fr`, `it`, `pl`, `cs`, `sk`, `de`, ...) **before lessons exist**, so Home, Library, Decks, Lexicon, Verbs, Grammar Studio, Listening/Music/Video, Writing/Speaking, and CEFR Exam Prep work on the first try. Once authoring lessons, follow [course-generation-brief.md](course-generation-brief.md) and [AGENTS.md](../AGENTS.md).

Derived from the non-lesson repair pass (`4d63cd62b`–`591c07c45`, 2026-11-17).

---

## 1. Gate, Profiles & Workers
- Keep `AVAILABLE = ['es-latam', 'es-es', 'hu']` in `engine/lang.js` gated until real lessons exist.
- Register the new `<code>` in ALL `engine/lang.js` maps: `VOICES`, `COURSE_NAMES`, `LANGUAGE_NAMES` (`sk` was previously missed), and `PROFILES[code]` (`tests`, `paradigm`, `diacritics`, `openers`, `examLabels`, `canDoCues`, `discourseConnectors`).
- Wire `<code>` in `engine/init.js` (`verbs` / deep-link routing), `index.html` (`<script>` tags for morphology/driller/verb-list), `sw.js` (`PRECACHE_ASSETS` + bump `CACHE_VERSION`), and Cloudflare workers (`cloudflare-worker/tts-worker.js`, `stt-worker.js`, `gloss-worker.js` supported-language sets and error strings).

## 2. Boot Skeletons, Manifests & Curriculum Indexes
- Generate all runtime skeletons with the project builders instead of shipping partial JSONs:
  ```
  python build-manifest.py <code>
  python scripts/build_word_lesson_index.py <code>
  python scripts/build_competencies_index.py <code>
  ```
  This creates `curriculum/curriculum.json`, `decks/decks.json`, `stories/manifest.json`, `indexes/translation-index.json`, `indexes/word-lesson-index.json` (`{"byLemma":{}}`), and `indexes/competencies-index.json` (`[]`), preventing Library/Reader/LearnerModel boot 404s. Also author `curriculum/challenges.json` (see `AGENTS.md` § "Adding a new course").
- `content/<code>/indexes/frequency.json` MUST be a flat JSON **array** of lowercase words in descending frequency order (`["a", "b", ...]`), never an object map.
- Include at least one starter story (`stories/current/b2/...`) and `backfill_sentences/starter.json` / frequency deck so Library and Decks are non-empty when previewing the gated course.

## 3. Lexicon & Morphology Contracts (`engine/morphology/<code>.js`)
- Handle `Lexicon.lookup(word, ctx)`'s `(word, ctx)` object signature — never expect positional `(word, dict)` arguments.
- Always return `{ word, found, readings: [] }` (never `null`, never omit `readings`), with readings shaped `{ lemma, pos, gender?, translation, analysis }` (+ `type`/`en` compatibility fields if needed), ranked by `frequency.json`.
- Strip punctuation cleanly before lookup, query both `wordIndex` and `verbIndex` (handling both bare string lemmas and structured entry objects `{ lemma, tense, person, gender }`), and call `Lexicon.registerMorphology('<code>', <Module>)`.

## 4. Dictionary & Reverse-Index Importers (`scripts/import_*_dictionary.py`)
- Map `"intj": "interjection"` (and `"interj": "interjection"`) in `POS_MAP`, and filter consistently on `pos in POS_MAP`.
- Anchor `FORM_RE` at `^` so legitimate single-word glosses mentioning grammatical terms (e.g. `ja` -> `"first-person pronoun; I"`) are kept.
- Allow 1-character glosses (`len(cg) >= 1`), rank modern grammatical/function senses ahead of obscure nouns (`POS_PRIORITY` + `DEPRIORITISE_TAGS`), reject `misspelling of` and `"the name of the latin script letter"` definitions, and **never** select the longest gloss.
- Maintain explicit `GLOSS_OVERRIDES` for high-frequency homographic clitics/articles (e.g. Italian `i/mi/ti/si/vi/li/lo/la/le/ne`) and `FOUNDATIONAL_DICT` for function words missing from Wiktionary.
- Strip Wiktextract UI junk (`table-tags`, `inflection-template`, `-`, multi-word entries, `form == word`) BEFORE saving `word-index.json` and `verb-index.json`; verify `verb-index.json` is populated and bounded (`<= 4` entries per form).
- Provide `--indexes-only` and `--verbs-only` flags so verb or index rebuilds stay fast and isolated.

## 5. Verb Conjugation Datasets & Verb Engine (`imports/verbs/<code>/`, `engine/verbs*.js`)
- Every verb JSON MUST include a clean `english.infinitivo` (never empty or fake `"to <lemma>"`; resolve verb-vs-interjection homographs explicitly, e.g. Polish `stać` = `"to stand; to afford"`, not `"halt!"`).
- Match tense and person keys to `Lang.profile('<code>').paradigm`:
  - In Slavic past/conditional tenses, populate `defaultPersons` keys (`ja`, `ty`, `my`, `wy`/`vy`, `oni`) alongside gender keys, joining accepted gender variants with `/` as full forms (e.g. `"robiłem/robiłam"`, `"dělal jsem/dělala jsem"`). `VerbsTable` and `VerbsSpeed` grade `/` alternatives via `_matchesAnswer()` while checking diacritics strictly.
  - Omit absent forms for impersonal/defective verbs (`falloir`, `pleuvoir`, `faillir`) and imperatives instead of inventing forms; `VerbsTable` skips empty person rows and `VerbsSpeed` falls back to populated persons.
- Source extraction rules:
  - **Lexique383**: ignore `ortho == lemme` on finite non-`inf` tags (`vous == inf` leaks), drop hyphenated tokens (`re-fuse`), and handle `-cre` (`convainqu-`) and `-faire` stems without slicing `-oir` stems with `[:-2]`.
  - **Kaikki**: determine aspect from `table-tags` (`'imperfective'`/`'perfective'`, Czech `'future present'` vs `'future'`), NEVER from partner-aspect links or prefix heuristics (`pomagać`, `zaczynać` are imperfective). Skip `'no-table-tags'` reflexive sub-tables, filter `colloquial`, `adjectival` participles, `-` placeholders, and non-infinitives (`bejt`, `pět`, `je`..`není`, `ďakujem`). Handle omitted person tags (Polish row order), shifted Slovak past tags (`-l`/`-la`/`-lo`/`-li`), and phonological rules (e.g. Slovak rhythmic law: `počkať` -> `počkám`).
- `Verbs.init()` validates `_state.tense` against `_getTenseOptions()` on initial boot as well as on language switches.

## 6. Workshop Drillers, Media Studios & CEFR Exams
- **Driller module API**: every module in `engine/drills/` MUST expose `render(container, options)` accepting a DOM `HTMLElement` (not only a string ID for `document.getElementById`, which left `SkGrammarStudio` blank in `Workshop`) and `stop()`.
- **Listening / Music / Video schemas**:
  - `listening-tasks.json`: `{ question, type: "listening-mc", options, correct: <int>, evidence }` — never `prompt`/string `answer`, and vary `correct` indices.
  - `songs.json`: `stanzas` with `[blank]`, `english`, `options`, `note` — never flat `lyrics`.
  - `videos.json`: `paragraphs`, `english`, `questions` (integer `answerIndex`), `cloze` — never `transcript`/`translation`.
  - **Live YouTube check**: verify every YouTube video ID in `songs.json` and `videos.json` via YouTube oEmbed HTTP 200 before committing; never invent or reuse placeholder IDs.
- **CEFR Exam Prep**: localize every static and dynamic string in `engine/cefr-exam.js` (`_t` + `EXTRA_UI_STRINGS`), use `"type": "reading-mc"` with varied integer `correct` + `evidence`/`explanation`, `"type": "audio-interview"`/`"audio-mc"` with `audio.turns`, normalized writing `options`/`maxWords`/`targetKeywords`, and complete `strategies`.

## 7. Pre-Push Verification Gates
Add the new `<code>` to the contract and browser suites, then pass all checks before pushing:
1. `node tests/test-lexicon-contracts.js`
2. `node tests/test-cefr-exams-nonlesson.js`
3. `node tests/test-verb-engine-nonlesson.js`
4. Course integration & studio tests (`tests/drills/test-<lang>-integration.js`, `test-listening-studio.js`)
5. Live headless Chromium verification across every tab and driller: `node tests/test-browser-nonlesson-smoke.js` (0 JS exceptions, 0 console errors, 0 unexpected HTTP >= 400)
6. Content validators: `python scripts/validate-content.py <code>` and `python scripts/validate-content.py --changed`.
