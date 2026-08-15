// ============================================
// LIBRARY
// ============================================
// The Library is where a learner reads whatever they want to read in
// Spanish, per PARLOUR_LIBRARY_SPEC.md. Three sections share one reading
// view (engine/reader.js's #reader-content, via makeClickable/showWord —
// nothing here reimplements tap-to-define):
//
//   Parlour   — curated readings, engine/reader.js's existing manifest-driven
//               library. Read-only; this module never touches it beyond
//               reading Reader.stories and re-rendering it on return.
//   Saved     — story ids the learner has bookmarked out of Parlour. Stores
//               the id only, never a copy of the reading.
//   My Texts  — text the learner pastes in themselves. Fully owned here:
//               storage, an editor, analysis, and the reading view (Reader
//               has no manifest entry for these, so they can't go through
//               Reader.loadStory).
//
// Library does not own SRS or vocabulary — reading a text, however
// unfamiliar, never adds anything to a deck by itself. That stays an
// explicit action (Add to deck, or the vocabulary-selection panel below),
// same principle as PARLOUR_DECKS_SPEC.md: the learner decides what's worth
// keeping.

const Library = (function () {
    'use strict';

    const PANES = { parlour: 'reader-library', saved: 'lib-saved', mytexts: 'lib-mytexts' };

    let activeSection = 'parlour';
    let savedIds = [];      // story ids, resolved against Reader.stories at render time
    let myTexts = [];       // [{ id, title, text, created, modified, analysis }]
    let textDraft = null;   // { id: null|existingId, title, text, analysis } while the editor is open

    function esc(value) {
        return (typeof UI !== 'undefined' && UI.escape)
            ? UI.escape(value) : String(value == null ? '' : value);
    }

    function withArticle(lemma) {
        return (typeof Lexicon !== 'undefined') ? Lexicon.withArticle(lemma) : lemma;
    }

    // ----------------------------------------
    // SAVED — bookmarks into the Parlour catalogue
    // ----------------------------------------
    const savedKey = () => Lang.key('savedReadings');

    function loadSaved() {
        try {
            savedIds = JSON.parse(localStorage.getItem(savedKey()) || '[]');
        } catch (error) {
            savedIds = [];
        }
    }

    function saveSaved() {
        localStorage.setItem(savedKey(), JSON.stringify(savedIds));
    }

    function isSaved(storyId) {
        return savedIds.includes(storyId);
    }

    // Returns the new saved state, so callers (the in-reading Save button)
    // can update their own label without a full re-render.
    function toggleSave(storyId) {
        if (!storyId) return false;
        const at = savedIds.indexOf(storyId);
        if (at === -1) { savedIds.push(storyId); } else { savedIds.splice(at, 1); }
        saveSaved();
        return at === -1;
    }

    async function renderSavedList() {
        const host = document.getElementById('lib-saved');
        if (!host) return;

        await Reader.ensureStories();
        const readIds = (typeof getReadStoryIds === 'function') ? getReadStoryIds() : [];
        const stories = savedIds
            .map(id => Reader.stories.find(s => s.id === id))
            .filter(Boolean);

        host.innerHTML = stories.length
            ? `<div class="story-grid">${stories.map(s => savedCardHtml(s, readIds.includes(s.id))).join('')}</div>`
            : '<p class="dk-empty">No saved readings yet. Open one from Parlour and tap Save.</p>';
    }

    // A div, not a button — buildStoryCardHtml()'s cards in Parlour are
    // buttons, and a Remove control can't nest inside one. Same visual
    // language (story-card/-cover/-body classes) so a saved reading looks
    // exactly like it did on its home shelf.
    function savedCardHtml(story, isRead) {
        const art = (typeof pathArt === 'function' && typeof coverArtIndexFor === 'function')
            ? pathArt(coverArtIndexFor(story.id), 'story-card-cover-icon')
            : '';
        const minutes = story.estimatedMinutes ? story.estimatedMinutes + ' min' : '';
        return `
            <div class="story-card lt-saved-card">
                <button class="story-card-open" data-saved-open="${esc(story.id)}">
                    <div class="story-card-cover">
                        ${art}
                        ${isRead ? '<span class="story-card-read-badge" title="Read">✓</span>' : ''}
                    </div>
                    <div class="story-card-body">
                        <div class="story-card-title">${esc(story.title)}</div>
                        <div class="story-card-meta">
                            <span class="story-card-badge">${esc(story.level || '')}${minutes ? ' · ' + minutes : ''}</span>
                        </div>
                    </div>
                </button>
                <button class="lt-saved-remove" data-saved-remove="${esc(story.id)}">Remove from Saved</button>
            </div>
        `;
    }

    // ----------------------------------------
    // MY TEXTS — data
    // ----------------------------------------
    const myTextsKey = () => Lang.key('myTexts');

    function loadMyTexts() {
        try {
            myTexts = JSON.parse(localStorage.getItem(myTextsKey()) || '[]');
        } catch (error) {
            myTexts = [];
        }
    }

    function saveMyTexts() {
        localStorage.setItem(myTextsKey(), JSON.stringify(myTexts));
    }

    function genTextId() {
        return 'text-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 8);
    }

    function listMyTexts() {
        return myTexts.slice().sort((a, b) => new Date(b.modified) - new Date(a.modified));
    }

    function getMyText(id) {
        return myTexts.find(t => t.id === id);
    }

    // ----------------------------------------
    // MY TEXTS — analysis
    // ----------------------------------------
    // Same character set Reader.makeClickable() tokenizes on, so a word
    // counted here is exactly a word that becomes tappable in the reading
    // view — no separate notion of "word" to keep in sync.
    const WORD_RE = /[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+/g;
    function tokenizeWords(text) {
        return (text || '').match(WORD_RE) || [];
    }

    // A conservative L2 reading pace — used consistently across every My
    // Text rather than tuned per text, so "~8 min" means the same thing
    // everywhere.
    const READING_WPM = 100;

    // Coarse, frequency-based — not a substitute for a real CEFR assessment.
    // Takes the 80th percentile of the text's resolvable word ranks rather
    // than the mean, so a page of otherwise-advanced writing isn't dragged
    // down to A1 by its function words. Returns null (-> "Unassessed") when
    // there isn't enough resolvable vocabulary to say anything reliable.
    function estimateLevel(lemmas) {
        if (typeof Lexicon === 'undefined' || !Lexicon.frequencyRank) return null;
        const ranks = [];
        lemmas.forEach(lemma => {
            const r = Lexicon.frequencyRank(lemma);
            if (r !== null && r !== undefined) ranks.push(r);
        });
        if (ranks.length < 15) return null;
        ranks.sort((a, b) => a - b);
        const p80 = ranks[Math.min(ranks.length - 1, Math.floor(ranks.length * 0.8))];
        if (p80 < 600) return 'A1';
        if (p80 < 1500) return 'A2';
        if (p80 < 4000) return 'B1';
        if (p80 < 9000) return 'B2';
        return 'C1';
    }

    // Everything downstream — the card, the analysis panel, the vocabulary
    // selection list — reads off this one object, computed once per
    // Analyse/Save. "Familiar" mirrors the same reviews>=1 threshold the
    // reader's word-colouring already uses (word-known), so a percentage
    // shown here means the same thing as the colour a learner sees while
    // actually reading.
    function analyseText(text) {
        const tokens = tokenizeWords(text);
        const totalWords = tokens.length;

        const seenSurface = new Set();
        const lemmaMap = new Map();
        let unrecognizedUnique = 0;

        tokens.forEach(tok => {
            const surface = tok.toLowerCase();
            if (seenSurface.has(surface)) return;
            seenSurface.add(surface);
            const readings = (typeof Lexicon !== 'undefined') ? Lexicon.lookup(tok).readings : [];
            if (readings.length) {
                const r = readings[0];
                const lemma = r.lemma.toLowerCase();
                if (!lemmaMap.has(lemma)) {
                    lemmaMap.set(lemma, { lemma: lemma, translation: r.translation, pos: r.pos });
                }
            } else {
                unrecognizedUnique++;
            }
        });

        const now = new Date();
        const deck = (typeof srsDeck !== 'undefined' && Array.isArray(srsDeck)) ? srsDeck : [];
        const myDeckLemmas = (typeof Decks !== 'undefined' && Decks.allMyDeckLemmas)
            ? Decks.allMyDeckLemmas() : new Set();

        let familiarCount = 0, notYetLearnedCount = 0, inDecksCount = 0, dueCount = 0;
        const lemmas = [];
        lemmaMap.forEach(item => {
            const card = deck.find(c => c.spanish === item.lemma);
            const familiar = !!(card && (card.reviews || 0) >= 1);
            const isNew = !card;
            const due = !!(card && (!card.nextReview || new Date(card.nextReview) <= now));
            const inDeckList = myDeckLemmas.has(item.lemma);

            if (familiar) familiarCount++;
            if (isNew) notYetLearnedCount++;
            if (due) dueCount++;
            if (inDeckList) inDecksCount++;

            lemmas.push(Object.assign({}, item, { familiar, isNew, due, inDeck: inDeckList }));
        });

        const recognizedUnique = lemmaMap.size;

        return {
            totalWords: totalWords,
            estimatedMinutes: Math.max(1, Math.round(totalWords / READING_WPM)),
            level: estimateLevel(Array.from(lemmaMap.keys())),
            recognizedUnique: recognizedUnique,
            unrecognizedUnique: unrecognizedUnique,
            familiar: familiarCount,
            notYetLearned: notYetLearnedCount,
            inDecks: inDecksCount,
            due: dueCount,
            // What "% familiar" means: of the words in this text Parlour's
            // dictionary recognises, how many the learner already has some
            // standing with — not raw dictionary coverage, which would sit
            // near 100% for almost any real text and say nothing useful.
            familiarPercent: recognizedUnique ? Math.round((familiarCount / recognizedUnique) * 100) : 0,
            lemmas: lemmas
        };
    }

    // ----------------------------------------
    // MY TEXTS — editor (create / edit, draft-based like the Deck editor)
    // ----------------------------------------
    function openAddText() {
        textDraft = { id: null, title: '', text: '', analysis: null };
        if (typeof Lexicon !== 'undefined') Lexicon.load();
        renderMyTextsPane();
    }

    function openEditText(id) {
        const t = getMyText(id);
        if (!t) return;
        textDraft = { id: t.id, title: t.title, text: t.text, analysis: t.analysis };
        if (typeof Lexicon !== 'undefined') Lexicon.load();
        renderMyTextsPane();
    }

    function closeTextEditor() {
        textDraft = null;
        renderMyTextsPane();
    }

    async function runAnalysis() {
        if (!textDraft.text.trim()) { alert('Paste some text first.'); return; }
        if (typeof Lexicon !== 'undefined' && !Lexicon.isLoaded()) {
            const btn = document.querySelector('[data-text-analyse]');
            if (btn) { btn.disabled = true; btn.textContent = 'Analysing…'; }
            await Lexicon.load();
            // the learner may have cancelled out of the editor meanwhile
            if (!textDraft) return;
        }
        textDraft.analysis = analyseText(textDraft.text);
        renderMyTextsPane();
    }

    async function saveText(andRead) {
        const title = (textDraft.title || '').trim();
        if (!title) { alert('Give the text a title first.'); return; }
        if (!textDraft.text.trim()) { alert('Paste some text first.'); return; }

        if (!textDraft.analysis) {
            if (typeof Lexicon !== 'undefined' && !Lexicon.isLoaded()) await Lexicon.load();
            textDraft.analysis = analyseText(textDraft.text);
        }

        const now = new Date().toISOString();
        let id = textDraft.id;
        if (id) {
            const t = getMyText(id);
            t.title = title;
            t.text = textDraft.text;
            t.analysis = textDraft.analysis;
            t.modified = now;
        } else {
            id = genTextId();
            myTexts.push({
                id: id, title: title, text: textDraft.text,
                created: now, modified: now, analysis: textDraft.analysis
            });
        }
        saveMyTexts();
        textDraft = null;

        if (andRead) {
            openMyText(id);
        } else {
            renderMyTextsPane();
        }
    }

    function deleteText() {
        if (!textDraft.id) return;
        // Only the text itself — its words keep whatever SRS/deck standing
        // they already had, same principle as removing a word from a My
        // Deck. See PARLOUR_LIBRARY_SPEC.md §14.
        if (!confirm(`Delete "${textDraft.title}"? Words you've saved from it stay in your decks.`)) return;
        myTexts = myTexts.filter(t => t.id !== textDraft.id);
        saveMyTexts();
        textDraft = null;
        renderMyTextsPane();
    }

    function quickDeleteText(id) {
        const t = getMyText(id);
        if (!t) return;
        if (!confirm(`Delete "${t.title}"? Words you've saved from it stay in your decks.`)) return;
        myTexts = myTexts.filter(x => x.id !== id);
        saveMyTexts();
        renderMyTextsPane();
    }

    // ----------------------------------------
    // MY TEXTS — vocabulary selection ("Add selected words to deck")
    // ----------------------------------------
    function vocabPanelHtml(a) {
        if (!a.lemmas.length) return '';

        const groups = [
            { key: 'familiar', label: 'Familiar', items: a.lemmas.filter(l => l.familiar) },
            { key: 'new', label: 'New', items: a.lemmas.filter(l => l.isNew) },
            { key: 'inDecks', label: 'In decks', items: a.lemmas.filter(l => l.inDeck) },
            { key: 'due', label: 'Due for review', items: a.lemmas.filter(l => l.due) }
        ];

        return `
            <div class="dk-group lt-vocab-group">
                <button class="dk-group-header" data-group-toggle="lt-vocab" aria-expanded="false">
                    <span>
                        <span class="dk-group-title">Inspect vocabulary</span>
                        <span class="dk-group-count">${a.lemmas.length}</span>
                    </span>
                    <span class="dk-group-arrow" id="dk-group-arrow-lt-vocab" aria-hidden="true">▶</span>
                </button>
                <div class="dk-group-body hidden" id="dk-group-body-lt-vocab">
                    ${groups.map(g => !g.items.length ? '' : `
                        <div class="lt-vocab-category">
                            <p class="lt-vocab-category-title">${esc(g.label)} (${g.items.length})</p>
                            <ul class="lt-vocab-list">
                                ${g.items.map(item => `
                                    <li>
                                        <label class="lt-vocab-item">
                                            <input type="checkbox" data-vocab-lemma="${esc(item.lemma)}"
                                                data-vocab-en="${esc(item.translation || '')}"
                                                data-vocab-pos="${esc(item.pos || '')}">
                                            <span class="lt-vocab-es">${esc(withArticle(item.lemma))}</span>
                                            <span class="lt-vocab-en">${esc(item.translation || '—')}</span>
                                        </label>
                                    </li>
                                `).join('')}
                            </ul>
                        </div>
                    `).join('')}
                    <div class="lt-vocab-actions">
                        <button class="dk-secondary" data-vocab-add-selected="1">Add selected words to deck</button>
                    </div>
                </div>
            </div>
        `;
    }

    function addSelectedVocabToDeck(host) {
        const checked = Array.from(host.querySelectorAll('[data-vocab-lemma]:checked'));
        if (!checked.length) { alert('Check a word first.'); return; }
        const items = checked.map(el => ({
            lemma: el.getAttribute('data-vocab-lemma'),
            translation: el.getAttribute('data-vocab-en'),
            pos: el.getAttribute('data-vocab-pos')
        }));
        if (typeof Decks !== 'undefined') Decks.openBulkAddPicker(items);
    }

    // ----------------------------------------
    // MY TEXTS — render
    // ----------------------------------------
    function textAnalysisHtml(a) {
        return `
            <div class="lt-analysis">
                <p class="lt-analysis-headline">${a.level ? 'Estimated level: ' + esc(a.level) : 'Level: Unassessed'}</p>
                <p class="lt-analysis-line">${a.totalWords.toLocaleString()} words · ~${a.estimatedMinutes} min read</p>
                <p class="lt-analysis-coverage">${a.familiarPercent}% familiar</p>
                <ul class="lt-analysis-breakdown">
                    <li>${a.familiar} recognised words</li>
                    <li>${a.notYetLearned} words not yet learned</li>
                    <li>${a.inDecks} already in your decks</li>
                    <li>${a.due} due for review</li>
                </ul>
                ${vocabPanelHtml(a)}
            </div>
        `;
    }

    function textEditorHtml() {
        const isNew = !textDraft.id;
        const a = textDraft.analysis;
        return `
            <button class="dk-back" data-text-cancel="1">← My Texts</button>
            <div class="dk-editor">
                <h3 class="dk-editor-title">${isNew ? 'Add text' : 'Edit text'}</h3>

                <label class="dk-editor-label" for="lt-text-title">Title</label>
                <input id="lt-text-title" class="dk-editor-input" type="text"
                    placeholder="e.g. La Revolución Mexicana" value="${esc(textDraft.title)}" maxlength="120">

                <label class="dk-editor-label" for="lt-text-body">Paste your text</label>
                <textarea id="lt-text-body" class="dk-editor-input lt-text-area"
                    placeholder="Paste any Spanish text here — an article, an essay, a story…">${esc(textDraft.text)}</textarea>

                <div class="dk-actions lt-analyse-row">
                    <button class="dk-secondary" data-text-analyse="1">Analyse text</button>
                </div>

                ${a ? textAnalysisHtml(a) : ''}

                <div class="dk-actions dk-editor-actions">
                    <button class="btn-primary" data-text-save="1">Save</button>
                    ${a ? '<button class="dk-secondary" data-text-save-read="1">Save &amp; read</button>' : ''}
                    ${!isNew ? '<button class="dk-danger" data-text-delete="1">Delete text</button>' : ''}
                </div>
            </div>
        `;
    }

    function myTextCardHtml(t) {
        const a = t.analysis;
        const meta = a
            ? `${a.level || 'Unassessed'} · ${a.totalWords.toLocaleString()} words · ~${a.estimatedMinutes} min`
            : 'Not analysed yet';
        return `
            <div class="lt-card">
                <button class="lt-card-main" data-text-open="${esc(t.id)}">
                    <span class="lt-card-title">${esc(t.title)}</span>
                    <span class="lt-card-meta">${esc(meta)}</span>
                    ${a ? `<span class="lt-card-coverage">${a.familiarPercent}% familiar</span>` : ''}
                </button>
                <div class="lt-card-actions">
                    <button class="lt-card-action" data-text-edit="${esc(t.id)}">Edit</button>
                    <button class="lt-card-action lt-card-action-danger" data-text-quick-delete="${esc(t.id)}">Delete</button>
                </div>
            </div>
        `;
    }

    function myTextsIndexHtml() {
        const texts = listMyTexts();
        return `
            <div class="lt-index-head">
                <p class="dk-group-blurb">Bring in any Spanish text and read it with the same dictionary
                    and deck tools as the rest of Parlour.</p>
                <button class="btn-primary" data-text-add="1">+ Add text</button>
            </div>
            ${texts.length
                ? `<div class="lt-list">${texts.map(myTextCardHtml).join('')}</div>`
                : '<p class="dk-empty">No texts yet. Paste one in to get started.</p>'}
        `;
    }

    function renderMyTextsPane() {
        const host = document.getElementById('lib-mytexts');
        if (!host) return;
        host.innerHTML = textDraft ? textEditorHtml() : myTextsIndexHtml();
        wireMyTextsPane(host);
    }

    function wireMyTextsPane(host) {
        host.querySelectorAll('[data-text-add]').forEach(el => { el.onclick = openAddText; });
        host.querySelectorAll('[data-text-open]').forEach(el => {
            el.onclick = function () { openMyText(el.getAttribute('data-text-open')); };
        });
        host.querySelectorAll('[data-text-edit]').forEach(el => {
            el.onclick = function () { openEditText(el.getAttribute('data-text-edit')); };
        });
        host.querySelectorAll('[data-text-quick-delete]').forEach(el => {
            el.onclick = function () { quickDeleteText(el.getAttribute('data-text-quick-delete')); };
        });

        const titleEl = document.getElementById('lt-text-title');
        const bodyEl = document.getElementById('lt-text-body');
        if (titleEl) titleEl.oninput = e => { textDraft.title = e.target.value; };
        // Editing the text invalidates any analysis run against the old
        // version — Save still works without re-analysing (it computes a
        // fresh one silently), but showing stale stats while the text has
        // changed underneath them would be worse than showing none.
        if (bodyEl) bodyEl.oninput = e => { textDraft.text = e.target.value; textDraft.analysis = null; };

        host.querySelectorAll('[data-text-cancel]').forEach(el => { el.onclick = closeTextEditor; });
        host.querySelectorAll('[data-text-analyse]').forEach(el => { el.onclick = runAnalysis; });
        host.querySelectorAll('[data-text-save]').forEach(el => { el.onclick = () => saveText(false); });
        host.querySelectorAll('[data-text-save-read]').forEach(el => { el.onclick = () => saveText(true); });
        host.querySelectorAll('[data-text-delete]').forEach(el => { el.onclick = deleteText; });

        host.querySelectorAll('[data-group-toggle]').forEach(el => {
            el.onclick = function () {
                const key = el.getAttribute('data-group-toggle');
                const body = document.getElementById('dk-group-body-' + key);
                const arrow = document.getElementById('dk-group-arrow-' + key);
                if (!body) return;
                const nowOpen = body.classList.toggle('hidden') === false;
                el.setAttribute('aria-expanded', String(nowOpen));
                if (arrow) arrow.textContent = nowOpen ? '▼' : '▶';
            };
        });
        host.querySelectorAll('[data-vocab-add-selected]').forEach(el => {
            el.onclick = function () { addSelectedVocabToDeck(host); };
        });
    }

    // ----------------------------------------
    // MY TEXTS — reading view
    // ----------------------------------------
    // Paragraphs by blank line, same as a learner would expect from pasted
    // prose — there is no paragraph-type/speaker structure to preserve like
    // a Parlour story has.
    function splitParagraphs(text) {
        return (text || '').split(/\n\s*\n/).map(p => p.trim()).filter(Boolean);
    }

    function openMyText(id) {
        const t = getMyText(id);
        if (!t) return;

        const container = document.getElementById('reader-content');
        if (!container) return;

        const level = t.analysis && t.analysis.level ? t.analysis.level : 'Unassessed';
        let html = '<div class="story-header">' +
            '<h3 class="story-title">' + esc(t.title) + '</h3>' +
            '<span class="story-level-badge">' + esc(level) + '</span>' +
            '<span class="story-header-actions">' +
                '<button class="btn-back" data-mytext-back="1">&larr; Back</button>' +
            '</span>' +
        '</div><div class="story-body">';

        const paragraphs = splitParagraphs(t.text);
        if (paragraphs.length) {
            paragraphs.forEach(p => {
                html += '<p class="story-paragraph narration">' + Reader.makeClickable(p) +
                    (typeof Speech !== 'undefined' ? Speech.button(p, 'Listen to this paragraph') : '') + '</p>';
            });
        }
        html += '</div>';

        container.innerHTML = html;
        const backBtn = container.querySelector('[data-mytext-back]');
        if (backBtn) backBtn.onclick = closeMyText;

        showReading();
        if (typeof updateReaderWordColors === 'function') updateReaderWordColors();
    }

    function closeMyText() {
        const container = document.getElementById('reader-content');
        if (container) {
            container.innerHTML = '';
            container.classList.add('hidden');
        }
        returnFromReading();
    }

    // ----------------------------------------
    // SECTION SWITCHING (Parlour / Saved / My Texts / reading)
    // ----------------------------------------
    function showSection(section) {
        activeSection = PANES[section] ? section : 'parlour';

        document.querySelectorAll('#lib-subnav [data-lib-tab]').forEach(btn => {
            btn.classList.toggle('active', btn.getAttribute('data-lib-tab') === activeSection);
        });
        Object.keys(PANES).forEach(key => {
            const el = document.getElementById(PANES[key]);
            if (el) el.classList.toggle('hidden', key !== activeSection);
        });
        const content = document.getElementById('reader-content');
        if (content) content.classList.add('hidden');
        const subnav = document.getElementById('lib-subnav');
        if (subnav) subnav.classList.remove('hidden');

        if (activeSection === 'parlour' && typeof Reader !== 'undefined') {
            const el = document.getElementById('reader-library');
            if (el) Reader.buildLibraryUI(el); // refresh read badges/shelf counts
        } else if (activeSection === 'saved') {
            renderSavedList();
        } else if (activeSection === 'mytexts') {
            renderMyTextsPane();
        }
    }

    // Called by Reader (and openMyText above) whenever any reading opens, so
    // the three index panes and the subnav get out of the way of the shared
    // #reader-content view.
    function showReading() {
        const subnav = document.getElementById('lib-subnav');
        if (subnav) subnav.classList.add('hidden');
        Object.keys(PANES).forEach(key => {
            const el = document.getElementById(PANES[key]);
            if (el) el.classList.add('hidden');
        });
        const content = document.getElementById('reader-content');
        if (content) content.classList.remove('hidden');
    }

    // Called by Reader.closeStory() and closeMyText() — returns to whichever
    // of Parlour/Saved/My Texts was active before the reading opened.
    function returnFromReading() {
        showSection(activeSection);
    }

    // ----------------------------------------
    // INIT
    // ----------------------------------------
    function init() {
        loadSaved();
        loadMyTexts();

        const subnav = document.getElementById('lib-subnav');
        if (subnav) {
            subnav.addEventListener('click', e => {
                const btn = e.target.closest('[data-lib-tab]');
                if (btn) showSection(btn.getAttribute('data-lib-tab'));
            });
        }

        const savedEl = document.getElementById('lib-saved');
        if (savedEl) {
            savedEl.addEventListener('click', e => {
                const openBtn = e.target.closest('[data-saved-open]');
                if (openBtn) { Reader.loadStory(openBtn.getAttribute('data-saved-open')); return; }
                const removeBtn = e.target.closest('[data-saved-remove]');
                if (removeBtn) { toggleSave(removeBtn.getAttribute('data-saved-remove')); renderSavedList(); }
            });
        }

        // No initial showSection() call: the static markup already matches
        // activeSection's default ('parlour' visible, Saved/My Texts hidden)
        // — Reader.renderLibrary() populates #reader-library on its own once
        // its manifest fetch resolves, on the same startup path this always
        // used before Saved/My Texts existed.
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    return {
        isSaved, toggleSave, showReading, returnFromReading, showSection
    };
})();
