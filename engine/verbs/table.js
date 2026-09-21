const VerbsTable = (function () {
    'use strict';

    // ---- Constants ----
    var PERSON_LABELS = {
        yo:        'yo',
        tu:        't\u00fa',
        ud:        '\u00e9l / ella',
        nosotros:  'nosotros',
        vosotros:  'vosotros',
        uds:       'ellos / ustedes'
    };

    // ---- Private state ----
    var _container = null;
    var _onNext    = null;
    var _persons   = [];
    var _allCorrect = false;

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

    // Accents are checked directly (2026-08-27) \u2014 a conjugated form's
    // accent can be the only thing distinguishing it from another person
    // or tense (hablo "I speak" vs habl\u00f3 "he/she spoke"), so stripping it
    // would let a wrong answer through undetected. Still canonicalise to
    // NFC so a decomposed accented letter from some keyboards/IMEs
    // string-equals a precomposed one, without discarding the accent
    // itself.
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

    // ---- Rendering ----
    function _buildHtml(verb, tenseLabel, meaning, persons, tenseData) {
        if (!verb) {
            return '<div class="vtable-empty">Loading verb data…</div>';
        }

        var verbAudio = (typeof ParlourTTS !== 'undefined')
            ? ParlourTTS.button(verb.infinitivo, { type: 'vocabulary', label: 'Listen to ' + verb.infinitivo })
            : (typeof Speech !== 'undefined' ? Speech.button(verb.infinitivo) : '');

        if (!tenseData) {
            return ''
                + '<div class="vtable-header">'
                +   '<div class="vtable-verb">' + _escapeHtml(verb.infinitivo.toUpperCase()) + verbAudio + '</div>'
                +   (meaning ? '<div class="vtable-meaning">' + _escapeHtml(meaning) + '</div>' : '')
                + '</div>'
                + '<div class="vtable-empty">This tense is not available for this verb.</div>'
                + '<div class="vtable-actions">'
                +   '<button class="vbtn vbtn-primary" data-action="next">Next Verb</button>'
                + '</div>';
        }

        var rows = '';
        for (var i = 0; i < persons.length; i++) {
            var p = persons[i];
            var correct = tenseData[p] || '';
            var rowAudio = (correct && typeof ParlourTTS !== 'undefined')
                ? ParlourTTS.button(correct, { type: 'vocabulary', label: 'Listen to ' + correct })
                : (correct && typeof Speech !== 'undefined' ? Speech.button(correct) : '');
            rows += ''
                + '<div class="vtable-row">'
                +   '<label class="vtable-label" for="vtable-' + p + '">' + PERSON_LABELS[p] + '</label>'
                +   '<input id="vtable-' + p + '" class="vtable-input" type="text"'
                +     ' autocomplete="off" autocapitalize="off" spellcheck="false"'
                +     ' data-person="' + p + '" data-correct="' + _escapeHtml(correct) + '"'
                +     ' aria-label="' + PERSON_LABELS[p] + '">'
                +   '<span class="vtable-correction hidden" aria-live="polite"></span>'
                +   rowAudio
                + '</div>';
        }

        return ''
            + '<div class="vtable-header">'
            +   '<div class="vtable-verb">' + _escapeHtml(verb.infinitivo.toUpperCase()) + verbAudio + '</div>'
            +   (meaning ? '<div class="vtable-meaning">' + _escapeHtml(meaning) + '</div>' : '')
            +   '<div class="vtable-tense">' + _escapeHtml(tenseLabel) + '</div>'
            + '</div>'
            + '<div class="vtable-body">' + rows + '</div>'
            + (typeof UI !== 'undefined' && UI.diacriticsBarHtml ? UI.diacriticsBarHtml('.vtable-input') : '')
            + '<div class="vtable-actions">'
            +   '<button class="vbtn vbtn-primary" data-action="check">Check</button>'
            +   '<button class="vbtn vbtn-secondary" data-action="reveal">Show Answers</button>'
            +   '<button class="vbtn vbtn-secondary" data-action="next" disabled>Next Verb</button>'
            + '</div>'
            + '<p class="vtable-feedback" aria-live="polite"></p>';
    }

    // ---- Event handling ----
    function _attachEvents(root) {
        var checkBtn  = root.querySelector('[data-action="check"]');
        var revealBtn = root.querySelector('[data-action="reveal"]');
        var nextBtn   = root.querySelector('[data-action="next"]');

        if (checkBtn)  checkBtn.addEventListener('click', _handleCheck);
        if (revealBtn) revealBtn.addEventListener('click', _handleReveal);
        if (nextBtn)   nextBtn.addEventListener('click', function () { _onNext(); });

        // Enter key triggers check (desktop convenience, not required)
        var inputs = root.querySelectorAll('.vtable-input');
        for (var i = 0; i < inputs.length; i++) {
            inputs[i].addEventListener('keydown', function (e) {
                if (e.key === 'Enter') _handleCheck();
            });
        }
    }

    function _handleReveal() {
        var rows = _container.querySelectorAll('.vtable-row');
        for (var i = 0; i < rows.length; i++) {
            var row = rows[i];
            var input = row.querySelector('.vtable-input');
            var corr = row.querySelector('.vtable-correction');
            if (!input) continue;
            var correctAnswer = input.dataset.correct;
            if (correctAnswer) {
                input.value = correctAnswer;
                input.classList.remove('vtable-wrong');
                input.classList.add('vtable-correct');
                input.readOnly = true;
                if (corr) { corr.textContent = ''; corr.classList.add('hidden'); }
            }
        }
        _allCorrect = true;
        var nextBtn = _container.querySelector('[data-action="next"]');
        if (nextBtn) {
            nextBtn.disabled = false;
            nextBtn.focus();
        }
        var feedback = _container.querySelector('.vtable-feedback');
        if (feedback) {
            feedback.textContent = 'All forms revealed for reference.';
            feedback.className = 'vtable-feedback vtable-feedback-success';
        }
    }

    // ---- Check logic ----
    function _handleCheck() {
        if (_allCorrect) return;

        var rows = _container.querySelectorAll('.vtable-row');
        var correctCount = 0;
        var total = 0;
        var missedLabels = [];

        for (var i = 0; i < rows.length; i++) {
            var row = rows[i];
            var input = row.querySelector('.vtable-input');
            var corr = row.querySelector('.vtable-correction');
            if (!input) continue;
            var correctAnswer = input.dataset.correct;
            if (!correctAnswer) continue; // person not available in this tense

            total++;
            var userVal = input.value;
            var normalisedUser    = _normalise(userVal);
            var normalisedCorrect = _normalise(correctAnswer);

            input.classList.remove('vtable-correct', 'vtable-wrong');

            if (normalisedUser === normalisedCorrect && userVal.trim() !== '') {
                input.classList.add('vtable-correct');
                input.readOnly = true;
                if (userVal !== correctAnswer.toLowerCase()) {
                    input.value = correctAnswer;
                }
                if (corr) { corr.textContent = ''; corr.classList.add('hidden'); }
                correctCount++;
            } else {
                input.classList.add('vtable-wrong');
                var p = input.dataset.person;
                if (p && PERSON_LABELS[p]) missedLabels.push(PERSON_LABELS[p]);
                if (corr) {
                    corr.textContent = 'Correct: ' + correctAnswer;
                    corr.classList.remove('hidden');
                }
            }
        }

        var feedback = _container.querySelector('.vtable-feedback');
        var nextBtn = _container.querySelector('[data-action="next"]');

        if (correctCount === total && total > 0) {
            _allCorrect = true;
            if (feedback) {
                feedback.textContent = '\u2713 Perfect!';
                feedback.className = 'vtable-feedback vtable-feedback-success';
            }
            if (nextBtn) {
                nextBtn.disabled = false;
                nextBtn.focus();
            }
        } else if (total > 0) {
            if (feedback) {
                var missedList = missedLabels.length ? ' (' + missedLabels.join(', ') + ')' : '';
                feedback.textContent = '\u2717 ' + correctCount + ' of ' + total + ' correct. Review the corrections shown above' + missedList + '.';
                feedback.className = 'vtable-feedback vtable-feedback-error';
            }
            // Enable next button so the learner can either correct their inputs or proceed after studying corrections
            if (nextBtn) nextBtn.disabled = false;
        }
    }

    // ---- Public API ----
    /**
     * Render the table mode into the given root element.
     * @param {HTMLElement} root
     * @param {{ verb:Object, tensePath:string, tenseLabel:string,
   *          persons:string[], meaning:string, onNext:function }} options
     */
    function render(root, options) {
        _container   = root;
        _onNext      = options.onNext || function () {};
        _persons     = options.persons || [];
        _allCorrect  = false;

        var verb      = options.verb;
        var tensePath = options.tensePath;
        var tenseLabel = options.tenseLabel;
        var meaning   = options.meaning || '';

        var tenseData = verb ? _getTenseData(verb, tensePath) : null;

        root.innerHTML = _buildHtml(verb, tenseLabel, meaning, _persons, tenseData);
        _attachEvents(root);

        if (typeof ParlourTTS !== 'undefined' && ParlourTTS.preload && verb) {
            ParlourTTS.preload({ text: verb.infinitivo, type: 'vocabulary' });
            if (tenseData) {
                for (var j = 0; j < _persons.length; j++) {
                    var form = tenseData[_persons[j]];
                    if (form) ParlourTTS.preload({ text: form, type: 'vocabulary' });
                }
            }
        }
    }

    return { render: render };
})();
