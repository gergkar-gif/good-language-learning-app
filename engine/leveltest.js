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
    let answers = {};       // question id -> chosen option text or typed input
    let order = {};         // question id -> shuffled options, fixed per sitting
    let readingAnswers = {}; // reading question id -> chosen option text or index string
    let readingOrder = {};  // reading question id -> shuffled options (reading-mc, gapped-text only)
    let listeningAnswers = {}; // listening question id -> chosen option text or index string
    let listeningOrder = {};   // listening question id -> shuffled options
    let listeningPass = 0;     // number of passes completed (0, 1, 2)
    let listeningPlaying = false; // audio currently playing flag
    let listeningIntermission = false; // inter-pass pause countdown active
    let listeningCountdown = 0; // seconds left in countdown
    let listeningTimer = null; // countdown interval handle
    let listeningTurnIdx = 0;  // active turn being spoken
    let listeningTranscriptShown = false; // review mode transcript reveal toggle
    let writingText = '';   // Part writing text
    let speakingTranscript = ''; // Part speaking transcript or typed text
    let speakingAudioUrl = null; // Part 3 audio recording blob url
    let isRecording = false; // Part 3 microphone recording flag
    let mediaRecorder = null;
    let audioChunks = [];
    let activeStream = null;
    let recognition = null;
    let marked = false;
    let diagnosticDismissed = false;
    let exitCallback = null;
    let openingTab = 'learn';

    function hasTest(level) {
        if (!level || typeof level !== 'string') return false;
        const norm = level.toUpperCase();
        if (typeof Lang !== 'undefined' && typeof Lang.profile === 'function') {
            const p = Lang.profile();
            if (p && Array.isArray(p.tests)) {
                return p.tests.includes(norm);
            }
        }
        if (norm === 'A1' || norm === 'A2') return true;
        const lang = (typeof Lang !== 'undefined' && typeof Lang.current === 'function')
            ? Lang.current()
            : ((typeof Lang !== 'undefined' && typeof Lang.code === 'function') ? Lang.code() : 'es');
        if (norm === 'B1') {
            return lang === 'hu' || lang === 'es-latam' || lang === 'es-es';
        }
        if (norm === 'B2') {
            return lang === 'es-latam';
        }
        if (norm === 'C1') {
            return lang === 'hu';
        }
        return false;
    }

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

    function countWords(str) {
        if (!str || typeof str !== 'string') return 0;
        const m = str.match(/[\p{L}\p{N}]+(?:['-][\p{L}\p{N}]+)*/gu);
        return m ? m.length : 0;
    }

    function hasKeyword(text, kw) {
        if (!text || !kw) return false;
        const normText = text.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
        const normKw = kw.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
        return normText.includes(normKw);
    }

    // ----------------------------------------
    // MARKING
    // ----------------------------------------
    function mark() {
        const wrongBy = {};
        let part1Correct = 0;

        test.questions.forEach(q => {
            const chosen = (answers[q.id] || '').trim();
            let isRight = false;

            if (q.type === 'text-input') {
                const cleanChosen = chosen.toLowerCase();
                const accepted = [q.answer, ...(q.altAnswers || [])].map(a => a.trim().toLowerCase());
                isRight = accepted.includes(cleanChosen);
            } else {
                const right = q.options[q.correct];
                isRight = chosen === right;
            }

            if (isRight) {
                part1Correct++;
            } else {
                (q.teaches || []).forEach(topic => {
                    wrongBy[topic] = (wrongBy[topic] || 0) + 1;
                });
            }
        });

        // Writing evaluation (up to 3 points)
        let writingScore = 0;
        let writingMax = 0;
        let writingBreakdown = null;
        if (test.writingTask) {
            writingMax = 3;
            const wWords = countWords(writingText);
            const reqWords = test.writingTask.minWords || 20;
            const matchedKw = (test.writingTask.targetKeywords || []).filter(kw => hasKeyword(writingText, kw));

            const lenPts = wWords >= reqWords ? 1 : (wWords >= reqWords * 0.6 ? 0.5 : 0);
            const kwPts = matchedKw.length >= 2 ? 1 : (matchedKw.length >= 1 ? 0.5 : 0);
            const structPts = (wWords >= 10 && /[.!?¿¡]/.test(writingText)) ? 1 : (wWords >= 6 ? 0.5 : 0);
            writingScore = Math.min(3, lenPts + kwPts + structPts);
            writingBreakdown = {
                words: wWords,
                requiredWords: reqWords,
                matchedKeywords: matchedKw,
                score: writingScore,
                max: writingMax
            };
        }

        // Speaking evaluation (up to 3 points)
        let speakingScore = 0;
        let speakingMax = 0;
        let speakingBreakdown = null;
        if (test.speakingTask) {
            speakingMax = 3;
            const sWords = countWords(speakingTranscript);
            const hasAudio = !!speakingAudioUrl;
            const matchedKw = (test.speakingTask.targetKeywords || []).filter(kw => hasKeyword(speakingTranscript, kw));

            const subPts = (hasAudio || sWords >= 8) ? 1 : 0;
            const kwPts = matchedKw.length >= 1 ? 1 : 0.5;
            const prodPts = (sWords >= 15 || (hasAudio && sWords >= 6)) ? 1 : 0.5;
            speakingScore = Math.min(3, subPts + kwPts + prodPts);
            speakingBreakdown = {
                words: sWords,
                hasAudio: hasAudio,
                matchedKeywords: matchedKw,
                score: speakingScore,
                max: speakingMax
            };
        }

        // Reading comprehension section scoring
        let readingCorrect = 0;
        let readingMax = 0;
        let readingBreakdown = null;
        if (test.readingSection) {
            readingMax = test.readingSection.questions.length;
            test.readingSection.questions.forEach(q => {
                const chosen = readingAnswers[q.id];
                let isRight = false;
                if (q.type === 'true-false-not-stated') {
                    // stored as string "0"/"1"/"2"
                    isRight = chosen === String(q.correct);
                } else {
                    // reading-mc and gapped-text: stored as the option text
                    isRight = chosen === q.options[q.correct];
                }
                if (isRight) readingCorrect++;
            });
            readingBreakdown = { correct: readingCorrect, total: readingMax };

            // Persist best reading score per level (for learner model / future UI)
            try {
                const rsKey = (typeof Lang !== 'undefined' && Lang.key)
                    ? Lang.key('readingScores') : 'readingScores';
                const allRS = JSON.parse(localStorage.getItem(rsKey) || '{}');
                const prevRS = allRS[test.level];
                const pct = readingCorrect / readingMax;
                const prevPct = prevRS ? prevRS.correct / prevRS.total : -1;
                if (pct > prevPct) {
                    allRS[test.level] = {
                        correct: readingCorrect,
                        total: readingMax,
                        takenAt: new Date().toISOString()
                    };
                    localStorage.setItem(rsKey, JSON.stringify(allRS));
                }
            } catch (e) {}
        }

        // Listening comprehension section scoring
        let listeningCorrect = 0;
        let listeningMax = 0;
        let listeningBreakdown = null;
        if (test.listeningSection) {
            listeningMax = test.listeningSection.questions.length;
            test.listeningSection.questions.forEach(q => {
                const chosen = listeningAnswers[q.id];
                let isRight = false;
                if (q.type === 'true-false-not-stated') {
                    isRight = chosen === String(q.correct);
                } else {
                    isRight = chosen === q.options[q.correct];
                }
                if (isRight) listeningCorrect++;
            });
            listeningBreakdown = { correct: listeningCorrect, total: listeningMax };

            try {
                const lsKey = (typeof Lang !== 'undefined' && Lang.key)
                    ? Lang.key('listeningScores') : 'listeningScores';
                const allLS = JSON.parse(localStorage.getItem(lsKey) || '{}');
                const prevLS = allLS[test.level];
                const pct = listeningCorrect / listeningMax;
                const prevPct = prevLS ? prevLS.correct / prevLS.total : -1;
                if (pct > prevPct) {
                    allLS[test.level] = {
                        correct: listeningCorrect,
                        total: listeningMax,
                        takenAt: new Date().toISOString()
                    };
                    localStorage.setItem(lsKey, JSON.stringify(allLS));
                }
            } catch (e) {}
        }

        const totalEarned = part1Correct + readingCorrect + listeningCorrect + writingScore + speakingScore;
        const totalPossible = test.questions.length + readingMax + listeningMax + writingMax + speakingMax;
        const score = totalEarned / totalPossible;
        const jumpAhead = score >= JUMP_AHEAD_MARK;

        const result = {
            level: test.level,
            correct: totalEarned,
            total: totalPossible,
            score: score,
            passed: score >= test.passMark,
            jumpAhead: jumpAhead,
            part1: {
                correct: part1Correct,
                total: test.questions.length
            },
            reading: readingBreakdown,
            listening: listeningBreakdown,
            writing: writingBreakdown,
            speaking: speakingBreakdown,
            weakest: Object.keys(wrongBy).sort((a, b) => wrongBy[b] - wrongBy[a]),
            takenAt: new Date().toISOString(),
            // Lets LearnerModel.troubleSkills() tell whether a flagged
            // skill has been answered right since (recycle cards count in
            // app opens, not dates).
            takenAtOpen: (typeof AppOpens !== 'undefined') ? AppOpens.current() : null
        };

        if (jumpAhead && typeof markLevelComplete === 'function') {
            result.newlyCompletedLessons = markLevelComplete(test.level).length;
        }

        saveResult(test.level, result);
        return result;
    }

    // ----------------------------------------
    // RENDER HELPERS
    // ----------------------------------------
    function questionHtml(q, index) {
        if (!order[q.id] && q.options) order[q.id] = shuffle(q.options);
        const chosen = (answers[q.id] || '').trim();

        if (q.type === 'text-input') {
            const cleanChosen = chosen.toLowerCase();
            const accepted = [q.answer, ...(q.altAnswers || [])].map(a => a.trim().toLowerCase());
            const isRight = accepted.includes(cleanChosen);

            const input = `
                <input type="text" class="lt-input" data-q="${esc(q.id)}" value="${esc(answers[q.id] || '')}"
                       placeholder="…" ${marked ? 'disabled' : ''} autocomplete="off" spellcheck="false" />
            `;
            const parts = q.sentence.split(/_{3,}/);
            const sentence = esc(parts[0]) + input + esc(parts[1] || '');

            let state = '';
            if (marked) {
                state = isRight
                    ? '<span class="lt-mark lt-right">✓</span>'
                    : `<span class="lt-mark lt-wrong">✗ ${esc(q.answer)}</span>`;
            }

            return `
                <li class="lt-question lt-q-text${marked ? (isRight ? ' is-right' : ' is-wrong') : ''}">
                    <span class="lt-num">${index + 1}</span>
                    <span class="lt-sentence">${sentence}${state}</span>
                </li>
            `;
        }

        if (q.type === 'choice') {
            const right = q.options[q.correct];
            const isRight = chosen === right;

            let state = '';
            if (marked) {
                state = isRight
                    ? '<span class="lt-mark lt-right">✓</span>'
                    : `<span class="lt-mark lt-wrong">✗ ${esc(right)}</span>`;
            }

            return `
                <li class="lt-question lt-q-choice${marked ? (isRight ? ' is-right' : ' is-wrong') : ''}">
                    <span class="lt-num">${index + 1}</span>
                    <div class="lt-choice-body">
                        ${q.context ? `<p class="lt-choice-context"><em>${esc(q.context)}</em></p>` : ''}
                        <p class="lt-choice-prompt">${esc(q.prompt || q.sentence || '')}${state}</p>
                        <div class="lt-options">
                            ${(order[q.id] || q.options).map(opt => `
                                <button type="button" class="lt-opt-btn ${chosen === opt ? 'is-selected' : ''} ${marked ? (opt === right ? 'is-correct-opt' : (chosen === opt ? 'is-wrong-opt' : '')) : ''}"
                                        data-q="${esc(q.id)}" data-opt="${esc(opt)}" ${marked ? 'disabled' : ''}>
                                    ${esc(opt)}
                                </button>
                            `).join('')}
                        </div>
                    </div>
                </li>
            `;
        }

        // Default: dropdown cloze
        const right = q.options[q.correct];
        const isRight = chosen === right;

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
            state = isRight
                ? '<span class="lt-mark lt-right">✓</span>'
                : `<span class="lt-mark lt-wrong">✗ ${esc(right)}</span>`;
        }

        return `
            <li class="lt-question lt-q-select${marked ? (isRight ? ' is-right' : ' is-wrong') : ''}">
                <span class="lt-num">${index + 1}</span>
                <span class="lt-sentence">${sentence}${state}</span>
            </li>
        `;
    }

    // ----------------------------------------
    // READING QUESTION RENDERER
    // Used by readingSectionHtml(). Separate from questionHtml() so reading
    // state (readingAnswers / readingOrder) stays isolated from Part 1.
    // ----------------------------------------
    function readingQuestionHtml(q, index) {
        const chosen = readingAnswers[q.id];

        if (q.type === 'true-false-not-stated') {
            // Fixed option order — True / False / Not stated. Never shuffled.
            // Labels are in the target language (CEFR exam convention).
            const lang = (typeof Lang !== 'undefined' && typeof Lang.current === 'function')
                ? Lang.current() : 'es';
            const labels = lang === 'hu'
                ? ['Igaz', 'Hamis', 'A szöveg nem tartalmaz ilyen információt']
                : ['Verdadero', 'Falso', 'No se menciona en el texto'];
            const right = String(q.correct);
            const isRight = chosen === right;

            let state = '';
            if (marked) {
                state = isRight
                    ? '<span class="lt-mark lt-right">✓</span>'
                    : `<span class="lt-mark lt-wrong">✗ ${esc(labels[q.correct])}</span>`;
            }

            return `
                <li class="lt-question lt-q-tfns${marked ? (isRight ? ' is-right' : ' is-wrong') : ''}">
                    <span class="lt-num">${index + 1}</span>
                    <div class="lt-choice-body">
                        <p class="lt-choice-prompt">${esc(q.statement)}${state}</p>
                        <div class="lt-options">
                            ${labels.map((label, i) => `
                                <button type="button" class="lt-opt-btn ${chosen === String(i) ? 'is-selected' : ''} ${marked ? (String(i) === right ? 'is-correct-opt' : (chosen === String(i) ? 'is-wrong-opt' : '')) : ''}"
                                        data-rq="${esc(q.id)}" data-ropt="${i}" ${marked ? 'disabled' : ''}>
                                    ${esc(label)}
                                </button>
                            `).join('')}
                        </div>
                    </div>
                </li>
            `;
        }

        if (q.type === 'gapped-text') {
            if (!readingOrder[q.id]) readingOrder[q.id] = shuffle(q.options);
            const right = q.options[q.correct];
            const isRight = chosen === right;

            // Render textWithGap: highlight [___] as a visible placeholder
            const gapHtml = esc(q.textWithGap).replace(
                /\[___\]/g,
                '<span class="lt-gap-marker">[___]</span>'
            );

            let state = '';
            if (marked) {
                state = isRight
                    ? '<span class="lt-mark lt-right">✓</span>'
                    : `<span class="lt-mark lt-wrong">✗ ${esc(right)}</span>`;
            }

            return `
                <li class="lt-question lt-q-gap${marked ? (isRight ? ' is-right' : ' is-wrong') : ''}">
                    <span class="lt-num">${index + 1}</span>
                    <div class="lt-choice-body">
                        <p class="lt-gap-context">${gapHtml}${state}</p>
                        <div class="lt-options">
                            ${readingOrder[q.id].map(opt => `
                                <button type="button" class="lt-opt-btn ${chosen === opt ? 'is-selected' : ''} ${marked ? (opt === right ? 'is-correct-opt' : (chosen === opt ? 'is-wrong-opt' : '')) : ''}"
                                        data-rq="${esc(q.id)}" data-ropt="${esc(opt)}" ${marked ? 'disabled' : ''}>
                                    ${esc(opt)}
                                </button>
                            `).join('')}
                        </div>
                    </div>
                </li>
            `;
        }

        // Default: reading-mc — standard multiple choice, options shuffled
        if (!readingOrder[q.id]) readingOrder[q.id] = shuffle(q.options);
        const right = q.options[q.correct];
        const isRight = chosen === right;

        let state = '';
        if (marked) {
            state = isRight
                ? '<span class="lt-mark lt-right">✓</span>'
                : `<span class="lt-mark lt-wrong">✗ ${esc(right)}</span>`;
        }

        return `
            <li class="lt-question lt-q-rmc${marked ? (isRight ? ' is-right' : ' is-wrong') : ''}">
                <span class="lt-num">${index + 1}</span>
                <div class="lt-choice-body">
                    <p class="lt-choice-prompt">${esc(q.question)}${state}</p>
                    <div class="lt-options">
                        ${readingOrder[q.id].map(opt => `
                            <button type="button" class="lt-opt-btn ${chosen === opt ? 'is-selected' : ''} ${marked ? (opt === right ? 'is-correct-opt' : (chosen === opt ? 'is-wrong-opt' : '')) : ''}"
                                    data-rq="${esc(q.id)}" data-ropt="${esc(opt)}" ${marked ? 'disabled' : ''}>
                                ${esc(opt)}
                            </button>
                        `).join('')}
                    </div>
                </div>
            </li>
        `;
    }

    // ----------------------------------------
    // READING SECTION HTML
    // Renders the full "Part 2: Reading Comprehension" block.
    // Part 1 question count is passed so question numbering is sequential.
    // ----------------------------------------
    // ----------------------------------------
    // READING SECTION HTML
    // Renders the full Reading Comprehension block.
    // ----------------------------------------
    function readingSectionHtml(part1Count, partNum) {
        if (!test.readingSection) return '';
        const rs = test.readingSection;

        return `
            <div class="lt-section lt-section-reading">
                <h3 class="lt-section-title">Part ${partNum || 2}: Reading Comprehension</h3>
                <div class="lt-task-card">
                    <div class="lt-task-head">
                        <h4>${esc(rs.title)}</h4>
                    </div>
                    <div class="lt-passage">
                        ${esc(rs.passage).replace(/\n/g, '<br>')}
                    </div>
                    ${rs.source ? `<p class="lt-passage-source">${esc(rs.source)}</p>` : ''}
                    <ol class="lt-questions lt-reading-questions">
                        ${rs.questions.map((q, i) => readingQuestionHtml(q, part1Count + i)).join('')}
                    </ol>
                </div>
            </div>
        `;
    }

    // ----------------------------------------
    // LISTENING SECTION AUDIO & CONTROLS
    // ----------------------------------------
    function stopListeningAudio() {
        listeningPlaying = false;
        if (listeningTimer) {
            clearInterval(listeningTimer);
            listeningTimer = null;
        }
        listeningIntermission = false;
        if (typeof ParlourTTS !== 'undefined' && ParlourTTS.stop) {
            ParlourTTS.stop();
        }
    }

    function playListeningPass(passNum) {
        if (!test || !test.listeningSection) return;
        const ls = test.listeningSection;
        const turns = ls.audio && ls.audio.turns ? ls.audio.turns : [];
        if (turns.length === 0) return;

        stopListeningAudio();
        listeningPlaying = true;
        listeningTurnIdx = 0;
        updateListeningConsole();

        const lang = (typeof Lang !== 'undefined' && typeof Lang.current === 'function')
            ? Lang.current()
            : ((typeof Lang !== 'undefined' && typeof Lang.code === 'function') ? Lang.code() : 'es');

        if (typeof ParlourTTS !== 'undefined' && ParlourTTS.preload) {
            turns.forEach(t => {
                ParlourTTS.preload({
                    text: t.text,
                    gender: t.gender || 'male',
                    language: lang
                });
            });
        }

        function playTurn() {
            if (!listeningPlaying) return;
            if (listeningTurnIdx >= turns.length) {
                finishListeningPass(passNum);
                return;
            }

            const current = turns[listeningTurnIdx];
            updateListeningConsole();

            if (typeof ParlourTTS !== 'undefined' && ParlourTTS.speak) {
                ParlourTTS.speak({
                    text: current.text,
                    gender: current.gender || 'male',
                    language: lang,
                    onEnded: () => {
                        if (!listeningPlaying) return;
                        listeningTurnIdx++;
                        setTimeout(playTurn, 450);
                    }
                });
            } else {
                listeningPlaying = false;
                updateListeningConsole();
            }
        }

        playTurn();
    }

    function finishListeningPass(passNum) {
        listeningPlaying = false;
        listeningPass = Math.max(listeningPass, passNum);

        if (listeningPass === 1 && !marked) {
            listeningIntermission = true;
            listeningCountdown = 15;
            updateListeningConsole();

            if (listeningTimer) clearInterval(listeningTimer);
            listeningTimer = setInterval(() => {
                listeningCountdown--;
                if (listeningCountdown <= 0) {
                    clearInterval(listeningTimer);
                    listeningTimer = null;
                    listeningIntermission = false;
                    playListeningPass(2);
                } else {
                    updateListeningConsole();
                }
            }, 1000);
        } else {
            listeningIntermission = false;
            updateListeningConsole();
        }
    }

    function listeningConsoleContentHtml(ls) {
        const turns = ls.audio && ls.audio.turns ? ls.audio.turns : [];
        let statusLabel = '';
        let statusDetail = '';
        let controls = '';

        if (marked) {
            statusLabel = 'Listening Assessment Completed';
            statusDetail = 'Review your score and check audio evidence below.';
            controls = `
                <button type="button" class="btn-secondary lt-audio-btn-sm" data-lis-start="1">
                    ↻ Replay Audio
                </button>
            `;
        } else if (listeningPlaying) {
            const currentSpeaker = (turns[listeningTurnIdx] && turns[listeningTurnIdx].speaker) ? turns[listeningTurnIdx].speaker : 'Speaker';
            statusLabel = `Playing Pass ${listeningPass + 1} of 2…`;
            statusDetail = `Speaking: ${esc(currentSpeaker)} (turn ${listeningTurnIdx + 1} of ${turns.length})`;
            controls = `
                <button type="button" class="lt-audio-btn lt-audio-btn-stop" data-lis-stop="1">
                    ⏹ Stop Audio
                </button>
            `;
        } else if (listeningIntermission) {
            statusLabel = 'Pass 1 complete. Paused before Pass 2';
            statusDetail = `Pass 2 begins automatically in ${listeningCountdown}s — review questions now.`;
            controls = `
                <button type="button" class="btn-primary lt-audio-btn" data-lis-start="2">
                    ▶ Start Pass 2 Now (${listeningCountdown}s)
                </button>
                <button type="button" class="btn-secondary lt-audio-btn-sm" data-lis-stop="1">
                    ⏹ Cancel Pause
                </button>
            `;
        } else if (listeningPass >= 2) {
            statusLabel = 'Audio complete (2 of 2 passes played)';
            statusDetail = 'Answer the comprehension questions below.';
            controls = `
                <span class="lt-audio-badge-done">✓ 2 passes played</span>
                <button type="button" class="btn-secondary lt-audio-btn-sm" data-lis-start="1">
                    ↻ Replay (Extra)
                </button>
            `;
        } else if (listeningPass === 1) {
            statusLabel = 'Pass 1 of 2 finished';
            statusDetail = 'Ready to begin second playback.';
            controls = `
                <button type="button" class="btn-primary lt-audio-btn" data-lis-start="2">
                    ▶ Play Pass 2 of 2
                </button>
            `;
        } else {
            statusLabel = 'CEFR 2-Pass Audio Protocol';
            statusDetail = `${turns.length} dialogue turns · You will hear this recording twice with a pause in between.`;
            controls = `
                <button type="button" class="btn-primary lt-audio-btn" data-lis-start="1">
                    ▶ Start Listening (Pass 1 of 2)
                </button>
            `;
        }

        const audioIconHtml = (typeof Art !== 'undefined' && Art.icon)
            ? Art.icon('listening')
            : '<svg class="art icon" viewBox="0 0 24 24" role="presentation" aria-hidden="true" focusable="false"><line class="ink-line" x1="4" y1="10" x2="4" y2="14"/><line class="ink-line" x1="8" y1="7" x2="8" y2="17"/><line class="ink-line" x1="12" y1="4" x2="12" y2="20"/><line class="ink-line" x1="16" y1="8" x2="16" y2="16"/><line class="ink-line" x1="20" y1="11" x2="20" y2="13"/></svg>';

        return `
            <div class="lt-audio-console-top">
                <span class="lt-audio-icon ${listeningPlaying ? 'is-playing' : ''}">${audioIconHtml}</span>
                <div class="lt-audio-status-wrap">
                    <span class="lt-audio-status-label">${statusLabel}</span>
                    <span class="lt-audio-status-detail">${statusDetail}</span>
                </div>
            </div>
            <div class="lt-audio-controls">
                ${controls}
            </div>
        `;
    }

    function updateListeningConsole() {
        const host = document.getElementById('leveltest-root');
        if (!host || !test || !test.listeningSection) return;
        const consoleEl = host.querySelector('.lt-audio-console');
        if (!consoleEl) return;
        consoleEl.innerHTML = listeningConsoleContentHtml(test.listeningSection);
        bindListeningConsoleButtons(consoleEl);
    }

    function bindListeningConsoleButtons(consoleEl) {
        if (!consoleEl) return;
        const startBtns = consoleEl.querySelectorAll('[data-lis-start]');
        startBtns.forEach(btn => {
            btn.onclick = function () {
                const pass = parseInt(btn.getAttribute('data-lis-start') || '1', 10);
                playListeningPass(pass);
            };
        });
        const stopBtn = consoleEl.querySelector('[data-lis-stop]');
        if (stopBtn) {
            stopBtn.onclick = function () {
                stopListeningAudio();
                updateListeningConsole();
            };
        }
    }

    function listeningQuestionHtml(q, index) {
        if (q.type === 'true-false-not-stated') {
            const labels = ['Verdadero', 'Falso', 'No se menciona'];
            const chosen = listeningAnswers[q.id];
            const right = String(q.correct);
            const isRight = chosen === right;

            let state = '';
            if (marked) {
                state = isRight
                    ? '<span class="lt-mark lt-right">✓</span>'
                    : `<span class="lt-mark lt-wrong">✗ ${esc(labels[q.correct])}</span>`;
            }

            return `
                <li class="lt-question lt-q-tfns${marked ? (isRight ? ' is-right' : ' is-wrong') : ''}">
                    <span class="lt-num">${index + 1}</span>
                    <div class="lt-choice-body">
                        <p class="lt-choice-prompt">${esc(q.statement)}${state}</p>
                        <div class="lt-options">
                            ${labels.map((label, i) => `
                                <button type="button" class="lt-opt-btn ${chosen === String(i) ? 'is-selected' : ''} ${marked ? (String(i) === right ? 'is-correct-opt' : (chosen === String(i) ? 'is-wrong-opt' : '')) : ''}"
                                        data-lq="${esc(q.id)}" data-lopt="${i}" ${marked ? 'disabled' : ''}>
                                    ${esc(label)}
                                </button>
                            `).join('')}
                        </div>
                        ${marked && (q.evidence || q.explanation) ? `
                            <div class="lt-evidence-box">
                                ${q.evidence ? `<p class="lt-evidence-quote"><strong>Evidence:</strong> "${esc(q.evidence)}"</p>` : ''}
                                ${q.explanation ? `<p class="lt-evidence-expl">${esc(q.explanation)}</p>` : ''}
                            </div>
                        ` : ''}
                    </div>
                </li>
            `;
        }

        if (!listeningOrder[q.id]) listeningOrder[q.id] = shuffle(q.options);
        const chosen = listeningAnswers[q.id];
        const right = q.options[q.correct];
        const isRight = chosen === right;

        let state = '';
        if (marked) {
            state = isRight
                ? '<span class="lt-mark lt-right">✓</span>'
                : `<span class="lt-mark lt-wrong">✗ ${esc(right)}</span>`;
        }

        return `
            <li class="lt-question lt-q-lmc${marked ? (isRight ? ' is-right' : ' is-wrong') : ''}">
                <span class="lt-num">${index + 1}</span>
                <div class="lt-choice-body">
                    <p class="lt-choice-prompt">${esc(q.question)}${state}</p>
                    <div class="lt-options">
                        ${listeningOrder[q.id].map(opt => `
                            <button type="button" class="lt-opt-btn ${chosen === opt ? 'is-selected' : ''} ${marked ? (opt === right ? 'is-correct-opt' : (chosen === opt ? 'is-wrong-opt' : '')) : ''}"
                                    data-lq="${esc(q.id)}" data-lopt="${esc(opt)}" ${marked ? 'disabled' : ''}>
                                ${esc(opt)}
                            </button>
                        `).join('')}
                    </div>
                    ${marked && (q.evidence || q.explanation) ? `
                        <div class="lt-evidence-box">
                            ${q.evidence ? `<p class="lt-evidence-quote"><strong>Evidence:</strong> "${esc(q.evidence)}"</p>` : ''}
                            ${q.explanation ? `<p class="lt-evidence-expl">${esc(q.explanation)}</p>` : ''}
                        </div>
                    ` : ''}
                </div>
            </li>
        `;
    }

    function listeningSectionHtml(partOffset, partNum) {
        if (!test.listeningSection) return '';
        const ls = test.listeningSection;

        return `
            <div class="lt-section lt-section-listening">
                <h3 class="lt-section-title">Part ${partNum}: Listening Comprehension</h3>
                <div class="lt-task-card">
                    <div class="lt-task-head">
                        <h4>${esc(ls.title)}</h4>
                        <span class="lt-task-badge">CEFR 2-pass protocol</span>
                    </div>
                    ${ls.context ? `<p class="lt-task-context"><em>${esc(ls.context)}</em></p>` : ''}
                    
                    <div class="lt-audio-console">
                        ${listeningConsoleContentHtml(ls)}
                    </div>

                    ${marked ? `
                        <div class="lt-transcript-toggle-bar">
                            <button type="button" class="lt-transcript-toggle-btn" data-lis-transcript-toggle="1">
                                ${listeningTranscriptShown ? '▲ Hide Audio Transcript' : '▼ View Audio Transcript'}
                            </button>
                        </div>
                        ${listeningTranscriptShown ? `
                            <div class="lt-transcript-card">
                                <h5 class="lt-transcript-title">Audio Transcript</h5>
                                <div class="lt-transcript-dialogue">
                                    ${(ls.audio && ls.audio.turns ? ls.audio.turns : []).map(t => `
                                        <div class="lt-turn">
                                            <span class="lt-turn-speaker">${esc(t.speaker || 'Speaker')}:</span>
                                            <span class="lt-turn-text">${esc(t.text)}</span>
                                        </div>
                                    `).join('')}
                                </div>
                            </div>
                        ` : ''}
                    ` : ''}

                    <ol class="lt-questions lt-listening-questions">
                        ${ls.questions.map((q, i) => listeningQuestionHtml(q, partOffset + i)).join('')}
                    </ol>
                    ${ls.source ? `<p class="lt-passage-source">${esc(ls.source)}</p>` : ''}
                </div>
            </div>
        `;
    }

    function writingSectionHtml(partNum) {
        if (!test.writingTask) return '';
        const t = test.writingTask;
        const wCount = countWords(writingText);
        const isValid = wCount >= t.minWords;

        return `
            <div class="lt-section lt-section-writing">
                <h3 class="lt-section-title">Part ${partNum || 3}: Short Written Production</h3>
                <div class="lt-task-card">
                    <div class="lt-task-head">
                        <h4>${esc(t.title)}</h4>
                        <span class="lt-task-badge">Target: min. ${t.minWords} words</span>
                    </div>
                    <p class="lt-task-prompt">${esc(t.prompt)}</p>
                    ${t.context ? `<p class="lt-task-context"><em>${esc(t.context)}</em></p>` : ''}
                    <div class="lt-keywords">
                        <span class="lt-keywords-label">Target structures to incorporate:</span>
                        <div class="lt-chips">
                            ${(t.targetKeywords || []).map(kw => `
                                <span class="lt-chip ${hasKeyword(writingText, kw) ? 'matched' : ''}">
                                    ${hasKeyword(writingText, kw) ? '✓ ' : ''}${esc(kw)}
                                </span>
                            `).join('')}
                        </div>
                    </div>
                    <textarea class="lt-textarea" data-writing="1" placeholder="Write your response here…" ${marked ? 'disabled' : ''}>${esc(writingText)}</textarea>
                    <div class="lt-task-footer">
                        <span class="lt-word-counter ${isValid ? 'is-valid' : ''}" data-writing-counter="1">
                            ${wCount} / ${t.minWords} words ${isValid ? '✓' : ''}
                        </span>
                    </div>
                </div>
            </div>
        `;
    }

    function speakingSectionHtml(partNum) {
        if (!test.speakingTask) return '';
        const t = test.speakingTask;

        return `
            <div class="lt-section lt-section-speaking">
                <h3 class="lt-section-title">Part ${partNum || 4}: Short Spoken Production</h3>
                <div class="lt-task-card">
                    <div class="lt-task-head">
                        <h4>${esc(t.title)}</h4>
                        <span class="lt-task-badge">Target: min. ${t.minSeconds || 15}s speech</span>
                    </div>
                    <p class="lt-task-prompt">${esc(t.prompt)}</p>
                    <div class="lt-keywords">
                        <span class="lt-keywords-label">Target oral expressions:</span>
                        <div class="lt-chips">
                            ${(t.targetKeywords || []).map(kw => `
                                <span class="lt-chip ${hasKeyword(speakingTranscript, kw) ? 'matched' : ''}">
                                    ${hasKeyword(speakingTranscript, kw) ? '✓ ' : ''}${esc(kw)}
                                </span>
                            `).join('')}
                        </div>
                    </div>
                    <div class="lt-speaking-controls">
                        <button type="button" class="lt-mic-btn ${isRecording ? 'recording' : ''}" data-mic="1" ${marked ? 'disabled' : ''}>
                            ${isRecording ? '⏹ Stop Recording' : (speakingTranscript ? '🎤 Record Again' : '🎤 Record Response')}
                        </button>
                        ${speakingAudioUrl ? `<audio class="lt-audio-playback" controls src="${speakingAudioUrl}"></audio>` : ''}
                    </div>
                    <div class="lt-transcript-wrapper">
                        <label class="lt-transcript-label">Spoken Response (dictated via mic or typed):</label>
                        <textarea class="lt-textarea lt-transcript-input" data-speaking="1" placeholder="Your speech will appear here automatically, or you may type if microphone is unavailable…" ${marked ? 'disabled' : ''}>${esc(speakingTranscript)}</textarea>
                    </div>
                </div>
            </div>
        `;
    }

    function resultHtml(result) {
        const percent = Math.round(result.score * 100);
        const next = { A1: 'A2', A2: 'B1', B1: 'B2', B2: 'C1' }[result.level];

        const verdict = result.jumpAhead
            ? `<p class="lt-verdict is-pass">${percent}% — that's ${result.level} mastered! Every lesson in the level is now marked complete, so you can move straight on to ${next || 'what comes next'}.</p>`
            : result.passed
            ? `<p class="lt-verdict is-pass">${percent}% — you have passed the ${result.level} assessment and are ready for ${next || 'what comes next'}.</p>`
            : `<p class="lt-verdict is-fail">${percent}% — not quite. ${Math.round(test.passMark * 100)}% is the mark for moving on.</p>`;

        const topics = result.weakest.length
            ? `<p class="lt-topics">Topics to revisit: ${result.weakest.slice(0, 5).map(esc).join(' · ')}</p>`
            : '<p class="lt-topics">All grammar and vocabulary checks mastered.</p>';

        return `
            <div class="lt-result">
                <p class="lt-score">${Math.round(result.correct * 10) / 10}<span class="lt-of"> / ${result.total} (${percent}%)</span></p>
                ${verdict}
                <div class="lt-result-breakdown">
                    <div class="lt-breakdown-row">
                        <span class="lt-breakdown-label">Part 1: Language in Context</span>
                        <span class="lt-breakdown-val">${result.part1.correct} / ${result.part1.total}</span>
                    </div>
                    ${result.reading ? `
                        <div class="lt-breakdown-row">
                            <span class="lt-breakdown-label">Part 2: Reading Comprehension</span>
                            <span class="lt-breakdown-val">${result.reading.correct} / ${result.reading.total}</span>
                        </div>
                    ` : ''}
                    ${result.listening ? `
                        <div class="lt-breakdown-row">
                            <span class="lt-breakdown-label">Part ${result.reading ? '3' : '2'}: Listening Comprehension</span>
                            <span class="lt-breakdown-val">${result.listening.correct} / ${result.listening.total}</span>
                        </div>
                    ` : ''}
                    ${result.writing ? `
                        <div class="lt-breakdown-row">
                            <span class="lt-breakdown-label">Part ${1 + (result.reading ? 1 : 0) + (result.listening ? 1 : 0) + 1}: Written Production</span>
                            <span class="lt-breakdown-val">${result.writing.score} / ${result.writing.max} (${result.writing.words} words, ${result.writing.matchedKeywords.length} targets)</span>
                        </div>
                    ` : ''}
                    ${result.speaking ? `
                        <div class="lt-breakdown-row">
                            <span class="lt-breakdown-label">Part ${1 + (result.reading ? 1 : 0) + (result.listening ? 1 : 0) + (result.writing ? 1 : 0) + 1}: Spoken Production</span>
                            <span class="lt-breakdown-val">${result.speaking.score} / ${result.speaking.max} (${result.speaking.hasAudio ? 'audio recorded' : 'transcript'}, ${result.speaking.matchedKeywords.length} targets)</span>
                        </div>
                    ` : ''}
                </div>
                ${topics}
                <button class="dk-secondary" data-retake="1">Take assessment again</button>
            </div>
        `;
    }

    async function render(level) {
        const host = document.getElementById('leveltest-root');
        if (!host) return;

        if (!test || test.level !== level) {
            answers = {}; order = {}; readingAnswers = {}; readingOrder = {}; marked = false;
            listeningAnswers = {}; listeningOrder = {}; listeningPass = 0; listeningPlaying = false;
            listeningIntermission = false; listeningTranscriptShown = false;
            stopListeningAudio();
            await load(level);
        }
        if (!test) {
            host.innerHTML = `
                <button class="dk-back" data-close-test="1">← Back</button>
                <p class="dk-empty">No test for this level yet.</p>
            `;
            const backBtn = host.querySelector('[data-close-test]');
            if (backBtn) backBtn.onclick = function () {
                closeTest();
            };
            return;
        }

        const answered = Object.keys(answers).filter(k => answers[k]).length;
        const previous = resultFor(level);

        // Pre-test readiness diagnostic
        if (!diagnosticDismissed && !marked && typeof LearnerModel !== 'undefined' && typeof LearnerModel.unverifiedCompetencies === 'function') {
            let stats = null;
            let unverified = [];
            try {
                stats = await LearnerModel.competencyStats(level);
                unverified = await LearnerModel.unverifiedCompetencies(level);
            } catch (e) {}

            if (unverified.length > 0 && stats && stats.total > 0) {
                host.innerHTML = `
                    <button class="dk-back" data-close-test="1">← Back to lessons</button>
                    <div class="lt-readiness-card">
                        <div class="lt-readiness-head">
                            <span class="sp-level-pill">${esc(level)} Diagnostic</span>
                            <h2 class="lt-readiness-title">${esc(level)} Readiness Check</h2>
                            <p class="lt-readiness-sub">
                                <strong>${stats.verified}</strong> of <strong>${stats.total}</strong> syllabus competencies verified (${stats.percent}%).
                            </p>
                        </div>
                        <div class="lt-readiness-body">
                            <p class="lt-readiness-alert">
                                You have <strong>${unverified.length}</strong> unchecked or developing ${unverified.length === 1 ? 'goal' : 'goals'} in ${esc(level)}:
                            </p>
                            <ul class="lt-readiness-list">
                                ${unverified.slice(0, 6).map(c => `
                                    <li class="lt-readiness-item">
                                        <div class="lt-readiness-item-main">
                                            <span class="lt-readiness-unit">${esc(c.unitTitle || ('Unit ' + c.unitLabel))}</span>
                                            <span class="lt-readiness-text">"${esc(c.text)}"</span>
                                        </div>
                                        <span class="cando-badge ${c.state === 'confidence-gap' ? 'cando-badge-gap' : 'cando-badge-review'}">
                                            ${c.state === 'confidence-gap' ? 'Confidence Gap' : 'Needs Practice'}
                                        </span>
                                    </li>
                                `).join('')}
                                ${unverified.length > 6 ? `<li class="lt-readiness-more">+${unverified.length - 6} more unverified competencies</li>` : ''}
                            </ul>
                        </div>
                        <div class="lt-readiness-actions">
                            <button type="button" class="vbtn vbtn-secondary lt-action-btn" data-lt-review-goals="1">
                                Review in Can-Do Passport →
                            </button>
                            <button type="button" class="vbtn vbtn-primary lt-action-btn" data-lt-proceed-test="1">
                                Proceed to Test →
                            </button>
                        </div>
                    </div>
                `;

                const proceedBtn = host.querySelector('[data-lt-proceed-test]');
                if (proceedBtn) {
                    proceedBtn.addEventListener('click', () => {
                        diagnosticDismissed = true;
                        render(level);
                    });
                }

                const reviewBtn = host.querySelector('[data-lt-review-goals]');
                if (reviewBtn) {
                    reviewBtn.addEventListener('click', () => {
                        showTab('journey', document.querySelector('.nav button[data-tab="journey"]'));
                    });
                }

                const backBtn = host.querySelector('[data-close-test]');
                if (backBtn) {
                    backBtn.addEventListener('click', closeTest);
                }

                return;
            }
        }

        const readingTotal = test.readingSection ? test.readingSection.questions.length : 0;
        const readingAnswered = test.readingSection
            ? test.readingSection.questions.filter(q => readingAnswers[q.id] !== undefined).length
            : 0;

        const listeningTotal = test.listeningSection ? test.listeningSection.questions.length : 0;
        const listeningAnswered = test.listeningSection
            ? test.listeningSection.questions.filter(q => listeningAnswers[q.id] !== undefined).length
            : 0;

        const isReady = answered === test.questions.length &&
            readingAnswered === readingTotal &&
            listeningAnswered === listeningTotal &&
            (!test.writingTask || countWords(writingText) >= 5) &&
            (!test.speakingTask || speakingTranscript.trim().length > 0 || speakingAudioUrl);

        const totalItems = test.questions.length + readingTotal + listeningTotal;
        const totalAnswered = answered + readingAnswered + listeningAnswered;

        let partCounter = 1;
        const part1Num = partCounter++;
        const readingPartNum = test.readingSection ? partCounter++ : null;
        const listeningPartNum = test.listeningSection ? partCounter++ : null;
        const writingPartNum = test.writingTask ? partCounter++ : null;
        const speakingPartNum = test.speakingTask ? partCounter++ : null;

        host.innerHTML = `
            <button class="dk-back" data-close-test="1">← Back to lessons</button>
            <div class="lt-head">
                <h2>${esc(test.title)}</h2>
                <p>${esc(test.intro)}</p>
                ${previous && !marked ? `<p class="lt-previous">Your best so far:
                    ${Math.round(previous.score * 100)}% (${previous.passed ? 'passed' : 'needs practice'}).</p>` : ''}
            </div>
            ${marked ? resultHtml(mark.lastResult) : ''}
            
            <div class="lt-section lt-section-context">
                <h3 class="lt-section-title">Part ${part1Num}: Language in Context</h3>
                <ol class="lt-questions">
                    ${test.questions.map(questionHtml).join('')}
                </ol>
            </div>

            ${readingSectionHtml(test.questions.length, readingPartNum)}
            ${listeningSectionHtml(test.questions.length + readingTotal, listeningPartNum)}

            ${writingSectionHtml(writingPartNum)}
            ${speakingSectionHtml(speakingPartNum)}

            ${marked ? '' : `
                <div class="lt-actions">
                    <button class="btn-primary" data-check="1" ${isReady ? '' : 'disabled'}>
                        ${isReady
                            ? 'Check &amp; Grade Assessment'
                            : `Complete all items to check (${totalAnswered}/${totalItems} answered)`}
                    </button>
                </div>
            `}
        `;

        // Bind dropdowns
        host.querySelectorAll('.lt-select').forEach(sel => {
            sel.onchange = function () {
                answers[sel.dataset.q] = sel.value;
                updateCheckButton();
            };
        });

        // Bind text-inputs
        host.querySelectorAll('.lt-input').forEach(inp => {
            inp.oninput = function () {
                answers[inp.dataset.q] = inp.value;
                updateCheckButton();
            };
        });

        // Bind option buttons
        host.querySelectorAll('.lt-opt-btn').forEach(btn => {
            btn.onclick = function () {
                if (marked) return;
                const qId = btn.dataset.q;
                answers[qId] = btn.dataset.opt;
                const parent = btn.closest('.lt-options');
                if (parent) {
                    parent.querySelectorAll('.lt-opt-btn').forEach(b => b.classList.remove('is-selected'));
                    btn.classList.add('is-selected');
                }
                updateCheckButton();
            };
        });

        // Bind writing textarea
        const writingArea = host.querySelector('[data-writing]');
        if (writingArea) {
            writingArea.oninput = function () {
                writingText = writingArea.value;
                const counter = host.querySelector('[data-writing-counter]');
                const wCount = countWords(writingText);
                const minWords = test.writingTask ? test.writingTask.minWords : 20;
                if (counter) {
                    counter.innerHTML = `${wCount} / ${minWords} words ${wCount >= minWords ? '✓' : ''}`;
                    if (wCount >= minWords) counter.classList.add('is-valid');
                    else counter.classList.remove('is-valid');
                }
                if (test.writingTask) {
                    host.querySelectorAll('.lt-section-writing .lt-chip').forEach((chip, i) => {
                        const kw = test.writingTask.targetKeywords[i];
                        if (kw && hasKeyword(writingText, kw)) {
                            chip.classList.add('matched');
                            if (!chip.textContent.startsWith('✓')) chip.textContent = '✓ ' + kw;
                        } else if (kw) {
                            chip.classList.remove('matched');
                            chip.textContent = kw;
                        }
                    });
                }
                updateCheckButton();
            };
        }

        // Bind speaking textarea
        const speakingArea = host.querySelector('[data-speaking]');
        if (speakingArea) {
            speakingArea.oninput = function () {
                speakingTranscript = speakingArea.value;
                if (test.speakingTask) {
                    host.querySelectorAll('.lt-section-speaking .lt-chip').forEach((chip, i) => {
                        const kw = test.speakingTask.targetKeywords[i];
                        if (kw && hasKeyword(speakingTranscript, kw)) {
                            chip.classList.add('matched');
                            if (!chip.textContent.startsWith('✓')) chip.textContent = '✓ ' + kw;
                        } else if (kw) {
                            chip.classList.remove('matched');
                            chip.textContent = kw;
                        }
                    });
                }
                updateCheckButton();
            };
        }

        // Bind mic recording
        const micBtn = host.querySelector('[data-mic]');
        if (micBtn) {
            micBtn.onclick = async function () {
                if (marked) return;
                if (!isRecording) {
                    await startRecording(host);
                } else {
                    stopRecording(host);
                }
            };
        }

        function updateCheckButton() {
            const chk = host.querySelector('[data-check]');
            if (!chk) return;
            const ansCount = Object.keys(answers).filter(k => (answers[k] || '').trim()).length;
            const rAnsCount = test.readingSection
                ? test.readingSection.questions.filter(q => readingAnswers[q.id] !== undefined).length
                : 0;
            const rTotal = test.readingSection ? test.readingSection.questions.length : 0;
            const lAnsCount = test.listeningSection
                ? test.listeningSection.questions.filter(q => listeningAnswers[q.id] !== undefined).length
                : 0;
            const lTotal = test.listeningSection ? test.listeningSection.questions.length : 0;
            const totalA = ansCount + rAnsCount + lAnsCount;
            const totalT = test.questions.length + rTotal + lTotal;
            const ready = ansCount === test.questions.length &&
                rAnsCount === rTotal &&
                lAnsCount === lTotal &&
                (!test.writingTask || countWords(writingText) >= 5) &&
                (!test.speakingTask || speakingTranscript.trim().length > 0 || speakingAudioUrl);

            chk.disabled = !ready;
            chk.textContent = ready
                ? 'Check & Grade Assessment'
                : `Complete all items to check (${totalA}/${totalT} answered)`;
        }

        // Bind reading option buttons (data-rq / data-ropt — separate from Part 1 data-q / data-opt)
        host.querySelectorAll('[data-rq]').forEach(btn => {
            btn.onclick = function () {
                if (marked) return;
                const qId = btn.getAttribute('data-rq');
                readingAnswers[qId] = btn.getAttribute('data-ropt');
                const parent = btn.closest('.lt-options');
                if (parent) {
                    parent.querySelectorAll('.lt-opt-btn').forEach(b => b.classList.remove('is-selected'));
                    btn.classList.add('is-selected');
                }
                updateCheckButton();
            };
        });

        // Bind listening option buttons (data-lq / data-lopt)
        host.querySelectorAll('[data-lq]').forEach(btn => {
            btn.onclick = function () {
                if (marked) return;
                const qId = btn.getAttribute('data-lq');
                listeningAnswers[qId] = btn.getAttribute('data-lopt');
                const parent = btn.closest('.lt-options');
                if (parent) {
                    parent.querySelectorAll('.lt-opt-btn').forEach(b => b.classList.remove('is-selected'));
                    btn.classList.add('is-selected');
                }
                updateCheckButton();
            };
        });

        // Bind listening audio console buttons
        const consoleEl = host.querySelector('.lt-audio-console');
        if (consoleEl) bindListeningConsoleButtons(consoleEl);

        // Bind listening transcript toggle button
        const transcriptToggle = host.querySelector('[data-lis-transcript-toggle]');
        if (transcriptToggle) {
            transcriptToggle.onclick = function () {
                listeningTranscriptShown = !listeningTranscriptShown;
                render(level);
            };
        }

        const check = host.querySelector('[data-check]');
        if (check) check.onclick = function () {
            if (isRecording) stopRecording(host);
            stopListeningAudio();
            mark.lastResult = mark();
            marked = true;
            render(level);
            host.scrollIntoView({ block: 'start' });
        };
        const retake = host.querySelector('[data-retake]');
        if (retake) retake.onclick = function () {
            answers = {}; order = {}; readingAnswers = {}; readingOrder = {}; marked = false;
            listeningAnswers = {}; listeningOrder = {}; listeningPass = 0; listeningPlaying = false;
            listeningIntermission = false; listeningTranscriptShown = false;
            stopListeningAudio();
            writingText = ''; speakingTranscript = ''; speakingAudioUrl = null;
            render(level);
        };
        const back = host.querySelector('[data-close-test]');
        if (back) back.onclick = function () {
            closeTest();
        };
    }

    function closeTest() {
        stop();
        if (exitCallback) {
            const cb = exitCallback;
            exitCallback = null;
            cb();
        } else {
            const targetTab = openingTab || 'learn';
            if (typeof showTab === 'function') {
                showTab(targetTab, document.querySelector(`[data-tab="${targetTab}"]`));
            }
        }
    }

    async function startRecording(host) {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            activeStream = stream;
            audioChunks = [];
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.ondataavailable = e => {
                if (e.data.size > 0) audioChunks.push(e.data);
            };
            mediaRecorder.onstop = () => {
                const blob = new Blob(audioChunks, { type: 'audio/webm' });
                speakingAudioUrl = URL.createObjectURL(blob);
                if (activeStream) {
                    try { activeStream.getTracks().forEach(t => t.stop()); } catch (e) {}
                    activeStream = null;
                }
                render(test.level);
            };
            mediaRecorder.start();
            isRecording = true;

            const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (SpeechRec) {
                recognition = new SpeechRec();
                recognition.continuous = true;
                recognition.interimResults = true;
                recognition.lang = test.level.startsWith('A') ? (typeof Lang !== 'undefined' && Lang.current() === 'hu' ? 'hu-HU' : 'es-ES') : 'es-ES';
                recognition.onresult = (e) => {
                    let transcript = '';
                    for (let i = 0; i < e.results.length; i++) {
                        transcript += e.results[i][0].transcript;
                    }
                    speakingTranscript = transcript;
                    // Defer displaying transcript in textarea until user stops speaking
                };
                try { recognition.start(); } catch (err) {}
            }

            render(test.level);
        } catch (err) {
            console.warn('Microphone access unavailable:', err);
            if (typeof UI !== 'undefined' && UI.toast) {
                UI.toast('Microphone unavailable. You can type your response directly into the transcript box.', 'warning');
            } else {
                alert('Microphone access could not be started. You can type your spoken response directly into the transcript box.');
            }
        }
    }

    function stop() {
        stopListeningAudio();
        isRecording = false;
        if (mediaRecorder && mediaRecorder.state !== 'inactive') {
            try { mediaRecorder.stop(); } catch (e) {}
        }
        if (activeStream) {
            try { activeStream.getTracks().forEach(t => t.stop()); } catch (e) {}
            activeStream = null;
        }
        if (recognition) {
            try { recognition.stop(); } catch (e) {}
            recognition = null;
        }
    }

    function stopRecording(host) {
        stop();
        if (test && test.level) render(test.level);
    }

    async function open(level, options) {
        exitCallback = (options && typeof options.onExit === 'function') ? options.onExit : null;
        diagnosticDismissed = false;
        try {
            const currentTab = document.querySelector('.tab:not(.hidden)');
            if (currentTab && currentTab.id && currentTab.id !== 'leveltest') {
                openingTab = currentTab.id;
            }
        } catch (e) {}
        if (typeof UI !== 'undefined') UI.showLoading('Loading level test…');
        try {
            document.querySelectorAll('.tab').forEach(tab => tab.classList.add('hidden'));
            document.getElementById('leveltest').classList.remove('hidden');
            if (typeof PageHeader !== 'undefined') PageHeader.render({
                title: level + ' Assessment',
                subtitle: 'Language in Context, Written Production & Spoken Production.',
                illustration: 'ascent'
            });
            await render(level);
        } finally {
            if (typeof UI !== 'undefined') UI.hideLoading();
        }
    }

    return { open, render, resultFor, stop, close: closeTest, hasTest };
})();

if (typeof window !== 'undefined') {
    window.LevelTest = LevelTest;
}
if (typeof module !== 'undefined' && module.exports) {
    module.exports = LevelTest;
}
