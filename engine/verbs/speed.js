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
    var _busy           = false;   // true while feedback is showing

    // ---- Helpers ----
    function _escapeHtml(text) {
        var d = document.createElement('div');
        d.textContent = text;
        return d.innerHTML;
    }

    function _normalise(text) {
        return String(text || '').toLowerCase().trim()
            .normalize('NFD').replace(/[\u0300-\u036f]/g, '');
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

        if (isCorrect) _score++;

        // Show feedback
        var feedbackEl = _container.querySelector('.vspeed-feedback');
        var prefix = isCorrect ? '\u2713 ' : '\u2717 ';
        feedbackEl.textContent = prefix + _currentAnswer;
        feedbackEl.className = 'vspeed-feedback ' + (isCorrect ? 'vspeed-feedback-correct' : 'vspeed-feedback-wrong');

        // Update score display
        var scoreEl = _container.querySelector('.vspeed-score-value');
        if (scoreEl) scoreEl.textContent = _score;

        // Disable input during feedback
        _busy = true;
        input.disabled = true;
        var submitBtn = _container.querySelector('[data-action="submit"]');
        if (submitBtn) submitBtn.disabled = true;

        setTimeout(function () {
            if (_phase !== PHASE.PLAYING) return;
            _busy = false;
            _showNextQuestion();
        }, FEEDBACK_MS);
    }

    function _endSession() {
        _phase = PHASE.RESULTS;
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
        _renderResults();
    }

    // ================================================================
    //  PHASE — RESULTS
    // ================================================================
    function _renderResults() {
        var stats = VerbsStats.getStats();

        var area = _container.querySelector('.vspeed-play-area');
        if (!area) return;

        area.innerHTML = ''
            + '<div class="vspeed-results">'
            +   '<h3 class="vspeed-results-title">Session Results</h3>'
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
            +     '<div class="vspeed-stat">'
            +       '<span class="vspeed-stat-label">Weakest tense</span>'
            +       '<span class="vspeed-stat-value">' + _escapeHtml(stats.weakestTense) + '</span>'
            +     '</div>'
            +     '<div class="vspeed-stat">'
            +       '<span class="vspeed-stat-label">Weakest person</span>'
            +       '<span class="vspeed-stat-value">' + _escapeHtml(stats.weakestPerson) + '</span>'
            +     '</div>'
            +   '</div>'
            +   '<div class="vspeed-results-actions">'
            +     '<button class="vbtn vbtn-primary" data-action="play-again">Play Again</button>'
            +     '<button class="vbtn vbtn-secondary" data-action="change-settings">Change Settings</button>'
            +   '</div>'
            + '</div>';

        area.querySelector('[data-action="play-again"]').addEventListener('click', function () {
            _startSession();
        });
        area.querySelector('[data-action="change-settings"]').addEventListener('click', function () {
            _phase = PHASE.SETTINGS;
            render(_container);
        });
    }

    // ================================================================
    //  PLAYING PHASE WRAPPER (timer + score header)
    // ================================================================
    function _renderPlaying(root) {
        root.innerHTML = ''
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
        _tense        = options.tense || 'indicativo.presente';
        _tenseLabel   = options.tenseLabel || '';
        _tenseOptions = options.tenseOptions || [];
        _persons      = options.persons || [];
        _verbList     = options.verbList || [];

        switch (_phase) {
            case PHASE.SETTINGS: _renderSettings(root);  break;
            case PHASE.PLAYING:  _renderPlaying(root); _showNextQuestion(); break;
            case PHASE.RESULTS:  _renderPlaying(root); _renderResults();   break;
        }
    }

    /** Stop any running timer and go back to settings. */
    function reset() {
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
        _phase = PHASE.SETTINGS;
        _score = 0;
    }

    return { render: render, reset: reset };
})();
