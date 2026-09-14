// ============================================
// HUNGARIAN VERB & MORPHOLOGY STUDIO
// ============================================
// Consolidates Hungarian's four specialized inflection and morphology drillers:
// 1. Verbs (HuVerbDriller): Present/past, definite/indefinite conjugation
// 2. Suffixes (HuSuffixDriller): Plurals, possessives, and cases
// 3. Prefixes (HuPrefixDriller): Verbal prefixes and directional meanings
// 4. Decomposition (HuMorphologyDriller): Word analysis and synthesis
//
// Unifies the Workshop experience for Hungarian learners into a single
// cohesive studio workspace while preserving full sub-tool independence.

const HuVerbStudio = (function () {
    'use strict';

    const TABS = [
        { id: 'verb', label: 'Conjugation', icon: '⚡', desc: 'Present/past tense, definite & indefinite forms' },
        { id: 'suffix', label: 'Suffixes', icon: '🧩', desc: 'Plurals, possession, and case endings' },
        { id: 'prefix', label: 'Prefixes', icon: '🎯', desc: 'Verbal prefixes and directional meanings' },
        { id: 'morphology', label: 'Decomposition', icon: '🔬', desc: 'Word analysis and morphological synthesis' }
    ];

    let _container = null;
    let _activeTabId = 'verb';
    let _activeSubOptions = null;

    function _subModuleFor(tabId) {
        if (tabId === 'verb') return typeof HuVerbDriller !== 'undefined' ? HuVerbDriller : null;
        if (tabId === 'suffix') return typeof HuSuffixDriller !== 'undefined' ? HuSuffixDriller : null;
        if (tabId === 'prefix') return typeof HuPrefixDriller !== 'undefined' ? HuPrefixDriller : null;
        if (tabId === 'morphology') return typeof HuMorphologyDriller !== 'undefined' ? HuMorphologyDriller : null;
        return null;
    }

    function _normalizeTabId(rawId) {
        if (!rawId) return 'verb';
        const s = String(rawId).toLowerCase().replace(/^hu-/, '');
        if (s === 'verbs' || s === 'verb') return 'verb';
        if (s === 'suffixes' || s === 'suffix') return 'suffix';
        if (s === 'prefixes' || s === 'prefix') return 'prefix';
        if (s === 'morphology') return 'morphology';
        return 'verb';
    }

    function stop() {
        const mod = _subModuleFor(_activeTabId);
        if (mod && typeof mod.stop === 'function') {
            try { mod.stop(); } catch (e) {}
        }
    }

    function _renderActiveSubTool() {
        const subMount = document.getElementById('hu-studio-sub-mount');
        if (!subMount) return;

        const mod = _subModuleFor(_activeTabId);
        if (mod && typeof mod.render === 'function') {
            mod.render(subMount, _activeSubOptions);
        } else {
            subMount.innerHTML = `
                <div class="gd-empty">
                    <p>Tool unavailable or loading...</p>
                </div>
            `;
        }
    }

    function _renderShell() {
        if (!_container) return;

        _container.innerHTML = `
            <div class="sp-studio-wrap hu-verb-studio-wrap">
                <div class="sp-studio-nav hu-studio-nav" role="tablist">
                    ${TABS.map(tab => `
                        <button type="button" class="sp-studio-tab ${_activeTabId === tab.id ? 'active' : ''}" data-hu-tab="${tab.id}" role="tab" aria-selected="${_activeTabId === tab.id}">
                            <span class="sp-tab-icon">${tab.icon}</span> ${tab.label}
                        </button>
                    `).join('')}
                </div>
                <div class="hu-studio-body" id="hu-studio-sub-mount"></div>
            </div>
        `;

        _container.querySelectorAll('[data-hu-tab]').forEach(btn => {
            btn.addEventListener('click', () => {
                const target = btn.getAttribute('data-hu-tab');
                if (target === _activeTabId) return;
                stop();
                _activeTabId = target;
                _activeSubOptions = null; // Clear deep sub-options on manual tab switch
                _renderShell();
            });
        });

        _renderActiveSubTool();
    }

    function render(container, options = {}) {
        _container = container;
        if (options && options.activeTab) {
            _activeTabId = _normalizeTabId(options.activeTab);
        }
        _activeSubOptions = options;
        _renderShell();
    }

    return {
        render,
        stop,
        TABS
    };
})();

if (typeof window !== 'undefined') {
    window.HuVerbStudio = HuVerbStudio;
}
