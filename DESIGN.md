---
name: Parlour
description: A place for language. Cream paper, ink navy, sand discs, and geometry as composition, with colours that each mean one thing.
colors:
  cream-paper: "#F5F1E8"
  ink-navy: "#102A47"
  ink-navy-deep: "#0A1D33"
  ink-navy-mid: "#3C5570"
  slate-grey: "#5F6B7E"
  muted-blue-grey: "#55677D"
  card-white: "#FFFFFF"
  note-cream: "#FDFBF6"
  vermilion: "#E94B16"
  vermilion-deep: "#A8371C"
  vermilion-text: "#B23A18"
  vermilion-tint: "#FCEBE3"
  ochre: "#E3A72F"
  ochre-text: "#855A08"
  sand-tone: "#E9DFC9"
  sand-wash: "#E7DCC3"
  brick-danger: "#B23A22"
  brick-tint: "#F6E4DF"
  pine-success: "#2F7A4D"
  pine-tint: "#E3EFE7"
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
    fontSize: "13px"
rounded:
  sm: "2px"
  md: "4px"
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
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink-navy}"
    rounded: "{rounded.sm}"
    padding: "13px 20px"
  answer-option:
    backgroundColor: "{colors.cream-paper}"
    textColor: "{colors.ink-navy}"
    rounded: "{rounded.sm}"
    padding: "15px 16px"
  keyword-chip:
    backgroundColor: "transparent"
    textColor: "{colors.muted-blue-grey}"
    rounded: "{rounded.sm}"
    padding: "7px 10px"
---

# Design System: Parlour

Reference implementation of every screen described here: `docs/overhaul-prototype/index.html` (open it through the dev server, `/docs/overhaul-prototype/index.html`). Its `screens.js` holds the generators and the screen list, its `overhaul.css` the rules. Where this file and the prototype disagree, fix the prototype or this file, not the app.

## Overview

**Creative North Star: "The Composed Room"**

Parlour is a sparse, architectural room, not a dashboard. It should feel like stepping into an abstract painting that happens to teach a language. Space comes first, then typography, then one dominant geometric gesture per screen, then small supporting details. The visual grammar comes from Kandinsky (discs, arcs, points) and Klutsis (axes, diagonals, tension), filtered through minimalism. They are sources of grammar, never pastiche.

The system is calm, precise, editorial and slightly strange. Rows sit open on cream paper and are separated by hairlines; there are no stacks of lifted white cards. Titles and content headings are set in a serif; interface chrome stays sans. Shapes are flat, clean and geometric, with no grain, texture or gradients (a textured, painted look was tried on 2026-09-29 and rejected). Every colour means exactly one thing (see Colour semantics).

It explicitly rejects the gamified language-app look (mascots, streak flames, confetti, glossy lifted cards) and the generic SaaS dashboard (a stack of white cards with an illustration bolted on).

**Key Characteristics:**
- Cream ground, ink-navy structure, tonal sand discs, a small vermilion accent, ochre for "waiting for you", pine and brick for right and wrong.
- Exactly one dominant geometric gesture per screen; everything else is type, rows and space.
- Serif for content, sans for chrome; system-font stacks, no webfonts.
- Flat by default; depth from hairlines and scale, never shadows.
- Sharp geometry: 2px radii, no pill controls.
- Every page has its own hero composition and its own nav icon, drawn from the same parts.
- A full dark theme that follows the system and can be forced.

## Colors

A near-monochrome paper-and-ink palette. Accent colours are punctuation, not fill.

### Primary
- **Ink Navy** (#102A47): Text, structure, primary buttons, and the default fill of geometry. Hairline borders are navy at low alpha.
- **Ink Navy Deep** (#0A1D33): Press state of primary actions.
- **Ink Navy Mid** (#3C5570): Secondary text actions such as back links.

### Secondary
- **Vermilion** (#E94B16): "Here and now". Never a large fill, except as a single accent shape in a hero.
- **Vermilion Text** (#B23A18): The darker vermilion for small text (labels, figures) where the bright one fails contrast on cream.
- **Ochre** (#E3A72F): "Waiting for you": due and new. A shape or marker, at most once per screen. For figures and small text use **Ochre Text** (#855A08 on light, #E3A72F on dark).
- **Vermilion Deep** (#A8371C): Accent text that needs more contrast.

### Neutral
- **Cream Paper** (#F5F1E8): The page and, deliberately, every container's ground.
- **Sand Tone** (#E9DFC9): The tonal fill for large discs and arcs, and the quiet region behind the Journey mountain.
- **Sand Wash** (#E7DCC3), **Note Cream** (#FDFBF6): Rare washes for regions that need to sit forward or back.
- **Card White** (#FFFFFF): Text on filled buttons and the vermilion or brick accents only.
- **Muted Blue-Grey** (#55677D): Secondary and muted text, empty tracks' labels.
- **Hairlines**: Ink Navy at 16 to 18% alpha.

### Semantic
- **Pine** (#2F7A4D, tint #E3EFE7): Finished or right.
- **Brick** (#B23A22, tint #F6E4DF): Wrong or needs redoing.

### Dark theme
Night Bg (#0C1B2B) ground, Night Surface (#12253B), Night Wash (#1E3A5A), navy and cream swapped (text cream, "navy" shapes cream), sand tone becomes #16304B, pine #52A374, brick #E87A63, vermilion text #F0784A. Hairlines become cream at 18% alpha.

### Colour semantics
Every colour has one meaning, everywhere in the app. State is never carried by colour alone: always a word, a mark or a shape as well.

| Colour | Meaning | Examples |
|---|---|---|
| Vermilion | Here and now: the one thing you are on or should do next | Current unit and its ring, the Continue line and dot, the active nav tab, focus rings, primary-button hover, a track's progress marker, your true position on the Journey mountain, the record disc |
| Pine green | Finished or right | Completed unit or level accent, full progress line, correct answer, completed stretch of the Journey, Easy grade, a passed test, a met keyword, "Complete" |
| Brick red | Wrong or needs redoing | Incorrect answer, the Again grade, marks in a learner's own text, error messages |
| Ochre | Waiting for you: due or new | Review door, due counts, new-story markers, new and review words in the Reader, confidence gaps, the Hard grade |
| Navy | Structure and ordinary content | Text, shapes, buttons, partial progress fill, streak dots, a selected answer or tense, score-track markers |
| Sand and grey | Background, or locked and not yet | Discs, empty tracks, locked units (faded, grey accent), row thumbnails with nothing due |

### Named Rules
**The One Meaning Rule.** Vermilion means "here and now", pine means "finished or right", brick means "wrong", ochre means "waiting for you". Do not borrow a colour for decoration where it would read as one of these states.
**The Illustration Rule.** Illustration follows the same table. A page's hero carries one vermilion accent that marks "you are here" (Home's knob, Lessons' point). Row thumbnails, exercise art and flash-card art use a grey accent, turning ochre only when the row has something due or new. A completion screen (lesson complete, test passed, all caught up) uses pine.
**The One Voice Rule.** If vermilion appears on more than one competing element on a screen, one of them is wrong.
**The Paper Rule.** Containers share the page's cream ground. White is for text on fills, not for lifting a surface off the page.
**The No Gradient, No Texture Rule.** Flat fills only.
**The Punctuation Rule.** Vermilion and ochre are a dot, a hairline, a small square. A large block of either is the exception.

## Typography

**Display Font:** Source Serif 4 (with Source Serif Pro, Charter, Iowan Old Style, Georgia, Cambria, serif)
**Body/UI Font:** Inter (with Segoe UI Variable Text, system UI faces, Arial, sans-serif). Confirmed: keep this system stack; no webfont is loaded.

**Character:** A transitional serif with a large x-height for titles and reading content against a plain neutral sans for interface chrome. The app works offline, never flashes unstyled text, and respects system font size.

### Hierarchy
- **Page title** (serif 400, clamp 2.4 to 3.2rem on phone, 4.4rem on desktop, line-height about 1, letter-spacing -0.02em): once per page, beside the hero.
- **Section heading** (serif, 1.3 to 1.4rem): "Explore", "Skills", shelf titles.
- **Row name** (serif, 1.15 to 1.3rem): rows, cards, unit titles.
- **Figure** (serif, 1.6 to 2.6rem): due counts, big stats, in ochre text when they mean "due".
- **Body** (sans, 16px): descriptions, in muted blue-grey when secondary.
- **Label** (sans 600, 12 to 13px): counts, tabs' small text, chips.
- Reader text: serif 1.25rem, line-height 1.75, measure about 34em.

### Named Rules
**The Serif-For-Content Rule.** Titles and content headings use the serif; controls, labels and chrome stay sans.
**The Paradigm Rule.** A grammar screen shows forms in a table, never buried in prose.

## Layout

Open rows on cream separated by hairlines; whitespace is the primary structure. Spacing follows a 4px base (4, 8, 12, 16, 24, 32, 48, 64). Page gutter 20px on phone, 56px (max width 940px) on desktop.

- **Phone (up to 639px)** is the primary device. **Bottom navigation** (70px, heavy 3px navy top rule). This changes the current app, which uses a top bar on phones.
- **Tablet (640 to 1023px)**: the phone layout as a centred column, 640px wide, with the bottom nav limited to 560px.
- **Desktop (1024px and up)**: a 210px sidebar with the Parlour wordmark and tagline, a 3px navy edge, and the six sections.
- **Focus screens hide navigation entirely**: lessons and their exercises, the level test, Speaking and Writing Studios, drillers, review, and sheets. The only way out is the close button.
- **Desktop specifics**: the unit path keeps phone geometry (460px wide) so its line never reaches the labels; focus screens sit in a centred 720px column; the streak line and grid stay 30em wide.
- **Page header**: serif title top-left, one-line lede (max 11.5em) beneath, the hero at top-right. Header minimum height 200px on phone.
- **Heroes** are 252 x 184 (20% wider and 20% shorter than the first attempt), sitting 36px from the top, anchored right; 380 x 277 on desktop (the header is 330px tall there so the hero never overlaps content below). Keep title and lede clear of the artwork (shorten diagonals and axes rather than letting them run under text).

## Elevation & Depth

Flat by default. `--shadow` exists but is unused. Depth comes from hairlines, a heavy 3px navy rule (navigation, section starts), sand discs behind content, and scale contrast. Sheets are separated from the page they sit over by dimming the page to 35% and giving the sheet a 3px navy top rule.

### Named Rules
**The Flat-By-Default Rule.** No resting shadows. Hover changes a hairline to navy or fills a control, never lifts it.

## Shapes

Sharp and architectural: 2px on controls, 4px only where a container needs a corner. **No pill, no capsule, no chip-shaped primary control.**

### The door (the app's mark)
The Home hero and the Home nav icon are the app's open door, deconstructed into Kandinsky and Klutsis parts: a free navy **wedge** for the leaf, a **hinge line** standing beside it, a short **lintel** line, a hairline **swing arc** sweeping out from the hinge, a **sand disc** behind as light, a diagonal axis running on from the wedge's hypotenuse, a baseline, and one vermilion **knob** on the wedge. Same parts in the nav icon at 30px, without the disc. The knob turns vermilion only when Home is active or hovered.

### Page heroes
Each page has its own single composition, built from sand disc, navy shapes, hairlines and one vermilion accent:
- Home: the door (above).
- Lessons: a navy half-disc on a baseline, hairlines rising to a vermilion point.
- Library: bars of unequal height, one outlined, with a vermilion circle.
- Workshop: a pivoting beam, a navy circle, a vermilion square.
- Decks: layered outlined cards in front of a navy card, a vermilion edge line.
- Journey: a navy start point, a curve, a vermilion square destination.

### Level marks (A1 to C1)
Five fixed two-part compositions on a sand disc, one accent each: A1 a half-disc on a baseline; A2 two overlapping discs and a diagonal; B1 a navy quarter-disc and a square; B2 a navy right triangle crossed by a vertical; C1 an arc over a small disc crossed by a diagonal. The accent colour follows state: pine when the level is complete, vermilion for the level you are on, grey otherwise.

### Unit marks and story covers (generated)
Each unit, and each library story cover, gets its own composition generated from its id (`unitMark(seed)` in the prototype; deterministic: the same id always gives the same picture). Rules: one sand disc (radius 21 to 25, slightly offset); one navy form from eight (half-disc, quadrant, small disc, ring, right triangle, band, big overlapping disc, two opposite quarters) rotated in 90 degree steps; optionally a hairline axis or a second, smaller navy form on the opposite side (never beside a navy disc); exactly one accent (dot or square) placed roughly opposite the main form. The accent follows state (pine complete, vermilion current, grey locked). Use the story or unit id as the seed, for example `b2-32`.

### Named Rules
**The Earned Object Rule.** A geometric object appears only if it carries meaning (state, axis, movement). Never add one because a screen feels empty.

## Components

### Buttons
- **Primary:** small rectangle (2px radius), navy fill, cream text, 13px 20px padding, 15px semibold. Hover fills vermilion; press deepens to navy deep. Disabled at 35% opacity.
- **Ghost:** transparent, 1.5px navy inset outline; hover fills navy.
- **Continue line:** the primary action on a page may carry a 1.5px vermilion rule running out to the edge with a small vermilion dot near its end. One per screen.
- **Text action** (`linkbtn`): muted, underlined 1px, 4px offset; danger variant in brick.
- **Choice block** (welcome flow): full-width 1.5px navy outline, serif label with a drawn arrow; hover fills navy.
- **Time options** ("Short on time?"): four small outlined rectangles (5, 10, 20, 30 min) directly under Resume lesson on Home, each opening the study plan.

### Tabs and segments
Tabs are type on a rule: serif labels on a 1px hairline, the selected one navy with a 3px navy underline. Segments (time picker) are rectangular outlined options; the selected one fills navy.

### Navigation
- Six sections: Home, Lessons, Library, Workshop, Decks, Journey. Each has its own icon at 30px, a small composition of navy shapes plus one accent: Home the door, Lessons a half-disc with lines rising to a point, Library bars with a circle, Workshop a pivoting beam with a square, Decks layered cards with a coloured edge, Journey a path to a square.
- Only the active or hovered item shows its accent in vermilion; the rest are single-colour. The active item takes a vermilion bar on the rule (top on phone, left 6px on desktop) and its accent nudges 2px. Labels 11px (phone) or 15px (desktop).

### Rows
Open rows on 1px hairlines: serif name, muted description, a figure only when it decides whether to open the row (due counts in ochre), and a 72px two-shape thumbnail on the right. No card frames, no shadows. Level rows lead with the level mark, the code in serif, the level name, a track and a count ("Complete" in pine at 100%). Story rows lead with the generated cover, then a "Part n" label, title, author or unit, and a meta line: "Within reach" (ochre), "Quiz 4/5" (pine), "% familiar" (grey); a green tick when read; a track with a vermilion marker and percent when in progress.

### Progress tracks
A 3px hairline track with a navy fill and a vermilion marker at the current position. At 100% the fill is pine and the marker disappears. Score and skill tracks use a navy marker.

### The Journey
- Order: hero, Consistency (streak, best and rank, the 30-day grid: navy squares for active days, a vermilion ring on today), the **mountain**, then quiet rows that open their own screens (Can-Do Passport, Grammar and vocabulary, Skills, Milestones, Account and appearance).
- **The mountain**: a right-triangle ridge, A1 at the left to C1 at the summit, in five equal bands. The climbed part is solid navy, the rest an unfilled sand region with a dashed ridge; gates between levels are green when passed and hollow otherwise; a hollow square flag marks the summit. The vermilion marker sits at the learner's true position between the gates (completed levels plus the fraction through the current one). A sand disc sits behind the upper ridge.

### Lesson exercises
- **Answer options:** bordered rectangles (2px radius) with a letter key. Neutral 1.5px hairline outline; hover navy outline; selected 2px navy outline on a light sand fill. Correct: pine outline, pine tint, drawn tick. Incorrect: brick outline, brick tint, drawn cross; the correct answer also shows pine. Correctness is always a mark and a word too.
- **Feedback strip** sticks to the bottom: 3px pine or brick top rule, tint fill, serif title with drawn mark ("Correct", "Not quite"), one line of explanation, Continue in pine or brick.
- **Typed answers:** a 1.5px field, accent keys (á é í ó ú ñ ¿ ¡) as 38px squares beneath.
- **Listen:** a 96px navy disc with a cream play triangle. **Speak:** a 96px vermilion disc with a ring (record), a stop square when live, a timer and waveform (navy where recorded, hairline ahead).
- **Match pairs:** two columns of options; matched pairs pine.
- **Dialogue:** speaker label in small caps sans, line in serif; the learner's lines indented; reply options as answer options.
- **Keyword chips** (writing, tests): outlined rectangles, turning pine with a tick as the learner uses each word. Word counter below the field.
- **Learner text feedback:** the learner's version struck through in brick, the correction in pine serif, a one-line reason in muted sans; marks inside running text are dashed brick underlines.

### Switches
A switch is a 46 x 24 rectangle (2px radius) with a 1.5px navy outline and a 16px navy square at the left when off; on, it fills navy and the square turns cream and slides right. The label is serif, "What's this?" is a text action. Never a pill toggle.

### Lessons: tools, units, Word Bank, diagnostic
- **Tool rows** sit above the level list on the Lessons page: "Search Grammar Guide" and "Take the placement diagnostic". The Hungarian Cultural Exam does not appear anywhere in Lessons (neither here nor on citizenship-track unit pages); it lives only in the Workshop's Exam Preparation section. Open rows on hairlines with a serif name, a muted description and a drawn arrow that nudges 4px on hover. A navy rule opens the group.
- **Unit page** (a unit on the path opens it): a muted unit number, the serif unit title, the track and lesson count, and the unit's generated mark at the top right. Then the tool rows (Grammar Guide, Word Bank, Oral Roleplay), then "Unit path": a vertical line with a node per lesson (pine when done, a vermilion ring for the one you are on, hollow when ahead), the lesson number, the title, and "Done" or "Continue" beside it.
- **Word Bank:** numbered topics ("What you'll encounter") with a navy rule under each heading, then word and meaning rows; "Add all to a deck" is a text action.
- **Placement diagnostic:** an introduction (format, time, passing mark as label and value rows, one honest note that it is a screener, not a certificate) with a Begin button; the questions reuse the lesson exercise screens; the result names a suggested level with a pass mark per level using the level marks.

### Reference pages (Grammar Guide, lexicon)
- **Topic list:** a large muted serif number, the topic in serif with its one-line description, and a text action "Practise" at the right. A "Search grammar across the whole course" text action follows.
- **Paradigm table:** forms always sit in a table (pronoun in small grey sans, form in serif), a navy rule above the first row, hairlines between rows. Examples follow as serif lines with a muted translation.
- **Level tag:** a small outlined square with the level code (A1 to C1) marks search results and topics.
- **Morphology ladder** (Hungarian Reader lexicon): a word is shown in a sheet split into its parts (stem, plural, possessive, case) as outlined boxes joined by plus signs, each with its meaning beneath.

### Word and story lists
Deck words carry a small status square: hollow ochre for new, half navy for learning, solid pine for mastered, always with the word beside it. Search matches are underlined with a sand highlight; a search with no results says what was searched and offers to clear it.

### Notes, support and states
- **First-time note:** a margin note between hairlines: a 10px navy square, one italic serif sentence in the app's voice (understated, slightly wry), and a "Got it" text action. Never a modal, never a coloured card.
- **Support sheets** (report a problem, back up your progress) follow the sheet pattern. The report sheet names what it is about (story and paragraph).
- **Offline and load-failure states** are full pages with a small hero (a dashed route to a hollow square for offline, a crossed frame for failure), a title, one muted reassurance line (progress is safe) and Try again plus an escape.

### Fields and sheets
Fields are a 1.5px hairline inset box (2px radius), serif text, navy 2px on focus. Checklist items use an 18px square box, navy filled with a cream tick when checked. Sheets sit at the bottom over a page dimmed to 35%, with a 3px navy top rule, a serif title, content, then the actions; cancel is a text action.

### Focus
One treatment app-wide: a 2px vermilion outline with a 2px offset on `:focus-visible`.

### Motion
Durations 120 to 280ms with `cubic-bezier(.16, 1, .3, 1)` for movement; hover fills are 120ms linear. One authored moment per page: the hero accent rising into place (800ms). Under `prefers-reduced-motion` all motion is off.

### Empty and complete states
A title in serif, one muted line, the actions as primary and ghost buttons, and a hero: sand disc and outlined shapes when empty, pine accent when there is nothing left to do.

## Do's and Don'ts

### Do:
- **Do** lead each screen with space, type and at most one dominant geometric gesture.
- **Do** separate rows with hairlines on cream and let cream dominate.
- **Do** give each colour one meaning and back it with a word, mark or shape.
- **Do** use the serif for titles and content, the sans for chrome.
- **Do** keep a dark equivalent for every colour and honour reduced motion.
- **Do** generate unit and story marks from their ids so they stay stable.
- **Do** show grammar forms as tables.
- **Do** hide navigation on focus screens and put the close button at top left.

### Don't:
- **Don't** use mascots, streak flames, confetti or glossy lifted cards.
- **Don't** stack shadowed cards or bolt illustrations onto a dashboard.
- **Don't** add resting shadows, gradients, grain, texture or large radii.
- **Don't** use pill buttons, capsule chips or rounded primary controls.
- **Don't** fill a screen with a navy slab or several colour blocks.
- **Don't** add geometric objects to fill emptiness.
- **Don't** use vermilion, ochre, pine or brick decoratively.
- **Don't** put running state (streaks, counters) in the header.
- **Don't** load webfonts; keep system stacks so the app stays offline-safe.
- **Don't** let a hero, its axes or arcs run under the title or lede.
- **Don't** give labels a background patch to hide a line behind them; keep labels compact so the line passes between them.
