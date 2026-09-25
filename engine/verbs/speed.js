const VerbsSpeed = (function () {
    'use strict';

    // ---- Constants ----
    var PHASE = { SETTINGS: 1, PLAYING: 2, RESULTS: 3 };
    var FEEDBACK_MS = 500;
    var PERSON_LABELS = {
        yo:       'yo',
        tu:       't\u00fa',
        ud:       '\u00e9l / ella',
        nosotros: 'nosotros',
        vosotros: 'vosotros',
        uds:      'ellos / ustedes'
    };

    // ---- Private state ----
    var _phase          = PHASE.SETTINGS;
    var _timerInterval  = null;
    var _endTime        = 0;
    var _timeRemaining  = 0;
    var _timerMinutes   = 2;
    var _verbIndex      = 0;
    var _score          = 0;
    var _container      = null;
    var _tense          = '';
    var _tenseLabel     = '';
    var _tenseOptions   = [];
    var _persons        = [];
    var _verbList       = [];
    var _currentAnswer  = '';
    var _currentTenseLabel = '';
    var _currentPersonLabel = '';
    var _currentMeaning = '';
    var _currentTensePath = '';   // e.g. 'indicativo.preterito'
    var _currentPersonKey  = '';   // PERSON_LABELS key, e.g. 'uds'
    var _currentVerbName   = '';
    // 'verb:<tensePath>:<person>' -> 'again' | 'good' for this session, sent
    // to the recycle schedule once at the end (_creditConjugations()).
    var _conjOutcomes = {};
    var _missedConjugations = [];
    var _busy           = false;   // true while feedback is showing

    // ---- Helpers ----
    function _escapeHtml(text) {
        return (typeof UI !== 'undefined' && UI.escape)
            ? UI.escape(text)
            : String(text == null ? '' : text)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;');
    }

    // Accents are checked directly (2026-08-27) \u2014 see engine/verbs/table.js's
    // _normalise for why (a conjugated form's accent can be the only thing
    // distinguishing it from another person or tense).
    function _normalise(text) {
        return String(text || '').toLowerCase().trim().normalize('NFC');
    }

    function _getTenseData(verb, tensePath) {
        var parts = tensePath.split('.');
        var data = verb;
        for (var i = 0; i < parts.length; i++) {
            if (!data) return null;
            data = data[parts[i]];
        }
        return data;
    }

    function _formatTime(totalSeconds) {
        var m = Math.floor(totalSeconds / 60);
        var s = totalSeconds % 60;
        return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
    }

    function _pickRandom(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }

    // ================================================================
    //  PHASE — SETTINGS
    // ================================================================
    function _renderSettings(root) {
        var options = '';
        var presets = [1, 2, 3, 4, 5];
        for (var i = 0; i < presets.length; i++) {
            var v = presets[i];
            var label = v === 1 ? '1 minute' : v + ' minutes';
            var sel = v === _timerMinutes ? ' selected' : '';
            options += '<option value="' + v + '"' + sel + '>' + label + '</option>';
        }

        root.innerHTML = ''
            + '<div class="vspeed-settings">'
            +   '<div class="vb-setting">'
            +     '<label for="vspeed-timer">Timer</label>'
            +     '<select id="vspeed-timer" class="vb-select">' + options + '</select>'
            +   '</div>'
            +   '<button class="vbtn vbtn-primary vbtn-block" data-action="start">Start</button>'
            + '</div>';

        root.querySelector('#vspeed-timer').addEventListener('change', function (e) {
            _timerMinutes = parseInt(e.target.value, 10);
        });
        root.querySelector('[data-action="start"]').addEventListener('click', function () {
            _startSession();
        });
    }

    // ================================================================
    //  PHASE — PLAYING
    // ================================================================
    function _startSession() {
        VerbsStats.init();
        _score = 0;
        _missedConjugations = [];
        _conjOutcomes = {};
        _verbIndex = Math.floor(Math.random() * _verbList.length);
        _timeRemaining = _timerMinutes * 60;
        _endTime = Date.now() + _timeRemaining * 1000;
        _busy = false;
        _phase = PHASE.PLAYING;

        // Swap the settings view for the playing view (HUD + question area)
        _renderPlaying(_container);

        // Start ticking
        _timerInterval = setInterval(function () {
            var remaining = Math.max(0, Math.ceil((_endTime - Date.now()) / 1000));
            _timeRemaining = remaining;
            var el = _container.querySelector('.vspeed-timer-display');
            if (el) el.textContent = _formatTime(remaining);
            var total = _timerMinutes * 60;
            var elapsed = Math.max(0, total - remaining);
            var pct = Math.min(100, Math.round((elapsed / Math.max(1, total)) * 100));
            var bar = _container.querySelector('.driller-progress-bar');
            if (bar) bar.style.width = pct + '%';
            if (remaining <= 0) _endSession();
        }, 250);

        _showNextQuestion();
    }

    function _showNextQuestion() {
        if (_phase !== PHASE.PLAYING) return;

        // Pick a random person
        var person = _pickRandom(_persons);
        var personLabel = PERSON_LABELS[person];

        // Pick a tense
        var tensePath, tenseLabel;
        if (_tense === 'all') {
            var opt = _pickRandom(_tenseOptions);
            tensePath  = opt.value;
            tenseLabel = opt.label;
        } else {
            tensePath  = _tense;
            tenseLabel = _tenseLabel;
        }

        // Try verbs until we find one that has the required conjugation
        var attempts = 0;
        var maxAttempts = _verbList.length;

        function tryLoad() {
            if (attempts >= maxAttempts || _phase !== PHASE.PLAYING) {
                _container.querySelector('.vspeed-question').innerHTML =
                    '<p class="vtable-empty">No questions available for this combination.</p>';
                return;
            }
            attempts++;

            var verbName = _verbList[_verbIndex];
            _verbIndex = (_verbIndex + 1) % _verbList.length;

            Content.verb(verbName).then(function (verb) {
                if (_phase !== PHASE.PLAYING) return;

                var tenseData = _getTenseData(verb, tensePath);
                if (!tenseData || !tenseData[person]) {
                    tryLoad();
                    return;
                }

                var correctAnswer = tenseData[person];
                _currentAnswer      = correctAnswer;
                _currentTenseLabel  = tenseLabel;
                _currentPersonLabel = personLabel;
                _currentTensePath   = tensePath;
                _currentPersonKey   = person;
                _currentVerbName    = verb.infinitivo || verbName;
                _currentMeaning     = (verb.english && verb.english.infinitivo) ? verb.english.infinitivo : '';

                _renderQuestion(verb.infinitivo.toUpperCase(), tenseLabel, personLabel, _currentMeaning);
            }).catch(function () {
                tryLoad();
            });
        }

        tryLoad();
    }

    function _renderQuestion(verbDisplay, tenseLabel, personLabel, meaning) {
        var questionArea = _container.querySelector('.vspeed-question');
        if (!questionArea) return;

        var tenseHtml = '';
        if (_tense === 'all') {
            tenseHtml = '<div class="vspeed-tense-label">' + _escapeHtml(tenseLabel) + '</div>';
        }

        var meaningHtml = meaning
            ? '<div class="vspeed-meaning">' + _escapeHtml(meaning) + '</div>'
            : '';

        questionArea.innerHTML = ''
            + '<div class="vspeed-verb">' + _escapeHtml(verbDisplay) + '</div>'
            + meaningHtml
            + tenseHtml
            + '<div class="vspeed-person">' + _escapeHtml(personLabel) + '</div>'
            + '<div class="vspeed-input-row">'
            +   '<input id="vspeed-answer" class="vtable-input" type="text"'
            +     ' autocomplete="off" autocapitalize="off" spellcheck="false"'
            +     ' aria-label="Conjugation input">'
            +   '<button class="vbtn vbtn-primary" data-action="submit">Submit</button>'
            + '</div>'
            + (typeof UI !== 'undefined' && UI.diacriticsBarHtml ? UI.diacriticsBarHtml('#vspeed-answer') : '')
            + '<div class="vspeed-feedback" aria-live="polite"></div>';

        // Focus the input
        var input = document.getElementById('vspeed-answer');
        if (input) input.focus();

        // Events
        var submitBtn = questionArea.querySelector('[data-action="submit"]');
        submitBtn.addEventListener('click', _handleSubmit);
        input.addEventListener('keydown', function (e) {
            if (e.key === 'Enter') _handleSubmit();
        });
    }

    function _handleSubmit() {
        if (_busy || _phase !== PHASE.PLAYING) return;

        var input = document.getElementById('vspeed-answer');
        if (!input) return;

        var userVal = input.value.trim();
        if (userVal === '') return; // ignore empty

        var isCorrect = _normalise(userVal) === _normalise(_currentAnswer);

        // Record stats
        VerbsStats.record(isCorrect, _currentTenseLabel, _currentPersonLabel);
        _noteConjugation(isCorrect);

        if (isCorrect) {
            _score++;
        } else {
            _missedConjugations.push({
                verb: _currentVerbName,
                meaning: _currentMeaning,
                tense: _currentTenseLabel,
                person: _currentPersonLabel,
                user: userVal,
                correct: _currentAnswer
            });
        }

        // Show feedback
        var feedbackEl = _container.querySelector('.vspeed-feedback');
        if (isCorrect) {
            feedbackEl.textContent = '\u2713 ' + _currentAnswer;
            feedbackEl.className = 'vspeed-feedback vspeed-feedback-correct';
        } else {
            feedbackEl.textContent = '\u2717 Correct: ' + _currentAnswer + ' (you wrote: "' + userVal + '")';
            feedbackEl.className = 'vspeed-feedback vspeed-feedback-wrong';
        }

        // Update score display
        var scoreEl = _container.querySelector('.vspeed-score-value');
        if (scoreEl) scoreEl.textContent = _score;

        // Disable input during feedback
        _busy = true;
        input.disabled = true;
        var submitBtn = _container.querySelector('[data-action="submit"]');
        if (submitBtn) submitBtn.disabled = true;

        var delay = isCorrect ? FEEDBACK_MS : Math.max(FEEDBACK_MS, 1200);
        setTimeout(function () {
            if (_phase !== PHASE.PLAYING) return;
            _busy = false;
            _showNextQuestion();
        }, delay);
    }

    // Each tense+person pair is its own card in the recycle schedule, so
    // "preterite, ellos" can be weak while "preterite, yo" is solid. A miss
    // is always 'again'; a correct form only counts when that card is due
    // (Recycle.credit()). LearnerModel joins these cards to grammar skills
    // through content/<lang>/indexes/verb-tense-skills.json and lists the
    // weakest pairs in weakConjugations(). One outcome per pair per
    // session; a miss wins.
    function _noteConjugation(isCorrect) {
        if (!_currentTensePath || !_currentPersonKey) return;
        var id = 'verb:' + _currentTensePath + ':' + _currentPersonKey;
        if (_conjOutcomes[id] === 'again') return;
        _conjOutcomes[id] = isCorrect ? 'good' : 'again';
    }

    function _creditConjugations() {
        var ids = Object.keys(_conjOutcomes);
        if (!ids.length || typeof Recycle === 'undefined' || !Recycle.credit) return;
        var results = ids.map(function (id) { return { id: id, rating: _conjOutcomes[id] }; });
        _conjOutcomes = {};
        Recycle.credit(results);
    }

    function _endSession() {
        _phase = PHASE.RESULTS;
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
        _creditConjugations();

        // Read the previous best before record() folds this session in, so
        // the results screen can tell whether this run just set a new one.
        var stats = VerbsStats.getStats();
        var previousBest = (typeof VerbsLeaderboard !== 'undefined') ? VerbsLeaderboard.best() : null;
        var newBest = (typeof VerbsLeaderboard !== 'undefined') ? VerbsLeaderboard.record({
            correct: stats.correct,
            wrong: stats.wrong,
            accuracy: stats.accuracy,
            tenseLabel: _tense === 'all' ? 'All tenses' : _tenseLabel,
            timerMinutes: _timerMinutes
        }) : null;
        var isNewBest = !!newBest && (!previousBest || newBest.accuracy > previousBest.accuracy ||
            (newBest.accuracy === previousBest.accuracy && newBest.correct > previousBest.correct));

        if (typeof DrillHistory !== 'undefined') {
            DrillHistory.record('verbs', { correct: stats.correct, wrong: stats.wrong });
        }

        _renderResults(newBest, isNewBest && (stats.correct + stats.wrong) > 0);
    }

    // ================================================================
    //  PHASE — RESULTS
    // ================================================================
    function _renderResults(best, isNewBest) {
        var stats = VerbsStats.getStats();
        best = best || ((typeof VerbsLeaderboard !== 'undefined') ? VerbsLeaderboard.best() : null);

        var area = _container.querySelector('.vspeed-play-area');
        if (!area) return;

        var bestHtml = best
            ? '<div class="vspeed-stat">'
                + '<span class="vspeed-stat-label">Best accuracy</span>'
                + '<span class="vspeed-stat-value">' + best.accuracy + '%</span>'
              + '</div>'
            : '';

        area.innerHTML = ''
            + '<div class="vspeed-results">'
            +   '<h3 class="vspeed-results-title">Session Results</h3>'
            +   (isNewBest ? '<p class="vspeed-new-best">New personal best!</p>' : '')
            +   '<div class="vspeed-results-grid">'
            +     '<div class="vspeed-stat">'
            +       '<span class="vspeed-stat-label">Correct</span>'
            +       '<span class="vspeed-stat-value">' + stats.correct + '</span>'
            +     '</div>'
            +     '<div class="vspeed-stat">'
            +       '<span class="vspeed-stat-label">Wrong</span>'
            +       '<span class="vspeed-stat-value">' + stats.wrong + '</span>'
            +     '</div>'
            +     '<div class="vspeed-stat">'
            +       '<span class="vspeed-stat-label">Accuracy</span>'
            +       '<span class="vspeed-stat-value">' + stats.accuracy + '%</span>'
            +     '</div>'
            +     bestHtml
            +     '<div class="vspeed-stat">'
            +       '<span class="vspeed-stat-label">Weakest tense</span>'
            +       '<span class="vspeed-stat-value">' + _escapeHtml(stats.weakestTense) + '</span>'
            +     '</div>'
            +     '<div class="vspeed-stat">'
            +       '<span class="vspeed-stat-label">Weakest person</span>'
            +       '<span class="vspeed-stat-value">' + _escapeHtml(stats.weakestPerson) + '</span>'
            +     '</div>'
            +   '</div>'
            +   (_missedConjugations.length ? (
                  '<div class="gd-missed-recap">'
                +   '<h4 class="gd-missed-title">Review Missed Conjugations</h4>'
                +   '<div class="gd-missed-list">'
                +   _missedConjugations.map(function (item) {
                        var qText = item.verb + ' (' + item.tense + ' \u2014 ' + item.person + ')' + (item.meaning ? ' \u2014 ' + item.meaning : '');
                        return '<div class="gd-missed-card">'
                            +   '<div class="gd-missed-q">' + _escapeHtml(qText) + '</div>'
                            +   '<div class="gd-missed-answers">'
                            +     (item.user ? '<div class="gd-missed-user"><span class="gd-badge-wrong">Your answer:</span> ' + _escapeHtml(item.user) + '</div>' : '')
                            +     '<div class="gd-missed-correct"><span class="gd-badge-correct">Correct:</span> <strong>' + _escapeHtml(item.correct) + '</strong></div>'
                            +   '</div>'
                            + '</div>';
                    }).join('')
                +   '</div>'
                + '</div>'
               ) : '')
            +   '<div class="vspeed-results-actions">'
            +     '<button class="vbtn vbtn-primary" data-action="play-again">Practice Again</button>'
            +     '<button class="vbtn vbtn-secondary" data-action="change-settings">Change Settings</button>'
            +     '<button class="vbtn vbtn-secondary" data-action="exit-workshop">Back to Workshop</button>'
            +   '</div>'
            + '</div>';

        area.querySelector('[data-action="play-again"]').addEventListener('click', function () {
            _startSession();
        });
        area.querySelector('[data-action="change-settings"]').addEventListener('click', function () {
            _phase = PHASE.SETTINGS;
            render(_container);
        });
        var exitBtn = area.querySelector('[data-action="exit-workshop"]');
        if (exitBtn) {
            exitBtn.addEventListener('click', function () {
                if (typeof Workshop !== 'undefined') Workshop.close();
            });
        }

        if (typeof RecommendationEngine !== 'undefined') {
            RecommendationEngine.mountNextAction(area, { excludeDrillerId: 'verbs' });
        }
    }

    // ================================================================
    //  PLAYING PHASE WRAPPER (timer + score header)
    // ================================================================
    function _renderPlaying(root) {
        root.innerHTML = ''
            + '<div class="driller-progress-track" aria-hidden="true">'
            +   '<div class="driller-progress-bar" style="width: 0%"></div>'
            + '</div>'
            + '<div class="vspeed-play-area">'
            +   '<div class="vspeed-hud">'
            +     '<div class="vspeed-timer-display">' + _formatTime(_timeRemaining) + '</div>'
            +     '<div class="vspeed-score">Score <span class="vspeed-score-value">' + _score + '</span></div>'
            +   '</div>'
            +   '<div class="vspeed-question"></div>'
            + '</div>';
    }

    // ================================================================
    //  PUBLIC API
    // ================================================================
    /**
     * @param {HTMLElement} root
     * @param {{ tense:string, tenseLabel:string, tenseOptions:Object[],
   *          persons:string[], verbList:string[] }} options
     */
    function render(root, options) {
        _container    = root;
        _tense        = (options && options.tense) || 'indicativo.presente';
        _tenseLabel   = (options && options.tenseLabel) || '';
        _tenseOptions = (options && options.tenseOptions) || [];
        _persons      = (options && options.persons) || [];
        _verbList     = (options && options.verbList) || [];

        if (options && options.duration) {
            _timerMinutes = Math.max(1, Math.round(options.duration / 60));
        }

        if (_phase === PHASE.SETTINGS && options && options.autoStart) {
            _startSession();
            return;
        }

        switch (_phase) {
            case PHASE.SETTINGS: _renderSettings(root);  break;
            case PHASE.PLAYING:  _renderPlaying(root); _showNextQuestion(); break;
            case PHASE.RESULTS:  _renderPlaying(root); _renderResults();   break;
        }
    }

    /** Stop any running timer and go back to settings. */
    function reset() {
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
        _creditConjugations(); // leaving mid-run still counts what was answered
        _phase = PHASE.SETTINGS;
        _score = 0;
    }

    return { render: render, reset: reset };
})();
