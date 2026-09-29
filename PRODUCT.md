# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
Self-directed adult learners studying alone in short sessions, largely on a phone, who want real CEFR progress (Spanish is DELE-aligned) rather than gamified streaks. The owner is currently the first learner (Spanish and Hungarian); multi-user support is deferred.

## Product Purpose
Parlour ("A place for language") is a modular, content-driven language curriculum covering CEFR A1 to C1. Learners follow lessons, read stories, practise with purpose and retain what matters. Spanish (Core plus Latin America tracks) and Hungarian are live through B1; B2 is being generated for Spanish. Success is measurable progression through CEFR levels and retained vocabulary and grammar, not time-on-app.

## Positioning
- An advanced speaking and writing engine plus CEFR-exam practice tasks that take learners past beginner phrasebook sentences.
- A learner model: every exercise carries `category` and `teaches` metadata, and grammar skills are recycled through it, with SM-2 spaced repetition for words.
- A story-led A1 to B1 curriculum, one story per unit, with a dual track (Core plus Latin America).
- A Reader/Library that analyses vocabulary in the learner's own pasted texts, plus Workshop drillers (vocabulary, listening, verb, suffix, etc.).
- A calm, non-gamified, editorial product stance: no streak pressure.

## Operating Context
Static site served as a PWA (service worker, manifest, custom domain via CNAME). Content is JSON under `content/<lang>/`, validated by `scripts/validate-content.py`. Cloud sync runs on a Cloudflare Worker with D1 and Resend. Text-to-speech uses Google Cloud TTS (Chirp3-HD) behind a provider abstraction. New content is largely generated and audited with AI assistance against the schemas in AGENTS.md.

## Capabilities and Constraints
- HTML, CSS, vanilla JavaScript and JSON only; no frameworks. Engine and content are separated so new languages are content packs.
- Learn tab (lessons and consolidations), Journey, Library (Parlour, Saved, My Texts), Decks/My Decks (SRS), My Dictionary, Workshop drillers, Listening, Hungarian Reader/Lexicon.
- Exercise metadata rules and course-adding rules live in AGENTS.md; grammar-skill titles in `grammar-titles.json`.
- Home shows exactly one recommendation card. The header is editorial and carries no running state. Grammar screens show the paradigm (tables), never buried in prose.
- Profile was folded into Journey; Settings deferred until multi-user.
- Cache changes require both a `?v=` bump and a `sw.js` CACHE_VERSION bump.

## Brand Commitments
Name: Parlour. Tagline: "A place for language." Voice is understated and slightly tongue-in-cheek ("we get it, here's what's different"). Never invent quotes or attributions for placeholder copy.

## Evidence on Hand
Real curriculum and exercise content in `content/`; ROADMAP.md and ACHIEVED.md; feature-guidance copy in `docs/feature-guidance-copy.md`. No testimonials, user metrics or press exist; do not fabricate them.

## Product Principles
1. Pedagogy first: technology serves education.
2. Practice beyond the phrasebook: push toward speaking, writing and exam-style tasks.
3. The learner model decides what to review; content is tagged so it can.
4. Calm over compulsion: no streak or guilt mechanics.
5. Reuse external resources (dictionaries, conjugations, frequency lists) rather than reinvent them.

## Accessibility & Inclusion
No product-specific standard established; not yet decided.
