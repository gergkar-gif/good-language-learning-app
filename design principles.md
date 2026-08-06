Spanish Mastery UI Design Principles (v1.0)
Vision

Spanish Mastery should feel like a beautifully organised notebook for mastering Spanish.

It is not a game, a productivity dashboard, or a flashcard app. The experience should encourage calm, focused study, similar to working through a well-designed language textbook.

The interface should be timeless, restrained, and pleasant to spend long periods using.

Core Design Principles
1. Calm

The interface should reduce cognitive load.

Use:

Generous whitespace
Soft rounded corners
Muted, warm colours
Subtle shadows
Clear typography
Simple animations

Avoid:

Visual clutter
Flashing effects
Loud colours
Busy layouts
Too many simultaneous actions
2. Purposeful

Every element should have a clear purpose.

Ask:

Why is this here?

Examples:

Progress bar → communicates progress
Icon → identifies content
Badge → conveys status
Button → initiates an action

If an element serves no clear purpose, remove it.

3. Physical

The app should feel like interacting with physical learning materials.

Digital	Feels Like
Lessons	Course workbook
Library	Bookshelf
Verbs	Grammar notebook
Vocabulary	Flashcards
Progress	Bookmark

The UI should feel tangible rather than abstract.

4. Structured

The interface should always communicate that the learner is progressing through a carefully designed course.

Avoid presenting content as disconnected exercises.

Always reinforce:

I am moving through a complete curriculum.

Information Architecture

Every section should have one clear identity.

Home

Purpose:

What should I study next?

Contains:

Continue Lesson
Continue Reading
Today's Review
Overall Progress

Nothing else.

Lessons

Purpose:

My structured course.

Primary object:

Large CEFR level cards.

Each card contains:

Icon
Level title
Progress
Progress bar
Expand button

Opening a level reveals lesson cards.

Library

Purpose:

My collection of readings.

Stories should resemble books rather than list items.

Browsing should feel like walking through a bookshelf.

Verbs

Purpose:

Focused grammar practice.

Verb groups should appear as collections, not spreadsheets.

Example:

Present

37 verbs
72% complete
Visual Hierarchy

Every screen should have one dominant object.

Large Card

Examples:

CEFR Level
Verb Group
Continue Learning

Medium Card

Examples:

Lesson
Story
Reading

Small Component

Examples:

Badge
Tag
Status
Difficulty

Avoid mixing hierarchy levels randomly.

Components

The design system should stay intentionally small.

Primary components:

Large Card
Medium Card
Button
Progress Bar
Badge
Input Field
Modal

Whenever possible, reuse existing components instead of creating new ones.

Colour Philosophy

Colour should communicate information.

Suggested meanings:

Teal → Primary action / current progress
Green → Completed
Orange → Needs review / warning
Grey → Locked / unavailable

Avoid decorative colours without meaning.

Progress

Progress should be visible throughout the application.

Every screen should answer:

How far have I come?

Examples:

Course completion
Lesson completion
Story completion
Verb mastery
Daily review

Progress should be easy to understand at a glance.

Typography

Typography should establish a clear hierarchy.

Use:

Large titles
Medium headings
Standard body text
Muted metadata

Avoid excessive variation in font sizes.

Spacing

Use a consistent spacing scale.

Preferred values:

8 px
12 px
16 px
24 px
32 px

Avoid arbitrary spacing.

Cards

Cards are the primary interaction pattern.

A clickable object should almost always be a card.

Cards should have:

Rounded corners
Subtle shadow
Comfortable padding
Hover elevation
Clear click affordance

Avoid clickable text floating in empty space.

Interaction

Animations should be subtle.

Examples:

Hover elevation
Smooth expand/collapse
Progress animation
Fade transitions

Avoid excessive motion.

Tone

The interface should feel:

Calm
Organised
Bookish
Premium
Friendly
Deliberate

It should not feel:

Hyper-gamified
Competitive
Noisy
Corporate
Overly playful
Design Rule

Before adding a feature, ask:

Does this make learning easier?
Does it simplify the interface?
Does it reinforce the feeling of progressing through a structured course?
Can it be built using existing components?

If the answer to any of these is "no", reconsider the design.

Long-Term Direction

Future additions should strengthen the same design language rather than introduce new visual styles.

Potential future features include:

Course map
Illustrated section icons
Bookshelf-style library
Achievement history
Learning statistics

These should only be introduced once the core experience is polished and consistent.

Guiding Principle

Every screen should feel like opening another page of a beautifully designed Spanish workbook. Users should experience calm, clarity, and steady progress, rather than distraction or gamification.