// ============================================
// HOME
// ============================================
// The screen that answers one question: what should I do now?
//
// Nothing is studied here. Every object on it is a door into the section that
// owns the work, and the screen is deliberately short — one dominant thing to
// continue, three other ways in, where today stands, and how far the course
// has come. Detail about progress belongs on My Journey; anything that needs
// choosing between belongs in the section that owns it.
//
// Home keeps no state of its own. Every figure is counted at render time from
// data another module owns, and the tab is redrawn on every entry (see
// showTab in engine/init.js), so it cannot go stale.

const Home = (function () {
    'use strict';

    function esc(value) {
        return (typeof UI !== 'undefined' && UI.escape)
            ? UI.escape(value) : String(value == null ? '' : value);
    }

    function plural(n, one, many) {
        return n === 1 ? one : (many || one + 's');
    }

    // The page title. Time of day, not progress: the header is editorial and
    // carries no running state, so the one thing on it that changes is the
    // one thing that has nothing to do with how the learner is doing.
    function greeting() {
        const hour = new Date().getHours();
        if (hour < 12) return 'Good morning';
        if (hour < 18) return 'Good afternoon';
        return 'Good evening';
    }

    // ----------------------------------------
    // GATHERING
    // ----------------------------------------

    // The next thing in the course: the first unfinished lesson, or — once a
    // level's lessons are all done — the test that closes it. Levels are
    // walked in order, so a half-finished A1 is never stepped over.
    function nextStep() {
        const data = window._curriculumData;
        if (!data || !data.levels) return null;

        const progress = (typeof getProgress === 'function') ? getProgress() : {};
        const order = (typeof LEVEL_ORDER !== 'undefined') ? LEVEL_ORDER : ['A1'];

        for (let i = 0; i < order.length; i++) {
            const level = order[i];
            const entry = data.levels[level];
            const lessons = (entry && entry.lessons) || [];
            if (!lessons.length) continue;

            const done = lessons.filter(l => progress[l.id]).length;
            const lesson = lessons.find(l => !progress[l.id]);

            const title = entry.title || '';

            if (lesson) {
                return { kind: 'lesson', level, title, lesson, done, total: lessons.length };
            }

            const result = (typeof LevelTest !== 'undefined') ? LevelTest.resultFor(level) : null;
            if (!result || !result.passed) {
                return { kind: 'test', level, title, result, done, total: lessons.length };
            }
        }

        return null;    // every lesson finished and every test passed
    }

    function courseTotals() {
        const data = window._curriculumData;
        const progress = (typeof getProgress === 'function') ? getProgress() : {};
        let done = 0, total = 0;

        Object.keys((data && data.levels) || {}).forEach(level => {
            const lessons = data.levels[level].lessons || [];
            done += lessons.filter(l => progress[l.id]).length;
            total += lessons.length;
        });

        return { done, total, percent: total ? Math.round((done / total) * 100) : 0 };
    }

    // Counted here rather than taken from getDueCards(), which answers within
    // whatever deck the last review session was scoped to. Home is asking
    // about the whole deck.
    function deckStanding() {
        const deck = (typeof srsDeck !== 'undefined' && Array.isArray(srsDeck)) ? srsDeck : [];
        const now = Date.now();
        let due = 0;
        let soonest = null;

        deck.forEach(card => {
            // No schedule means the card has never been reviewed. The deck
            // browser counts those as due; so does this.
            if (!card.nextReview) { due++; return; }
            const at = new Date(card.nextReview).getTime();
            if (at <= now) { due++; return; }
            if (soonest === null || at < soonest) soonest = at;
        });

        return {
            size: deck.length,
            due: due,
            waitMinutes: soonest === null ? null : Math.max(1, Math.round((soonest - now) / 60000))
        };
    }

    // The next story to read: one at the level being studied if there is one,
    // otherwise the easiest thing left unread. Reaching over an unread A1
    // story to offer a B1 one is not what "read a story" should mean.
    async function nextStory(level) {
        let stories = [];
        try {
            stories = (typeof Reader !== 'undefined') ? await Reader.ensureStories() : [];
        } catch (error) {
            console.warn('Home: no story manifest for this course.', error);
            return { total: 0, story: null };
        }

        const read = (typeof getReadStoryIds === 'function') ? getReadStoryIds() : [];
        const unread = stories.filter(s => !read.includes(s.id));
        if (!unread.length) return { total: stories.length, story: null };

        const order = (typeof LEVEL_ORDER !== 'undefined') ? LEVEL_ORDER : [];
        const rank = s => {
            const i = order.indexOf(s.level);
            return i === -1 ? order.length : i;
        };

        const atLevel = unread.filter(s => s.level === level);
        const pool = atLevel.length ? atLevel : unread.slice().sort((a, b) => rank(a) - rank(b));

        return { total: stories.length, story: pool[0] };
    }

    // ----------------------------------------
    // PIECES
    // ----------------------------------------

    function meter(percent) {
        const width = Math.max(0, Math.min(100, percent));
        return `<span class="hm-track"><span class="hm-fill" style="width:${width}%"></span></span>`;
    }

    // The dominant object on the screen, and the only thing wearing the
    // accent: the course is the spine of the app, so what comes next in it
    // leads whatever else is waiting.
    function continueCard(step) {
        if (!step) {
            return `
                <section class="hm-continue is-done">
                    <span class="hm-eyebrow">The course</span>
                    <span class="hm-continue-title">Every lesson is finished</span>
                    <span class="hm-continue-sub">Nothing is left to unlock. Keep the
                        words alive in Decks, and read.</span>
                </section>
            `;
        }

        const level = step.level;
        const levelTitle = step.title;
        const percent = step.total ? Math.round((step.done / step.total) * 100) : 0;
        const count = `${step.done} of ${step.total} ${plural(step.total, 'lesson')}`;

        if (step.kind === 'test') {
            const best = step.result
                ? `Best so far ${step.result.correct} / ${step.result.total} · 80% to move on`
                : '20 questions · 80% to move on';

            return `
                <button class="hm-continue" data-open-test="${esc(level)}">
                    <span class="hm-eyebrow">${esc(level)}${levelTitle ? ' · ' + esc(levelTitle) : ''}</span>
                    <span class="hm-continue-title">${esc(level)} level test</span>
                    <span class="hm-continue-sub">${esc(best)}</span>
                    ${meter(percent)}
                    <span class="hm-continue-foot">
                        <span class="hm-count">${count}</span>
                        <span class="hm-cta">Take the test →</span>
                    </span>
                </button>
            `;
        }

        const lesson = step.lesson;
        const sub = [
            lesson.label ? 'Lesson ' + lesson.label : '',
            lesson.grammar || '',
            lesson.estimatedMinutes ? lesson.estimatedMinutes + ' min' : ''
        ].filter(Boolean).join(' · ');

        return `
            <button class="hm-continue" data-start-lesson="${esc(lesson.id)}">
                <span class="hm-eyebrow">${esc(level)}${levelTitle ? ' · ' + esc(levelTitle) : ''}</span>
                <span class="hm-continue-title">${esc(lesson.title)}</span>
                <span class="hm-continue-sub">${esc(sub)}</span>
                ${meter(percent)}
                <span class="hm-continue-foot">
                    <span class="hm-count">${count}</span>
                    <span class="hm-cta">${step.done ? 'Continue' : 'Begin'} →</span>
                </span>
            </button>
        `;
    }

    // A door: one line of what is behind it, and the number that decides
    // whether it is worth opening.
    function door(config) {
        const icon = (typeof Art !== 'undefined') ? Art.icon(config.icon) : '';
        const attrs = Object.keys(config.data || {})
            .map(key => ` data-${key}="${esc(config.data[key])}"`).join('');

        return `
            <button class="hm-door"${attrs}>
                ${icon}
                <span class="hm-door-body">
                    <span class="hm-door-title">${esc(config.title)}</span>
                    <span class="hm-door-sub">${esc(config.sub)}</span>
                </span>
                <span class="hm-door-value">${config.value ? esc(config.value) : ''}</span>
            </button>
        `;
    }

    function reviewDoor(deck) {
        if (!deck.size) {
            return door({
                icon: 'decks', title: 'Review',
                sub: 'No words yet. Tap one while reading to add it.',
                data: { go: 'review' }
            });
        }

        if (!deck.due) {
            // Naming the wait is kinder than an empty state that reads as
            // "nothing here" — the deck is working, it just isn't asking yet.
            const wait = (typeof formatInterval === 'function' && deck.waitMinutes !== null)
                ? ' Next in ' + formatInterval(deck.waitMinutes) + '.'
                : '';
            return door({
                icon: 'decks', title: 'Review',
                sub: `Nothing due.${wait}`,
                data: { go: 'review' }
            });
        }

        return door({
            icon: 'decks', title: 'Review',
            sub: `${deck.due} ${plural(deck.due, 'word')} ready to come round again.`,
            value: deck.due,
            data: { 'review-all': '1' }
        });
    }

    function readDoor(reading) {
        if (!reading.total) {
            return door({
                icon: 'library', title: 'Read',
                sub: 'No stories in this course yet.',
                data: { go: 'reader' }
            });
        }

        if (!reading.story) {
            return door({
                icon: 'library', title: 'Read',
                sub: 'You have read every story. Any of them again?',
                data: { go: 'reader' }
            });
        }

        const story = reading.story;
        const meta = [story.level, story.estimatedMinutes ? story.estimatedMinutes + ' min' : '']
            .filter(Boolean).join(' · ');

        return door({
            icon: 'library', title: 'Read',
            sub: `${story.title}${meta ? ' · ' + meta : ''}`,
            data: { 'open-story': story.id }
        });
    }

    function practiseDoor() {
        // No number here on purpose: drill accuracy is kept for the length of
        // a session and never written down, so any figure would be invented.
        return door({
            icon: 'workshop', title: 'Practise',
            sub: 'Conjugation tables and speed drills.',
            data: { go: 'drills' }
        });
    }

    // Today's three activities and the streak they keep. The ids are the ones
    // updateXPHeader() writes to, so this markup is filled in after painting
    // rather than built here.
    function todayStrip() {
        return `
            <div class="today">
                <div class="today-head">
                    <span id="header-streak">No streak yet</span>
                    <span id="header-xp">0 XP</span>
                </div>
                <div id="daily-activities" class="daily-activities"></div>
            </div>
        `;
    }

    // One line for the whole course, and a door to the screen that breaks it
    // down. Home states how far; My Journey answers how.
    function progressLine(totals) {
        return `
            <button class="hm-progress" data-go="journey">
                <span class="hm-progress-head">
                    <span>Your course</span>
                    <span class="hm-count">${totals.done} of ${totals.total}
                        ${plural(totals.total, 'lesson')}</span>
                </span>
                ${meter(totals.percent)}
                <span class="hm-progress-foot">My Journey →</span>
            </button>
        `;
    }

    // ----------------------------------------
    // ACTIONS
    // ----------------------------------------

    function goTab(id) {
        const button = document.querySelector('.nav button[data-tab="' + id + '"]');
        if (typeof showTab === 'function') showTab(id, button);
    }

    function attach(host) {
        host.addEventListener('click', e => {
            const start = e.target.closest('[data-start-lesson]');
            if (start && typeof startLesson === 'function') {
                startLesson(start.getAttribute('data-start-lesson'));
                return;
            }

            const test = e.target.closest('[data-open-test]');
            if (test && typeof LevelTest !== 'undefined') {
                LevelTest.open(test.getAttribute('data-open-test'));
                return;
            }

            // Straight into a session over the whole deck — the door already
            // said how many were waiting, so the deck browser in between would
            // only ask the question a second time.
            if (e.target.closest('[data-review-all]')) {
                goTab('review');
                if (typeof Decks !== 'undefined') Decks.reviewDeck('all');
                return;
            }

            const story = e.target.closest('[data-open-story]');
            if (story) {
                goTab('reader');
                if (typeof Reader !== 'undefined') Reader.loadStory(story.getAttribute('data-open-story'));
                return;
            }

            const go = e.target.closest('[data-go]');
            if (go) goTab(go.getAttribute('data-go'));
        });
    }

    // ----------------------------------------
    // RENDER
    // ----------------------------------------

    async function render() {
        const host = document.getElementById('home-root');
        if (!host) return;

        const step = nextStep();
        const deck = deckStanding();
        const totals = courseTotals();
        const reading = await nextStory(step ? step.level : null);

        host.innerHTML = `
            ${continueCard(step)}
            <div class="hm-doors">
                ${reviewDoor(deck)}
                ${readDoor(reading)}
                ${practiseDoor()}
            </div>
            ${todayStrip()}
            ${progressLine(totals)}
        `;

        // The streak, the XP and the three activity marks are written by the
        // XP module, which owns them and keeps them right everywhere.
        if (typeof updateXPHeader === 'function') updateXPHeader();

        if (!host.dataset.wired) {
            attach(host);
            host.dataset.wired = '1';
        }
    }

    return { render, greeting, nextStep };
})();
