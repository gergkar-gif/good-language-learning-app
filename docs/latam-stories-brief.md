# LatAm B1 story rewrite: brief for Antigravity (ROADMAP 145c)

You are rewriting the reading texts of the Spanish (Latin America) B1 **`latam` track**:
36 history units, 5 lesson stories each. Read this whole file, then
[AGENTS.md](../AGENTS.md) § "Exercise metadata", before you change anything.

**Start with the pilot unit `central-america-revolution-conflict` only, then stop.**
The user and Claude review it before the other 35 units are done.

## What is wrong

The stories were bulk-generated in one commit (`4bcdc76b`, 2026-09-24). They read like
sentences spliced from templates:

- fragments that start in lower case after a full stop:
  *"…y en las Antillas mayores. sostenido por el trabajo forzoso de millones…"*
- a capital letter after a comma: *"…del 'derrame' de mercado, Se reconoció…"*
- the lesson's grammar frame stacked unnaturally, e.g. three sentences in a row
  starting *"Por más que…"* (`b1-legadosigloveinte-03`)
- empty filler: *"A lo largo de las décadas, los países fueron modificando sus
  sistemas políticos y económicos."*
- **stories that cover the wrong lesson.** In the pilot unit every story is shifted
  one lesson back:

| Lesson | Lesson title | Its story is currently about |
|---|---|---|
| 01 | Nicaragua | roots of the crisis: oligarchy and latifundio |
| 02 | El Salvador | the Sandinista revolution in Nicaragua |
| 03 | Guatemala | the civil war in El Salvador, Romero |
| 04 | Intervención y Guerra Fría | Guatemala: armed conflict, Maya genocide |
| 05 | Los Acuerdos de Paz | Esquipulas and the post-conflict period |

Other units known to be shifted or blurred: `regional-integration` 03/04 (03 is mostly
NAFTA), `end-cold-war` 02–04, `latin-america-1990s` 01–05. The rest are garbled in
places. The exercises, goals and listening sentences were later rewritten **to match
the garbled stories**, so they have to move with the stories.

Only this track has the problem. ES LatAm B2 and HU B1/B2/C1 were checked
(2026-10-08) and are clean: don't touch them.

## Files in one unit

The unit table is `content/es-latam/curriculum/units/b1.json` (entries with
`"track": "latam"`). Each unit has a short file prefix: `central-america-revolution-conflict` is
`b1-centroamerica`. All paths below are under `content/es-latam/`.

| What | File | Per unit |
|---|---|---|
| Lesson (goal, checklist, which story/grammar/vocab it uses) | `lessons/b1/<prefix>-0N.json` | 5 |
| Lesson story | `stories/world/b1/<prefix>-0N-<slug>.json` (path in the lesson's `story` section) | 5 |
| Unit story for the Library | `stories/world/b1/<prefix>.json`, **generated**, see step 6 | 1 |
| Vocabulary list | `vocabulary/b1/<prefix>-0N-voc.json` | 5 |
| Grammar screen | the `grammar` section's `ref` in the lesson | 5 |
| Exercises | `exercises/b1/<prefix>-0N-ex.json` and `<prefix>-consolidation-ex.json` | 6 |

Read the lesson file first: its `sections` list says exactly which story, vocabulary and
grammar file the lesson uses. Other `*-gr.json` files in `grammar/b1/` with the same
prefix that no lesson references are left over from before the overhaul (see step 7).

## Steps, per unit

1. **Read** the five lessons, their vocabulary lists, grammar screens and exercise files,
   and the current stories. Note what each lesson is *supposed* to be about: the
   lesson `title` and the vocabulary decide it, not the current story.
2. **Write five new lesson stories**, in the same files (keep `id`, `level` and the
   file names; replace `title` and `paragraphs`):
   - About the lesson's own topic, in the lesson order. No overlap with the
     neighbouring lessons beyond a linking sentence.
   - B1 Latin American Spanish, 220–280 words, 4–5 `narration` paragraphs, plain
     sentences that a B1 learner can follow. Historically accurate. Use only facts
     you are sure of, with dates and names where they help.
   - Uses **every word in that lesson's vocabulary list** at least once, in the meaning the list
     gives.
   - Uses the lesson's grammar structure (the screen's topic, e.g. *una vez que*,
     *al cabo de*) **2–3 times, naturally**. Never stack it sentence after sentence.
   - The story `title` says the lesson topic in Spanish.
3. **Comprehension questions** in each story: `narration.pedagogical.comprehensionQuestions`
   (3 per story, same shape as now). Each must need the story to answer: quote or
   depend on a specific fact in it, not general knowledge.
4. **Exercises** in that lesson's `-ex.json`. **Keep every exercise `id`, `type`,
   `category` and `teaches`/`distractor_skills` as they are**; only change the text.
   - `reading` exercises: rewrite to ask about the new story (same rule as step 3).
     Wrong options must be plausible, about the same length as the right one, and
     clearly wrong according to the story.
   - `listening` exercises: the sentence they play should be a sentence (or close
     paraphrase) from the new story.
   - `grammar` and `vocabulary` exercises: change them only if they quote or rely on
     story content that no longer exists. Keep the tested form or word the same.
   - The consolidation file: same rules, across all five stories.
   - If an exercise can't be fixed without changing what it tests, don't change its
     tags. Leave it and list it in your report.
5. **Lesson goals.** In each lesson file, rewrite `goal` (one sentence starting
   "Read how…"/"Read about…") and the 5 `goal` section items, with the 5 `checklist` items
   mirroring them ("I can …"), so they describe what the new story, screen and
   exercises actually cover. Fix the grammar screen's example sentences only if they quote
   the old story.
6. **Rebuild the unit's Library story**, for this unit only:
   ```
   python scripts/stitch_track_unit_stories.py --unit es-latam b1 latam <unit id>
   ```
   **Never run it without `--unit`**: that rewrites ~140 unit stories in other courses,
   including hand-edited HU C1 ones.
7. **Leftover grammar screens.** `*-gr.json` files with the unit's prefix that no lesson
   references (in the pilot: `-01-impersonal-se`, `-02-passive-voice`, `-03-gerund`,
   `-04-formal-connectors`, `-05-passive-voice-legado`) are not used anywhere. Delete them,
   after checking with a search that nothing in `content/`, `engine/` or `scripts/`
   mentions their file name. Units 13–36 each have five of these; units 1–12 have none.
8. **Check**, and fix everything it reports:
   ```
   python scripts/validate-content.py --changed
   python scripts/dup_report.py es-latam b1 <unit id>
   ```
   (`dup_report.py` prints nothing when no exercise is copied between lessons.)
   Set `PYTHONIOENCODING=utf-8` on every python command. Write JSON as UTF-8, 2-space
   indent, with no other formatting changes. Then run `git diff --stat`: only this unit's files
   (and the deleted screens) should be listed.

## Hard rules

- **Never** add, rename or merge a skill, edit `skills/*.json`, the generated
  `indexes/*` files or `tags.lock.json`, or run `lock_tags.py` / `apply_tags.py`. The
  units are locked, so the validator fails if a tag changes. That is intended.
- Don't touch the `es-es` course, the `core` track of es-latam B1, or any other level.
- Keep exercise ids, lesson ids, file names and the unit table unchanged.
- One commit per unit: `content(es-latam/b1): rewrite <unit id> stories (ROADMAP 145c)`.
  `git pull --rebase origin master` before `git push origin HEAD:master`.

## Report (per unit, in your final message)

- Each lesson: old story topic → new story topic, word count.
- Every vocabulary word or grammar structure you could not use naturally, and why.
- Exercises you left unchanged because fixing them would change what they test (id + reason).
- Screens deleted, and anything else you noticed but did not fix.

Then update ROADMAP.md item 148(p) with a dated status line: units done, units left,
and anything waiting for review. **Checkpoint:** after the pilot, stop and wait for
review. Don't start the next unit until the user says so.

## Order after the pilot

Shifted units first (`regional-integration`, `end-cold-war`, `latin-america-1990s`), then
the units with the most splice marks (`economiacolonial`, `latamnoventa`, `conosur`,
`movimientosindigenas`, `llegadaeuropeos`), then the rest in unit order. Do at most
three or four units per session, each fully checked and committed before you start the next.
