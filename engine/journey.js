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
        { id: 'words-250',     label: '250 words met',            test: d => d.wordsMet >= 250 },
        { id: 'words-500',     label: '500 words met (A1 threshold)', test: d => d.wordsMet >= 500 },
        { id: 'words-1000',    label: '1,000 words met (A2 threshold)', test: d => d.wordsMet >= 1000 },
        { id: 'deck-50',       label: '50 words in your deck',    test: d => d.deckSize >= 50 },
        { id: 'mastered-50',   label: '50 words mastered in SRS', test: d => d.deckMastered >= 50 },
        { id: 'mastered-150',  label: '150 words mastered in SRS', test: d => d.deckMastered >= 150 },
        { id: 'grammar-10',    label: '10 grammar points',        test: d => d.grammarDone >= 10 },
        { id: 'reviews-100',   label: '100 reviews completed',    test: d => d.reviews >= 100 },
        { id: 'streak-7',      label: 'A week without missing',   test: d => d.bestStreak >= 7 },
        { id: 'streak-30',     label: 'A month of consistency',   test: d => d.bestStreak >= 30 },
        { id: 'level-a1',      label: 'A1 complete',              test: d => !!d.levelDone.A1 },
        { id: 'test-a1',       label: 'A1 Level Test passed',     test: d => !!(d.levelTests && d.levelTests.A1 && d.levelTests.A1.passed) },
        { id: 'test-a2',       label: 'A2 Level Test passed',     test: d => !!(d.levelTests && d.levelTests.A2 && d.levelTests.A2.passed) },
        { id: 'test-b1',       label: 'B1 Level Test passed',     test: d => !!(d.levelTests && d.levelTests.B1 && d.levelTests.B1.passed) }
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
                    grammarAll.push({ label: lesson.grammar, lesson: lesson.label, lessonId: lesson.id, done: complete });
                    if (complete) grammarDone.push(lesson.grammar);
                }

                Object.keys(lesson.exercises || {}).forEach(category => {
                    const n = lesson.exercises[category];
                    totalSkills[category] = (totalSkills[category] || 0) + n;
                    if (complete) doneSkills[category] = (doneSkills[category] || 0) + n;
                });
            });
        });

        const levelTests = {};
        if (typeof LevelTest !== 'undefined' && typeof LEVEL_ORDER !== 'undefined') {
            LEVEL_ORDER.forEach(lvl => {
                const res = LevelTest.resultFor(lvl);
                if (res) levelTests[lvl] = res;
            });
        }

        return {
            levels: levels,
            levelTests: levelTests,
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
        if (typeof xpData === 'undefined' || !xpData.history) return (typeof getImportedStreak === 'function') ? getImportedStreak() : 0;
        const days = Object.keys(xpData.history).filter(d => isStreakDay(d)).sort();
        let best = 0, run = 0, previous = null;

        days.forEach(day => {
            if (previous && (new Date(day) - new Date(previous)) === 86400000) run++;
            else run = 1;
            best = Math.max(best, run);
            previous = day;
        });
        const current = (typeof getStreak === 'function') ? getStreak() : 0;
        const imported = (typeof getImportedStreak === 'function') ? getImportedStreak() : 0;
        return Math.max(best, current, imported);
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
                <li class="jr-row jr-row-clickable" data-jr-level="${esc(key)}">
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
            ? `<p class="jr-next">Next:
                ${pending.map(g => `<button class="jr-next-link" data-jr-lesson="${esc(g.lessonId)}">${esc(g.label)}</button>`).join(' · ')}
               </p>`
            : '<p class="jr-next">Every grammar point in the course is covered.</p>';

        return card('Grammar', 'Points taught by the lessons you have finished.', `
            <button class="jr-big-link" data-jr-drill="grammar">
                <p class="jr-big">${d.grammarDone}<span class="jr-of"> of ${d.grammarTotal}</span></p>
                ${meter(d.grammarTotal ? (d.grammarDone / d.grammarTotal) * 100 : 0)}
            </button>
            ${next}
        `);
    }

    function vocabularyBlock(d) {
        let horizonText = '';
        if (d.wordsMet < 250) {
            horizonText = `${d.wordsMet} / 250 words to Basic Phrases`;
        } else if (d.wordsMet < 500) {
            horizonText = `${d.wordsMet} / 500 words to A1 Reading Horizon`;
        } else if (d.wordsMet < 1000) {
            horizonText = `${d.wordsMet} / 1,000 words to A2 Reading Horizon`;
        } else {
            horizonText = `${d.wordsMet} words met · Beyond A2 Reading Horizon`;
        }

        return card('Vocabulary', 'Words the course has introduced to you.', `
            <button class="jr-big-link" data-jr-drill="vocabulary">
                <p class="jr-big">${d.wordsMet}<span class="jr-of"> of ${d.wordsTotal}</span></p>
                ${meter(d.wordsTotal ? (d.wordsMet / d.wordsTotal) * 100 : 0)}
            </button>
            <p class="jr-next">${horizonText}</p>
            <ul class="jr-facts">
                <li><button class="jr-fact-link" data-jr-tab="review"><strong>${d.deckSize}</strong> in active SRS review</button></li>
                <li><strong>${d.deckMastered}</strong> mastered (retained across reviews)</li>
                <li><strong>${d.newWordsLearned}</strong> acquired through review</li>
                <li><button class="jr-fact-link" data-jr-tab="reader"><strong>${d.storiesRead}</strong>${d.storiesTotal ? ' of ' + d.storiesTotal : ''} stories read</button></li>
            </ul>
        `);
    }

    // Only skills with somewhere to actually go get a click target — Writing
    // and Dialogue have no dedicated Workshop driller yet (their practice
    // lives inside lessons only), so those two rows stay inert rather than
    // linking to something that doesn't exist.
    const SKILL_DESTINATIONS = {
        reading: { tab: 'reader' },
        listening: { drill: 'listening' },
        grammar: { drill: 'grammar' },
        vocab: { drill: 'vocabulary' }
    };

    function skillsBlock(d) {
        const rows = SKILLS.map(skill => {
            const done = d.doneSkills[skill.from] || 0;
            const total = d.totalSkills[skill.from] || 0;
            if (!total) return '';
            const dest = SKILL_DESTINATIONS[skill.key];
            const attrs = dest
                ? (dest.tab ? `data-jr-tab="${esc(dest.tab)}"` : `data-jr-drill="${esc(dest.drill)}"`)
                : '';
            return `
                <li class="jr-row${dest ? ' jr-row-clickable' : ''}" ${attrs}>
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

    // Rank leads (it's the new headline reading of the same total XP this
    // card always showed), with the raw number demoted into the facts list
    // alongside reviews/stories rather than dropped — see engine/xp.js's
    // getRank() for why this is deliberately not called a "level."
    function xpBlock(d) {
        const rank = (typeof getRank === 'function') ? getRank() : null;
        const headline = rank ? `
            <p class="jr-big">Rank ${rank.rank}</p>
            ${meter(rank.percent)}
            <p class="jr-next">${rank.xpIntoRank} / ${rank.xpForNextRank} XP to Rank ${rank.rank + 1}</p>
        ` : `<p class="jr-big">${d.totalXP.toLocaleString()}<span class="jr-of"> XP</span></p>`;

        return card('XP', 'Earned for reviews, reading and lessons.', `
            ${headline}
            <ul class="jr-facts">
                <li><strong>${d.totalXP.toLocaleString()}</strong> XP earned</li>
                <li><strong>${d.reviews}</strong> ${plural(d.reviews, 'review')} completed</li>
                <li><strong>${d.storiesRead}</strong> ${plural(d.storiesRead, 'story', 'stories')} read</li>
            </ul>
        `);
    }

    function streakBlock(d) {
        const current = d.streak
            ? `${d.streak} day${d.streak === 1 ? '' : 's'}`
            : 'Not started';
        const imported = (typeof getImportedStreak === 'function') ? getImportedStreak() : 0;
        return card('Streak', 'Two of the three daily activities keeps it alive.', `
            <p class="jr-big">${esc(current)}</p>
            <ul class="jr-facts">
                <li><strong>${d.bestStreak}</strong> days at your longest</li>
                <li><strong>${d.perfectDays}</strong> days with all three done</li>
                ${imported ? `<li><strong>${imported}</strong> days imported from previous app</li>` : ''}
            </ul>
            <div class="jr-streak-actions">
                <button class="dk-secondary jr-import-btn" data-jr-import-streak="1">
                    ${imported ? 'Update imported streak' : 'Import streak from another app'}
                </button>
            </div>
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

    // Step 7 of the learner-model roadmap: cloud backup/restore, folded
    // into Journey rather than a new tab — this is the "multi-user
    // support" moment profile-section-plan deferred a standalone Settings
    // screen to. Last-write-wins on purpose: two explicit, clearly-
    // labeled actions rather than an automatic merge, so the learner
    // always knows which direction is about to overwrite which.
    function accountBlock() {
        const loggedIn = (typeof Sync !== 'undefined') && Sync.isLoggedIn();
        const body = loggedIn ? `
            <p class="jr-account-email">${esc(Sync.email())}</p>
            <div class="jr-account-actions">
                <button class="dk-secondary" data-sync-backup="1">Back up now</button>
                <button class="dk-secondary" data-sync-restore="1">Restore from cloud</button>
            </div>
            <p class="jr-account-status" id="jr-account-status"></p>
            <button class="jr-account-logout" data-sync-logout="1">Log out</button>
        ` : `
            <p class="jr-account-blurb">Back up your progress so it isn't stuck on one device.</p>
            <div class="jr-account-login">
                <input type="email" id="jr-account-email-input" class="dk-editor-input"
                    placeholder="you@example.com" maxlength="254">
                <button class="dk-secondary" data-sync-request-link="1">Send me a login link</button>
            </div>
            <p class="jr-account-status" id="jr-account-status"></p>
        `;
        return card('Account', loggedIn ? 'Synced across devices' : 'Not signed in', body);
    }

    function appearanceBlock() {
        const currentPref = (typeof Theme !== 'undefined') ? Theme.getPreference() : 'system';
        const iconSystem = (typeof Art !== 'undefined') ? Art.icon('themeSystem') : '';
        const iconLight = (typeof Art !== 'undefined') ? Art.icon('themeLight') : '';
        const iconDark = (typeof Art !== 'undefined') ? Art.icon('themeDark') : '';
        const body = `
            <div class="jr-theme-switcher" role="radiogroup" aria-label="Appearance theme">
                <button type="button" class="jr-theme-option${currentPref === 'system' ? ' active' : ''}"
                    data-theme-choice="system" role="radio" aria-checked="${currentPref === 'system'}">
                    <span class="jr-theme-icon" aria-hidden="true">${iconSystem}</span>
                    <span class="jr-theme-label">System</span>
                </button>
                <button type="button" class="jr-theme-option${currentPref === 'light' ? ' active' : ''}"
                    data-theme-choice="light" role="radio" aria-checked="${currentPref === 'light'}">
                    <span class="jr-theme-icon" aria-hidden="true">${iconLight}</span>
                    <span class="jr-theme-label">Light</span>
                </button>
                <button type="button" class="jr-theme-option${currentPref === 'dark' ? ' active' : ''}"
                    data-theme-choice="dark" role="radio" aria-checked="${currentPref === 'dark'}">
                    <span class="jr-theme-icon" aria-hidden="true">${iconDark}</span>
                    <span class="jr-theme-label">Dark</span>
                </button>
            </div>
            <p class="jr-theme-hint">Constructivist low-light palette for night reading, or warm open cream.</p>
        `;
        return card('Appearance', 'Theme & visual mode', body);
    }

    // Fetches the cloud's last-backup time without touching local data,
    // once render() has already drawn the (synchronous) card — patched in
    // afterward rather than making render() itself async, since nothing
    // else in this file needs to await a network call to draw correctly.
    async function _refreshAccountStatus(host) {
        if (typeof Sync === 'undefined' || !Sync.isLoggedIn()) return;
        const statusEl = host.querySelector('#jr-account-status');
        if (!statusEl) return;
        try {
            const data = await Sync.status();
            statusEl.textContent = data && data.updatedAt
                ? 'Last backed up ' + new Date(data.updatedAt).toLocaleString() + '.'
                : 'No backup yet.';
        } catch (error) {
            statusEl.textContent = 'Could not reach the cloud right now.';
        }
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
                ${appearanceBlock()}
                ${accountBlock()}
            </div>
        `;
        _wireClicks(host);
        _refreshAccountStatus(host);
    }

    function showImportStreakModal() {
        const existing = document.getElementById('streak-import-overlay');
        if (existing) existing.remove();

        const currentImported = (typeof getImportedStreak === 'function') ? getImportedStreak() : 0;

        const overlay = document.createElement('div');
        overlay.id = 'streak-import-overlay';
        overlay.className = 'wp-overlay';
        overlay.innerHTML = `
            <div class="wp-sheet sync-prompt-sheet">
                <div class="wp-header">
                    <h2 class="sync-prompt-title">Import your streak</h2>
                    <button class="wp-close" data-streak-modal-close="1" aria-label="Close">×</button>
                </div>
                <p class="jr-account-blurb">Switching from Duolingo or another app? Bring your existing streak over so your daily momentum continues uninterrupted.</p>
                <div class="jr-account-login">
                    <input type="number" id="streak-modal-input" class="dk-editor-input"
                        placeholder="e.g. 45" min="0" max="9999" value="${currentImported || ''}">
                    <button class="dk-secondary" id="streak-modal-save">Save streak</button>
                </div>
                <p class="jr-account-status" id="streak-modal-status"></p>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px;">
                    <button class="jr-account-logout" data-streak-modal-close="1">Cancel</button>
                    ${currentImported > 0 ? '<button class="jr-account-logout" id="streak-modal-clear" style="color:var(--muted);">Clear imported streak</button>' : ''}
                </div>
            </div>
        `;

        document.body.appendChild(overlay);

        const input = overlay.querySelector('#streak-modal-input');
        const saveBtn = overlay.querySelector('#streak-modal-save');
        const clearBtn = overlay.querySelector('#streak-modal-clear');
        const statusEl = overlay.querySelector('#streak-modal-status');

        function close() {
            overlay.remove();
        }

        overlay.querySelectorAll('[data-streak-modal-close]').forEach(btn => {
            btn.addEventListener('click', close);
        });

        overlay.addEventListener('click', e => {
            if (e.target === overlay) close();
        });

        if (clearBtn) {
            clearBtn.addEventListener('click', () => {
                if (typeof importStreak === 'function') {
                    importStreak(0);
                    if (typeof updateXPHeader === 'function') updateXPHeader();
                    render();
                    close();
                }
            });
        }

        saveBtn.addEventListener('click', () => {
            const raw = input.value.trim();
            const val = parseInt(raw, 10);
            if (raw === '' || isNaN(val) || val < 0) {
                if (statusEl) statusEl.textContent = 'Please enter a valid number of days (0 or more).';
                return;
            }
            if (typeof importStreak === 'function') {
                importStreak(val);
                if (typeof updateXPHeader === 'function') updateXPHeader();
                render();
                close();
            } else {
                if (statusEl) statusEl.textContent = 'Unable to save streak.';
            }
        });

        input.addEventListener('keydown', e => {
            if (e.key === 'Enter') {
                e.preventDefault();
                saveBtn.click();
            } else if (e.key === 'Escape') {
                close();
            }
        });

        setTimeout(() => { if (input) input.focus(); }, 50);
    }

    // Every stat here is counted from something the learner did — so every
    // stat also gets somewhere to go do more of it. One delegated listener
    // (guarded the same way engine/curriculum.js guards its own root
    // listener) rather than per-row handlers, since the whole grid is
    // rebuilt on every render().
    function _wireClicks(host) {
        if (host.dataset.wired) return;
        host.dataset.wired = '1';

        host.addEventListener('click', e => {
            if (e.target.closest('[data-jr-import-streak]')) {
                showImportStreakModal();
                return;
            }

            const level = e.target.closest('[data-jr-level]');
            if (level) {
                openLevel = level.getAttribute('data-jr-level');
                openUnit = null;
                showTab('learn', document.querySelector('.nav button[data-tab="learn"]'));
                return;
            }

            const lesson = e.target.closest('[data-jr-lesson]');
            if (lesson) {
                const lessonId = lesson.getAttribute('data-jr-lesson');
                if (lessonId && typeof startLesson === 'function') startLesson(lessonId);
                return;
            }

            const tab = e.target.closest('[data-jr-tab]');
            if (tab) {
                const tabId = tab.getAttribute('data-jr-tab');
                showTab(tabId, document.querySelector('.nav button[data-tab="' + tabId + '"]'));
                return;
            }

            const drill = e.target.closest('[data-jr-drill]');
            if (drill) {
                const drillId = drill.getAttribute('data-jr-drill');
                showTab('drills', document.querySelector('.nav button[data-tab="drills"]'));
                if (typeof Workshop !== 'undefined') Workshop.open(drillId);
                return;
            }

            if (e.target.closest('[data-sync-request-link]')) {
                const input = host.querySelector('#jr-account-email-input');
                const statusEl = host.querySelector('#jr-account-status');
                const value = input ? input.value.trim() : '';
                if (!value) {
                    if (statusEl) statusEl.textContent = 'Enter an email first.';
                    return;
                }
                if (statusEl) statusEl.textContent = 'Sending…';
                Sync.requestLink(value)
                    .then(() => { if (statusEl) statusEl.textContent = 'Check your email for a link.'; })
                    .catch(error => { if (statusEl) statusEl.textContent = error.message || 'Something went wrong.'; });
                return;
            }

            if (e.target.closest('[data-sync-backup]')) {
                const statusEl = host.querySelector('#jr-account-status');
                if (statusEl) statusEl.textContent = 'Backing up…';
                Sync.backup()
                    .then(() => { if (statusEl) statusEl.textContent = 'Backed up just now.'; })
                    .catch(error => { if (statusEl) statusEl.textContent = error.message || 'Backup failed.'; });
                return;
            }

            if (e.target.closest('[data-sync-restore]')) {
                const statusEl = host.querySelector('#jr-account-status');
                if (statusEl) statusEl.textContent = 'Restoring…';
                // Sync.restore() reloads the page on success — status only
                // ever shows up on the failure path.
                Sync.restore()
                    .catch(error => { if (statusEl) statusEl.textContent = error.message || 'Restore failed.'; });
                return;
            }

            if (e.target.closest('[data-sync-logout]')) {
                Sync.logout();
                render();
                return;
            }

            const themeBtn = e.target.closest('[data-theme-choice]');
            if (themeBtn) {
                const choice = themeBtn.getAttribute('data-theme-choice');
                if (choice && typeof Theme !== 'undefined') {
                    Theme.set(choice);
                }
                return;
            }
        });
    }

    // MILESTONES is exposed so the lesson-complete screen (engine/lessons.js)
    // can check "did finishing this lesson just cross one of these" without
    // duplicating the list — same milestones, same test functions, one
    // source of truth.
    return { render, collect, MILESTONES };
})();
