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

    // The whole course, flattened into one ordered walk — every lesson, and
    // a level-test placeholder right after each level's last lesson, in the
    // same level→unit→lesson order the app has always used. nextStep()
    // below walks this twice: once forward from wherever the learner
    // actually left off, once from the very start as a fallback.
    function courseWalk() {
        const data = window._curriculumData;
        if (!data || !data.levels) return [];
        const order = (typeof LEVEL_ORDER !== 'undefined') ? LEVEL_ORDER : ['A1'];

        const steps = [];
        order.forEach(level => {
            const entry = data.levels[level];
            const units = (entry && entry.units) || [];
            const lessons = units.flatMap(u => u.lessons || []);
            if (!lessons.length) return;

            lessons.forEach(lesson => {
                // The unit's own title is more useful here than the level's —
                // "Greetings & Introductions" says more than "Fundamentals".
                const unit = units.find(u => (u.lessons || []).some(l => l.id === lesson.id));
                steps.push({ kind: 'lesson', level, title: (unit && unit.title) || entry.title || '', lesson });
            });
            steps.push({ kind: 'test', level, title: entry.title || '' });
        });
        return steps;
    }

    function stepIsDone(step, progress) {
        if (step.kind === 'lesson') return !!progress[step.lesson.id];
        const result = (typeof LevelTest !== 'undefined') ? LevelTest.resultFor(step.level) : null;
        return !!(result && result.passed);
    }

    function levelStats(level, progress) {
        const data = window._curriculumData;
        const entry = data && data.levels && data.levels[level];
        const lessons = ((entry && entry.units) || []).flatMap(u => u.lessons || []);
        return { done: lessons.filter(l => progress[l.id]).length, total: lessons.length };
    }

    function stepToResult(step, progress) {
        const stats = levelStats(step.level, progress);
        if (step.kind === 'test') {
            const result = (typeof LevelTest !== 'undefined') ? LevelTest.resultFor(step.level) : null;
            return { kind: 'test', level: step.level, title: step.title, result, done: stats.done, total: stats.total };
        }
        return { kind: 'lesson', level: step.level, title: step.title, lesson: step.lesson, done: stats.done, total: stats.total };
    }

    // The next thing to continue with. Follows the learner rather than the
    // course's own order: it continues forward from wherever their most
    // recently completed lesson actually sits, so clearing Unit 10 out of
    // order recommends Unit 11 next, not a snap back to Unit 1 just because
    // it's still the earliest unfinished thing overall. Only falls back to
    // sweeping from the very start of the course — the old, order-only
    // behaviour — once there's genuinely nothing left ahead, which is what
    // keeps a real gap left behind (an earlier unit never finished) from
    // being lost track of forever rather than just not being the default.
    function nextStep() {
        const data = window._curriculumData;
        if (!data || !data.levels) return null;

        const progress = (typeof getProgress === 'function') ? getProgress() : {};
        const steps = courseWalk();
        if (!steps.length) return null;

        const lastId = lastCompletedLessonId();
        const lastIndex = lastId ? steps.findIndex(s => s.kind === 'lesson' && s.lesson.id === lastId) : -1;

        if (lastIndex !== -1) {
            for (let i = lastIndex + 1; i < steps.length; i++) {
                const step = steps[i];
                if (stepIsDone(step, progress)) continue;

                // A level test only belongs here once the whole level is
                // actually done — reaching it mid-forward-scan while an
                // earlier lesson in the SAME level is still incomplete
                // (behind the scan's start point, so never visited above)
                // means there's a real gap to go back to first. Stop
                // scanning forward and fall through to the sweep below,
                // which will find that gap rather than offering the test
                // prematurely.
                if (step.kind === 'test') {
                    const stats = levelStats(step.level, progress);
                    if (stats.done < stats.total) break;
                }

                return stepToResult(step, progress);
            }
        }

        for (let i = 0; i < steps.length; i++) {
            if (!stepIsDone(steps[i], progress)) return stepToResult(steps[i], progress);
        }

        return null;    // every lesson finished and every test passed
    }

    function courseTotals() {
        const data = window._curriculumData;
        const progress = (typeof getProgress === 'function') ? getProgress() : {};
        let done = 0, total = 0;

        Object.keys((data && data.levels) || {}).forEach(level => {
            const lessons = (data.levels[level].units || []).flatMap(u => u.lessons || []);
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

    // The lesson most recently marked complete, by timestamp — used only to
    // detect whether the learner just closed out a whole unit, not to drive
    // nextStep() (which already walks the curriculum in order regardless of
    // what was done most recently).
    function lastCompletedLessonId() {
        const progress = (typeof getProgress === 'function') ? getProgress() : {};
        let bestId = null, bestTime = -1;
        Object.keys(progress).forEach(id => {
            const t = Date.parse((progress[id] || {}).completedAt || '') || 0;
            if (t > bestTime) { bestTime = t; bestId = id; }
        });
        return bestId;
    }

    // Which unit (and level) a lesson id belongs to, or null if the
    // curriculum isn't loaded or the id isn't in it.
    function unitFor(lessonId) {
        const data = window._curriculumData;
        if (!data || !data.levels || !lessonId) return null;

        for (const levelKey of Object.keys(data.levels)) {
            const units = data.levels[levelKey].units || [];
            const unit = units.find(u => (u.lessons || []).some(l => l.id === lessonId));
            if (unit) return { levelKey, unit };
        }
        return null;
    }

    // A unit's practice nudge, once resolved (practised or skipped), never
    // comes back for that unit — a one-time "before you move on" beat, not
    // a recurring interruption. Persisted per course, same as everything
    // else keyed off Lang.key().
    function dismissedUnitsKey() {
        return Lang.key('unitPracticeDismissed');
    }

    function dismissedUnits() {
        try {
            return JSON.parse(localStorage.getItem(dismissedUnitsKey()) || '[]');
        } catch (error) {
            return [];
        }
    }

    function dismissUnit(unitId) {
        const list = dismissedUnits();
        if (!list.includes(unitId)) {
            list.push(unitId);
            try { localStorage.setItem(dismissedUnitsKey(), JSON.stringify(list)); }
            catch (error) { /* private browsing with storage disabled — the nudge just won't stay dismissed */ }
        }
    }

    // The exact exercises-file path a lesson id resolves to — the same
    // level/rest split loadLesson() uses in engine/lessons.js, applied to
    // the "-ex.json" sibling every lesson's exercise-group sections point
    // at, rather than fetching each lesson file just to read its own ref
    // back out.
    function exerciseRefFor(lessonId) {
        const parts = lessonId.replace(/^lesson\./, '').split('.');
        const level = parts[0];
        const rest = parts.slice(1).join('-');
        return `exercises/${level}/${level}-${rest}-ex.json`;
    }

    // The grammar concept a unit leans on most, read from the same
    // teaches-tag index Workshop's Grammar Driller already builds its skill
    // list from (content/<lang>/indexes/grammar-index.json) — no new
    // content or index needed. Ties a unit to a skill by matching that
    // skill's exercise refs against the unit's own lesson ids; the most
    // frequent match wins. Returns null (not "mixed") when nothing matches,
    // so the caller can decide not to offer a nudge with nothing behind it.
    async function unitSkillFor(unit) {
        if (typeof Content === 'undefined' || typeof Lang === 'undefined') return null;

        let index;
        try {
            index = await Content.json(Lang.content('indexes/grammar-index.json'));
        } catch (error) {
            return null;
        }

        const refs = new Set((unit.lessons || []).map(l => exerciseRefFor(l.id)));
        const counts = {};
        Object.keys((index && index.bySkill) || {}).forEach(skill => {
            index.bySkill[skill].forEach(entry => {
                if (refs.has(entry.ref)) counts[skill] = (counts[skill] || 0) + 1;
            });
        });

        const ranked = Object.keys(counts).sort((a, b) => counts[b] - counts[a]);
        return ranked[0] || null;
    }

    // Home's post-unit practice beat: the last lesson completed was the
    // last lesson in its unit, that unit hasn't already been resolved, and
    // there's an actual grammar skill to point Workshop at. Any one of
    // those failing means "no nudge" — this never blocks or delays the
    // normal continue card, it only sometimes stands in front of it once.
    async function practiceNudge() {
        const lessonId = lastCompletedLessonId();
        if (!lessonId) return null;

        const found = unitFor(lessonId);
        if (!found) return null;

        const { levelKey, unit } = found;
        const lessons = unit.lessons || [];
        const last = lessons[lessons.length - 1];
        if (!last || last.id !== lessonId) return null; // not the unit's last lesson

        if (dismissedUnits().includes(unit.id)) return null;

        const skill = await unitSkillFor(unit);
        if (!skill) return null;

        return { levelKey, unit, skill };
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
            lesson.grammar || ''
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

    // Stands in the continue card's slot for exactly one visit after a unit
    // ends — same dominant position, because this is the one moment a
    // detour here is worth more than the default "keep going." Two real
    // actions rather than one whole-row click (unlike continueCard's
    // button), since "practise" and "not now" aren't the same weight.
    function practiceNudgeCard(nudge) {
        const title = nudge.unit.title || 'that unit';
        return `
            <section class="hm-continue hm-nudge">
                <span class="hm-eyebrow">${esc(nudge.levelKey)} · Unit complete</span>
                <span class="hm-continue-title">Practise before moving on?</span>
                <span class="hm-continue-sub">A quick round on what "${esc(title)}" just taught,
                    while it's still fresh.</span>
                <span class="hm-continue-foot">
                    <button class="hm-cta-btn" data-practice-unit="${esc(nudge.unit.id)}"
                        data-skill="${esc(nudge.skill)}">Practise now →</button>
                    <button class="dk-link-btn" data-skip-unit="${esc(nudge.unit.id)}">Not now</button>
                </span>
            </section>
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
                icon: 'reader', title: 'Read',
                sub: 'No stories in this course yet.',
                data: { go: 'reader' }
            });
        }

        if (!reading.story) {
            return door({
                icon: 'reader', title: 'Read',
                sub: 'You have read every story. Any of them again?',
                data: { go: 'reader' }
            });
        }

        const story = reading.story;
        const meta = [story.level, story.estimatedMinutes ? story.estimatedMinutes + ' min' : '']
            .filter(Boolean).join(' · ');

        return door({
            icon: 'reader', title: 'Read',
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

            const practise = e.target.closest('[data-practice-unit]');
            if (practise) {
                dismissUnit(practise.getAttribute('data-practice-unit'));
                goTab('drills');
                if (typeof Workshop !== 'undefined') {
                    Workshop.open('grammar', { skill: practise.getAttribute('data-skill') });
                }
                return;
            }

            const skip = e.target.closest('[data-skip-unit]');
            if (skip) {
                dismissUnit(skip.getAttribute('data-skip-unit'));
                render();
                return;
            }
        });

        host.addEventListener('change', e => {
            const select = e.target.closest('#hm-lang-select');
            if (!select || select.value === Lang.code()) return;
            Lang.set(select.value);
            location.reload();
        });
    }

    // Which course the learner is studying. Lives at the top of Home rather
    // than buried in My Journey — a course choice isn't a reading of
    // progress, it's the frame everything else on screen (including Home
    // itself) is drawn inside, so it belongs where the learner lands first.
    // Only courses with real content are offered; see Lang.available() in
    // engine/lang.js.
    function courseBlock() {
        const options = Lang.available()
            .map(code => `<option value="${code}"${code === Lang.code() ? ' selected' : ''}>${esc(Lang.nameFor(code))}</option>`)
            .join('');

        return `
            <div class="jr-course">
                <label class="jr-course-label" for="hm-lang-select">Course</label>
                <select id="hm-lang-select" class="jr-lang-select" aria-label="Course">${options}</select>
            </div>
        `;
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
        const nudge = await practiceNudge();

        host.innerHTML = `
            ${courseBlock()}
            ${nudge ? practiceNudgeCard(nudge) : continueCard(step)}
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
