# Parlour CEFR Curriculum Roadmap

**Status**: Phases 1 through 14 **COMPLETED** ✅ — archived to `ACHIEVED.md` (section "Completed Curriculum Phases").  
**Remaining**: Strategic & product ideas scheduled as **TO-BE-DONE LATER** ⏳

---

## How units get wired in (as of 2026-09-16)

Authoring a unit's lesson/grammar/exercise/vocabulary files is not enough
on its own — a level's unit titles, ordering, and lesson-stem groupings
are a separate, curated list, and a lesson file with nothing pointing at
it is invisible to the Learn tab (this happened to the Phase 2 imperfecto
content: it validated cleanly for a while before anyone wired it in).

For a level that already has an explicit table (Spanish A1/A2/B1,
Hungarian B1), add a new unit like this:

1. Author and validate the lesson/grammar/exercise/vocabulary files as
   usual (`python scripts/validate-content.py`).
2. Append one entry to `content/<lang>/curriculum/units/<level>.json`:
   `{"title": "...", "stems": ["<level>-<slug>-01", ..., "<level>-<slug>-consolidation"]}`
   (add `"track": "core"` / `"latam"` / etc. only for a level that runs
   more than one parallel track). Schema:
   `content/<lang>/schemas/units.schema.json`.
3. Run `python build-manifest.py` (or just push — `sync-generated-content.yml`
   does this automatically for anything touching `content/**`) to
   regenerate `curriculum.json`, `decks.json`, and the story/grammar
   indexes.

No `build-manifest.py` edit needed — before 2026-09-16 this table lived
in a hardcoded Python dict there, which is exactly what made Phase 2's
imperfecto units hard to wire in after the fact. A level with no such
file (Hungarian A1/A2 today) instead auto-groups plain-numbered lesson
files from disk (`auto_group_units()` in `build-manifest.py`) — nothing
to hand-wire there either way.

---

## 💡 Strategic & Product Ideas [TO-BE-DONE LATER]

*Most of these are product/design-level ideas. No priority order — capture for future sprints.*

- [ ] **Reverse-engineer competitor apps for feature ideas** — systematically audit apps like Duolingo, Babbel, Clozemaster, Conjuguemos, Busuu etc. for UX patterns, exercise types, and engagement hooks worth adapting.
- [ ] **Listening Lab — extended audio-passage comprehension** — the existing Listening Driller (`engine/drills/listening.js`) is single-sentence/TTS-based only; this is a longer-form mode adapting the Conjuguemos model for paragraphs and short dialogues at A2–B1, not a from-scratch listening feature.
- [ ] **Cyberpunk hero page load animation** — on page load, the hero section "powers up" element by element (think a machine booting, cyberpunk aesthetic). Stagger reveals of logo, tagline, CTA buttons, stat cards, etc.
- [ ] **User-configurable feature visibility (especially Workshop)** — let users choose which modules/features are shown in their dashboard. Too many options at once creates friction; a simple onboarding toggle or settings page can hide unused sections.
- [ ] **IP / attribution audit for content-engine resources** — review all third-party content used (word lists, texts, images, audio). Where Creative Commons material is used, add a dedicated acknowledgments page or footer alongside AI-use disclosure.
- [ ] **Language expansion roadmap** — finish Spanish & Hungarian content → V4 release milestone → Eastern European languages (e.g. Polish, Czech, Romanian) → Vietnamese.
- [ ] **Hungarian Stories Length Expansion (B1 & B2 Classics)** — expand compressed Hungarian literary classic adaptations in `content/hu/stories/classics/` to align with the library word-count standards:
  - **B1 Classics (~400 words target)**: 32 of 36 Hungarian B1 classic adaptations currently average ~225 words, with severe outliers under 120 words (*Édes Anna* `b1-10`: 114w, *Légy jó mindhalálig* `b1-11`: 98w, *Szindbád* `b1-12`: 91w). Expand these to ~400 words while maintaining B1 grammar and dialogue.
  - **B2 Classics (~700 words target)**: All 36 Hungarian B2 classics currently average ~288 words (e.g. *Pacsirta*, *A vörös postakocsi*, *Bánk bán*, *Ábel a rengetegben*, *Sorstalanság*, *Az ajtó*). The prose and dialogue are authentic, but need expansion from 1-page vignettes into immersive ~700-word B2 literary adaptations with text-grounded comprehension questions.
  - **B1/B2 World/Civics shelf**: Consider expanding short thematic cultural vignettes (currently averaging ~130 words at B1 and ~360 words at B2).

