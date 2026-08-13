# Parlour Visual Overhaul Specification

## 1. Purpose

This document specifies the complete visual overhaul of **Parlour**, the language-learning application.

The implementation target is the existing Parlour application. This is a **visual and interaction-language redesign**, not a rewrite of the application architecture or learning engine.

The existing functionality, content, navigation, data structures, lesson logic, exercise logic, progress tracking, deck logic, and other behaviour should remain intact unless a visual implementation genuinely requires a small structural change.

The redesign should make Parlour feel like entering a carefully composed abstract space rather than opening a conventional language-learning dashboard.

The central visual references are:

- **Wassily Kandinsky** for abstract geometric composition, circles, semicircles, arcs, points, overlapping shapes, spatial rhythm and colour relationships.
- **Gustav Klutsis** for Constructivist structure, diagonals, axes, geometric framing, typographic hierarchy, directional composition and visual tension.
- **Minimalism** as the controlling principle. The interface must remain sparse, legible and calm. The references are sources of visual grammar, not instructions to imitate individual artworks.

The resulting product should feel contemporary, distinctive and coherent.

---

# 2. Core Design Principle

## Minimal interface. Maximum compositional character.

Parlour should not look like a conventional SaaS dashboard with an abstract illustration added to it.

The **interface itself is the composition**.

A circle can be an interaction state.

A line can be a navigation axis.

A semicircle can indicate movement.

A triangle can represent an active state.

A geometric object can be both decorative and functional.

However, objects should never be added merely because the screen looks empty. Empty space is an intentional part of the design.

The design should follow this hierarchy:

1. Space
2. Typography
3. One dominant geometric gesture
4. Small supporting geometric details
5. Interaction feedback

A typical screen should therefore contain relatively few visual elements, but those elements should have strong scale, position and relationships.

---

# 3. Visual Personality

Parlour should feel:

- abstract
- intellectual
- editorial
- architectural
- experimental
- calm
- precise
- slightly strange
- confident
- spacious

It should not feel:

- cute
- childish
- corporate
- gamified
- cartoon-like
- futuristic
- glossy
- generic
- excessively decorative
- like a conventional language-learning app

The user should never encounter emoji-style visual language.

Do not use:

- emoji
- cartoon mascots
- generic educational illustrations
- trophy graphics
- badges
- stars used as reward symbols
- hearts
- flames
- generic achievement icons
- colourful icon packs
- generic line-icon libraries where an abstract geometric treatment would work better

---

# 4. Colour System

Use a deliberately restricted palette.

## 4.1 Warm cream

The primary background should be a warm, slightly ivory cream.

Suggested starting value:

`#F5F1E8`

This is a starting point, not an immutable requirement. It should feel like warm paper rather than pure white.

Use it for:

- page backgrounds
- large empty fields
- inactive geometric areas
- negative space

Avoid pure white backgrounds.

## 4.2 Deep navy

The primary structural colour should be a very dark navy.

Suggested starting value:

`#102A47`

Use it for:

- primary text
- headings
- structural lines
- active/inactive geometric forms
- navigation
- borders
- large dark shapes

It should read almost as black at normal size, but retain a clear navy character.

## 4.3 Deep orange

Orange is the principal accent and must be significantly stronger than the current implementation.

Suggested starting value:

`#E94B16`

A slightly deeper or more saturated orange may be used after visual testing.

Orange should be:

- striking
- warm
- saturated
- scarce

Use it for:

- active states
- progress
- selected navigation
- important interaction states
- focal geometric objects
- small visual anchors

Do not use orange everywhere.

If a screen contains five orange objects, the colour has probably lost its function.

## 4.4 Secondary neutrals

Use muted navy/grey for secondary text.

Use a slightly darker cream or light neutral for:

- subtle dividers
- inactive progress tracks
- low-emphasis borders

Avoid introducing many additional colours.

## 4.5 Colour principle

The dominant combination is:

**cream + navy + orange**

The interface should remain recognisable even if all secondary colours are removed.

---

# 5. Typography

Typography is a major part of the visual identity.

## 5.1 Display and major headings

Use a refined serif typeface with a literary/editorial character.

The current visual direction suggests a high-contrast or elegant serif rather than a chunky traditional book serif.

Examples to investigate:

- Cormorant Garamond
- Libre Baskerville
- EB Garamond
- DM Serif Display
- Instrument Serif
- another high-quality web-safe or bundled serif with a similar character

Do not blindly adopt one font. Choose the option that gives the best combination of:

- readability
- elegance
- strong large-scale forms
- Spanish diacritic support
- available weights

## 5.2 Interface text

Use a restrained sans-serif for:

- labels
- metadata
- navigation
- progress counts
- secondary descriptions
- small instructional text

The sans-serif should be clean and neutral.

Possible families to investigate:

- Inter
- IBM Plex Sans
- Source Sans 3
- Manrope
- another similarly restrained sans-serif

## 5.3 Typographic hierarchy

Large page titles should be genuinely large.

For desktop layouts:

- page title: approximately 64 to 96px
- major section heading: approximately 36 to 56px
- content heading: approximately 26 to 40px
- body: approximately 16 to 19px
- metadata: approximately 12 to 15px
- navigation labels: approximately 11 to 13px

These are starting points. Responsive scaling is required.

Do not make every piece of text large.

The contrast between very large headings and small metadata is part of the aesthetic.

## 5.4 Typography rules

Avoid:

- excessive bold
- all-caps headings everywhere
- rounded playful fonts
- excessive letter spacing
- too many font weights

Uppercase can be used for small labels and navigation.

Major page headings should remain primarily title case or normal case.

---

# 6. Geometric Visual Language

The application should have a reusable geometric vocabulary.

The primary objects are:

- circle
- semicircle
- quarter circle
- triangle
- square
- rectangle
- arc
- dot
- diagonal line
- horizontal axis
- vertical line
- intersecting lines
- radial lines
- simple geometric clusters

These are not conventional icons.

They are **visual objects**.

## 6.1 Circle

Use for:

- inactive states
- focal points
- progress anchors
- selected objects
- navigation markers

A circle may be:

- filled
- outlined
- intersected by a line
- partially obscured
- connected to another object

## 6.2 Triangle

Use for:

- active states
- forward movement
- directional emphasis
- selected interaction states

Triangles should be simple and geometric.

## 6.3 Semicircle

Use for:

- section transitions
- navigation
- large page compositions
- partially visible objects
- movement between states

## 6.4 Lines

Lines should usually be thin.

They can:

- connect objects
- define axes
- cross the page
- extend beyond containers
- create directional relationships
- intersect geometric forms

Do not use lines as generic decorative dividers everywhere.

## 6.5 Overlap

Objects may overlap:

- text
- lines
- page boundaries
- other objects

But overlap must remain controlled and must not reduce readability.

---

# 7. Interaction Language

This is one of the most important parts of the redesign.

## 7.1 Do not make every interaction look like a conventional UI control

Avoid relying on:

- pill buttons
- rounded rectangular buttons
- standard toggles
- conventional checkbox boxes
- radio buttons
- large CTA rectangles
- generic dropdown controls

The underlying semantic controls must remain accessible and usable, but their visible treatment should be abstract.

The interaction should be expressed through:

**shape + position + colour + typography + motion**

rather than:

**rounded rectangle + label**

## 7.2 Abstract state controls

A toggle is the clearest example.

For a vocabulary drill setting such as:

**Show translations**

the inactive state might use a navy circle.

The active state might transform into a deep orange triangle.

The two states are visually distinct.

Example concept:

`OFF = navy circle`

`ON = orange triangle`

The shape can move along an axis or line as the user changes state.

The transition should be simple and deliberate.

Do not use a generic sliding pill.

## 7.3 State changes

State changes can use:

- shape transformation
- position movement
- rotation
- scale
- colour transition
- line appearance
- alignment
- intersection

Keep animation short.

Recommended range:

`180ms to 450ms`

Use easing that feels physical but restrained.

Avoid:

- bouncing
- elastic effects
- excessive rotation
- cartoon animation
- long decorative transitions

## 7.4 Clickability

The visible composition may be abstract, but the clickable region should still be generous.

A user must be able to understand:

- what can be interacted with
- what state it is in
- what will happen after interaction

Do not sacrifice accessibility for visual novelty.

Use appropriate semantic HTML beneath the visual treatment.

---

# 8. Buttons

Buttons should be treated as a last resort for the visual language.

Where possible, replace conventional buttons with typographic/geometric actions.

Instead of:

`[ Start lesson ]`

consider:

`START LESSON`

with a geometric object acting as the interaction anchor.

Instead of:

`[ Continue ]`

use:

`CONTINUE`

with a line, triangle or other directional object.

## 8.1 When a rectangular button is acceptable

Rectangular buttons may still be used when:

- the action is unusually important
- the interaction needs maximum clarity
- the available space is constrained
- accessibility testing shows that the abstract treatment is insufficient

Even then, avoid excessive rounding and pill shapes.

Use:

- sharp or minimally rounded geometry
- navy or cream
- orange as a state/accent
- strong typography

The current app's generic rounded blue button treatment should not remain as the dominant language.

---

# 9. Cards and Containers

The existing application uses conventional rounded cards heavily.

Reduce this substantially.

Containers should generally become:

- open layouts
- thin bordered areas
- horizontal compositions
- separated by rules
- full-width rows
- geometric framing

Cards can still exist where grouping genuinely helps comprehension.

However, avoid a page composed of:

`card + card + card + card`

The redesigned interface should feel like one continuous composition.

---

# 10. Navigation

The six main destinations are:

1. Home
2. Lessons
3. Library
4. Workshop
5. Decks
6. Journey

Navigation should use a consistent geometric icon system.

Each icon should be an abstract geometric composition rather than a conventional pictogram.

The selected navigation item should not simply be a filled rounded rectangle.

Use a combination of:

- geometric transformation
- orange accent
- stronger typography
- subtle background or spatial emphasis
- line/shape changes

The selected state should be immediately obvious.

## Navigation icon principles

Icons should be:

- monochrome by default
- navy when inactive
- orange used selectively
- based on 2 to 4 geometric primitives
- visually consistent in stroke weight
- recognisable at small sizes

Do not use emoji or generic icon-library glyphs.

---

# 11. Main Page Visual Identities

Each of the six pages needs its own abstract logo/composition.

These should work both:

- as the page's hero graphic
- as the basis for its small navigation icon

The small icon should be a simplified version of the larger composition.

---

## 11.1 HOME

### Concept

**The doorway.**

Home is the entry point into Parlour.

The visual should communicate:

- arrival
- opening
- balance
- possibility
- a place to begin

### Suggested composition

A vertical rectangular doorway in navy.

A deep orange semicircle sits adjacent to or partially behind it.

A small orange dot may act as a handle or focal point.

The shape should remain extremely simple.

Concept:

`navy rectangle + orange semicircle + small dot`

### Small icon

Simplified doorway:

- navy vertical rectangle
- orange half-circle or small orange dot

### Motion

On hover/selection:

- the semicircle can shift slightly
- the door can open by a small amount
- the orange dot can move

Do not use a literal door animation.

---

## 11.2 LESSONS

### Concept

**Focus and direction.**

Lessons are where the learner moves forward through structured learning.

### Suggested composition

A navy semicircle or half-disc sits on a horizontal baseline.

Several fine navy lines extend diagonally towards a small orange circle.

The orange circle represents the destination/focus point.

Concept:

`large navy semicircle → radial lines → orange point`

This is already established as one of the strongest visual motifs for Lessons.

### Small icon

Reduce to:

- diagonal line
- small orange point
- simple angular/semicircular form

### Motion

The radial lines can subtly draw towards the orange point.

Progress can cause the orange point to move along the composition.

---

## 11.3 LIBRARY

### Concept

**Reading rooms / collected knowledge.**

Library should feel ordered and archival without looking like a traditional bookshelf illustration.

### Suggested composition

Several navy vertical bars of varying heights.

An orange circle overlaps or sits behind the bars.

A thin outlined rectangle can sit among the bars.

Concept:

`navy vertical structures + orange circle + outlined form`

### Small icon

A reduced series of 3 to 5 vertical bars.

One small orange point or circle can provide the accent.

### Motion

When selected:

- bars can shift slightly
- orange circle can move into position
- a single bar can rise or fall

Do not animate every bar independently.

---

## 11.4 WORKSHOP

### Concept

**Making and practice.**

Workshop is the place where language is actively manipulated.

### Suggested composition

A diagonal or horizontal axis.

A navy circle acts as a balance point.

A small orange square or rectangle sits on one side of the axis.

The composition should suggest construction, balance and experimentation.

Concept:

`diagonal beam + navy circle + orange square`

### Small icon

Three elements:

- line
- circle
- square

### Motion

Interaction can cause the square to move across the line or the line to pivot slightly.

This makes Workshop feel different from Lessons.

---

## 11.5 DECKS

### Concept

**Layers / spaced repetition.**

The Decks identity already has a useful visual motif and should preserve it.

The current miniature deck logo is preferred over the alternative abstract logo.

### Suggested composition

Several overlapping card-like rectangles.

The first shape is filled navy.

Subsequent shapes are outlined.

The final or active layer uses orange.

Concept:

`navy filled rectangle + outlined rectangles + orange edge`

The miniature version should remain close to the current Decks logo.

### Small icon

Three or four overlapping cards/rectangles.

Keep the current recognisable structure.

Do not replace it with a completely unrelated geometric symbol.

### Motion

Cards can shift laterally by a few pixels.

The orange edge can move between layers.

---

## 11.6 JOURNEY

### Concept

**Path forward.**

Journey represents progress through the entire learning experience.

### Suggested composition

A thin curved line begins at a small navy point and travels upward or forward.

It ends at an orange square or other geometric destination.

Concept:

`navy starting point → curved path → orange destination`

### Small icon

A simple rising/curving line ending in a small orange point or square.

### Motion

The path may progressively draw itself as progress increases.

The destination object can move further along the path as the learner advances.

Avoid conventional progress bars as the primary visual representation.

---

# 12. Page Headers

Every major page should have:

1. Large serif title
2. Short subtitle
3. Abstract hero composition
4. Main navigation

Example:

`Lessons`

`Your Spanish course.`

followed by the geometric Lessons composition.

Headers should occupy substantial vertical space on desktop.

The composition should not be treated as a tiny illustration underneath the title.

It is part of the page identity.

---

# 13. Lessons Page

The Lessons page should use the established five-level structure:

- Fundamentals
- Basic
- Intermediate
- Upper Intermediate
- Advanced

Do not reproduce the current rounded-card list literally.

Instead, use spacious horizontal rows.

Each row should include:

- level number
- geometric identity
- level name
- level description
- progress
- lesson count
- directional interaction

Example structure:

`01    geometric object    Fundamentals`

`A1 · Survival skills`

`progress line                 6 / 115 lessons`

The right side can use:

- an arc
- semicircle
- triangle
- large geometric object

rather than a conventional chevron button.

The entire row should be clickable.

---

# 14. Library Page

The Library page should preserve the current information architecture:

- Parlour
- Saved
- My Texts

Then levels:

- A1
- A2
- B1
- B2
- C1

The current compact list can become more spatial.

Each level row should contain:

- large level typography
- reading progress
- progress line
- geometric object
- directional cue

Example:

`A1`

`2 / 20 read`

`────────●───`

with a geometric orange/navy composition nearby.

Avoid large rounded cards.

The level rows should feel like sections of an archive.

---

# 15. Decks Page

Preserve the existing information architecture.

Top section:

**All my words**

Then:

- due count
- review state
- review action
- browse action

Below:

- My Decks
- Parlour Decks

Then user-created decks.

The main review area can use a large abstract composition.

The deck list should use open rows or lightly framed areas.

The existing deck logo should remain recognisable.

The Decks page can use overlapping rectangles as its dominant geometric language.

---

# 16. Workshop Page

Workshop should feel more interactive than Library.

The visual language should suggest:

- experimentation
- construction
- practice
- manipulation
- language being assembled

Use:

- diagonals
- balance lines
- circles
- squares
- small orange objects

Controls inside Workshop should particularly avoid conventional buttons.

For example:

A setting such as:

`Show translations`

can use the abstract state system:

- OFF = navy circle
- ON = orange triangle

The user should interact directly with the shape.

---

# 17. Journey Page

Journey should not use a standard progress bar as its main visual.

Instead, progress should be spatial.

Use:

- a curved path
- nodes
- geometric milestones
- orange destination markers
- navy starting points

The user's progress can be represented by the location of a geometric object on the path.

Completed stages can use:

- filled navy shapes
- orange accents
- completed geometric intersections

Future stages can use:

- outlines
- lighter structural lines

The page should communicate forward movement without looking like a game map.

---

# 18. Lessons and Exercise UI

Exercises are where the redesign should become most distinctive.

Avoid:

- answer cards
- giant rectangular answer buttons
- coloured correctness badges
- gamified score popups

Instead, answers can be positioned spatially.

Example:

`GRANDE`

`pequeño`

`ALTO`

`bajo`

Each word can be a typographic object.

Selection can cause:

- movement
- alignment
- geometric transformation
- orange emphasis

Correctness should be communicated clearly but elegantly.

Possible states:

### Neutral

Navy text and thin line.

### Selected

Orange shape or orange line.

### Correct

Composition resolves into a stable relationship.

### Incorrect

Object moves away or line breaks subtly.

Do not use green/red as the primary correctness language.

Accessibility requirements still apply. Colour must never be the only indication of state.

---

# 19. Progress Indicators

Avoid conventional thick progress bars.

Use:

- thin horizontal lines
- small dots
- geometric endpoints
- orange segments
- radial progression
- spatial movement

A progress indicator might be:

`●───────────`

where the dot moves as progress changes.

Or:

`──────●─────`

with an orange segment behind it.

For larger visualisations, use a path or arc.

---

# 20. Icons

All icons should belong to one coherent geometric family.

Rules:

- simple geometry
- consistent stroke thickness
- navy base colour
- orange only where meaningful
- no visual metaphor that requires an emoji-like pictogram
- no random mixture of icon styles

The six primary navigation icons should feel like they were designed as a single alphabet.

They should be recognisable both at:

- 20 to 24px
- approximately 40 to 60px

Do not use an off-the-shelf icon library unless a specific accessibility or browser requirement makes it necessary.

---

# 21. Responsive Design

The redesign must work on:

- desktop
- tablet
- mobile

Do not simply shrink the desktop composition.

At smaller widths:

- reduce decorative objects
- simplify geometric relationships
- preserve the dominant composition
- maintain large typography where possible
- avoid horizontal overflow
- preserve generous vertical spacing

The six-item navigation may remain horizontal on larger screens.

On narrow screens it can become:

- a compact horizontal navigation
- a scrollable navigation strip
- or another minimal arrangement

Do not replace it with a generic hamburger menu unless there is no viable alternative.

The geometric identities must remain recognisable at mobile size.

---

# 22. Spacing

Whitespace is fundamental.

Use a generous spacing scale.

Suggested base unit:

`4px`

Prefer spacing values based on multiples of 4 or 8.

Major page sections should have substantially more space than individual controls.

Do not compress content simply to fit more information on one screen.

The application should feel deliberately spacious.

---

# 23. Borders and Dividers

Use thin lines.

Typical:

`1px solid`

with a low-contrast neutral/navy treatment.

Dividers should:

- establish structure
- align sections
- create axes
- connect geometric objects

Do not put borders around every element.

---

# 24. Border Radius

Reduce the current reliance on rounded corners.

Default:

`0px`

Small radius:

`2px to 6px`

Use larger rounding only where it has a specific compositional purpose.

Avoid:

`border-radius: 999px`

for ordinary controls.

Pills should be extremely rare.

---

# 25. Shadows

Avoid conventional UI shadows.

Do not use:

- floating-card shadows
- heavy drop shadows
- glossy elevation
- neumorphism

The visual hierarchy should come from:

- position
- scale
- colour
- line weight
- whitespace
- overlap

---

# 26. Animation

Animation should reinforce composition.

Use it for:

- state transitions
- navigation changes
- shape transformation
- progress
- selection
- page entry

Do not animate merely to make the application feel dynamic.

Recommended principles:

- 180 to 450ms for UI transitions
- smooth easing
- minimal overshoot
- no bouncing
- no excessive rotation

Respect `prefers-reduced-motion`.

When reduced motion is enabled, replace movement with:

- opacity
- colour
- shape/state changes
- simple instant transitions

---

# 27. Accessibility

The visual redesign must not reduce accessibility.

Requirements:

- semantic HTML
- keyboard navigation
- visible focus states
- appropriate ARIA only where necessary
- sufficient text contrast
- state communicated through more than colour
- large enough click/touch targets
- screen-reader labels for abstract controls
- reduced-motion support

Abstract visual controls must still expose meaningful accessible names.

For example:

A shape-based toggle must still behave like a semantic checkbox or switch.

The visual representation and semantic representation are separate layers.

---

# 28. Implementation Architecture

The current application is vanilla HTML/CSS/JavaScript/JSON.

Keep it that way unless the existing project explicitly requires otherwise.

Do not introduce:

- React
- Vue
- Angular
- Tailwind
- large component frameworks
- unnecessary dependencies

The redesign should primarily be implemented through:

- updated HTML structure where required
- a central CSS visual system
- reusable CSS classes
- CSS custom properties
- small JavaScript enhancements for interaction state and animation

## 28.1 CSS variables

Create a central visual token section.

Example:

```css
:root {
  --parlour-cream: #F5F1E8;
  --parlour-navy: #102A47;
  --parlour-orange: #E94B16;

  --parlour-line: rgba(16, 42, 71, 0.18);
  --parlour-muted: rgba(16, 42, 71, 0.68);

  --font-display: ...;
  --font-ui: ...;

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;
  --space-8: 64px;
  --space-9: 96px;
}
```

Actual values can be refined during implementation.

---

# 29. Geometric CSS System

Build reusable primitives rather than drawing each object independently.

Potential primitives:

- `.geo-circle`
- `.geo-triangle`
- `.geo-square`
- `.geo-semicircle`
- `.geo-arc`
- `.geo-line`
- `.geo-dot`
- `.geo-axis`
- `.geo-stack`
- `.geo-path`

These should be composable.

For example:

```html
<div class="geo-composition geo-lessons">
  <span class="geo-semicircle"></span>
  <span class="geo-axis"></span>
  <span class="geo-line"></span>
  <span class="geo-dot"></span>
</div>
```

The implementation can use:

- CSS
- pseudo-elements
- borders
- transforms
- SVG where genuinely useful

Do not create hundreds of unique SVG assets for simple shapes.

---

# 30. Shape State System

Create reusable abstract state patterns.

For example:

```text
state-off
  navy circle

state-on
  orange triangle
```

The exact shape pair can vary by control, but the principle should be consistent.

A state component should support:

- default
- hover
- focus
- active
- selected
- disabled

The user should learn the visual language over time.

---

# 31. Interaction Priority

When redesigning existing controls, use this order:

1. Preserve semantic function.
2. Preserve usability.
3. Preserve accessibility.
4. Apply the geometric visual language.
5. Add restrained animation.
6. Remove unnecessary visual chrome.

Do not redesign functionality simply because it looks conventional.

The objective is a visual overhaul, not a product rewrite.

---

# 32. Content Density

Parlour should favour **curation over density**.

If a screen currently contains many small cards, first ask whether those cards can become:

- rows
- typographic groups
- open sections
- geometric compositions

Do not simply reproduce the same information in prettier boxes.

However, do not remove information merely to make the screen look minimalist.

Information architecture remains important.

---

# 33. Visual Rhythm

Screens should alternate between:

- dense and sparse areas
- large and small typography
- geometric and textual sections
- horizontal and diagonal structures
- quiet and striking compositions

Do not use the same geometric arrangement on every page.

Each page needs its own visual identity while sharing the same visual grammar.

---

# 34. What Must Not Happen

The implementation should be rejected if it starts looking like:

- a generic SaaS dashboard
- a modern banking app
- a children's language-learning game
- Duolingo-style gamification
- a generic Bootstrap application
- a collection of rounded cards
- a Material Design application
- an icon-library showcase
- an AI-generated landing page full of decorative blobs
- excessive Bauhaus decoration
- literal Kandinsky imitation
- literal Soviet Constructivist poster imitation

The design should be recognisably **Parlour**, not a collage of references.

---

# 35. Reference Relationship

Use the artistic references as follows.

## Kandinsky contributes

- circles
- semicircles
- abstract geometry
- spatial composition
- colour relationships
- visual rhythm
- independent geometric objects

## Klutsis contributes

- diagonals
- axes
- structural lines
- geometric framing
- typography as graphic structure
- directional movement
- asymmetry
- compositional tension

## Minimalism contributes

- restraint
- whitespace
- limited colour
- limited object count
- clarity
- repetition
- consistency
- refusal to decorate without purpose

---

# 36. Overall Visual Formula

The visual identity can be summarised as:

**Warm cream canvas**

+

**deep navy structure**

+

**strong deep orange accent**

+

**large serif typography**

+

**thin geometric lines**

+

**circles / triangles / semicircles / squares**

+

**diagonal and radial structures**

+

**large areas of negative space**

+

**abstract interaction states**

=

**Parlour**

---

# 37. Implementation Order

Claude should implement the overhaul in the following order.

## Phase 1: Global foundation

- colour tokens
- typography
- spacing
- global background
- borders
- responsive foundations
- focus states
- animation system

## Phase 2: Geometric primitives

Build and test:

- circle
- triangle
- square
- semicircle
- arc
- line
- dot
- axis
- path
- stacked rectangles

## Phase 3: Main navigation

Redesign:

- Home icon
- Lessons icon
- Library icon
- Workshop icon
- Decks icon
- Journey icon

Implement selected/unselected states.

## Phase 4: Page headers

Implement six page-specific hero compositions.

## Phase 5: Main pages

Redesign:

1. Home
2. Lessons
3. Library
4. Workshop
5. Decks
6. Journey

Preserve existing functionality.

## Phase 6: Controls

Replace conventional visual controls where appropriate with:

- abstract toggles
- geometric action links
- typographic actions
- shape-based state indicators

## Phase 7: Lesson/exercise interfaces

Apply the visual language to:

- lesson screens
- exercise screens
- answer selection
- feedback
- progress
- navigation between exercises

## Phase 8: Responsive refinement

Test:

- desktop
- tablet
- mobile
- keyboard navigation
- reduced motion

## Phase 9: Visual cleanup

Remove:

- unnecessary rounded cards
- redundant borders
- generic icons
- unnecessary colours
- decorative elements that do not contribute to composition
- inconsistent spacing
- inconsistent geometry

---

# 38. Acceptance Criteria

The redesign is complete when:

### Visual identity

- Parlour is immediately recognisable from its geometry and typography.
- Cream, navy and deep orange dominate.
- No emoji-style graphics remain.
- No generic icon system dominates.
- Kandinsky and Constructivist influences are visible without literal imitation.

### Composition

- Major pages feel like composed spaces.
- Empty space is intentional.
- Geometric objects have clear relationships.
- Screens do not become visually cluttered.

### Interaction

- Conventional controls have been replaced where appropriate.
- Abstract controls still communicate state clearly.
- A switch can visually transform between distinct geometric states.
- Interactions have restrained, purposeful motion.

### Navigation

- Six main destinations have distinct but related visual identities.
- Active navigation is obvious without relying on a conventional pill/button.
- Icons remain recognisable at small sizes.

### Functionality

- Existing learning functionality remains intact.
- Existing content remains intact.
- Existing progress tracking remains intact.
- Existing deck functionality remains intact.
- Existing Library functionality remains intact.
- Existing navigation remains intact.

### Accessibility

- Keyboard navigation works.
- Focus states are visible.
- Abstract controls have semantic labels.
- Colour is not the sole state indicator.
- Reduced motion is supported.
- Text remains readable.

### Technical

- Remains compatible with the existing vanilla HTML/CSS/JavaScript architecture.
- No unnecessary framework is introduced.
- Geometry is reusable rather than duplicated.
- Colours, typography and spacing are centrally controlled through CSS variables.
- Responsive behaviour is intentional rather than simply scaled.

---

# 39. Final Design Test

Before considering any screen finished, ask:

1. Could this screen exist without the geometric objects?
2. If yes, are the objects actually contributing something?
3. Is there one dominant visual gesture?
4. Is there enough empty space?
5. Is the orange still meaningful?
6. Does the typography carry enough of the hierarchy?
7. Does any element look like a generic app component?
8. Can a conventional button be replaced by a more appropriate geometric interaction?
9. Is the user's current state immediately understandable?
10. Does the screen feel like Parlour rather than a reskinned language-learning application?

The final test is simple:

**It should feel like stepping into an abstract composition that happens to be a language-learning application.**

Not a language-learning application decorated with abstract art.


# 22A. Mobile-First Compositional Architecture

Mobile transferability is a **core design constraint**, not a later responsive task.

The visual system must be designed so that every desktop composition has a natural mobile equivalent without requiring a separate mobile design language.

## 22A.1 Design for reflow, not shrinkage

Do not design a wide desktop composition and then simply scale it down.

Every major composition must be able to:

- collapse from horizontal to vertical
- reduce the number of geometric objects
- reposition shapes without losing its identity
- preserve the visual hierarchy
- retain the same interaction semantics
- remain readable at narrow widths

The desktop and mobile versions should feel like two compositions from the same visual system.

## 22A.2 Use layout structures that naturally collapse

Prefer:

- CSS Grid
- Flexbox
- normal document flow
- relative positioning
- percentage-based dimensions
- `clamp()` for typography and spacing

Avoid layouts that depend on:

- fixed pixel coordinates
- absolute positioning of large numbers of independent objects
- fixed-width panels
- desktop-only horizontal compositions
- text embedded inside images

Absolute positioning may be used for individual geometric objects where it is part of the composition, but the underlying layout must remain flow-based.

## 22A.3 Geometric objects must be independently repositionable

A geometric composition should be constructed from separate DOM/CSS elements rather than one flattened image.

For example:

```text
composition
├── circle
├── line
├── triangle
└── dot
```

On desktop these might form a wide diagonal composition.

On mobile they can become:

```text
circle
   \
    line
     \
      triangle
```

The identity survives even though the spatial arrangement changes.

## 22A.4 Mobile composition rules

At narrow widths:

- simplify rather than overcrowd
- reduce the number of simultaneous geometric objects
- shorten long lines
- reduce overlap
- preserve one dominant shape
- retain strong typography
- retain cream negative space
- keep orange scarce and meaningful

Do not try to fit the entire desktop composition into a narrow viewport.

## 22A.5 Navigation

The six main destinations must remain easily accessible on mobile.

The preferred mobile pattern is a compact horizontal navigation system that can fit within the viewport or scroll horizontally without feeling like a conventional tab bar.

The six identities remain:

- Home
- Lessons
- Library
- Workshop
- Decks
- Journey

Do not rely on a hamburger menu simply to solve the layout problem.

The navigation should remain visually recognisable as part of Parlour's geometric system.

## 22A.6 Touch interaction

Abstract controls must work comfortably with touch.

The visible geometric object may be small, but its interactive hit area should be significantly larger.

Use an invisible semantic interaction area where necessary.

Target approximately:

`44px × 44px` minimum touch area.

Do not force users to tap a tiny geometric point.

## 22A.7 Mobile typography

Use responsive typography rather than separate arbitrary font sizes.

Example:

```css
.page-title {
  font-size: clamp(3rem, 10vw, 6rem);
}
```

Major headings should remain visually prominent without creating horizontal overflow.

Long Spanish text must be allowed to wrap naturally.

Do not use fixed heights for areas containing unpredictable text.

## 22A.8 Mobile page identity

Each page's geometric logo/composition must have a simplified mobile form.

For example:

### Lessons

Desktop:

`semicircle → radial lines → orange point`

Mobile:

`semicircle`
`   \`
`    \`
`     orange point`

### Library

Desktop:

`multiple vertical bars + orange circle`

Mobile:

`3 vertical bars + orange circle`

### Workshop

Desktop:

`diagonal axis + circle + square`

Mobile:

`short diagonal + circle + square`

### Decks

Desktop:

`multiple overlapping cards`

Mobile:

`3 overlapping cards`

### Journey

Desktop:

`long curved path + destination`

Mobile:

`short curved path + destination`

The icon remains the same identity while the composition becomes simpler.

## 22A.9 Content rows

Large desktop rows should collapse naturally.

For example:

```text
DESKTOP

01    [GEOMETRY]    Fundamentals
                  A1 · Survival skills
                  ─────────── 6 / 115
                                  [OBJECT]
```

can become:

```text
MOBILE

01    [GEOMETRY]

Fundamentals
A1 · Survival skills

───────────
6 / 115
```

The entire row remains the interaction target.

Do not create a second, completely different mobile component unless absolutely necessary.

## 22A.10 Exercises

Exercise layouts must be designed around vertical mobile space from the beginning.

Do not rely on four answer options sitting across one horizontal row.

Instead, use:

- vertical spatial arrangements
- staggered text
- controlled radial arrangements
- stacked geometric objects

The abstract composition can become more linear on mobile while retaining its visual character.

For example:

```text
        GRANDE

  pequeño

             ALTO

       bajo
```

is naturally mobile-friendly.

## 22A.11 Avoid desktop-only decorative systems

Do not create geometric compositions that are only possible at desktop widths.

Every major visual object should have:

- desktop placement
- tablet placement
- mobile placement

These can be controlled with CSS media queries and CSS custom properties.

## 22A.12 Mobile should feel intentional

A successful mobile implementation should not feel like:

> desktop Parlour squeezed into a phone.

It should feel like:

> a smaller, more concentrated Parlour composition.

The same visual grammar should remain:

**cream + navy + orange + serif typography + geometric objects + space + restrained interaction.**

