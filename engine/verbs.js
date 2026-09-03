const Verbs = (function () {
    'use strict';

    // ---- Tense catalogue ----
    var TENSE_OPTIONS = [
        { value: 'indicativo.presente',    label: 'Present' },
        { value: 'indicativo.preterito',   label: 'Preterite' },
        { value: 'indicativo.imperfecto',  label: 'Imperfect' },
        { value: 'indicativo.futuro',      label: 'Future' },
        { value: 'indicativo.condicional', label: 'Conditional' },
        { value: 'subjuntivo.presente',    label: 'Present Subjunctive' },
        { value: 'subjuntivo.imperfecto',  label: 'Imperfect Subjunctive' },
        { value: 'subjuntivo.futuro',      label: 'Future Subjunctive' },
        { value: 'all',                    label: 'All Tenses' }
    ];

    // Only the real (non-"all") tenses, for random picking
    var REAL_TENSES = TENSE_OPTIONS.filter(function (t) { return t.value !== 'all'; });

    var PERSONS_WITHOUT_VOSOTROS = ['yo', 'tu', 'ud', 'nosotros', 'uds'];
    var PERSONS_WITH_VOSOTROS   = ['yo', 'tu', 'ud', 'nosotros', 'vosotros', 'uds'];

    // ---- Module state (single owner) ----
    var _state = {
        mode:            'table',
        tense:           'indicativo.presente',
        includeVosotros: false,
        timer:           120,
        currentVerb:     null,
        currentVerbIndex: 0,
        verbList:        [],
        session:         null
    };

    // ---- Helpers ----
    function _getPersons() {
        return _state.includeVosotros
            ? PERSONS_WITH_VOSOTROS.slice()
            : PERSONS_WITHOUT_VOSOTROS.slice();
    }

    function _getTenseLabel() {
        for (var i = 0; i < TENSE_OPTIONS.length; i++) {
            if (TENSE_OPTIONS[i].value === _state.tense) return TENSE_OPTIONS[i].label;
        }
        return _state.tense;
    }

    function _shuffle(arr) {
        for (var i = arr.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
        }
        return arr;
    }

    function _escapeHtml(text) {
        var d = document.createElement('div');
        d.textContent = text;
        return d.innerHTML;
    }

    /**
     * Resolve the effective tense path for table mode.
     * If "all" is selected, pick a random real tense.
     * Returns { path, label }.
     */
    function _effectiveTense() {
        if (_state.tense !== 'all') {
            return { path: _state.tense, label: _getTenseLabel() };
        }
        var pick = REAL_TENSES[Math.floor(Math.random() * REAL_TENSES.length)];
        return { path: pick.value, label: pick.label };
    }

    // ---- Verb loading ----
    function _loadVerb(name) {
        return Content.verb(name).then(function (data) {
            _state.currentVerb = data;
            return data;
        }).catch(function (err) {
            console.error('Failed to load verb:', name, err);
            _state.currentVerb = null;
            return null;
        });
    }

    function _loadRandomVerb() {
        var name = _state.verbList[_state.currentVerbIndex];
        _state.currentVerbIndex = (_state.currentVerbIndex + 1) % _state.verbList.length;
        return _loadVerb(name);
    }

    // ================================================================
    //  RENDERING — Main shell (mode switcher + shared settings)
    // ================================================================
    function _buildShellHtml() {
        // Tense options
        var tenseOptions = '';
        for (var i = 0; i < TENSE_OPTIONS.length; i++) {
            var t = TENSE_OPTIONS[i];
            var sel = _state.tense === t.value ? ' selected' : '';
            tenseOptions += '<option value="' + t.value + '"' + sel + '>' + _escapeHtml(t.label) + '</option>';
        }

        return ''
            + '<div class="vb">'
            +   '<h2 class="vb-title">Verb Drills</h2>'

            // Mode switcher
            +   '<div class="vb-mode-switcher" role="tablist">'
            +     '<button class="vb-mode-btn' + (_state.mode === 'table' ? ' active' : '') + '"'
            +       ' data-action="switch-mode" data-mode="table" role="tab"'
            +       ' aria-selected="' + (_state.mode === 'table') + '">Table</button>'
            +     '<button class="vb-mode-btn' + (_state.mode === 'speed' ? ' active' : '') + '"'
            +       ' data-action="switch-mode" data-mode="speed" role="tab"'
            +       ' aria-selected="' + (_state.mode === 'speed') + '">Speed</button>'
            +   '</div>'

            // Shared settings
            +   '<div class="vb-settings">'
            +     '<div class="vb-setting">'
            +       '<label for="vb-tense">Tense</label>'
            +       '<select id="vb-tense" class="vb-select">' + tenseOptions + '</select>'
            +     '</div>'
            +     '<div class="vb-setting vb-setting-row">'
            +       '<label id="vb-vosotros-label">Include vosotros</label>'
            +       '<button class="geo-toggle"'
            +         ' data-action="toggle-vosotros" role="switch"'
            +         ' aria-checked="' + _state.includeVosotros + '"'
            +         ' aria-labelledby="vb-vosotros-label">'
            +         '<span class="geo-toggle-track"></span>'
            +         '<span class="geo-toggle-shape geo-toggle-shape--off"></span>'
            +         '<span class="geo-toggle-shape geo-toggle-shape--on"></span>'
            +       '</button>'
            +     '</div>'
            +   '</div>'

            // Mode-specific content area
            +   '<div id="vb-mode-content" class="vb-mode-content"></div>'
            + '</div>';
    }

    function _attachShellEvents(root) {
        // Mode switcher
        var modeBtns = root.querySelectorAll('[data-action="switch-mode"]');
        for (var i = 0; i < modeBtns.length; i++) {
            modeBtns[i].addEventListener('click', function () {
                Verbs.switchMode(this.dataset.mode);
            });
        }

        // Tense select
        var tenseSelect = root.querySelector('#vb-tense');
        if (tenseSelect) {
            tenseSelect.addEventListener('change', function (e) {
                _state.tense = e.target.value;
                // If switching to/from "all", reset speed mode
                VerbsSpeed.reset();
                _renderModeContent();
            });
        }

        // Vosotros toggle
        var vosotrosBtn = root.querySelector('[data-action="toggle-vosotros"]');
        if (vosotrosBtn) {
            vosotrosBtn.addEventListener('click', function () {
                _state.includeVosotros = !_state.includeVosotros;
                this.setAttribute('aria-checked', String(_state.includeVosotros));
                VerbsSpeed.reset();
                _renderModeContent();
            });
        }
    }

    // ================================================================
    //  RENDERING — Mode-specific content
    // ================================================================
    function _renderModeContent() {
        var container = document.getElementById('vb-mode-content');
        if (!container) return;

        if (_state.mode === 'table') {
            var effective = _effectiveTense();
            var meaning = '';
            if (_state.currentVerb && _state.currentVerb.english) {
                meaning = _state.currentVerb.english.infinitivo || '';
            }

            VerbsTable.render(container, {
                verb:       _state.currentVerb,
                tensePath:  effective.path,
                tenseLabel: effective.label,
                persons:    _getPersons(),
                meaning:    meaning,
                onNext:     function () { Verbs.nextVerb(); }
            });
        } else {
            VerbsSpeed.render(container, {
                tense:        _state.tense,
                tenseLabel:   _getTenseLabel(),
                tenseOptions: REAL_TENSES,
                persons:      _getPersons(),
                verbList:     _state.verbList
            });
        }
    }

    // ================================================================
    //  FULL RENDER
    // ================================================================
    function _render() {
        var root = document.getElementById('verb-driller-root');
        if (!root) return;
        root.innerHTML = _buildShellHtml();
        _attachShellEvents(root);
        _renderModeContent();
    }

    // ================================================================
    //  PUBLIC API
    // ================================================================

    /**
     * One-time initialisation.
     * Loads the verb list and renders the Drills tab.
     */
    function init() {
        _state.verbList = (typeof ALL_VERBS !== 'undefined')
            ? ALL_VERBS.slice()
            : ['hablar', 'comer', 'vivir'];
        _shuffle(_state.verbList);
        _state.currentVerbIndex = 0;

        // Load first verb but do NOT render — avoid racing with user interactions.
        // The first full render happens when render() is called (tab switch).
        _loadRandomVerb().then(function () {
            // If the drills tab is visible and we are in table mode, refresh just the
            // table content so the loaded verb appears without rebuilding the shell.
            var drillsTab = document.getElementById('drills');
            if (drillsTab && !drillsTab.classList.contains('hidden') && _state.mode === 'table') {
                _renderModeContent();
            }
        });
    }

    /** Re-render the current state (call when the tab becomes visible). */
    function render() {
        _render();
    }

    /** Switch between 'table' and 'speed' modes. Preserves shared settings. */
    function switchMode(mode) {
        if (_state.mode === mode) return;
        _state.mode = mode;
        // Leaving Speed mode mid-session (same as the tense/vosotros
        // handlers below) must stop its timer — otherwise it keeps
        // ticking against a container this module no longer renders into,
        // and silently records an abandoned session to the leaderboard
        // once it runs out.
        VerbsSpeed.reset();
        _render();
    }

    /** Load a specific verb by name and refresh the view. */
    function loadVerb(name) {
        _loadVerb(name).then(function () {
            _renderModeContent();
        });
    }

    /** Advance to a random next verb and refresh the view. */
    function nextVerb() {
        _loadRandomVerb().then(function () {
            _renderModeContent();
        });
    }

    /** Reset everything to initial defaults. */
    function reset() {
        VerbsSpeed.reset();
        _state.mode = 'table';
        _state.tense = 'indicativo.presente';
        _state.includeVosotros = false;
        _state.currentVerbIndex = 0;
        _shuffle(_state.verbList);
        _loadRandomVerb().then(function () {
            _render();
        });
    }

    // ---- Expose ----
    return {
        init:       init,
        render:     render,
        switchMode: switchMode,
        loadVerb:   loadVerb,
        nextVerb:   nextVerb,
        reset:      reset
    };
})();
