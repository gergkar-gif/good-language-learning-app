// ============================================
// LEVEL TEST
// ============================================
// The check at the end of a level: twenty gapped sentences, answered from a
// dropdown, marked all at once.
//
// Marked at the end rather than question by question, because that is the
// difference between a test and a drill. Told after each answer, a learner
// corrects course and the score stops measuring what they knew walking in.
//
// The result is not just a number. Wrong answers are grouped by what each
// question tested, so the screen can say which topics to go back to — a bare
// "14/20" tells a learner they failed without telling them what to do about
// it.
//
// Advisory, not a gate. It records that a level was passed and says so; it
// does not lock the next level. Blocking content someone wants to study is a
// product decision nobody has made, and there is no A2 content to block yet.

const LevelTest = (function () {
    'use strict';

    let test = null;        // the loaded test
    let answers = {};       // question id -> chosen option text
    let order = {};         // question id -> shuffled options, fixed per sitting
    let marked = false;

    // A learner who scores this high on a level's test knows the level, not
    // just enough of it to be waved through — high enough above the 80%
    // pass mark that a lucky guess or two on a 20+ question test can't
    // cross it. Distinct from (and always at or above) passMark: the test
    // content files don't carry this value because it isn't a property of
    // the test, it's a product decision about how sure the app needs to be
    // before it assumes a whole level's worth of lessons was already
    // learned elsewhere.
    const JUMP_AHEAD_MARK = 0.9;

    function resultsKey() {
        return Lang.key('testResults');
    }

    function allResults() {
        try {
            return JSON.parse(localStorage.getItem(resultsKey()) || '{}');
        } catch (error) {
            return {};
        }
    }

    function resultFor(level) {
        return allResults()[level] || null;
    }

    function saveResult(level, result) {
        const all = allResults();
        // Keep the best attempt: a learner who passes and then tries again out
        // of curiosity should not lose the pass.
        const previous = all[level];
        if (!previous || result.score > previous.score) {
            all[level] = result;
            localStorage.setItem(resultsKey(), JSON.stringify(all));
        }
    }

    async function load(level) {
        const file = level.toLowerCase() + '-test.json';
        try {
            const res = await fetch(Lang.content('tests/' + file));
            test = res.ok ? await res.json() : null;
        } catch (error) {
            console.warn('LevelTest: no test for', level, error);
            test = null;
        }
        return test;
    }

    // Options are shuffled here rather than scattered through the content
    // file. Written out, every correct answer sits first, which keeps the file
    // reviewable at a glance; if that order reached the learner they would
    // learn the position rather than the language.
    function shuffle(list) {
        const out = list.slice();
        for (let i = out.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [out[i], out[j]] = [out[j], out[i]];
        }
        return out;
    }

    function esc(value) {
        return (typeof UI !== 'undefined' && UI.escape)
            ? UI.escape(value) : String(value == null ? '' : value);
    }

    // ----------------------------------------
    // MARKING
    // ----------------------------------------
    function mark() {
        const wrongBy = {};
        let correct = 0;

        test.questions.forEach(q => {
            const chosen = answers[q.id];
            const right = q.options[q.correct];
            if (chosen === right) {
                correct++;
            } else {
                (q.teaches || []).forEach(topic => {
                    wrongBy[topic] = (wrongBy[topic] || 0) + 1;
                });
            }
        });

        const score = correct / test.questions.length;
        const jumpAhead = score >= JUMP_AHEAD_MARK;
        const result = {
            level: test.level,
            correct: correct,
            total: test.questions.length,
            score: score,
            passed: score >= test.passMark,
            jumpAhead: jumpAhead,
            weakest: Object.keys(wrongBy).sort((a, b) => wrongBy[b] - wrongBy[a]),
            takenAt: new Date().toISOString()
        };

        // A score this high means the level's actual content was already
        // known walking in — credit the whole level, not just the test, so
        // the rest of the app (Continue, My Journey, the level's own
        // progress bar) treats it as done rather than showing every one of
        // its lessons as still to do. See markLevelComplete()'s own
        // comment on why this carries no XP. Computed before saveResult()
        // below, not after — this field needs to be part of `result` before
        // it gets JSON-stringified into localStorage, or the persisted copy
        // would never carry it (found via bug sweep, 2026-09-02).
        if (jumpAhead && typeof markLevelComplete === 'function') {
            result.newlyCompletedLessons = markLevelComplete(test.level).length;
        }

        saveResult(test.level, result);
        return result;
    }

    // ----------------------------------------
    // RENDER
    // ----------------------------------------
    function questionHtml(q, index) {
        if (!order[q.id]) order[q.id] = shuffle(q.options);
        const chosen = answers[q.id];
        const right = q.options[q.correct];

        const select = `
            <select class="lt-select" data-q="${esc(q.id)}" ${marked ? 'disabled' : ''}>
                <option value=""${chosen ? '' : ' selected'}>—</option>
                ${order[q.id].map(option => `
                    <option value="${esc(option)}"${chosen === option ? ' selected' : ''}>${esc(option)}</option>
                `).join('')}
            </select>
        `;

        const parts = q.sentence.split(/_{3,}/);
        const sentence = esc(parts[0]) + select + esc(parts[1] || '');

        let state = '';
        if (marked) {
            state = chosen === right
                ? '<span class="lt-mark lt-right">✓</span>'
                : `<span class="lt-mark lt-wrong">✗ ${esc(right)}</span>`;
        }

        return `
            <li class="lt-question${marked ? (chosen === right ? ' is-right' : ' is-wrong') : ''}">
                <span class="lt-num">${index + 1}</span>
                <span class="lt-sentence">${sentence}${state}</span>
            </li>
        `;
    }

    function resultHtml(result) {
        const percent = Math.round(result.score * 100);
        const next = { A1: 'A2', A2: 'B1', B1: 'B2', B2: 'C1' }[result.level];

        const verdict = result.jumpAhead
            ? `<p class="lt-verdict is-pass">${percent}% — that's ${
                 result.level} known. Every lesson in the level is now
                 marked complete, so you can move straight on to ${
                 next || 'what comes next'}.</p>`
            : result.passed
            ? `<p class="lt-verdict is-pass">${percent}% — you are ready for
                 ${next || 'what comes next'}.</p>`
            : `<p class="lt-verdict is-fail">${percent}% — not quite. ${
                 Math.round(test.passMark * 100)}% is the mark for moving on.</p>`;

        // Naming the topics is the point of the screen. A score alone tells
        // someone they failed without telling them what to do about it.
        const topics = result.weakest.length
            ? `<p class="lt-topics">Worth going back to:
                 ${result.weakest.slice(0, 5).map(esc).join(' · ')}</p>`
            : '<p class="lt-topics">Nothing missed.</p>';

        return `
            <div class="lt-result">
                <p class="lt-score">${result.correct}<span class="lt-of"> / ${result.total}</span></p>
                ${verdict}
                ${topics}
                <button class="dk-secondary" data-retake="1">Take it again</button>
            </div>
        `;
    }

    async function render(level) {
        const host = document.getElementById('leveltest-root');
        if (!host) return;

        if (!test || test.level !== level) {
            answers = {}; order = {}; marked = false;
            await load(level);
        }
        if (!test) {
            host.innerHTML = '<p class="dk-empty">No test for this level yet.</p>';
            return;
        }

        const answered = Object.keys(answers).filter(k => answers[k]).length;
        const previous = resultFor(level);

        host.innerHTML = `
            <button class="dk-back" data-close-test="1">← Back to lessons</button>
            <div class="lt-head">
                <h2>${esc(test.title)}</h2>
                <p>${esc(test.intro)}</p>
                ${previous && !marked ? `<p class="lt-previous">Your best so far:
                    ${previous.correct}/${previous.total}${previous.passed ? ' — passed' : ''}.</p>` : ''}
            </div>
            ${marked ? resultHtml(mark.lastResult) : ''}
            <ol class="lt-questions">
                ${test.questions.map(questionHtml).join('')}
            </ol>
            ${marked ? '' : `
                <div class="lt-actions">
                    <button class="btn-primary" data-check="1" ${answered === test.questions.length ? '' : 'disabled'}>
                        ${answered === test.questions.length
                            ? 'Check answers'
                            : `Answer all ${test.questions.length} (${answered} done)`}
                    </button>
                </div>
            `}
        `;

        host.querySelectorAll('.lt-select').forEach(sel => {
            sel.onchange = function () {
                answers[sel.dataset.q] = sel.value;
                render(level);
            };
        });
        const check = host.querySelector('[data-check]');
        if (check) check.onclick = function () {
            mark.lastResult = mark();
            marked = true;
            render(level);
            host.scrollIntoView({ block: 'start' });
        };
        const retake = host.querySelector('[data-retake]');
        if (retake) retake.onclick = function () {
            answers = {}; order = {}; marked = false;
            render(level);
        };
        const back = host.querySelector('[data-close-test]');
        if (back) back.onclick = function () {
            showTab('learn', document.querySelector('[data-tab="learn"]'));
        };
    }

    function open(level) {
        document.querySelectorAll('.tab').forEach(tab => tab.classList.add('hidden'));
        document.getElementById('leveltest').classList.remove('hidden');
        if (typeof PageHeader !== 'undefined') PageHeader.render({
            title: level + ' level test',
            subtitle: 'Twenty questions. Eighty per cent to move on.',
            illustration: 'ascent'
        });
        render(level);
    }

    return { open, render, resultFor };
})();
