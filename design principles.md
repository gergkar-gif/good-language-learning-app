# Parlour Visual Identity Principles (v2.0)

Supersedes `archive/design-principles-v1-superseded.md` (soft-workbook/teal-green direction — contradicted the geometric identity already built). Drafted 2026-08-14 from a set of reference mockups the user shared and a series of decisions made while reviewing them.

## Vision

**Parlour should feel like stepping into an abstract painting.**

Not a digital workbook. The geometric shapes, colour and composition aren't decoration around the interface — they *are* the interface. Every screen should read as one considered composition in the Kandinsky / Constructivist lineage already established in `parlour_visual_overhaul_spec.md` §35, expressed now with more specificity: a fixed per-level icon system, a hand-drawn-feeling path connecting units, and full page compositions rather than isolated hero art.

## How this doc relates to others

- **This file** — vision and principles, concise, meant to be kept current.
- **`parlour_visual_overhaul_spec.md`** — the exhaustive technical spec (exact colour ramps, geometric primitives, spacing scale, CSS architecture). Still authoritative for anything this doc doesn't explicitly update.
- **`archive/design-principles-v1-superseded.md`** — the old doc, kept for history, not for guidance.
- **The reference mockups themselves are visual references only**, not feature or IA specs. Page structure, tab sets, and exercise mechanics they show are illustrative — defer to each feature's own spec (`workshop-drillers-spec`, `parlour-listening-driller`, `parlour-vocabulary-driller-redesign`, `parlour-library-my-texts-feature`, `parlour-decks-my-decks-feature`, `home-screen-spec`, and the `PARLOUR_*.md` files).

## Core Principles

1. **Compositional, not decorative.** Geometry is the interface's language. Shapes, lines and colour placement should read as a single considered composition — the way the reference mockups treat per-unit illustrations, hero art, and nav icons as one coherent system, never clip-art bolted onto a conventional UI.
2. **Calm but not sterile.** Restrained palette, generous whitespace — but warm and tactile, not flat-minimal. Rounded cards and soft shadows read as inviting, not corporate.
3. **Purposeful.** Every element earns its place. Ask "why is this here?" before adding anything.
4. **Structured.** The learner is always visibly moving through a defined path. The winding unit-path visualization — and its fork/join for dual-track levels like B1 — draws progress rather than just stating it.

## Palette

Cream `#F5F1E8`, deep navy `#102A47`, deep orange `#E94B16` remain the primary system — see spec §4 for full ramps and usage.

**Updated 2026-08-14: green and red are reintroduced, sparingly.** Scoped to spaced-repetition/mastery feedback — the "Mastered" stat, "¡Correcto!" review confirmation, retention chart, and Again/Easy SRS buttons. General lesson-exercise correctness stays navy (correct) / accent-dark (incorrect) unless later revisited — this scoping is a working assumption, not something explicitly confirmed, so check before leaning on it further.

## Geometry & Iconography

Shape vocabulary — circle, semicircle, triangle, line+dot ("lollipop") — combines into per-page hero compositions and small icons, per spec §6 and §11.

**New: a fixed per-CEFR-level icon**, reused everywhere that level appears (nav, lesson list, unit headers):

| Level | Icon |
|---|---|
| A1 | solid semicircle + mast + dot |
| A2 | circle + wedge |
| B1 | circle bisected diagonally + dot |
| B2 | angle + crossing rule + small triangle |
| C1 | diagonal line + dot |

Each is **two-tone: navy structure with exactly one orange element** (`.li-accent`). Rationing orange to a single mark per icon keeps it scarce while still giving the level list its rhythm.

**New: the winding unit path.** Units sit as nodes on a hand-drawn-feeling connecting line rather than a plain vertical list. Dual-track levels (B1 Core/LatAm) fork into two paths and rejoin at a ringed junction node.

## Typography

Serif display for titles (`--font-display`, system serif stack, no webfont), sans-serif for interface text — unchanged, see spec §5.

## Cards, radius & shadow — settled 2026-08-14

**Open rows on cream, divided by hairlines — not a stack of lifted white cards.** Sharp radius (`--radius: 4px`, `--radius-sm: 2px`) and **no shadows anywhere**; `--shadow` stays defined but unused.

This was briefly reversed earlier the same day (14px/8px radius with a real shadow, cards applied across the app) before checking against the reference Lessons list, which is unambiguously open rows. Applies to list surfaces app-wide — the Lessons level list and the Workshop picker are both open rows. Lightly framed panels (a bordered area with a background) are still allowed where a region genuinely needs bounding; what is not allowed is a list rendered as a stack of elevated cards.

Answer options are the deliberate exception — see below.

## Answer / interactive options — reversed 2026-08-14

Multiple-choice and similar options are **bordered boxes with a fill-tint highlight** for the selected/correct/incorrect state (e.g. orange-tinted fill for the selected option), replacing the underlined-typographic-object treatment. This reverses `.lsn-option`/`.gd-option` in `styles/components.css`.

This is the one place a bordered, filled box is correct — the references show it clearly, and an answer needs to read as a target you hit. It is not licence to reintroduce cards elsewhere.

## The Lessons level list

The canonical example of the row language. Each level is an open row: a two-tone level mark (~48px), the **level code as the serif heading** with the level name beneath it as the gloss and the description below that, a short right-aligned progress track with an orange fill, and a thin drawn chevron. The level code leads because this is the list of levels — the code is what identifies one.

## Navigation

- Target: a **desktop sidebar shell** — logo mark, nav list (Home, Lessons/Learn, Library, Workshop, Decks, Journey, Settings), streak pinned at the foot. **Not yet built** — deferred; the app stays a single ~500px column at all widths for now.
- The "Lessons" vs "Learn" nav label, and a possible future rename to "Study," are both unsettled and deliberately deferred — don't resolve either as part of this pass.
- Mobile nav (bottom bar) is untouched by this reference set — no mobile mockups were shared.

## Small components worth adopting

- **Word-status pill** — a "known / new / to review" indicator next to vocabulary (filled / outline / dashed dot). Worth making a shared component wherever word familiarity is shown: Reader, Decks, Vocabulary driller.
- **Inline word popup** — tap a word → definition, Listen, Add to deck, in a small rounded card. The visual treatment is worth carrying over; the feature itself is already spec'd in the Library/Reader work.

## Copy discipline

Never fabricate quotes or attributions — in mockups, placeholder copy, or shipped content. If a design calls for a quote, source and cite a real one, or leave the slot empty.

## Guiding principle

Every screen should feel like a piece of the same abstract composition — geometry, colour and structure carrying meaning, never decoration for its own sake.
