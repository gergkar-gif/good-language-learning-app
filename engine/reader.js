// Word lookup lives in engine/lexicon.js (Lexicon), which loads the
// dictionary and morphology indexes lazily on the first word tap — they
// total several MB and shouldn't block app startup.

// =============================================
// READER WORD COLORING (Familiarity Ramp)
// ============================================
function getWordStatus(spanish) {
    const clean = spanish.toLowerCase().replace(/[.,]/g, '');
    const card = srsDeck.find(w => w.spanish === clean);
    if (!card) return 'unknown';
    if (card.reviews >= 3) return 'mastered';
    if (card.reviews >= 1) return 'known';
    return 'seen';
}

function updateReaderWordColors() {
    document.querySelectorAll('[data-word]').forEach(el => {
        const word = el.getAttribute('data-word');
        const status = getWordStatus(word);
        el.className = 'word word-' + status;
    });
}

// ============================================
// WORD POPUP
// ============================================
function _ensureWordPopup() {
    let popup = document.getElementById('word-popup');
    if (popup) return popup;

    popup = document.createElement('div');
    popup.id = 'word-popup';
    popup.innerHTML = `
        <div id="popup-overlay" class="wp-overlay">
            <div class="wp-sheet">
                <div class="wp-header">
                    <div>
                        <h2 id="popup-word" class="wp-word"></h2>
                        <button id="popup-speak" class="speak-btn wp-speak" type="button"
                                aria-label="Listen" hidden>🔊</button>
                        <p id="popup-analysis" class="wp-analysis"></p>
                    </div>
                    <button class="wp-close" onclick="closePopup()" aria-label="Close">×</button>
                </div>
                <div id="popup-body"></div>
                <p id="popup-new-word-cap" class="wp-cap">⚠️ Daily new word limit reached (20/20)</p>
                <button id="popup-add-btn" class="wp-add" onclick="addToSRS()">➕ Add to SRS Deck</button>
            </div>
        </div>
    `;
    document.body.appendChild(popup);
    return popup;
}

// The popup's speaker button is a fixed element rather than fresh markup, so
// it is pointed at the current word instead of being re-rendered. It stays
// hidden on a device with no voice for this course's language.
function _setSpeakTarget(text) {
    const btn = document.getElementById('popup-speak');
    if (!btn) return;
    const ok = typeof Speech !== 'undefined' && Speech.available() && text;
    btn.hidden = !ok;
    if (ok) btn.setAttribute('data-speak', Speech.sayable(text));
}

function _renderWordReadings(tappedWord, readings, phrase) {
    const body = document.getElementById('popup-body');
    const analysisEl = document.getElementById('popup-analysis');

    // A multi-word expression leads, since translating it word by word
    // gives the wrong meaning ("mucho gusto" is not "much" + "taste").
    let phraseHtml = '';
    if (phrase) {
        document.getElementById('popup-word').textContent = phrase.phrase;
        _setSpeakTarget(phrase.phrase);
        analysisEl.textContent = ['expression', phrase.pos].filter(Boolean).join(' · ');
        phraseHtml =
            `<p class="wp-meaning">${Reader.escapeHtml(phrase.translation)}</p>` +
            `<p class="wp-lemma">You tapped <strong>${Reader.escapeHtml(tappedWord)}</strong>, part of this expression.</p>`;
    }

    if (!readings.length) {
        if (phrase) { body.innerHTML = phraseHtml; return; }
        analysisEl.textContent = '';
        body.innerHTML = '<p class="wp-empty">Not in the dictionary yet.</p>';
        return;
    }

    // Primary reading fills the header; any others are listed below, so an
    // ambiguous word ("casas" = houses / you marry) still shows both.
    const primary = readings[0];
    if (!phrase) {
        analysisEl.textContent = [primary.pos, primary.gender, primary.analysis]
            .filter(Boolean).join(' · ');
    }

    let html = phraseHtml;
    if (phrase) {
        html += `<p class="wp-alts-title" style="margin-top:16px">${Reader.escapeHtml(tappedWord)} on its own</p>`;
    }
    if (primary.lemma.toLowerCase() !== String(tappedWord).toLowerCase()) {
        html += `<p class="wp-lemma">from <strong>${Reader.escapeHtml(primary.lemma)}</strong></p>`;
    }
    html += `<p class="wp-meaning">${Reader.escapeHtml(primary.translation || '— no translation available —')}</p>`;

    if (readings.length > 1) {
        html += '<div class="wp-alts"><p class="wp-alts-title">Other readings</p>';
        readings.slice(1, 4).forEach(r => {
            const meta = [r.pos, r.analysis].filter(Boolean).join(' · ');
            html += `
                <div class="wp-alt">
                    <div class="wp-alt-lemma">${Reader.escapeHtml(r.lemma)}
                        <span class="wp-alt-meta">${Reader.escapeHtml(meta)}</span>
                    </div>
                    <div class="wp-alt-en">${Reader.escapeHtml(r.translation || '—')}</div>
                </div>
            `;
        });
        html += '</div>';
    }
    body.innerHTML = html;
}

async function showWord(spanish, contextTokens, tokenIndex) {
    const popup = _ensureWordPopup();
    document.getElementById('popup-word').textContent = spanish;
    _setSpeakTarget(spanish);
    popup.style.display = 'block';

    if (!Lexicon.isLoaded()) {
        document.getElementById('popup-analysis').textContent = '';
        document.getElementById('popup-body').innerHTML = '<p class="wp-empty">Loading dictionary…</p>';
        await Lexicon.load();
        // the learner may have closed the popup or tapped another word meanwhile
        if (document.getElementById('popup-word').textContent !== spanish) return;
    }

    const phrase = Lexicon.findPhrase(contextTokens, tokenIndex);
    const readings = Lexicon.lookup(spanish).readings;
    _renderWordReadings(spanish, readings, phrase);

    // The deck stores dictionary forms, so a tapped "días" is saved as "día".
    currentWord = readings.length
        ? readings[0].lemma.toLowerCase()
        : String(spanish).toLowerCase().replace(/[.,]/g, '');
    currentWordTranslation = readings.length ? readings[0].translation : null;
    currentWordPos = readings.length ? readings[0].pos : 'unknown';

    const cleanWord = currentWord;
    const capWarning = document.getElementById('popup-new-word-cap');
    const btn = document.getElementById('popup-add-btn');
    const alreadySaved = srsDeck.find(w => w.spanish === cleanWord);
    const atCap = !canAddNewWord();

    btn.classList.remove('is-saved', 'is-disabled');
    capWarning.style.display = 'none';

    if (alreadySaved) {
        btn.textContent = '✓ Already in deck';
        btn.classList.add('is-saved');
    } else if (atCap) {
        btn.textContent = 'Daily limit reached';
        btn.classList.add('is-disabled');
        capWarning.style.display = 'block';
    } else {
        btn.textContent = '➕ Add to SRS Deck';
    }
}

function closePopup() {
    const popup = document.getElementById('word-popup');
    if (popup) popup.style.display = 'none';
}

// ============================================
// READ-STATE TRACKING (which stories a learner has opened)
// ============================================
const readStoriesKey = () => Lang.key('readStories');

function getReadStoryIds() {
    try {
        return JSON.parse(localStorage.getItem(readStoriesKey()) || '[]');
    } catch (e) {
        return [];
    }
}

// Returns true only the first time a story is finished, so re-reading keeps
// the daily activity but doesn't pay the reading XP again.
function markStoryRead(storyId) {
    const read = getReadStoryIds();
    if (read.includes(storyId)) return false;
    read.push(storyId);
    localStorage.setItem(readStoriesKey(), JSON.stringify(read));
    return true;
}

function hasReadStory(storyId) {
    return getReadStoryIds().includes(storyId);
}

// ============================================
// READER ENGINE — Dynamic JSON Story Loader
// ============================================

const STORY_TYPE_LABELS = {
    original: 'Original',
    classics: 'Classics',
    world: 'World'
};

// Every CEFR level gets a reading room, even before it has any stories —
// matches the Learn tab, which shows all levels up front.
const CEFR_LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1'];

// Deterministic pastel cover per story, so the same book always
// looks the same instead of reshuffling colors on every render.
const COVER_VARIANTS = ['cover-teal', 'cover-clay', 'cover-sage', 'cover-sand'];
function coverVariantFor(id) {
    let hash = 0;
    for (let i = 0; i < id.length; i++) hash = (hash * 31 + id.charCodeAt(i)) >>> 0;
    return COVER_VARIANTS[hash % COVER_VARIANTS.length];
}

window.Reader = {
    // Resolved on every read rather than captured at load. The course can
    // change after this file runs — startup falls back to the default when
    // the chosen one has no content — and a value frozen here would leave the
    // Library fetching stories from a language the rest of the app has left.
    get storiesBasePath() { return Lang.content('stories/'); },
    stories: [],
    currentStory: null,

    init() {
        this.renderLibrary();
    },

    // The manifest, loaded once. Home asks for it too — it names the next
    // unread story — and it must not depend on the Library having been opened
    // first, which is what reading Reader.stories directly would require.
    // Content caches by path, so this is one fetch however often it is called.
    async ensureStories() {
        if (this.stories.length) return this.stories;
        const manifest = await Content.manifest('stories');
        this.stories = manifest.stories || [];
        return this.stories;
    },

    async renderLibrary() {
        const libraryEl = document.getElementById('reader-library');
        if (!libraryEl) {
            console.error('Reader: #reader-library not found in DOM');
            return;
        }

        try {
            await this.ensureStories();
            console.log('Reader: loaded', this.stories.length, 'stories from manifest');
            this.buildLibraryUI(libraryEl);

            // Event delegation, attached once — buildLibraryUI() replaces the
            // container's innerHTML on every re-render (e.g. after closing a
            // story), but this listener on the container itself survives that.
            const self = this;
            libraryEl.addEventListener('click', function(e) {
                const roomToggle = e.target.closest('[data-room-toggle]');
                if (roomToggle) {
                    const levelId = roomToggle.getAttribute('data-room-toggle');
                    const body = document.getElementById('reading-room-body-' + levelId);
                    const arrow = document.getElementById('reading-room-arrow-' + levelId);
                    if (!body) return;
                    const nowOpen = body.classList.toggle('hidden') === false;
                    roomToggle.setAttribute('aria-expanded', String(nowOpen));
                    if (arrow) arrow.textContent = nowOpen ? '▼' : '▶';
                    return;
                }

                const card = e.target.closest('.story-card');
                if (!card) return;
                const storyId = card.getAttribute('data-story-id');
                if (storyId) self.loadStory(storyId);
            });
        } catch (e) {
            libraryEl.innerHTML = '<p class="text-muted">No stories found. Run build-manifest.py</p>';
            console.error('Reader: failed to load manifest', e);
        }
    },

    buildLibraryUI(container) {
        const self = this;
        const readIds = getReadStoryIds();

        // Each CEFR level is a "reading room" — a collapsible top-level section.
        const byLevel = {};
        this.stories.forEach(function(s) {
            const level = s.level || 'Unknown';
            if (!byLevel[level]) byLevel[level] = [];
            byLevel[level].push(s);
        });

        // Any level present in the data but outside the known CEFR set
        // (shouldn't normally happen) still gets shown, appended at the end.
        const extraLevels = Object.keys(byLevel).filter(l => !CEFR_LEVELS.includes(l)).sort();
        const levels = CEFR_LEVELS.concat(extraLevels);

        let html = '';

        levels.forEach(function(level) {
            const roomStories = byLevel[level] || [];
            const readCount = roomStories.filter(s => readIds.includes(s.id)).length;
            const levelId = level.toLowerCase().replace(/[^a-z0-9]/g, '-');

            // Rooms start collapsed — fifty story cards across five levels is
            // a wall to scroll past before you reach the one you want.
            html += '<div class="reading-room">' +
                '<button class="reading-room-header" data-room-toggle="' + levelId + '" aria-expanded="false">' +
                    '<div>' +
                        '<h3 class="reading-room-title">' + self.escapeHtml(level) + '</h3>' +
                        '<span class="reading-room-count">' + readCount + ' / ' + roomStories.length + ' read</span>' +
                    '</div>' +
                    '<span class="reading-room-arrow" id="reading-room-arrow-' + levelId + '">▶</span>' +
                '</button>' +
                '<div class="reading-room-body hidden" id="reading-room-body-' + levelId + '">';

            if (!roomStories.length) {
                html += '<p class="text-muted reading-room-empty">No stories at this level yet.</p>';
            } else {
                // Within a room, stories are always split into shelves by type
                // (original / classics / world) — whichever are available.
                const types = Array.from(new Set(roomStories.map(s => s.type || s.source || 'original')));

                types.forEach(function(type) {
                    const group = roomStories.filter(s => (s.type || s.source || 'original') === type);
                    html += '<div class="story-shelf">' +
                        '<h4 class="story-shelf-title">' +
                            self.escapeHtml(STORY_TYPE_LABELS[type] || type) +
                        '</h4>' +
                        '<div class="story-grid">' +
                            group.map(story => self.buildStoryCardHtml(story, readIds)).join('') +
                        '</div>' +
                    '</div>';
                });
            }

            html += '</div></div>';
        });

        container.innerHTML = html;
    },

    buildStoryCardHtml(story, readIds) {
        const isRead = readIds.includes(story.id);
        const cover = coverVariantFor(story.id);
        const minutes = story.estimatedMinutes
            ? story.estimatedMinutes + ' min'
            : '';

        return '<button class="story-card" data-story-id="' + this.escapeHtml(story.id) + '">' +
            '<div class="story-card-cover ' + cover + '">' +
                '<svg class="story-card-cover-icon" viewBox="0 0 24 24" fill="none" aria-hidden="true">' +
                    '<path d="M4 5.5C4 4.67 4.67 4 5.5 4H11v16H5.5A1.5 1.5 0 0 1 4 18.5v-13Z" stroke="currentColor" stroke-width="1.3"/>' +
                    '<path d="M20 5.5c0-.83-.67-1.5-1.5-1.5H13v16h5.5a1.5 1.5 0 0 0 1.5-1.5v-13Z" stroke="currentColor" stroke-width="1.3"/>' +
                '</svg>' +
                (isRead ? '<span class="story-card-read-badge" title="Read">✓</span>' : '') +
            '</div>' +
            '<div class="story-card-body">' +
                '<div class="story-card-title">' + this.escapeHtml(story.title) + '</div>' +
                '<div class="story-card-meta">' +
                    '<span class="story-card-badge">' + this.escapeHtml(story.level || '') +
                        (minutes ? ' · ' + minutes : '') +
                    '</span>' +
                '</div>' +
            '</div>' +
        '</button>';
    },

    async loadStory(storyId) {
        const storyMeta = this.stories.find(s => s.id === storyId);
        if (!storyMeta) {
            console.error('Story not found in manifest:', storyId);
            return;
        }

        console.log('Reader: loading story', storyId, 'from', storyMeta.path);

        try {
            const story = await Content.story(storyMeta.path);
            // The manifest id is what read-state is keyed on; the story file
            // itself doesn't necessarily carry the same id.
            this.currentStoryId = storyId;
            this.currentStory = story;
            this.renderStory(story);
        } catch (e) {
            console.error('Reader: failed to load story file', storyMeta.path, e);
            alert('Failed to load story: ' + storyMeta.path);
        }
    },

    renderStory(story) {
        const container = document.getElementById('reader-content');
        if (!container) return;

        let html = '<div class="story-header">' +
            '<h3 class="story-title">' + this.escapeHtml(story.title) + '</h3>' +
            '<span class="story-level-badge">' + this.escapeHtml(story.level) + '</span>' +
            '<button class="btn-back" id="reader-back-btn">&larr; Back</button>' +
        '</div>';

        html += '<div class="story-body">';

        const self = this;
        if (story.paragraphs && story.paragraphs.length) {
            story.paragraphs.forEach(function(para, idx) {
                const paraClass = para.type === 'dialogue' ? 'story-paragraph dialogue' : 'story-paragraph narration';
                const speakerHtml = para.speaker
                    ? '<span class="speaker-label">' + self.escapeHtml(para.speaker) + ':</span> '
                    : '';
                const clickableText = self.makeClickable(para.text);
                html += '<p class="' + paraClass + '" data-para-index="' + idx + '">' +
                    speakerHtml + clickableText + Speech.button(para.text, 'Listen to this paragraph') +
                '</p>';
            });
        } else if (story.text) {
            // Fallback: single text field
            html += '<p class="story-paragraph narration">' +
                self.makeClickable(story.text) + Speech.button(story.text, 'Listen') +
            '</p>';
        }

        html += '</div>';

        // Reading XP is for finishing a text, so it needs an explicit end —
        // opening a story says nothing about having read it.
        const alreadyRead = hasReadStory(this.currentStoryId);
        html += '<div class="story-finish">' +
            '<button class="btn-primary" id="reader-finish-btn">' +
                (alreadyRead ? 'Finished again ✓' : 'I finished this story ✓') +
            '</button>' +
        '</div>';

        container.innerHTML = html;

        // Back button
        const backBtn = document.getElementById('reader-back-btn');
        if (backBtn) {
            backBtn.addEventListener('click', function() {
                self.closeStory();
            });
        }

        const finishBtn = document.getElementById('reader-finish-btn');
        if (finishBtn) {
            finishBtn.addEventListener('click', function() {
                self.finishStory();
            });
        }

        const libraryEl = document.getElementById('reader-library');
        if (libraryEl) libraryEl.classList.add('hidden');
        container.classList.remove('hidden');

        updateReaderWordColors();
    },

    makeClickable(text) {
        if (!text) return '';
        const tokens = text.match(/[a-zA-Z\u00e1\u00e9\u00ed\u00f3\u00fa\u00c1\u00c9\u00cd\u00d3\u00da\u00f1\u00d1\u00fc\u00dc]+|[0-9]+|[^a-zA-Z\u00e1\u00e9\u00ed\u00f3\u00fa\u00c1\u00c9\u00cd\u00d3\u00da\u00f1\u00d1\u00fc\u00dc0-9]+/g) || [];
        const self = this;

        return tokens.map(function(token) {
            if (/^[a-zA-Z\u00e1\u00e9\u00ed\u00f3\u00fa\u00c1\u00c9\u00cd\u00d3\u00da\u00f1\u00d1\u00fc\u00dc0-9]+$/.test(token)) {
                const cleanWord = token.toLowerCase().replace(/[.,]/g, '');

                // Taps are handled by a delegated listener (see below), not an
                // inline onclick: JSON.stringify emits double quotes, which
                // terminate the HTML attribute early and silently break every
                // word in the story. No translation is baked in either —
                // showWord() resolves the word through the Lexicon on tap.
                return '<span class="word" data-word="' + self.escapeHtml(cleanWord) + '">' +
                    self.escapeHtml(token) + '</span>';
            }
            return self.escapeHtml(token);
        }).join('');
    },

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    },

    finishStory() {
        if (!this.currentStoryId) return;

        const firstTime = markStoryRead(this.currentStoryId);
        if (typeof recordStoryCompleted === 'function') {
            recordStoryCompleted(firstTime);
        }

        this.closeStory();
    },

    closeStory() {
        const contentEl = document.getElementById('reader-content');
        const libraryEl = document.getElementById('reader-library');
        if (contentEl) {
            contentEl.innerHTML = '';
            contentEl.classList.add('hidden');
        }
        if (libraryEl) {
            libraryEl.classList.remove('hidden');
            this.buildLibraryUI(libraryEl); // refresh read badges/shelf counts
        }
        this.currentStory = null;
        this.currentStoryId = null;
    }
};

// ============================================
// AUTO-INIT
// ============================================

// Word taps, delegated once at the document level so it covers both the
// Library's story view and the story step inside a lesson, and survives
// every re-render of either.
document.addEventListener('click', function (e) {
    const wordEl = e.target.closest('.word');
    if (!wordEl) return;

    // Pass the surrounding words so showWord() can recognise a multi-word
    // expression the tapped word belongs to ("mucho gusto", "hasta luego").
    const scope = wordEl.closest('p, div') || document;
    const siblings = Array.from(scope.querySelectorAll('.word'));
    showWord(
        wordEl.textContent.trim(),
        siblings.map(el => el.textContent.trim()),
        siblings.indexOf(wordEl)
    );
});

(function initWhenReady() {
    function start() {
        if (window.Reader) {
            window.Reader.init();
        } else {
            console.error('Reader object missing');
        }
    }
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', start);
    } else {
        start();
    }
})();