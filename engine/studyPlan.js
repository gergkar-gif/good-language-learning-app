// ============================================
// STUDY PLAN — time-budget allocation ("Time-Based Sessions")
// ============================================
// Step 5 of the Learner model & personalized path roadmap initiative,
// built on steps 1-3 (LearnerPath, LearnerModel, RecommendationEngine).
// Roadmap spec: "Learner picks a time budget... the app builds a finite
// session out of curriculum position, knowledge gaps, reviews due, and
// priorities, with a clear start and end. No countdown timer."
//
// Deliberately NOT named "session" anywhere in this module — every
// driller (engine/drills/*.js) already uses that word internally for one
// driller run start-to-finish (PHASE.SESSION, "Session Results",
// DrillHistory's own "session" = one run). This module's queue spans
// MULTIPLE activities across possibly-different screens, so it gets its
// own name, "plan," to keep call sites unambiguous. The roadmap's own
// "Time-Based Sessions" phrase stays as user-facing copy only.
//
// Pure allocation + queue-position logic — no DOM. engine/studyPlanRunner.js
// owns the screen/rendering; RecommendationEngine.mountNextAction() checks
// isActive() to hand off to the runner instead of computing a fresh
// generic recommendation whenever a plan is in progress.
//
// In-memory only, discarded on leaving early or on page reload — matches
// the roadmap's "a clear start and end," not a lingering to-do list.
//
// How a plan is built (reworked 2026-09-24):
//   1st — the single most urgent thing (see SOURCES below for the ranking);
//         when nothing is urgent, the lesson moves up to 1st
//   2nd — the next lesson (or level test), when it fits the budget
//   3rd — a short speaking prompt, always
//   then — the next most urgent thing, and so on, until the budget is full.
// Practice comes in short blocks (~1.5 min) rather than one long block per
// kind, and the same kind never runs twice in a row when anything else is
// available. Activities with no weakness signal (never-tried drillers,
// Library reading, Match Game) are filler: they rank below everything
// urgent and rotate so a long session gets variety.
//
// The budget is also a clock: if the learner gets through the plan with
// time to spare, extend() keeps recommending the next most urgent thing
// until the chosen minutes have passed (wall-clock time since the plan
// started, breaks included). If time runs out with planned items left,
// the runner ends the session and offers the rest as optional.

const StudyPlan = (function () {
    'use strict';

    // Per-item-type pace. Untimed, thoughtful pace — NOT the countdown-race
    // pace of Verb Speed's/Grammar Driller's own "Timed" mode. Used to size
    // blocks and to fill the budget up front.
    const SEC_PER_REVIEW = 20;
    const SEC_PER_GRAMMAR_Q = 30;
    const SEC_PER_VOCAB_WORD = 25;
    const SEC_PER_LISTENING_Q = 35;
    const SEC_PER_SPEAKING_Q = 35;
    const SEC_PER_TRANSLATION_Q = 30;
    const SEC_PER_MORPH_Q = 15;        // Hungarian verb/suffix/prefix/morphology drillers
    const SEC_PER_MATCH_PAIR = 8;
    const BLOCK_MINUTES = 1.5;         // one practice block — several short ones beat one long one
    const REVIEW_BLOCK_WORDS = 10;     // ~3 min: flashcards are quick, 4-word blocks would be choppy
    const VERB_SPEED_SECONDS = 60;
    const SPEAKING_PROMPT_SECONDS = 40;
    const DEFAULT_LESSON_MINUTES = 10; // fallback when estimatedMinutes is null (100% of HU, ~38% of ES)
    const LESSON_GRACE_MINUTES = 2;    // estimate slop tolerance, not a hard wall
    const TEST_MINUTES = 18;           // a level test is one indivisible block
    const MIN_EXTEND_MINUTES = 1;      // don't start something new with less than this left

    // Urgency scale shared by every source, so different kinds of work can
    // be ranked against each other. Higher goes first.
    const URGENCY = {
        REVIEW: 90,          // + up to 10 for a bigger backlog: overdue SM-2 cards decay the most
        GRAMMAR_WEAK: 80,    // +5 when the level test also flagged it
        VOCAB_WEAK: 75,
        SPEAKING_WEAK: 70,
        DRILLER_WEAK: 60,    // + up to 10 the lower the accuracy
        GRAMMAR_DEVELOPING: 50,
        LESSON: 30,          // only as an extend() candidate — build() gives it slot 2
        FILLER: 10
    };
    const REPEAT_PENALTY = 25; // each block already taken from a source lowers its next one

    let _queue = null;   // array of plan items, or null when no plan is active
    let _index = 0;      // pointer into _queue — the current/next item
    let _minutes = null;
    let _skipped = null;
    let _startedAt = null;
    let _overtime = false; // learner chose to keep going after time ran out
    let _used = {};        // source key -> blocks taken this plan
    let _passed = new Set(); // queue indices the learner skipped (not the same as _skipped, the lesson that didn't fit)

    // ----------------------------------------
    // SOURCES
    // ----------------------------------------
    // Each source can hand out blocks of one kind of work. urgency is its
    // base rank; take() returns the next item (or null once it runs dry).

    function _source(key, kind, urgency, take) {
        return { key, kind, urgency, take };
    }

    function _chunks(list, size) {
        const out = [];
        for (let i = 0; i < list.length; i += size) out.push(list.slice(i, i + size));
        return out;
    }

    function _perBlock(secPerItem) {
        return Math.max(1, Math.round(BLOCK_MINUTES * 60 / secPerItem));
    }

    async function _sources(opts) {
        const sources = [];
        const curLevel = (typeof LearnerPath !== 'undefined' && LearnerPath.currentLevel)
            ? LearnerPath.currentLevel().toLowerCase()
            : 'all';
        const canListen = typeof ParlourTTS !== 'undefined' && ParlourTTS.available();
        const canSpeak = (typeof SpeechInput !== 'undefined' && SpeechInput.isSupported()) || canListen;

        // Reviews due — the backlog is split into blocks.
        const due = (typeof getDueCards === 'function') ? getDueCards() : [];
        if (due.length) {
            let left = due.length;
            sources.push(_source('review', 'review', URGENCY.REVIEW + Math.min(10, Math.floor(due.length / 5)), () => {
                if (left <= 0) return null;
                const count = Math.min(left, REVIEW_BLOCK_WORDS);
                left -= count;
                return { kind: 'review', count, estMinutes: count * SEC_PER_REVIEW / 60 };
            }));
        }

        // Grammar — each weak/developing skill is its own source.
        const grammarCount = _perBlock(SEC_PER_GRAMMAR_Q);
        const grammarItem = skill => ({ kind: 'grammar', skill, count: grammarCount, estMinutes: grammarCount * SEC_PER_GRAMMAR_Q / 60 });
        const skills = (typeof LearnerModel !== 'undefined') ? await LearnerModel.weakSkills() : [];
        skills.forEach((s, rank) => {
            const base = s.state === 'weak'
                ? URGENCY.GRAMMAR_WEAK + (s.levelTestFlagged ? 5 : 0)
                : URGENCY.GRAMMAR_DEVELOPING;
            let given = false;
            sources.push(_source('grammar:' + s.skillId, 'grammar', base - rank, () => {
                if (given) return null;
                given = true;
                return grammarItem(s.skillId);
            }));
        });
        if (!skills.length && typeof RecommendationEngine !== 'undefined' && RecommendationEngine.grammarVocabCandidate) {
            const gv = await RecommendationEngine.grammarVocabCandidate();
            if (gv && gv.skill) sources.push(_source('grammar:' + gv.skill, 'grammar', URGENCY.FILLER, () => grammarItem(gv.skill)));
        }

        // Vocabulary — weakest words first, a few per block.
        const weak = (typeof LearnerModel !== 'undefined') ? LearnerModel.weakWords(20) : [];
        const drilled = new Set(opts.drilledWords || []);
        const wordBlocks = _chunks(weak.filter(w => !drilled.has(w.lemma)), _perBlock(SEC_PER_VOCAB_WORD));
        if (wordBlocks.length) {
            sources.push(_source('vocabulary', 'vocabulary', URGENCY.VOCAB_WEAK, () => {
                const words = wordBlocks.shift();
                return words ? { kind: 'vocabulary', words, estMinutes: words.length * SEC_PER_VOCAB_WORD / 60 } : null;
            }));
        }

        // Drillers — weak ones are urgent, the rest are filler.
        const drillers = (typeof LearnerModel !== 'undefined' && LearnerModel.availableDrillers) ? LearnerModel.availableDrillers() : [];
        const weakSpoken = (canSpeak && typeof LearnerModel !== 'undefined' && LearnerModel.weakProductionSkills)
            ? await LearnerModel.weakProductionSkills(1, 'oral')
            : [];
        drillers.forEach(d => {
            const id = d.drillerId;
            let urgency = d.state === 'weak'
                ? URGENCY.DRILLER_WEAK + Math.min(10, Math.round((60 - (d.avgAccuracy || 0)) / 6))
                : URGENCY.FILLER;
            let make = null;
            if (id === 'listening') {
                if (!canListen) return;
                const count = _perBlock(SEC_PER_LISTENING_Q);
                make = () => ({ kind: 'listening', count, level: curLevel, estMinutes: count * SEC_PER_LISTENING_Q / 60 });
            } else if (id === 'speaking') {
                if (!canSpeak) return;
                const count = _perBlock(SEC_PER_SPEAKING_Q);
                const skill = weakSpoken.length ? weakSpoken[0].skillId : null;
                if (skill) urgency = Math.max(urgency, URGENCY.SPEAKING_WEAK);
                make = () => Object.assign({ kind: 'speaking', count, level: curLevel, estMinutes: count * SEC_PER_SPEAKING_Q / 60 }, skill ? { skill } : {});
            } else if (id === 'translation') {
                const count = _perBlock(SEC_PER_TRANSLATION_Q);
                make = () => ({ kind: 'translation', count, level: curLevel, estMinutes: count * SEC_PER_TRANSLATION_Q / 60 });
            } else if (id === 'verbs') {
                make = () => ({ kind: 'verbs', seconds: VERB_SPEED_SECONDS, estMinutes: BLOCK_MINUTES });
            } else if (id.indexOf('hu-') === 0) {
                const count = _perBlock(SEC_PER_MORPH_Q);
                make = () => ({ kind: 'driller', drillerId: id, title: d.title, count, estMinutes: count * SEC_PER_MORPH_Q / 60 });
            }
            if (make) sources.push(_source('driller:' + id, id, urgency, make));
        });

        // Match Game — filler, needs at least four words to pair.
        if (typeof DeckMatch !== 'undefined') {
            let pool = weak.length >= 4 ? weak.slice(0, 12) : [];
            if (pool.length < 4 && typeof srsDeck !== 'undefined' && srsDeck.length >= 4) {
                pool = srsDeck.slice(0, 12).map(c => ({ lemma: c.spanish, translation: c.english }));
            }
            if (pool.length >= 4) {
                const pairs = Math.min(pool.length, Math.max(4, Math.round(BLOCK_MINUTES * 60 / SEC_PER_MATCH_PAIR)));
                sources.push(_source('match', 'match', URGENCY.FILLER, () => {
                    const words = pool.slice(0, pairs);
                    const timeLimit = Math.min(120, words.length * SEC_PER_MATCH_PAIR);
                    return { kind: 'match', words, count: words.length, timeLimit, estMinutes: timeLimit / 60 };
                }));
            }
        }

        // Library reading — filler, one story that fits the time left.
        if (typeof Reader !== 'undefined' && Reader.ensureStories && Reader.getRecommendations) {
            try {
                await Reader.ensureStories();
                const rec = Reader.getRecommendations();
                const story = rec && rec.comfortable && rec.comfortable.story;
                if (story) {
                    const est = story.estimatedMinutes || 5;
                    let given = false;
                    sources.push(_source('reading', 'reading', URGENCY.FILLER, () => {
                        if (given) return null;
                        given = true;
                        return { kind: 'reading', storyId: story.id, title: story.title, estMinutes: est };
                    }));
                }
            } catch (e) { /* no stories for this course — just no reading filler */ }
        }

        // Next lesson — build() places it itself; extend() ranks it.
        if (opts.includeLesson) {
            const step = (typeof LearnerPath !== 'undefined') ? LearnerPath.nextStep() : null;
            if (step && step.kind === 'lesson' && !opts.doneLessons.has(step.lesson.id)) {
                sources.push(_source('lesson', 'lesson', URGENCY.LESSON, () => _lessonItem(step)));
            }
        }

        return sources;
    }

    function _lessonItem(step) {
        const est = step.lesson.estimatedMinutes || DEFAULT_LESSON_MINUTES;
        return { kind: 'lesson', lessonId: step.lesson.id, title: step.lesson.title, estMinutes: est };
    }

    // What "the same kind twice in a row" compares — a source's kind, or
    // for a plan item the driller it runs.
    function _variety(item) {
        if (!item) return null;
        if (item.kind === 'speaking-cando') return 'speaking';
        return item.drillerId || item.kind;
    }

    // The next block: most urgent source whose kind differs from the
    // previous item's (falls back to same-kind only when nothing else is
    // left), and whose block fits in `room` minutes. A source that runs dry
    // or whose block doesn't fit is dropped — room only shrinks from here.
    function _pick(sources, prevKind, room) {
        const ranked = sources
            .map(s => ({ s, score: s.urgency - REPEAT_PENALTY * (_used[s.key] || 0) }))
            .sort((a, b) => b.score - a.score);
        const order = ranked.filter(r => r.s.kind !== prevKind).concat(ranked.filter(r => r.s.kind === prevKind));
        for (const { s } of order) {
            const item = s.take();
            if (!item || item.estMinutes > room + LESSON_GRACE_MINUTES) {
                sources.splice(sources.indexOf(s), 1);
                continue;
            }
            _used[s.key] = (_used[s.key] || 0) + 1;
            return item;
        }
        return null;
    }

    // ----------------------------------------
    // ALLOCATION
    // ----------------------------------------

    async function build(minutes) {
        _used = {};
        const items = [];
        let remaining = minutes;
        let skipped = null;
        const sources = await _sources({ includeLesson: false, doneLessons: new Set() });
        const add = item => { items.push(item); remaining -= item.estMinutes; };
        const last = () => _variety(items[items.length - 1]);

        // 1st — the most urgent thing. When nothing is actually urgent (a
        // new learner, say), the lesson goes first instead and filler
        // follows it.
        if (sources.some(s => s.urgency > URGENCY.FILLER)) {
            const first = _pick(sources, null, remaining);
            if (first) add(first);
        }

        // 2nd — the next lesson, or the level test.
        const step = (typeof LearnerPath !== 'undefined') ? LearnerPath.nextStep() : null;
        if (step && step.kind === 'lesson') {
            const lesson = _lessonItem(step);
            if (lesson.estMinutes <= remaining + LESSON_GRACE_MINUTES) add(lesson);
            else skipped = { reason: 'lesson-too-long', title: lesson.title, estMinutes: lesson.estMinutes };
        } else if (step && step.kind === 'test') {
            if (remaining >= TEST_MINUTES) add({ kind: 'test', level: step.level, estMinutes: TEST_MINUTES });
            else skipped = { reason: 'test-needs-bigger-block', level: step.level, estMinutes: TEST_MINUTES };
        }
        while (items.length < 2) {
            const next = _pick(sources, last(), remaining);
            if (!next) break;
            add(next);
        }

        // 3rd — a short speaking prompt, always (when speech is available
        // and the learner has a competency to practise).
        const canSpeak = (typeof SpeechInput !== 'undefined' && SpeechInput.isSupported()) || (typeof ParlourTTS !== 'undefined' && ParlourTTS.available());
        if (canSpeak && typeof LearnerModel !== 'undefined' && LearnerModel.pickSpeakingPrompt) {
            const curLevel = (typeof LearnerPath !== 'undefined' && LearnerPath.currentLevel) ? LearnerPath.currentLevel().toLowerCase() : 'all';
            const prompt = await LearnerModel.pickSpeakingPrompt(curLevel);
            if (prompt) {
                add({
                    kind: 'speaking-cando',
                    text: prompt.text,
                    level: prompt.level || curLevel,
                    lessonId: prompt.lessonId,
                    seconds: SPEAKING_PROMPT_SECONDS,
                    estMinutes: SPEAKING_PROMPT_SECONDS / 60
                });
            }
        }

        // Then — most urgent next, until the budget is full.
        while (remaining > 0.5) {
            const next = _pick(sources, last(), remaining);
            if (!next) break;
            add(next);
        }

        _queue = items;
        _index = 0;
        _minutes = minutes;
        _skipped = skipped;
        _startedAt = Date.now();
        _overtime = false;
        _passed = new Set();

        return { minutes, items, skipped };
    }

    // Appends one more activity when the planned ones are done and time is
    // left. Re-reads the learner's state (reviews just done no longer count
    // as due, etc.). Returns the new item, or null when time is up or
    // nothing fits.
    async function extend() {
        if (!Array.isArray(_queue) || _overtime) return null;
        const left = minutesLeft();
        if (left < MIN_EXTEND_MINUTES) return null;

        const done = _queue.slice(0, _index + 1);
        const sources = await _sources({
            includeLesson: true,
            doneLessons: new Set(done.filter(i => i.kind === 'lesson').map(i => i.lessonId)),
            drilledWords: done.filter(i => i.kind === 'vocabulary').flatMap(i => i.words.map(w => w.lemma))
        });
        const prev = _variety(_queue[_queue.length - 1]);
        const item = _pick(sources, prev, left);
        if (item) _queue.push(item);
        return item;
    }

    // ----------------------------------------
    // CLOCK
    // ----------------------------------------

    function minutesLeft() {
        if (!_startedAt || _minutes == null) return 0;
        return _minutes - (Date.now() - _startedAt) / 60000;
    }

    function isTimeUp() {
        return Array.isArray(_queue) && minutesLeft() <= 0;
    }

    function overtime() {
        return _overtime;
    }

    function keepGoing() {
        _overtime = true;
    }

    // ----------------------------------------
    // QUEUE POSITION
    // ----------------------------------------

    function isActive() {
        return Array.isArray(_queue) && _index < _queue.length;
    }

    // A plan exists (built, not discarded) — even with its queue used up,
    // since extend() can still add to it.
    function exists() {
        return Array.isArray(_queue);
    }

    function items() {
        return _queue || [];
    }

    function minutes() {
        return _minutes;
    }

    function skipped() {
        return _skipped;
    }

    function startedAt() {
        return _startedAt;
    }

    function currentIndex() {
        return _index;
    }

    function current() {
        return isActive() ? _queue[_index] : null;
    }

    // Marks the current item done and moves the pointer forward. Never
    // touches progress.js/xp.js/srs.js itself — those are written only by
    // whichever real activity (lesson, driller, review) the learner
    // actually completed, through its own unmodified code path. This just
    // advances the plan's own queue pointer.
    function advance() {
        if (isActive()) _index += 1;
        return current();
    }

    // Moves past the current item without it counting as done.
    function skip() {
        if (isActive()) _passed.add(_index);
        return advance();
    }

    function wasSkipped(index) {
        return _passed.has(index);
    }

    // Items actually done (behind the pointer, not skipped).
    function doneCount() {
        return _index - [..._passed].filter(i => i < _index).length;
    }

    // Ends the plan without finishing it — "Leave session," no persistence,
    // matches "a clear start and end" rather than a lingering resumable to-do.
    function discard() {
        _queue = null;
        _index = 0;
        _minutes = null;
        _skipped = null;
        _startedAt = null;
        _overtime = false;
        _used = {};
        _passed = new Set();
    }

    return {
        build,
        extend,
        isActive,
        exists,
        items,
        minutes,
        minutesLeft,
        isTimeUp,
        overtime,
        keepGoing,
        skipped,
        startedAt,
        currentIndex,
        current,
        advance,
        skip,
        wasSkipped,
        doneCount,
        discard
    };
})();
