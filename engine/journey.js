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
        { id: 'mastered-50',   label: '50 words mastered',        test: d => d.deckMastered >= 50 },
        { id: 'mastered-150',  label: '150 words mastered',       test: d => d.deckMastered >= 150 },
        { id: 'grammar-10',    label: '10 grammar points',        test: d => d.grammarDone >= 10 },
        { id: 'reviews-100',   label: '100 reviews completed',    test: d => d.reviews >= 100 },
        { id: 'streak-7',      label: 'A week without missing',   test: d => d.bestStreak >= 7 },
        { id: 'streak-30',     label: 'A month of consistency',   test: d => d.bestStreak >= 30 },
        { id: 'level-a1',      label: 'A1 complete',              test: d => !!d.levelDone.A1 },
        { id: 'test-a1',       label: 'A1 Level Test passed',     test: d => !!(d.levelTests && d.levelTests.A1 && d.levelTests.A1.passed) },
        { id: 'test-a2',       label: 'A2 Level Test passed',     test: d => !!(d.levelTests && d.levelTests.A2 && d.levelTests.A2.passed) },
        { id: 'test-b1',       label: 'B1 Level Test passed',     test: d => !!(d.levelTests && d.levelTests.B1 && d.levelTests.B1.passed) },
        { id: 'test-b2',       label: 'B2 Level Test passed',     test: d => !!(d.levelTests && d.levelTests.B2 && d.levelTests.B2.passed) },
        { id: 'test-c1',       label: 'C1 Level Test passed',     test: d => !!(d.levelTests && d.levelTests.C1 && d.levelTests.C1.passed) }
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

    // Skills the app cannot honestly report on yet, for a learner with no
    // evidence at all — named rather than hidden, so the absence is legible
    // as a plan rather than an oversight. Speaking drops out of this list
    // once LearnerModel.productionSummary('oral') has anything to show (see
    // skillsBlock below); it isn't unmeasurable, just unmeasured until the
    // learner actually speaks.
    const UNMEASURED = [
        { key: 'speaking', label: 'Speaking', note: 'Not measured yet.' }
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

        let candoStats = { total: 0, verified: 0, confidenceGap: 0, blindspot: 0, deficit: 0, decayed: 0 };
        if (typeof LearnerModel !== 'undefined' && typeof LearnerModel.allCompetencies === 'function') {
            const all = LearnerModel.allCompetencies();
            Object.keys(all).forEach(k => {
                const rec = all[k];
                if (rec.state === 'verified') {
                    const days = rec.verifiedAt ? (Date.now() - rec.verifiedAt) / (1000 * 3600 * 24) : 0;
                    if (days > 30) candoStats.decayed++;
                    else candoStats.verified++;
                } else if (rec.state === 'confidence-gap') {
                    candoStats.confidenceGap++;
                } else if (rec.state === 'blindspot') {
                    candoStats.blindspot++;
                } else if (rec.state === 'deficit') {
                    candoStats.deficit++;
                }
            });
        }

        const speakingProduction = (typeof LearnerModel !== 'undefined' && typeof LearnerModel.productionSummary === 'function')
            ? LearnerModel.productionSummary('oral')
            : null;

        return {
            candoStats: candoStats,
            speakingProduction: speakingProduction,
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

    function canDoPortfolioBlock(d) {
        const stats = d.candoStats || { verified: 0, confidenceGap: 0, blindspot: 0, deficit: 0, decayed: 0 };
        const needsReview = (stats.blindspot || 0) + (stats.deficit || 0) + (stats.decayed || 0);

        return card('CEFR Can-Do Passport', 'Real-world competencies demonstrated across your journey.', `
            <button class="jr-big-link" data-jr-cando-open="1">
                <p class="jr-big">${stats.verified}<span class="jr-of"> verified</span></p>
            </button>
            <div class="jr-cando-chips">
                <span class="jr-cando-chip chip-verified">${stats.verified} Verified</span>
                ${stats.confidenceGap > 0 ? `<span class="jr-cando-chip chip-gap">${stats.confidenceGap} Confidence Gap</span>` : ''}
                ${needsReview > 0 ? `<span class="jr-cando-chip chip-review">${needsReview} Needs Review</span>` : ''}
            </div>
            <div class="jr-streak-actions" style="margin-top:14px;">
                <button class="dk-secondary jr-import-btn" data-jr-cando-open="1">
                    Open Can-Do Portfolio →
                </button>
            </div>
        `);
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
                <li><button class="jr-fact-link" data-jr-tab="review"><strong>${d.deckSize}</strong> in active review</button></li>
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

        const sp = d.speakingProduction;
        const speakingRow = sp
            ? `
                <li class="jr-row jr-row-clickable" data-jr-drill="speaking">
                    <span class="jr-row-label">Speaking</span>
                    <span class="jr-row-meter">${meter(sp.avgAccuracy)}</span>
                    <span class="jr-row-value">${sp.avgAccuracy}% over ${sp.attempts} ${plural(sp.attempts, 'attempt')}</span>
                </li>
            `
            : UNMEASURED.filter(skill => skill.key === 'speaking').map(skill => `
                <li class="jr-row jr-row-muted">
                    <span class="jr-row-label">${esc(skill.label)}</span>
                    <span class="jr-row-note" colspan="2">${esc(skill.note)}</span>
                </li>
            `).join('');

        const unmeasured = UNMEASURED.filter(skill => skill.key !== 'speaking').map(skill => `
            <li class="jr-row jr-row-muted">
                <span class="jr-row-label">${esc(skill.label)}</span>
                <span class="jr-row-note" colspan="2">${esc(skill.note)}</span>
            </li>
        `).join('');

        return card('Skills', 'Exercises completed, by the skill they train.', `
            <ul class="jr-list">${rows}${speakingRow}${unmeasured}</ul>
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
        const withStatus = MILESTONES.map(m => ({ label: m.label, reached: !!m.test(d) }));
        const itemHtml = m => `
            <li class="jr-milestone${m.reached ? ' is-reached' : ''}">
                <span class="jr-tick" aria-hidden="true">${m.reached ? '✓' : ''}</span>
                <span>${esc(m.label)}</span>
            </li>
        `;
        const count = withStatus.filter(m => m.reached).length;
        // Sixteen milestones flat was a wall to scroll past for the two or
        // three actually still ahead of you — show just the next few
        // (already-reached ones are already summed up by the count line
        // above) and put the full list, reached items included, behind the
        // same collapsible pattern the Library uses for its rooms/shelves.
        const upcoming = withStatus.filter(m => !m.reached).slice(0, 5);
        const hasMore = withStatus.length > upcoming.length;

        return card('Milestones', `${count} of ${MILESTONES.length} reached.`, `
            <ul class="jr-milestones" id="jr-milestones-upcoming">${upcoming.map(itemHtml).join('')}</ul>
            ${hasMore ? `
                <button class="jr-milestones-toggle" data-jr-milestones-toggle="1" aria-expanded="false">
                    <span>See all</span>
                    <span class="jr-milestones-arrow" id="jr-milestones-arrow">▶</span>
                </button>
                <ul class="jr-milestones hidden" id="jr-milestones-all">${withStatus.map(itemHtml).join('')}</ul>
            ` : ''}
        `);
    }

    // Step 7 of the learner-model roadmap: cloud backup/restore, folded
    // into Journey rather than a new tab — this is the "multi-user
    // support" moment profile-section-plan deferred a standalone Settings
    // screen to. Last-write-wins on purpose: two explicit, clearly-
    // labeled actions rather than an automatic merge, so the learner
    // always knows which direction is about to overwrite which.
    function accountBlock() {
        const loggedIn = (typeof Sync !== 'undefined') && Sync.isLoggedIn();
        const googleAuthAvailable = (typeof Sync !== 'undefined') && Sync.isGoogleAuthAvailable && Sync.isGoogleAuthAvailable();
        const googleSection = googleAuthAvailable ? `
            <div id="jr-google-signin-btn" class="jr-google-signin-container"></div>
            <div class="jr-account-divider"><span>or sign in with email</span></div>
        ` : '';

        const rememberedEmail = (typeof Sync !== 'undefined' && Sync.email) ? Sync.email() : '';
        const expiredNotice = (!loggedIn && rememberedEmail) ? `
            <p class="jr-account-expired" style="font-size:13px; color:var(--accent, #dc4e2e); margin:0 0 10px;">Your session has expired. Sign in again to resume syncing.</p>
        ` : '';

        const body = loggedIn ? `
            <p class="jr-account-email">${esc(Sync.email())}</p>
            <p class="jr-account-sub" style="font-size:12px; color:var(--muted); margin: 4px 0 12px;">Automatic cloud saving active. Progress syncs automatically as you study.</p>
            <div class="jr-account-actions">
                <button class="dk-secondary" data-sync-backup="1">Back up now</button>
                <button class="dk-secondary" data-sync-restore="1">Restore from cloud</button>
            </div>
            <p class="jr-account-status" id="jr-account-status"></p>
            <div class="jr-account-footer">
                <button class="jr-account-logout" data-sync-logout="1">Log out</button>
                <button class="jr-account-logout jr-account-delete" data-sync-delete="1">Delete account</button>
            </div>
        ` : `
            ${expiredNotice}
            <p class="jr-account-blurb">${expiredNotice ? 'Sign in to reconnect this device to your cloud progress.' : 'Back up your progress so it isn\'t stuck on one device.'}</p>
            ${googleSection}
            <div class="jr-account-login">
                <input type="email" id="jr-account-email-input" class="dk-editor-input"
                    placeholder="you@example.com" value="${esc(rememberedEmail)}" maxlength="254">
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
                ? 'Cloud backup: ' + new Date(data.updatedAt).toLocaleString() + ' · Up to date'
                : 'No backup yet.';
        } catch (error) {
            statusEl.textContent = (error.message && error.message.includes('Session expired'))
                ? error.message
                : 'Could not reach the cloud right now.';
        }
    }

    // ----------------------------------------
    // RENDER
    // ----------------------------------------
    // The page is one hero, the streak, one mountain and a short list of rows.
    // Each row opens the older readings (kept as they were, restyled as open
    // sections) as a view of its own, so nothing is lost and nothing competes.
    let _view = 'main';

    function _levelKeys(d) {
        const order = (typeof LEVEL_ORDER !== 'undefined') ? LEVEL_ORDER : ['A1', 'A2', 'B1', 'B2', 'C1'];
        return order.filter(k => d.levels[k]);
    }

    // A right-triangle ridge from A1 (left) to the last level (summit), in
    // equal bands. Gates between bands are green once a level is finished;
    // the vermilion marker sits at the learner's true position: the levels
    // finished plus the fraction of the current one.
    function mountainHtml(d) {
        const keys = _levelKeys(d);
        if (!keys.length) return '';
        const n = keys.length;
        const next = (typeof LearnerPath !== 'undefined') ? LearnerPath.nextStep() : null;
        let idx = next && next.level ? keys.indexOf(next.level) : -1;
        if (idx !== -1 && d.levelDone[keys[idx]]) idx = keys.findIndex(k => !d.levelDone[k]);
        if (idx === -1) idx = keys.findIndex(k => !d.levelDone[k]);
        if (idx === -1) idx = n - 1;
        const cur = d.levels[keys[idx]];
        const frac = d.levelDone[keys[idx]] ? 1 : (cur.percent || 0) / 100;
        const t = Math.min(1, (idx + frac) / n);

        const x0 = 14, y0 = 200, x1 = 336, y1 = 52;
        const pt = u => [x0 + (x1 - x0) * u, y0 + (y1 - y0) * u];
        const me = pt(t), top = pt(1);
        const r1 = v => Math.round(v * 10) / 10;

        let lines = '', gates = '', labels = '';
        for (let i = 1; i < n; i++) {
            const g = pt(i / n), passed = i / n < t;
            lines += `<path d="M${r1(g[0])} ${r1(g[1])}V${y0}" stroke="${passed ? 'var(--bg)' : 'var(--muted)'}" stroke-width="1" opacity="${passed ? '.55' : '.45'}" fill="none"/>`;
            gates += d.levelDone[keys[i - 1]]
                ? `<circle cx="${r1(g[0])}" cy="${r1(g[1])}" r="5.5" fill="var(--success)"/>`
                : `<circle cx="${r1(g[0])}" cy="${r1(g[1])}" r="4.5" fill="var(--bg)" stroke="var(--muted)" stroke-width="1.5"/>`;
        }
        keys.forEach((k, i) => {
            const m = pt((i + 0.5) / n);
            const cls = d.levelDone[k] ? 'is-done' : i === idx ? 'is-now' : 'is-todo';
            labels += `<text x="${r1(m[0])}" y="${r1(m[1] - 16)}" text-anchor="middle" class="jr-mt-label ${cls}">${esc(k)}</text>`;
        });

        const svg = `
            <svg class="jr-mt" viewBox="0 0 360 236" role="img"
                aria-label="${esc(keys[idx])}, ${cur.done} of ${cur.total} lessons done, on the way from ${esc(keys[0])} to ${esc(keys[n - 1])}">
                <circle cx="262" cy="86" r="64" fill="var(--wash)"/>
                <path d="M${r1(me[0])} ${r1(me[1])}L${x1} ${y1}V${y0}H${r1(me[0])}z" fill="var(--wash)" opacity=".7"/>
                <path d="M${r1(me[0])} ${r1(me[1])}L${x1} ${y1}V${y0}" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 5"/>
                <path d="M${x0} ${y0}L${r1(me[0])} ${r1(me[1])}V${y0}z" fill="var(--primary)"/>
                ${lines}
                <path d="M8 ${y0}H352" stroke="var(--primary)" stroke-width="1.2" fill="none"/>
                <path d="M${r1(top[0])} ${r1(top[1])}V${r1(top[1] - 26)}" stroke="var(--muted)" stroke-width="1.2" fill="none"/>
                <rect x="${r1(top[0] - 5)}" y="${r1(top[1] - 36)}" width="10" height="10" fill="var(--bg)" stroke="var(--muted)" stroke-width="1.5"/>
                ${gates}${labels}
                <circle cx="${r1(me[0])}" cy="${r1(me[1])}" r="9.5" fill="var(--accent)" stroke="var(--bg)" stroke-width="2.5"/>
            </svg>`;

        return `
            <section class="jr-mountain">
                ${svg}
                <p class="jr-mt-sum">${esc(keys[idx])} · ${cur.done} of ${cur.total} ${plural(cur.total, 'lesson')} · ${d.lessonsComplete} of ${d.lessonsTotal} overall</p>
            </section>
        `;
    }

    function consistencyHtml(d) {
        const cells = [];
        const today = new Date();
        for (let i = 29; i >= 0; i--) {
            const day = new Date(today);
            day.setDate(day.getDate() - i);
            const key = day.toISOString().slice(0, 10);
            const active = (typeof isStreakDay === 'function') && isStreakDay(key);
            cells.push(`<i class="${active ? 'on' : ''}${i === 0 ? ' is-today' : ''}"></i>`);
        }
        const rank = (typeof getRank === 'function') ? getRank() : null;
        const side = ['Best ' + d.bestStreak + (d.bestStreak === 1 ? ' day' : ' days')]
            .concat(rank ? ['Rank ' + rank.rank] : []).join(' · ');
        const imported = (typeof getImportedStreak === 'function') ? getImportedStreak() : 0;
        return `
            <section class="jr-consistency">
                <div class="jr-cline">
                    <p class="jr-big">${d.streak}<span class="jr-of"> ${d.streak === 1 ? 'day' : 'days'} in a row</span></p>
                    <span class="jr-cside">${esc(side)}</span>
                </div>
                <div class="jr-dgrid" role="img" aria-label="${d.consistency.activeDays} active days of the last ${d.consistency.windowDays}">${cells.join('')}</div>
                <p class="jr-next">${d.consistency.activeDays} active of the last ${d.consistency.windowDays} days.
                    <button class="jr-link" data-jr-import-streak="1">${imported ? 'Update imported streak' : 'Import a streak'}</button></p>
            </section>
        `;
    }

    let _socialData = null;
    let _socialLoading = false;
    let _socialOffline = false;
    let _socialNotice = '';

    function _socialRowValue() {
        if (typeof Sync === 'undefined' || !Sync.isLoggedIn()) return '';
        const cached = _socialData || ((typeof Social !== 'undefined' && Social.readCache) ? Social.readCache() : null);
        if (!cached) return 'Optional';
        const pending = (cached.pendingFriendRequests || 0) + (cached.pendingQuestInvites || 0);
        if (pending > 0) return `${pending} waiting`;
        if (!cached.optedIn) return 'Optional';
        const count = (cached.friendsData && Array.isArray(cached.friendsData.friends)) ? cached.friendsData.friends.length : 0;
        if (cached.quests && cached.quests.currentQuest && cached.quests.currentQuest.status === 'active') {
            return 'Quest active';
        }
        return count > 0 ? `${count} ${plural(count, 'friend', 'friends')}` : 'Weekly board';
    }

    function _renderAvatar(name, isSelf) {
        const initials = (typeof Social !== 'undefined' && Social.initialsFor) ? Social.initialsFor(name) : 'L';
        return `<span class="soc-avatar${isSelf ? ' is-self' : ''}" aria-hidden="true">${esc(initials)}</span>`;
    }

    function _renderQuestSection(data) {
        const qData = data.quests || {};
        const q = qData.currentQuest;
        const friends = (data.friendsData && data.friendsData.friends) || [];
        const lastWeek = qData.lastWeekCompleted;

        let inner = '';
        if (q && q.status === 'pending') {
            if (q.isInviter) {
                inner = `<p class="soc-note">Invited <strong>${esc(q.partner.displayName)}</strong> to ${esc(q.label.toLowerCase())} (${q.target} ${esc(q.unit)}). Waiting for them to accept.</p>`;
            } else {
                inner = `
                    <p class="soc-note"><strong>${esc(q.partner.displayName)}</strong> invited you to a shared weekly quest: <strong>${esc(q.label)}</strong> (${q.target} ${esc(q.unit)}).</p>
                    <div class="soc-inline-actions">
                        <button class="dk-primary" type="button" data-soc-quest-respond="accept" data-quest-id="${esc(q.id)}">Accept quest</button>
                        <button class="dk-secondary" type="button" data-soc-quest-respond="decline" data-quest-id="${esc(q.id)}">Decline</button>
                    </div>
                `;
            }
        } else if (q && (q.status === 'active' || q.status === 'completed')) {
            const pct = Math.min(100, Math.round((q.totalProgress / Math.max(1, q.target)) * 100));
            const cheeredRecently = q.myLastCheerAt && (Date.now() - q.myLastCheerAt) < (20 * 60 * 60 * 1000);
            const partnerCheered = q.partnerLastCheerAt
                ? `<p class="soc-cheer-note">${esc(q.partner.displayName)} sent encouragement.</p>`
                : '';
            const statusTag = q.status === 'completed'
                ? '<span class="soc-status-done">Completed</span>'
                : `<span class="soc-status-week">${esc(q.weekKey)}</span>`;
            inner = `
                <div class="soc-quest-head">
                    <div class="soc-quest-title-wrap">
                        ${_renderAvatar(q.partner.displayName, false)}
                        <div>
                            <p class="soc-quest-title">${esc(q.label)}</p>
                            <p class="soc-quest-sub">With ${esc(q.partner.displayName)}</p>
                        </div>
                    </div>
                    ${statusTag}
                </div>
                <div class="soc-quest-meter">
                    <div class="jr-track"><div class="jr-fill${q.status === 'completed' ? ' is-done' : ''}" style="width:${pct}%"></div></div>
                    <p class="soc-quest-nums"><strong>${q.totalProgress} / ${q.target} ${esc(q.unit)}</strong> · You: ${q.myProgress} · ${esc(q.partner.displayName)}: ${q.partnerProgress}</p>
                </div>
                ${partnerCheered}
                <div class="soc-inline-actions">
                    <button class="dk-secondary" type="button" data-soc-quest-cheer="${esc(q.id)}"${cheeredRecently ? ' disabled' : ''}>${cheeredRecently ? 'Encouragement sent' : 'Send encouragement'}</button>
                </div>
            `;
        } else if (friends.length > 0) {
            const types = (qData.questTypes && qData.questTypes.length) ? qData.questTypes : [
                { type: 'lessons', label: 'Complete lessons together', target: 6, unit: 'lessons' },
                { type: 'stories', label: 'Read stories together', target: 4, unit: 'stories' },
                { type: 'active_days', label: 'Study days together', target: 8, unit: 'days' },
                { type: 'xp', label: 'Earn XP together', target: 350, unit: 'XP' }
            ];
            const typeOpts = types.map(t => `<option value="${esc(t.type)}">${esc(t.label)} (${t.target} ${esc(t.unit)})</option>`).join('');
            const friendOpts = friends.map(f => `<option value="${esc(f.userId)}">${esc(f.displayName)}</option>`).join('');
            inner = `
                <p class="soc-note">Share one calm goal with a friend from Monday to Sunday.</p>
                <div class="soc-form-stack">
                    <label class="soc-label" for="soc-quest-type">Weekly goal</label>
                    <select id="soc-quest-type" class="dk-editor-input">${typeOpts}</select>
                    <div class="soc-inline-actions">
                        <button class="dk-primary" type="button" data-soc-quest-automatch="1">Auto-match with a friend</button>
                    </div>
                    <div class="soc-divider"><span>or invite a specific friend</span></div>
                    <div class="soc-inline-row">
                        <select id="soc-quest-friend" class="dk-editor-input">${friendOpts}</select>
                        <button class="dk-secondary" type="button" data-soc-quest-start="1">Invite</button>
                    </div>
                </div>
            `;
        } else {
            inner = '<p class="soc-note">Add a friend below to start a shared weekly quest.</p>';
        }

        const lastWeekHtml = lastWeek
            ? `<p class="soc-footnote">Last week: completed "${esc(lastWeek.label)}" with ${esc(lastWeek.partner.displayName)}.</p>`
            : '';

        return card('Friend Quest', 'Shared weekly goal', inner + lastWeekHtml);
    }

    function _renderWeeklyBoardSection(data) {
        const board = data.leaderboard || { entries: [], dailyCap: 120, reviewDailyCap: 60 };
        const entries = board.entries || [];
        const weekLabel = board.weekKey || data.weekKey || 'This week';
        const capNote = `${weekLabel} · ${board.dailyCap || 120} XP daily cap (${board.reviewDailyCap || 60} review XP) so steady study beats grinding.`;

        if (!entries.length) {
            return card('Weekly board', capNote, '<p class="soc-note">Sync after your next lesson, story, or review to appear on this week\'s board.</p>');
        }

        const rows = entries.map(item => `
            <li class="soc-board-row${item.isSelf ? ' is-self' : ''}">
                <span class="soc-pos">${item.position}</span>
                ${_renderAvatar(item.displayName, item.isSelf)}
                <div class="soc-board-meta">
                    <span class="soc-board-name">${esc(item.displayName)}${item.isSelf ? ' <span class="soc-you-tag">you</span>' : ''}</span>
                    <span class="soc-board-sub">Rank ${item.rank} · ${item.activeDays}/7 days</span>
                </div>
                <span class="soc-board-xp">${item.weeklyXp} XP</span>
            </li>
        `).join('');

        return card('Weekly board', capNote, `<ol class="soc-board-list">${rows}</ol>`);
    }

    function _renderFriendsSection(data) {
        const prof = data.profile || {};
        const fData = data.friendsData || { friends: [], incoming: [], outgoing: [] };
        const friendCode = prof.friendCode || '';
        const pendingInvite = (typeof Social !== 'undefined' && Social.getPendingInvite) ? Social.getPendingInvite() : '';

        const inviteBanner = pendingInvite ? `
            <div class="soc-invite-banner">
                <p>Invite code ready: <strong>${esc(pendingInvite)}</strong></p>
                <div class="soc-inline-actions">
                    <button class="dk-primary" type="button" data-soc-send-pending="${esc(pendingInvite)}">Send friend request</button>
                    <button class="dk-secondary" type="button" data-soc-dismiss-pending="1">Dismiss</button>
                </div>
            </div>
        ` : '';

        const incomingHtml = fData.incoming.length ? `
            <div class="soc-subsection">
                <p class="soc-subhead">Waiting for your reply</p>
                <ul class="soc-list">
                    ${fData.incoming.map(req => `
                        <li class="soc-friend-row">
                            <div class="soc-board-meta">
                                <span class="soc-board-name">${esc(req.displayName)}</span>
                                <span class="soc-board-sub">${esc(req.friendCode)}</span>
                            </div>
                            <div class="soc-inline-actions">
                                <button class="dk-primary" type="button" data-soc-friend-respond="accept" data-user-id="${esc(req.userId)}">Accept</button>
                                <button class="dk-secondary" type="button" data-soc-friend-respond="decline" data-user-id="${esc(req.userId)}">Decline</button>
                            </div>
                        </li>
                    `).join('')}
                </ul>
            </div>
        ` : '';

        const outgoingHtml = fData.outgoing.length ? `
            <div class="soc-subsection">
                <p class="soc-subhead">Sent requests</p>
                <ul class="soc-list">
                    ${fData.outgoing.map(req => `
                        <li class="soc-friend-row">
                            <div class="soc-board-meta">
                                <span class="soc-board-name">${esc(req.displayName)}</span>
                                <span class="soc-board-sub">Pending</span>
                            </div>
                            <button class="jr-link" type="button" data-soc-friend-remove="${esc(req.userId)}">Cancel</button>
                        </li>
                    `).join('')}
                </ul>
            </div>
        ` : '';

        const friendsHtml = fData.friends.length ? `
            <div class="soc-subsection">
                <p class="soc-subhead">Friends (${fData.friends.length})</p>
                <ul class="soc-list">
                    ${fData.friends.map(f => `
                        <li class="soc-friend-row">
                            <div class="soc-friend-id">
                                ${_renderAvatar(f.displayName, false)}
                                <div class="soc-board-meta">
                                    <span class="soc-board-name">${esc(f.displayName)}</span>
                                    <span class="soc-board-sub">Rank ${f.rank} · ${f.weeklyXp} XP this week</span>
                                </div>
                            </div>
                            <button class="jr-link" type="button" data-soc-friend-remove="${esc(f.userId)}">Remove</button>
                        </li>
                    `).join('')}
                </ul>
            </div>
        ` : '<p class="soc-note">No friends connected yet. Share your code or invite link below.</p>';

        const body = `
            ${inviteBanner}
            <div class="soc-code-box">
                <div>
                    <span class="soc-label">Your friend code</span>
                    <p class="soc-code-val">${esc(friendCode)}</p>
                </div>
                <button class="dk-secondary" type="button" data-soc-copy-invite="${esc(friendCode)}">Copy invite link</button>
            </div>
            <div class="soc-inline-row">
                <input type="text" id="soc-friend-code-input" class="dk-editor-input" placeholder="PRL-XXXXX" maxlength="12" aria-label="Friend code">
                <button class="dk-secondary" type="button" data-soc-add-friend="1">Add friend</button>
            </div>
            ${incomingHtml}
            ${outgoingHtml}
            ${friendsHtml}
        `;
        return card('Friends', 'Private invite codes — emails are never shared', body);
    }

    function _renderSocialSettingsSection(data) {
        const prof = data.profile || {};
        const body = `
            <div class="soc-inline-row">
                <input type="text" id="soc-display-name-input" class="dk-editor-input"
                    value="${esc(prof.displayName || '')}" placeholder="Display name (2-24 chars)" maxlength="24" aria-label="Display name">
                <button class="dk-secondary" type="button" data-soc-save-name="1">Save name</button>
            </div>
            <p class="soc-footnote">Only your display name, Rank, and weekly study counts are visible to accepted friends. You can turn this off at any time without affecting your progress.</p>
            <div class="jr-account-footer">
                <button class="jr-account-logout" type="button" data-soc-opt-out="1">Turn off social</button>
            </div>
        `;
        return card('Social settings', 'Privacy and display name', body);
    }

    function socialHtml() {
        const loggedIn = (typeof Sync !== 'undefined') && Sync.isLoggedIn();
        if (!loggedIn) {
            const pendingInvite = (typeof Social !== 'undefined' && Social.getPendingInvite) ? Social.getPendingInvite() : '';
            const inviteHint = pendingInvite
                ? `<p class="soc-note">Sign in to accept invite code <strong>${esc(pendingInvite)}</strong>.</p>`
                : '';
            return card(
                'Friends and weekly board',
                'Sign in required',
                `${inviteHint}<p class="soc-note">Compare steady weekly study with friends and share calm weekly quests. Signing in is optional and your progress stays synced across devices.</p>
                 <div class="soc-inline-actions"><button class="dk-primary" type="button" data-soc-open-signin="1">Sign in</button></div>`
            );
        }

        const data = _socialData || ((typeof Social !== 'undefined' && Social.readCache) ? Social.readCache() : null);
        if (_socialLoading && !data) {
            return card('Friends and weekly board', 'Loading', '<p class="soc-note">Loading your friends and weekly board…</p>');
        }

        const noticeHtml = _socialNotice
            ? `<p class="soc-status-banner" role="status">${esc(_socialNotice)}</p>`
            : (_socialOffline ? '<p class="soc-status-banner" role="status">Offline — showing cached data.</p>' : '');

        if (!data || !data.optedIn) {
            const defaultName = (data && data.profile && data.profile.displayName)
                || ((typeof Sync !== 'undefined' && Sync.getUserName) ? Sync.getUserName() : '')
                || '';
            const pendingInvite = (typeof Social !== 'undefined' && Social.getPendingInvite) ? Social.getPendingInvite() : '';
            const inviteHint = pendingInvite
                ? `<p class="soc-note">You followed invite code <strong>${esc(pendingInvite)}</strong>. Enable your profile below to send the friend request.</p>`
                : '';
            return noticeHtml + card(
                'Friends and weekly board',
                'Optional · Friends only',
                `${inviteHint}
                 <p class="soc-note">Choose a display name to get a private friend code, compare weekly consistency (capped at 120 XP/day), and share weekly Friend Quests. Your email is never shown.</p>
                 <div class="soc-inline-row">
                     <input type="text" id="soc-optin-name-input" class="dk-editor-input"
                         value="${esc(defaultName)}" placeholder="Your display name" maxlength="24" aria-label="Display name">
                     <button class="dk-primary" type="button" data-soc-opt-in="1">Enable</button>
                 </div>`
            );
        }

        return noticeHtml
            + _renderQuestSection(data)
            + _renderWeeklyBoardSection(data)
            + _renderFriendsSection(data)
            + _renderSocialSettingsSection(data);
    }

    async function _refreshSocial(host) {
        if (typeof Sync === 'undefined' || !Sync.isLoggedIn() || typeof Social === 'undefined') return;
        _socialLoading = true;
        _socialOffline = false;
        const container = host.querySelector('#jr-social-root');
        if (container && !_socialData) container.innerHTML = socialHtml();
        try {
            _socialData = await Social.loadDashboard();
            _socialLoading = false;
            _socialOffline = false;
        } catch (err) {
            _socialLoading = false;
            _socialOffline = true;
            if (!_socialData) _socialData = Social.readCache();
        }
        const latest = host.querySelector('#jr-social-root');
        if (latest && _view === 'social') {
            latest.innerHTML = socialHtml();
        }
    }

    function rowsHtml(d) {
        const stats = d.candoStats || { verified: 0 };
        const skillsMeasured = SKILLS.filter(sk => (d.totalSkills[sk.from] || 0) > 0).length + (d.speakingProduction ? 1 : 0);
        const remaining = MILESTONES.filter(m => !m.test(d)).length;
        const row = (attrs, label, value, cls) => `
            <button class="jr-nav-row" type="button" ${attrs}>
                <span class="jr-nav-label">${label}</span>
                <span class="jr-nav-value${cls ? ' ' + cls : ''}">${value}</span>
                <span class="jr-nav-chev" aria-hidden="true"></span>
            </button>`;
        return `
            <div class="jr-nav-rows">
                ${row('data-jr-cando-open="1"', 'Can-Do Passport', `${stats.verified} verified`, 'is-good')}
                ${row('data-jr-view="knowledge"', 'Grammar and vocabulary', `${d.grammarDone} / ${d.grammarTotal}`)}
                ${row('data-jr-view="skills"', 'Skills', `${skillsMeasured} measured`)}
                ${row('data-jr-view="milestones"', 'Milestones', remaining ? `${remaining} to go` : 'All reached')}
                ${row('data-jr-view="social"', 'Friends and weekly board', _socialRowValue())}
                ${row('data-jr-view="account"', 'Account and appearance', (typeof Sync !== 'undefined' && Sync.isLoggedIn()) ? 'Signed in' : '')}
            </div>
        `;
    }

    function detailHtml(view, d) {
        const titles = {
            knowledge: 'Grammar and vocabulary',
            skills: 'Skills',
            milestones: 'Milestones',
            social: 'Friends and weekly board',
            account: 'Account and appearance'
        };
        const body = view === 'knowledge' ? curriculumBlock(d) + grammarBlock(d) + vocabularyBlock(d)
            : view === 'skills' ? skillsBlock(d) + xpBlock(d)
            : view === 'milestones' ? milestonesBlock(d)
            : view === 'social' ? `<div id="jr-social-root" class="soc-root">${socialHtml()}</div>`
            : accountBlock() + appearanceBlock();
        return `
            <div class="jr-detail">
                <button class="jr-back" type="button" data-jr-back="1">← Journey</button>
                <h2 class="jr-detail-title">${esc(titles[view] || '')}</h2>
                <div class="jr-grid">${body}</div>
            </div>
        `;
    }

    function _draw() {
        const host = document.getElementById('journey-root');
        if (!host) return;

        const d = collect();

        host.innerHTML = _view === 'main'
            ? `${consistencyHtml(d)}${mountainHtml(d)}${rowsHtml(d)}`
            : detailHtml(_view, d);
        _wireClicks(host);
        if (_view === 'account') _refreshAccountStatus(host);
        if (_view === 'social') _refreshSocial(host);

        if (typeof Guide !== 'undefined') {
            Guide.clearNote();
            const imported = (typeof getImportedStreak === 'function') ? getImportedStreak() : 0;
            if (_view === 'main' && !imported && (d.streak || 0) < 7) {
                Guide.note('journey-streak', host.querySelector('[data-jr-import-streak]'),
                    'If you\'re coming from another app, you can bring your streak with you.');
            }
        }

        if (_view === 'account' && typeof Sync !== 'undefined' && !Sync.isLoggedIn() && Sync.isGoogleAuthAvailable && Sync.isGoogleAuthAvailable()) {
            Sync.renderGoogleButton('jr-google-signin-btn', {
                onStart: () => {
                    const statusEl = host.querySelector('#jr-account-status');
                    if (statusEl) statusEl.textContent = 'Signing in with Google\u2026';
                },
                onSuccess: () => {
                    location.reload();
                },
                onError: (err) => {
                    const statusEl = host.querySelector('#jr-account-status');
                    if (statusEl) statusEl.textContent = err.message || 'Google sign-in failed.';
                }
            });
        }
    }

    if (typeof window !== 'undefined') {
        window.addEventListener('sync-session-expired', () => {
            _socialData = null;
            _draw();
        });
    }

    // Entering the tab always starts at the top of the page.
    function render() {
        _view = 'main';
        _socialNotice = '';
        _draw();
    }

    function openView(viewName) {
        _view = viewName || 'main';
        _socialNotice = '';
        _draw();
    }

    async function showCanDoPassportModal(initialLevel) {
        const existing = document.getElementById('cando-passport-overlay');
        if (existing) existing.remove();

        let activeLvl = initialLevel || 'All';
        const overlay = document.createElement('div');
        overlay.id = 'cando-passport-overlay';
        overlay.className = 'wp-overlay';

        let index = [];
        if (typeof LearnerModel !== 'undefined' && typeof LearnerModel.loadCompetenciesIndex === 'function') {
            index = await LearnerModel.loadCompetenciesIndex();
        }

        const store = (typeof LearnerModel !== 'undefined' && typeof LearnerModel.allCompetencies === 'function')
            ? LearnerModel.allCompetencies()
            : {};

        function renderContent() {
            const filtered = activeLvl === 'All'
                ? index
                : index.filter(c => (c.level || '').toUpperCase() === activeLvl.toUpperCase());

            // Group by level and unit
            const grouped = {};
            filtered.forEach(c => {
                const uKey = (c.level || 'A1') + ' · Unit ' + (c.unitLabel || '1') + ': ' + (c.unitTitle || 'General');
                if (!grouped[uKey]) grouped[uKey] = [];
                grouped[uKey].push(c);
            });

            const unitKeys = Object.keys(grouped);

            const levels = ['All', 'A1', 'A2', 'B1', 'B2'];
            const tabsHtml = levels.map(lvl => `
                <button type="button" class="sp-studio-tab ${activeLvl === lvl ? 'active' : ''}" data-cando-lvl="${lvl}">
                    ${lvl}
                </button>
            `).join('');

            const unitsHtml = unitKeys.length === 0
                ? '<p class="dk-empty" style="padding:24px 0;">No competencies loaded for this level.</p>'
                : unitKeys.map(uKey => {
                    const items = grouped[uKey];
                    const rowsHtml = items.map(item => {
                        const rec = store[item.text];
                        let badgeClass = 'cando-badge-upcoming';
                        let badgeText = 'Upcoming';
                        if (rec) {
                            if (rec.state === 'verified') {
                                const days = rec.verifiedAt ? (Date.now() - rec.verifiedAt) / (1000 * 3600 * 24) : 0;
                                if (days > 30) {
                                    badgeClass = 'cando-badge-review';
                                    badgeText = 'Needs Review';
                                } else {
                                    badgeClass = 'cando-badge-verified';
                                    badgeText = 'Verified';
                                }
                            } else if (rec.state === 'confidence-gap') {
                                badgeClass = 'cando-badge-gap';
                                badgeText = 'Confidence Gap';
                            } else {
                                badgeClass = 'cando-badge-review';
                                badgeText = 'Needs Practice';
                            }
                        }

                        return `
                            <li class="cando-row" data-cando-item="${esc(item.text)}" data-lesson-id="${esc(item.lessonId)}">
                                <div class="cando-row-main">
                                    <span class="cando-row-text">"${esc(item.text)}"</span>
                                    <span class="cando-row-meta">${esc(item.lessonTitle || item.lessonId)}</span>
                                </div>
                                <div class="cando-row-actions">
                                    <span class="cando-badge ${badgeClass}">${badgeText}</span>
                                    <button type="button" class="dk-secondary cando-btn" data-action-speaking="${esc(item.text)}" title="Practice in Speaking Practice">
                                        Speak
                                    </button>
                                    <button type="button" class="dk-secondary cando-btn" data-action-writing="${esc(item.text)}" title="Practice in Writing Practice">
                                        Write
                                    </button>
                                </div>
                            </li>
                        `;
                    }).join('');

                    return `
                        <div class="cando-unit-group">
                            <h4 class="cando-unit-title">${esc(uKey)}</h4>
                            <ul class="cando-list">${rowsHtml}</ul>
                        </div>
                    `;
                }).join('');

            overlay.innerHTML = `
                <div class="wp-sheet cando-portfolio-sheet">
                    <div class="wp-header">
                        <div>
                            <h2 class="sync-prompt-title">CEFR Can-Do Passport</h2>
                            <p class="sp-setup-sub" style="font-size:13px; margin:2px 0 0 0;">
                                What you can actually do in the language, checked against your speaking and writing.
                            </p>
                        </div>
                        <button class="wp-close" data-cando-modal-close="1" aria-label="Close">×</button>
                    </div>

                    <div class="sp-studio-nav" style="margin:16px 0 12px 0;">
                        ${tabsHtml}
                    </div>

                    <div class="cando-scroll-body">
                        ${unitsHtml}
                    </div>
                </div>
            `;

            // Wire tabs
            overlay.querySelectorAll('[data-cando-lvl]').forEach(btn => {
                btn.addEventListener('click', () => {
                    activeLvl = btn.getAttribute('data-cando-lvl');
                    renderContent();
                });
            });

            // Wire close
            overlay.querySelectorAll('[data-cando-modal-close]').forEach(btn => {
                btn.addEventListener('click', () => overlay.remove());
            });

            // Wire Speaking action
            overlay.querySelectorAll('[data-action-speaking]').forEach(btn => {
                btn.addEventListener('click', () => {
                    const text = btn.getAttribute('data-action-speaking');
                    overlay.remove();
                    showTab('drills', document.querySelector('.nav button[data-tab="drills"]'));
                    if (typeof Workshop !== 'undefined') {
                        Workshop.open('speaking', { targetCompetency: text });
                    }
                });
            });

            // Wire Writing action
            overlay.querySelectorAll('[data-action-writing]').forEach(btn => {
                btn.addEventListener('click', () => {
                    const text = btn.getAttribute('data-action-writing');
                    overlay.remove();
                    showTab('drills', document.querySelector('.nav button[data-tab="drills"]'));
                    if (typeof Workshop !== 'undefined') {
                        Workshop.open('writing', { targetCompetency: text });
                    }
                });
            });
        }

        renderContent();
        document.body.appendChild(overlay);
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
                <p class="jr-account-blurb">Switching from Duolingo or another app? Bring your day count over so you don't start back at zero.</p>
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
                    _draw();
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
                _draw();
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

    function showDeleteAccountModal(host) {
        const existing = document.getElementById('delete-account-overlay');
        if (existing) existing.remove();

        const overlay = document.createElement('div');
        overlay.id = 'delete-account-overlay';
        overlay.className = 'wp-overlay';
        overlay.innerHTML = `
            <div class="wp-sheet sync-prompt-sheet">
                <div class="wp-header">
                    <h2 class="sync-prompt-title">Delete cloud account</h2>
                    <button class="wp-close" data-delete-modal-close="1" aria-label="Close">×</button>
                </div>
                <p class="jr-account-blurb">This permanently deletes your email address, cloud progress snapshot, uploaded <em>My Texts</em> books, and login links from Parlour's servers. Progress already on this device stays in your browser until you clear site data.</p>
                <p class="jr-account-status" id="jr-delete-status"></p>
                <div class="jr-account-actions" style="justify-content:flex-end; margin-top:8px;">
                    <button type="button" class="dk-secondary" data-delete-modal-close="1">Cancel</button>
                    <button type="button" class="dk-secondary jr-delete-confirm-btn" id="jr-delete-confirm">Permanently delete account</button>
                </div>
            </div>
        `;

        document.body.appendChild(overlay);

        const statusEl = overlay.querySelector('#jr-delete-status');
        const confirmBtn = overlay.querySelector('#jr-delete-confirm');

        function close() {
            document.removeEventListener('keydown', onEsc);
            overlay.remove();
        }
        function onEsc(e) {
            if (e.key === 'Escape') close();
        }
        document.addEventListener('keydown', onEsc);

        overlay.querySelectorAll('[data-delete-modal-close]').forEach(btn => {
            btn.addEventListener('click', close);
        });
        overlay.addEventListener('click', e => {
            if (e.target === overlay) close();
        });

        confirmBtn.addEventListener('click', async () => {
            confirmBtn.disabled = true;
            if (statusEl) statusEl.textContent = 'Deleting account\u2026';
            try {
                await Sync.deleteAccount();
                close();
                _draw();
                const acctStatus = host.querySelector('#jr-account-status');
                if (acctStatus) acctStatus.textContent = 'Account and cloud data deleted.';
            } catch (error) {
                confirmBtn.disabled = false;
                if (statusEl) statusEl.textContent = error.message || 'Could not delete account.';
            }
        });
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
            const view = e.target.closest('[data-jr-view]');
            if (view) {
                if (typeof pushNavState === 'function') pushNavState('journey-detail');
                _view = view.getAttribute('data-jr-view');
                _draw();
                window.scrollTo(0, 0);
                return;
            }
            if (e.target.closest('[data-jr-back]')) { _view = 'main'; _draw(); window.scrollTo(0, 0); return; }

            const milestonesToggle = e.target.closest('[data-jr-milestones-toggle]');
            if (milestonesToggle) {
                const upcomingEl = document.getElementById('jr-milestones-upcoming');
                const allEl = document.getElementById('jr-milestones-all');
                const arrow = document.getElementById('jr-milestones-arrow');
                if (!allEl) return;
                const nowOpen = allEl.classList.toggle('hidden') === false;
                if (upcomingEl) upcomingEl.classList.toggle('hidden', nowOpen);
                milestonesToggle.setAttribute('aria-expanded', String(nowOpen));
                if (arrow) arrow.textContent = nowOpen ? '▼' : '▶';
                return;
            }

            if (e.target.closest('[data-jr-import-streak]')) {
                if (typeof Guide !== 'undefined') Guide.markSeen('journey-streak');
                showImportStreakModal();
                return;
            }

            if (e.target.closest('[data-jr-cando-open]')) {
                showCanDoPassportModal();
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
                _socialData = null;
                if (typeof Social !== 'undefined' && Social.clearCache) Social.clearCache();
                _draw();
                return;
            }

            if (e.target.closest('[data-sync-delete]')) {
                showDeleteAccountModal(host);
                return;
            }

            if (e.target.closest('[data-soc-open-signin]')) {
                if (typeof Sync !== 'undefined' && Sync.openSignInModal) Sync.openSignInModal();
                return;
            }

            const _setSocialNotice = (msg) => {
                _socialNotice = msg || '';
                const el = host.querySelector('#jr-social-root');
                if (el && _view === 'social') el.innerHTML = socialHtml();
            };

            if (e.target.closest('[data-soc-opt-in]')) {
                const input = host.querySelector('#soc-optin-name-input');
                const name = input ? input.value.trim() : '';
                if (!name || name.length < 2) {
                    _setSocialNotice('Enter a display name (2 to 24 characters).');
                    return;
                }
                _setSocialNotice('Enabling…');
                Social.saveProfile({ displayName: name, socialOptIn: true })
                    .then(() => { _socialNotice = 'Friends and weekly board enabled.'; return _refreshSocial(host); })
                    .catch(err => _setSocialNotice(err.message || 'Could not enable social profile.'));
                return;
            }

            if (e.target.closest('[data-soc-opt-out]')) {
                _setSocialNotice('Turning off…');
                Social.saveProfile({ socialOptIn: false })
                    .then(() => { _socialNotice = 'Social turned off. Your learning progress is unchanged.'; return _refreshSocial(host); })
                    .catch(err => _setSocialNotice(err.message || 'Could not update settings.'));
                return;
            }

            if (e.target.closest('[data-soc-save-name]')) {
                const input = host.querySelector('#soc-display-name-input');
                const name = input ? input.value.trim() : '';
                if (!name || name.length < 2) {
                    _setSocialNotice('Display name must be 2 to 24 characters.');
                    return;
                }
                _setSocialNotice('Saving…');
                Social.saveProfile({ displayName: name })
                    .then(() => { _socialNotice = 'Display name updated.'; return _refreshSocial(host); })
                    .catch(err => _setSocialNotice(err.message || 'Could not update display name.'));
                return;
            }

            const copyBtn = e.target.closest('[data-soc-copy-invite]');
            if (copyBtn) {
                const code = copyBtn.getAttribute('data-soc-copy-invite');
                const url = (typeof Social !== 'undefined' && Social.inviteUrlFor) ? Social.inviteUrlFor(code) : code;
                if (navigator.clipboard && navigator.clipboard.writeText) {
                    navigator.clipboard.writeText(url)
                        .then(() => _setSocialNotice('Invite link copied to clipboard.'))
                        .catch(() => _setSocialNotice('Share this link: ' + url));
                } else {
                    _setSocialNotice('Share this link: ' + url);
                }
                return;
            }

            if (e.target.closest('[data-soc-dismiss-pending]')) {
                if (typeof Social !== 'undefined' && Social.clearPendingInvite) Social.clearPendingInvite();
                _setSocialNotice('');
                return;
            }

            const sendPendingBtn = e.target.closest('[data-soc-send-pending]');
            if (sendPendingBtn) {
                const code = sendPendingBtn.getAttribute('data-soc-send-pending');
                _setSocialNotice('Sending request…');
                Social.requestFriend(code)
                    .then(res => {
                        Social.clearPendingInvite();
                        _socialNotice = res.status === 'accepted'
                            ? `You and ${res.displayName} are now friends.`
                            : `Friend request sent to ${res.displayName}.`;
                        return _refreshSocial(host);
                    })
                    .catch(err => _setSocialNotice(err.message || 'Could not send friend request.'));
                return;
            }

            if (e.target.closest('[data-soc-add-friend]')) {
                const input = host.querySelector('#soc-friend-code-input');
                const code = input ? input.value.trim().toUpperCase() : '';
                if (!code) {
                    _setSocialNotice('Enter a friend code first.');
                    return;
                }
                _setSocialNotice('Sending request…');
                Social.requestFriend(code)
                    .then(res => {
                        _socialNotice = res.status === 'accepted'
                            ? `You and ${res.displayName} are now friends.`
                            : `Friend request sent to ${res.displayName}.`;
                        return _refreshSocial(host);
                    })
                    .catch(err => _setSocialNotice(err.message || 'Could not send friend request.'));
                return;
            }

            const friendRespBtn = e.target.closest('[data-soc-friend-respond]');
            if (friendRespBtn) {
                const action = friendRespBtn.getAttribute('data-soc-friend-respond');
                const uid = friendRespBtn.getAttribute('data-user-id');
                _setSocialNotice('Updating…');
                Social.respondFriend(uid, action)
                    .then(() => { _socialNotice = action === 'accept' ? 'Friend request accepted.' : 'Request updated.'; return _refreshSocial(host); })
                    .catch(err => _setSocialNotice(err.message || 'Could not update request.'));
                return;
            }

            const friendRemBtn = e.target.closest('[data-soc-friend-remove]');
            if (friendRemBtn) {
                const uid = friendRemBtn.getAttribute('data-soc-friend-remove');
                _setSocialNotice('Updating…');
                Social.removeFriend(uid)
                    .then(() => { _socialNotice = 'Removed.'; return _refreshSocial(host); })
                    .catch(err => _setSocialNotice(err.message || 'Could not remove friend.'));
                return;
            }

            if (e.target.closest('[data-soc-quest-automatch]')) {
                const typeSel = host.querySelector('#soc-quest-type');
                const questType = typeSel ? typeSel.value : 'lessons';
                _setSocialNotice('Matching with an active friend…');
                Social.autoMatchQuest(questType)
                    .then(res => {
                        _socialNotice = res.matched && res.quest
                            ? `Quest started with ${res.quest.partner.displayName}.`
                            : (res.message || 'No friends are free for a quest this week yet.');
                        return _refreshSocial(host);
                    })
                    .catch(err => _setSocialNotice(err.message || 'Could not auto-match quest.'));
                return;
            }

            if (e.target.closest('[data-soc-quest-start]')) {
                const typeSel = host.querySelector('#soc-quest-type');
                const friendSel = host.querySelector('#soc-quest-friend');
                const questType = typeSel ? typeSel.value : 'lessons';
                const friendId = friendSel ? friendSel.value : '';
                _setSocialNotice('Sending quest invite…');
                Social.startQuest(friendId, questType)
                    .then(res => {
                        _socialNotice = res.quest
                            ? `Quest invite sent to ${res.quest.partner.displayName}.`
                            : 'Quest invite sent.';
                        return _refreshSocial(host);
                    })
                    .catch(err => _setSocialNotice(err.message || 'Could not start quest.'));
                return;
            }

            const questRespBtn = e.target.closest('[data-soc-quest-respond]');
            if (questRespBtn) {
                const action = questRespBtn.getAttribute('data-soc-quest-respond');
                const questId = questRespBtn.getAttribute('data-quest-id');
                _setSocialNotice('Updating quest…');
                Social.respondQuest(questId, action)
                    .then(() => { _socialNotice = action === 'accept' ? 'Quest accepted.' : 'Quest declined.'; return _refreshSocial(host); })
                    .catch(err => _setSocialNotice(err.message || 'Could not respond to quest.'));
                return;
            }

            const cheerBtn = e.target.closest('[data-soc-quest-cheer]');
            if (cheerBtn) {
                const questId = cheerBtn.getAttribute('data-soc-quest-cheer');
                Social.sendCheer(questId)
                    .then(() => { _socialNotice = 'Encouragement sent.'; return _refreshSocial(host); })
                    .catch(err => _setSocialNotice(err.message || 'Could not send encouragement.'));
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
    return { render, openView, collect, MILESTONES };
})();
