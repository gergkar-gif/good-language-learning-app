---
name: Parlour
description: A place for language. Cream paper, ink navy, one scarce vermilion mark, and geometry as composition.
colors:
  cream-paper: "#F5F1E8"
  ink-navy: "#102A47"
  ink-navy-deep: "#0A1D33"
  ink-navy-mid: "#3C5570"
  slate-grey: "#5F6B7E"
  muted-blue-grey: "#5A6B80"
  card-white: "#FFFFFF"
  note-cream: "#FDFBF6"
  vermilion: "#E94B16"
  vermilion-deep: "#A8371C"
  vermilion-text: "#B23A18"
  ochre: "#E3A72F"
  sand-tone: "#E9DFC9"
  vermilion-tint: "#FCEBE3"
  brick-danger: "#B23A22"
  brick-tint: "#FAEDE9"
  pine-success: "#2F7A4D"
  pine-tint: "#E8F3EC"
  sand-wash: "#E7DCC3"
  night-bg: "#0C1B2B"
  night-surface: "#12253B"
  night-wash: "#1E3A5A"
  night-vermilion: "#E07148"
typography:
  display:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Charter, 'Bitstream Charter', 'Iowan Old Style', Georgia, Cambria, serif"
  body:
    fontFamily: "Inter, 'Segoe UI Variable Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "16px"
  label:
    fontFamily: "Inter, 'Segoe UI Variable Text', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "14px"
rounded:
  sm: "2px"
  md: "4px"
  pill: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  2xl: "48px"
  3xl: "64px"
components:
  button-primary:
    backgroundColor: "{colors.ink-navy}"
    textColor: "{colors.card-white}"
    rounded: "{rounded.sm}"
    padding: "13px 20px"
  button-primary-hover:
    backgroundColor: "{colors.vermilion}"
  button-accent:
    backgroundColor: "{colors.vermilion}"
    textColor: "{colors.card-white}"
    rounded: "{rounded.sm}"
    padding: "12px"
  button-accent-hover:
    backgroundColor: "{colors.vermilion-deep}"
  button-back:
    backgroundColor: "transparent"
    textColor: "{colors.ink-navy-mid}"
    padding: "6px 4px"
  card:
    backgroundColor: "{colors.cream-paper}"
    textColor: "{colors.ink-navy}"
    rounded: "{rounded.md}"
    padding: "16px"
---

# Design System: Parlour

## Overview

**Creative North Star: "The Composed Room"**

Parlour is a sparse, architectural room, not a dashboard. It should feel like stepping into an abstract painting that happens to teach a language. Space comes first, then typography, then one dominant geometric gesture, then small supporting details. The interface is the composition: a circle can be a state, a line can be an axis, a semicircle can be movement. The visual grammar comes from Kandinsky (circles, arcs, points) and Klutsis (axes, diagonals, tension), filtered through minimalism. They are sources of grammar, never pastiche.

The system is calm, precise, editorial and slightly strange. Rows sit open on cream paper and are separated by hairlines, not stacked in lifted white cards. Titles and content headings are set in a serif; interface chrome stays sans. Colour is rationed: navy carries structure, and vermilion is the one scarce voice for active or live states. Empty space is intentional and must not be filled just because it is empty.

It explicitly rejects the gamified language-app look (mascots, streak flames, confetti, glossy lifted cards) and the generic SaaS dashboard (a stack of white cards with an illustration bolted on). No gradients anywhere.

**Key Characteristics:**
- Warm cream ground, deep navy structure, one vermilion accent, a small ochre second accent, and quiet tonal sand shapes.
- Exactly one dominant geometric gesture per screen; everything else is type, rows and space.
- Serif for content, sans for chrome; system-font stacks, no webfonts loaded.
- Flat by default; depth from hairlines, wash tint and scale.
- Sharp geometry: 2px and 4px radii, pill only when a control truly needs it.
- Geometric primitives (`geo-*`) are functional objects, not decoration.
- Full dark theme (deep navy ground) that follows the system and can be forced.

## Colors

A restrained, near-monochrome paper-and-ink palette with a single hot accent. Semantic colours exist but stay quiet.

### Primary
- **Ink Navy** (#102A47): Text, structure, primary buttons, and the default fill of geometry. Also the source of all hairline borders (as low-alpha tints).
- **Ink Navy Deep** (#0A1D33): Hover state of primary actions.
- **Ink Navy Mid** (#3C5570): Secondary text actions such as back links.

### Secondary
- **Vermilion** (#E94B16): The scarce accent. Active, live and focus states; the single accent button; the geometric gesture that says "here".
- **Vermilion Text** (#B23A18): The darker vermilion for small text (nav labels, figures) where bright vermilion fails contrast on cream.
- **Ochre** (#E3A72F): The colour of material waiting for you: due and new. Used at most once per screen as a shape or marker; for figures and small text use Ochre Text (#855A08 on light, #E3A72F on dark). Added 2026-09-29.
- **Vermilion Deep** (#A8371C): Hover on accent controls and accent text that needs contrast.
- **Vermilion Tint** (#FCEBE3): Quiet background for accent-marked regions.

### Neutral
- **Cream Paper** (#F5F1E8): The page and, deliberately, the card ground.
- **Note Cream** (#FDFBF6): Notes and callouts, a half-step lighter than the page.
- **Card White** (#FFFFFF): Text on filled buttons; not a general card surface.
- **Sand Wash** (#E7DCC3) and **Sand Tone** (#E9DFC9): Warm washes. Sand Tone is the quiet tonal fill for large geometric shapes (discs, arcs) that sit on cream without shouting.
- **Slate Grey** (#5F6B7E) and **Muted Blue-Grey** (#5A6B80): Secondary and muted text.
- **Hairlines**: Ink Navy at 18% (border), 10% (light) and 8% (subtle) alpha.

### Semantic
- **Brick** (#B23A22, tint #FAEDE9): Wrong or needs redoing: incorrect answers, the Again grade, errors.
- **Pine** (#2F7A4D, tint #E8F3EC): Finished or right: correct answers, completed units and levels (accent and progress fill), the Easy grade, mastered words.

### Dark theme
Night Bg (#0C1B2B) ground, Night Surface (#12253B) for surfaces, Night Wash (#1E3A5A), text inverted to cream, and vermilion softened to #E07148 for contrast. Hairlines become cream at 6 to 15% alpha.

### Colour semantics
Every colour has one meaning, everywhere in the app. A colour is never used for a second job, and state is never carried by colour alone (always a word, a mark or a shape as well).

| Colour | Meaning | Examples |
|---|---|---|
| Vermilion | Here and now: the one thing you are on or should do next | Current unit and its ring, the Continue line and dot, the active nav tab, focus rings, primary-button hover, a track's progress marker, your true position on the Journey mountain |
| Pine green | Finished or right | Completed unit or level accent, full progress line, correct answer, Easy grade |
| Brick red | Wrong or needs redoing | Incorrect answer, Again grade, error messages |
| Ochre | Waiting for you: due or new | Review door, due counts, new-story markers, Hard grade |
| Navy | Structure and ordinary content | Text, shapes, buttons, partial progress fill, streak dots |
| Sand and grey | Background, or locked and not yet | Discs, empty tracks, locked units (faded, grey accent) |

### Named Rules
**The Illustration Rule.** Illustration follows the same table. A page's hero accent is vermilion and marks "you are here"; row thumbnails and exercise art carry a neutral grey accent, turning ochre only when the row has something due or new; a lesson-complete screen's accent is pine. Selection (a chosen answer, a chosen tense) is navy, not vermilion.
**The One Meaning Rule.** Vermilion means "here and now", pine means "finished or right", brick means "wrong", ochre means "waiting for you". Do not borrow a colour for decoration where it would read as one of these states.
**The One Voice Rule.** Vermilion is rationed for active or live states and focus. If it appears on more than one element competing for attention, one of them is wrong.
**The Paper Rule.** Cards share the page's cream ground. White is for text on fills, not for lifting a surface off the page.
**The No Gradient Rule.** Flat fills only.
**The Punctuation Rule.** Vermilion and ochre are punctuation, not fill: a dot, a hairline, a small square. A full block of either is the exception, not the pattern.

## Typography

**Display Font:** Source Serif 4 (with Source Serif Pro, Charter, Iowan Old Style, Georgia, Cambria, serif)
**Body/UI Font:** Inter (with Segoe UI Variable Text, system UI faces, Arial, sans-serif)

**Character:** A transitional serif with a large x-height for titles and reading content against a plain neutral sans for interface chrome. No webfonts are loaded, so the app works offline, never flashes unstyled text, and respects system font-size settings.

### Hierarchy
- **Display** (serif, page and section titles, content headings): Sets the editorial voice.
- **Body** (sans, 16px): Interface text and controls; also the default button text size.
- **Label** (sans, 13 to 14px): Secondary actions, back links, small controls.
- Exact sizes for headings are set per component and not yet consolidated into a scale.

### Named Rules
**The Serif-For-Content Rule.** Titles and content headings use the serif; controls, labels and chrome stay sans.
**The Paradigm Rule.** A grammar screen shows forms in a table, never buried in prose.

## Layout

Open rows on cream separated by hairlines; whitespace is the primary structure. Spacing follows a 4px base (4, 8, 12, 16, 24, 32, 48, 64, 96) exposed as `--space-1` to `--space-9`, though many existing components keep hand-tuned px values; the scale is for new composition work. Responsive behaviour breaks at 639px and below (phone), 640 to 1023px (tablet) and 1024px and above (desktop, where a sidebar replaces bottom navigation). Phone is the primary device. Text scale can be adjusted by the reader.

## Elevation & Depth

Flat by default. `--shadow` (0 1px 3px, navy at 6% alpha) is defined but deliberately unused: a softened, shadowed card style was tried and reversed on 2026-08-14 because the identity is open rows and hairlines. Depth comes from hairline borders, the sand wash, and scale contrast of a single geometric gesture.

### Named Rules
**The Flat-By-Default Rule.** No resting shadows. Hover changes border colour (hairline to navy), not elevation.

## Shapes

Composition comes from a few large tonal shapes (sand discs, navy half-discs) with hairline axes ending in a small dot. Sharp and architectural: 2px on buttons, 4px on cards and containers, pill (999px) reserved for the rare control that needs it. Recurring form language is Kandinsky-derived geometric primitives (circle, semicircle, arc, triangle, square, dot) built as reusable `geo-*` objects with `--geo-size` modifiers (12, 24, 64, 128px). Preferred motif: two-tone disc art centred on a line, with no dot marker.

### Named Rules
**The Earned Object Rule.** A geometric object appears only if it carries meaning (state, axis, movement). Never add one because a screen feels empty.

## Components

### Buttons
- **Shape:** Small and rectangular (2px radius), 13px 20px padding, 15px semibold text, no border. Never a pill.
- **Primary:** Ink Navy fill, cream text. A hairline vermilion line may extend from it and end in a dot. Hover turns it vermilion; press deepens it to Ink Navy Deep.
- **Accent:** Vermilion fill, white text; hover to Vermilion Deep. Use for the single most important action.
- **Back / typographic action:** No fill; Ink Navy Mid text that darkens to Ink Navy on hover.

### Cards / Containers
- **Corner Style:** 4px radius.
- **Background:** Cream Paper, same as the page.
- **Border:** 1px hairline (Ink Navy 18%); hover shifts the border to full Ink Navy over 180ms.
- **Shadow Strategy:** None.
- **Internal Padding:** 16px, 12px gap between cards.

### Focus
- One treatment app-wide: a 2px vermilion outline with a 2px offset on `:focus-visible`. Components already in a vermilion active state may override.

### Motion
- Durations 180ms (fast), 280ms (base), 450ms (slow) with `cubic-bezier(.4, 0, .2, 1)`. Sections enter with a 200ms fade and 8px rise. Under `prefers-reduced-motion` all durations collapse to 1ms.

### Navigation
- Bottom navigation on phone (70px, heavy 3px navy top rule); a sidebar at 1024px and above with a 3px navy edge. Header is editorial and carries no running state.
- Each page has its own icon, a small composition of navy shapes plus one accent shape: Home a doorway with a half-disc, Lessons a half-disc with lines rising to a point, Library bars with a circle, Workshop a pivoting beam with a square, Decks layered cards with a coloured edge, Journey a path to a square. Icons are 30px.
- Only the active or hovered item shows its accent in vermilion; the rest are single-colour. The active tab gets a vermilion bar on the rule (top on phone, left on desktop) and the accent nudges 2px.

### List rows
- Open rows on 1px hairlines with a serif name, muted description, a figure only when it decides whether to open the row, and a small two-shape thumbnail. No card frames, no shadows.

## Do's and Don'ts

### Do:
- **Do** lead each screen with space, type and at most one dominant geometric gesture.
- **Do** separate rows with hairlines (Ink Navy at 8 to 18% alpha) on cream.
- **Do** ration Vermilion to active, live and focus states.
- **Do** use the serif for titles and content, the sans for chrome.
- **Do** keep a dark theme equivalent for every new colour and honour reduced motion.
- **Do** show grammar forms as tables.

- **Do** keep to one dominant gesture and large amounts of cream per screen.
- **Do** use ochre once and vermilion sparingly on a screen.

### Don't:
- **Don't** use mascots, streak flames, confetti or glossy lifted cards: no gamified language-app look.
- **Don't** stack white shadowed cards or bolt illustrations onto a dashboard.
- **Don't** add resting shadows, gradients or large radii.
- **Don't** add geometric objects to fill emptiness.
- **Don't** load webfonts; keep system stacks so the app stays offline-safe.
- **Don't** put running state (streaks, counters) in the header.
- **Don't** fill a screen with a navy slab or several colour blocks; that reads as an app, not a painting.
- **Don't** use pill buttons or rounded chips as primary controls.
- **Don't** show every nav icon's accent in vermilion at once.
