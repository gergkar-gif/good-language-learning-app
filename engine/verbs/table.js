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

    // ---- Rendering ----
    function _buildHtml(verb, tenseLabel, meaning, persons, tenseData) {
        if (!verb) {
            return '<div class="vtable-empty">Loading verb data\u2026</div>';
        }

        if (!tenseData) {
            return ''
                + '<div class="vtable-header">'
                +   '<div class="vtable-verb">' + _escapeHtml(verb.infinitivo.toUpperCase()) + '</div>'
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
            rows += ''
                + '<div class="vtable-row">'
                +   '<label class="vtable-label" for="vtable-' + p + '">' + PERSON_LABELS[p] + '</label>'
                +   '<input id="vtable-' + p + '" class="vtable-input" type="text"'
                +     ' autocomplete="off" autocapitalize="off" spellcheck="false"'
                +     ' data-person="' + p + '" data-correct="' + _escapeHtml(correct) + '"'
                +     ' aria-label="' + PERSON_LABELS[p] + '">'
                + '</div>';
        }

        return ''
            + '<div class="vtable-header">'
            +   '<div class="vtable-verb">' + _escapeHtml(verb.infinitivo.toUpperCase()) + '</div>'
            +   (meaning ? '<div class="vtable-meaning">' + _escapeHtml(meaning) + '</div>' : '')
            +   '<div class="vtable-tense">' + _escapeHtml(tenseLabel) + '</div>'
            + '</div>'
            + '<div class="vtable-body">' + rows + '</div>'
            + '<div class="vtable-actions">'
            +   '<button class="vbtn vbtn-primary" data-action="check">Check</button>'
            +   '<button class="vbtn vbtn-secondary" data-action="next" disabled>Next Verb</button>'
            + '</div>'
            + '<p class="vtable-feedback" aria-live="polite"></p>';
    }

    // ---- Event handling ----
    function _attachEvents(root) {
        var checkBtn = root.querySelector('[data-action="check"]');
        var nextBtn  = root.querySelector('[data-action="next"]');

        if (checkBtn) checkBtn.addEventListener('click', _handleCheck);
        if (nextBtn)  nextBtn.addEventListener('click', function () { _onNext(); });

        // Enter key triggers check (desktop convenience, not required)
        var inputs = root.querySelectorAll('.vtable-input');
        for (var i = 0; i < inputs.length; i++) {
            inputs[i].addEventListener('keydown', function (e) {
                if (e.key === 'Enter') _handleCheck();
            });
        }
    }

    // ---- Check logic ----
    function _handleCheck() {
        if (_allCorrect) return;

        var inputs = _container.querySelectorAll('.vtable-input');
        var correctCount = 0;
        var total = 0;

        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
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
                // Fix accent/casing to canonical form
                if (userVal !== correctAnswer.toLowerCase()) {
                    input.value = correctAnswer;
                }
                correctCount++;
            } else {
                input.classList.add('vtable-wrong');
                input.value = correctAnswer;
                // Input stays editable so the user can study the answer
            }
        }

        var feedback = _container.querySelector('.vtable-feedback');
        if (!feedback) return;

        if (correctCount === total && total > 0) {
            _allCorrect = true;
            feedback.textContent = '\u2713 Perfect!';
            feedback.className = 'vtable-feedback vtable-feedback-success';
            var nextBtn = _container.querySelector('[data-action="next"]');
            if (nextBtn) nextBtn.disabled = false;
            // Focus the next button for quick progression
            if (nextBtn) nextBtn.focus();
        } else if (total > 0) {
            feedback.textContent = correctCount + '/' + total + ' correct';
            feedback.className = 'vtable-feedback vtable-feedback-error';
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
    }

    return { render: render };
})();
