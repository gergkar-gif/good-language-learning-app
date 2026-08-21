// ============================================
// MY JOURNEY
// ============================================
// What the learner has actually done, in eight separate readings rather than
// one blended score. A single number would be easier to draw and would hide
// exactly the thing a learner needs to see: that vocabulary is running ahead
// of grammar, or that nothing has been read in a fortnight.
//
// Every figure here is counted from something the learner did. Where a skill
// is not measured yet — listening has no exercises until A2, speaking has no
// input at all — it says so rather than showing a zero, because a zero reads
// as failure and a blank reads as a bug. Nothing on this screen is estimated.

const Journey = (function () {
    'use strict';

    // Enough words to be worth celebrating, and each is a real threshold
    // rather than a round number chosen to fire often.
    const MILESTONES = [
        { id: 'first-lesson',  label: 'First lesson finished',    test: d => d.lessonsComplete >= 1 },
        { id: 'first-story',   label: 'First story read',         test: d => d.storiesRead >= 1 },
        { id: 'words-100',     label: '100 words met',            test: d => d.wordsMet >= 100 },
        { id: 'deck-50',       label: '50 words in your deck',    test: d => d.deckSize >= 50 },
        { id: 'grammar-10',    label: '10 grammar points',        test: d => d.grammarDone >= 10 },
        { id: 'reviews-100',   label: '100 reviews completed',    test: d => d.reviews >= 100 },
        { id: 'streak-7',      label: 'A week without missing',   test: d => d.bestStreak >= 7 },
        { id: 'level-a1',      label: 'A1 complete',              test: d => d.levelDone.A1 }
    ];

    // Categories a lesson's exercises fall into, mapped to the skill each one
    // trains. Vocabulary and grammar exercises are counted separately from the
    // words and grammar points themselves — one is practice, the other is
    // coverage, and conflating them flatters the learner.
    const SKILLS = [
        { key: 'reading',   label: 'Reading',   from: 'reading' },
        { key: 'listening', label: 'Listening', from: 'listening' },
        { key: 'writing',   label: 'Writing',   from: 'writing' },
        { key: 'dialogue',  label: 'Dialogue',  from: 'dialogue' },
        { key: 'grammar',   label: 'Grammar',   from: 'grammar' },
        { key: 'vocab',     label: 'Vocabulary', from: 'vocabulary' }
    ];

    // Skills the app cannot honestly report on yet. Named rather than hidden,
    // so the absence is legible as a plan rather than an oversight.
    const UNMEASURED = [
        { label: 'Speaking', note: 'Not measured yet.' }
    ];

    // ----------------------------------------
    // GATHERING
    // ----------------------------------------
    function collect() {
        const curriculum = window._curriculumData;
        const progress = (typeof getProgress === 'function') ? getProgress() : {};
        const stats = (typeof getStats === 'function') ? getStats() : {};
        const deck = (typeof srsDeck !== 'undefined' && Array.isArray(srsDeck)) ? srsDeck : [];
        const readIds = (typeof getReadStoryIds === 'function') ? getReadStoryIds() : [];

        const levels = {};
        const grammarAll = [];
        const grammarDone = [];
        let wordsMet = 0, wordsTotal = 0;
        let lessonsComplete = 0, lessonsTotal = 0;
        const doneSkills = {}, totalSkills = {};

        Object.keys((curriculum && curriculum.levels) || {}).forEach(levelKey => {
            const lessons = (curriculum.levels[levelKey].units || []).flatMap(u => u.lessons || []);
            if (!lessons.length) return;

            const done = lessons.filter(l => progress[l.id]);
            lessonsComplete += done.length;
            lessonsTotal += lessons.length;
            levels[levelKey] = {
                title: curriculum.levels[levelKey].title,
                done: done.length,
                total: lessons.length,
                percent: Math.round((done.length / lessons.length) * 100)
            };

            lessons.forEach(lesson => {
                const complete = !!progress[lesson.id];
                wordsTotal += lesson.newWords || 0;
                if (complete) wordsMet += lesson.newWords || 0;

                // Review lessons carry no grammar of their own.
                if (lesson.grammar && lesson.grammar !== 'Consolidation') {
                    grammarAll.push({ label: lesson.grammar, lesson: lesson.label, done: complete });
                    if (complete) grammarDone.push(lesson.grammar);
                }

                Object.keys(lesson.exercises || {}).forEach(category => {
                    const n = lesson.exercises[category];
                    totalSkills[category] = (totalSkills[category] || 0) + n;
                    if (complete) doneSkills[category] = (doneSkills[category] || 0) + n;
                });
            });
        });

        return {
            levels: levels,
            lessonsComplete: lessonsComplete,
            lessonsTotal: lessonsTotal,
            levelDone: Object.keys(levels).reduce((acc, k) => {
                acc[k] = levels[k].total > 0 && levels[k].done === levels[k].total;
                return acc;
            }, {}),
            grammarAll: grammarAll,
            grammarDone: grammarDone.length,
            grammarTotal: grammarAll.length,
            wordsMet: wordsMet,
            wordsTotal: wordsTotal,
            deckSize: deck.length,
            deckMastered: deck.filter(c => (c.reviews || 0) >= 3).length,
            deckSeen: deck.filter(c => (c.reviews || 0) >= 1).length,
            storiesRead: readIds.length,
            storiesTotal: (typeof Reader !== 'undefined' && Reader.stories) ? Reader.stories.length : 0,
            doneSkills: doneSkills,
            totalSkills: totalSkills,
            totalXP: stats.totalXP || 0,
            reviews: stats.reviewsCompleted || 0,
            lessonsDone: stats.lessonsCompleted || 0,
            newWordsLearned: stats.newWordsLearned || 0,
            streak: stats.currentStreak || 0,
            bestStreak: bestStreak(),
            perfectDays: stats.perfectDays || 0,
            consistency: stats.monthlyConsistency || { activeDays: 0, windowDays: 30, percent: 0 }
        };
    }

    // getStreak() only reports the run ending today. The longest run ever is a
    // different and more encouraging number once a streak has been broken.
    function bestStreak() {
        if (typeof xpData === 'undefined' || !xpData.history) return 0;
        const days = Object.keys(xpData.history).filter(d => isStreakDay(d)).sort();
        let best = 0, run = 0, previous = null;

        days.forEach(day => {
            if (previous && (new Date(day) - new Date(previous)) === 86400000) run++;
            else run = 1;
            best = Math.max(best, run);
            previous = day;
        });
        return best;
    }

    // ----------------------------------------
    // PIECES
    // ----------------------------------------
    function esc(value) {
        return (typeof UI !== 'undefined' && UI.escape) ? UI.escape(value) : String(value == null ? '' : value);
    }

    function plural(n, one, many) {
        return n === 1 ? one : (many || one + 's');
    }

    function meter(percent) {
        const width = Math.max(0, Math.min(100, percent));
        return `<span class="jr-track"><span class="jr-fill" style="width:${width}%"></span></span>`;
    }

    function card(title, subtitle, body) {
        return `
            <section class="jr-card">
                <div class="jr-card-head">
                    <h3>${esc(title)}</h3>
                    ${subtitle ? `<p>${esc(subtitle)}</p>` : ''}
                </div>
                ${body}
            </section>
        `;
    }

    function curriculumBlock(d) {
        const rows = Object.keys(d.levels).map(key => {
            const level = d.levels[key];
            return `
                <li class="jr-row">
                    <span class="jr-row-label">${esc(key)} · ${esc(level.title)}</span>
                    <span class="jr-row-meter">${meter(level.percent)}</span>
                    <span class="jr-row-value">${level.done} / ${level.total}</span>
                </li>
            `;
        }).join('');
        return card('Curriculum', 'Lessons finished, level by level.', `
            <ul class="jr-list">${rows || '<li class="jr-empty">No course loaded.</li>'}</ul>
            <ul class="jr-facts">
                <li><strong>${d.lessonsComplete}</strong> of ${d.lessonsTotal}
                    ${plural(d.lessonsTotal, 'lesson')} finished</li>
            </ul>
        `);
    }

    function grammarBlock(d) {
        const pending = d.grammarAll.filter(g => !g.done).slice(0, 3);
        const next = pending.length
            ? `<p class="jr-next">Next: ${pending.map(g => esc(g.label)).join(' · ')}</p>`
            : '<p class="jr-next">Every grammar point in the course is covered.</p>';

        return card('Grammar', 'Points taught by the lessons you have finished.', `
            <p class="jr-big">${d.grammarDone}<span class="jr-of"> of ${d.grammarTotal}</span></p>
            ${meter(d.grammarTotal ? (d.grammarDone / d.grammarTotal) * 100 : 0)}
            ${next}
        `);
    }

    function vocabularyBlock(d) {
        return card('Vocabulary', 'Words the course has introduced to you.', `
            <p class="jr-big">${d.wordsMet}<span class="jr-of"> of ${d.wordsTotal}</span></p>
            ${meter(d.wordsTotal ? (d.wordsMet / d.wordsTotal) * 100 : 0)}
            <ul class="jr-facts">
                <li><strong>${d.deckSize}</strong> in your review deck</li>
                <li><strong>${d.deckMastered}</strong> reviewed three times or more</li>
                <li><strong>${d.newWordsLearned}</strong> learned through review</li>
                <li><strong>${d.storiesRead}</strong>${d.storiesTotal ? ' of ' + d.storiesTotal : ''} stories read</li>
            </ul>
        `);
    }

    function skillsBlock(d) {
        const rows = SKILLS.map(skill => {
            const done = d.doneSkills[skill.from] || 0;
            const total = d.totalSkills[skill.from] || 0;
            if (!total) return '';
            return `
                <li class="jr-row">
                    <span class="jr-row-label">${esc(skill.label)}</span>
                    <span class="jr-row-meter">${meter((done / total) * 100)}</span>
                    <span class="jr-row-value">${done} / ${total}</span>
                </li>
            `;
        }).join('');

        const unmeasured = UNMEASURED.map(skill => `
            <li class="jr-row jr-row-muted">
                <span class="jr-row-label">${esc(skill.label)}</span>
                <span class="jr-row-note" colspan="2">${esc(skill.note)}</span>
            </li>
        `).join('');

        return card('Skills', 'Exercises completed, by the skill they train.', `
            <ul class="jr-list">${rows}${unmeasured}</ul>
        `);
    }

    function xpBlock(d) {
        return card('XP', 'Earned for reviews, reading and lessons.', `
            <p class="jr-big">${d.totalXP.toLocaleString()}<span class="jr-of"> XP</span></p>
            <ul class="jr-facts">
                <li><strong>${d.reviews}</strong> ${plural(d.reviews, 'review')} completed</li>
                <li><strong>${d.storiesRead}</strong> ${plural(d.storiesRead, 'story', 'stories')} read</li>
            </ul>
        `);
    }

    function streakBlock(d) {
        const current = d.streak
            ? `${d.streak} day${d.streak === 1 ? '' : 's'}`
            : 'Not started';
        return card('Streak', 'Two of the three daily activities keeps it alive.', `
            <p class="jr-big">${esc(current)}</p>
            <ul class="jr-facts">
                <li><strong>${d.bestStreak}</strong> days at your longest</li>
                <li><strong>${d.perfectDays}</strong> days with all three done</li>
            </ul>
        `);
    }

    function activityBlock(d) {
        const today = new Date();
        const cells = [];
        for (let i = 29; i >= 0; i--) {
            const day = new Date(today);
            day.setDate(day.getDate() - i);
            const key = day.toISOString().slice(0, 10);
            const active = (typeof isStreakDay === 'function') && isStreakDay(key);
            const entry = (typeof xpData !== 'undefined' && xpData.history) ? xpData.history[key] : null;
            const earned = entry ? (entry.total || 0) : 0;
            cells.push(
                `<span class="jr-day${active ? ' is-active' : ''}" title="${key}: ${earned} XP"></span>`
            );
        }
        return card('Activity', 'The last thirty days.', `
            <div class="jr-days">${cells.join('')}</div>
            <p class="jr-next">${d.consistency.activeDays} active of the last
                ${d.consistency.windowDays} days.</p>
        `);
    }

    function milestonesBlock(d) {
        const items = MILESTONES.map(m => {
            const reached = !!m.test(d);
            return `
                <li class="jr-milestone${reached ? ' is-reached' : ''}">
                    <span class="jr-tick" aria-hidden="true">${reached ? '✓' : ''}</span>
                    <span>${esc(m.label)}</span>
                </li>
            `;
        }).join('');
        const count = MILESTONES.filter(m => m.test(d)).length;
        return card('Milestones', `${count} of ${MILESTONES.length} reached.`,
            `<ul class="jr-milestones">${items}</ul>`);
    }

    // ----------------------------------------
    // RENDER
    // ----------------------------------------
    function render() {
        const host = document.getElementById('journey-root');
        if (!host) return;

        const d = collect();

        host.innerHTML = `
            <div class="jr-grid">
                ${curriculumBlock(d)}
                ${grammarBlock(d)}
                ${vocabularyBlock(d)}
                ${skillsBlock(d)}
                ${xpBlock(d)}
                ${streakBlock(d)}
                ${activityBlock(d)}
                ${milestonesBlock(d)}
            </div>
        `;
    }

    return { render, collect };
})();
