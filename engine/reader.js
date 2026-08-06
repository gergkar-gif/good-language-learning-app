// ============================================
// WORD DATABASE (for the reader)
// ============================================
let wordDB = {};

async function loadDictionary() {
    try {
        // Updated path to include language prefix
        const response = await fetch('imports/dictionary/spanish-en.json');
        if (!response.ok) {
            console.warn('Dictionary not found. Using inline fallbacks only.');
            return;
        }
        wordDB = await response.json();
        console.log('Dictionary loaded:', Object.keys(wordDB).length, 'words');
    } catch (error) {
        console.error('Failed to load dictionary:', error);
    }
}

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
function showWord(spanish, english) {
    currentWord = spanish.toLowerCase().replace(/[.,]/g, '');
    currentWordInlineEnglish = english;
    const cleanWord = currentWord;
    const data = wordDB[cleanWord] || { en: english, type: 'unknown', note: 'Not in database yet' };

    let popup = document.getElementById('word-popup');
    if (!popup) {
        popup = document.createElement('div');
        popup.id = 'word-popup';
        popup.innerHTML = `
            <div id="popup-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 100; display: flex; align-items: flex-end; justify-content: center;">
                <div style="background: #F2EFE6; width: 100%; max-width: 500px; border-radius: 20px 20px 0 0; padding: 25px; animation: slideUp 0.3s ease-out;">
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 15px;">
                        <div>
                            <h2 id="popup-word" style="font-size: 28px; color: #1B4B5A; margin: 0;"></h2>
                            <p id="popup-type" style="color: #8FB4BA; font-size: 14px; margin: 5px 0 0 0;"></p>
                        </div>
                        <button onclick="closePopup()" style="background: none; border: none; font-size: 24px; cursor: pointer; color: #8FB4BA;">×</button>
                    </div>
                    <p id="popup-meaning" style="font-size: 20px; margin-bottom: 10px; font-weight: 500; color: #2E2A26;"></p>
                    <p id="popup-note" style="color: #8FB4BA; font-size: 14px; margin-bottom: 20px; font-style: italic;"></p>
                    <p id="popup-new-word-cap" style="color: #E4572E; font-size: 13px; margin-bottom: 10px; display: none;">⚠️ Daily new word limit reached (20/20)</p>
                    <button id="popup-add-btn" onclick="addToSRS()" style="width: 100%; padding: 14px; background: #1B4B5A; color: white; border: none; border-radius: 10px; font-size: 16px; cursor: pointer; font-weight: bold;">➕ Add to SRS Deck</button>
                </div>
            </div>
        `;
        document.body.appendChild(popup);
    }

    document.getElementById('popup-word').textContent = spanish;
    document.getElementById('popup-type').textContent = data.type;
    document.getElementById('popup-meaning').textContent = data.en;
    document.getElementById('popup-note').textContent = data.note || 'No additional notes';

    const capWarning = document.getElementById('popup-new-word-cap');
    const btn = document.getElementById('popup-add-btn');
    const alreadySaved = srsDeck.find(w => w.spanish === cleanWord);
    const atCap = !canAddNewWord();

    if (alreadySaved) {
        btn.textContent = '✓ Already in deck';
        btn.style.background = '#8FB4BA';
        btn.style.cursor = 'default';
        capWarning.style.display = 'none';
    } else if (atCap) {
        btn.textContent = 'Daily limit reached';
        btn.style.background = '#ccc';
        btn.style.cursor = 'default';
        capWarning.style.display = 'block';
    } else {
        btn.textContent = '➕ Add to SRS Deck';
        btn.style.background = '#1B4B5A';
        btn.style.cursor = 'pointer';
        capWarning.style.display = 'none';
    }

    popup.style.display = 'block';
}

function closePopup() {
    const popup = document.getElementById('word-popup');
    if (popup) popup.style.display = 'none';
}

// ============================================
// READ-STATE TRACKING (which stories a learner has opened)
// ============================================
const READ_STORIES_KEY = 'spanishApp_readStories';

function getReadStoryIds() {
    try {
        return JSON.parse(localStorage.getItem(READ_STORIES_KEY) || '[]');
    } catch (e) {
        return [];
    }
}

function markStoryRead(storyId) {
    const read = getReadStoryIds();
    if (read.includes(storyId)) return;
    read.push(storyId);
    localStorage.setItem(READ_STORIES_KEY, JSON.stringify(read));
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
    storiesBasePath: 'content/es/stories/', // Updated to include language prefix
    stories: [],
    currentStory: null,

    init() {
        this.renderLibrary();
    },

    async renderLibrary() {
        const libraryEl = document.getElementById('reader-library');
        if (!libraryEl) {
            console.error('Reader: #reader-library not found in DOM');
            return;
        }

        try {
            const manifest = await Content.manifest('stories');
            this.stories = manifest.stories || [];
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

            html += '<div class="reading-room">' +
                '<button class="reading-room-header" data-room-toggle="' + levelId + '" aria-expanded="true">' +
                    '<div>' +
                        '<h3 class="reading-room-title">' + self.escapeHtml(level) + '</h3>' +
                        '<span class="reading-room-count">' + readCount + ' / ' + roomStories.length + ' read</span>' +
                    '</div>' +
                    '<span class="reading-room-arrow" id="reading-room-arrow-' + levelId + '">▼</span>' +
                '</button>' +
                '<div class="reading-room-body" id="reading-room-body-' + levelId + '">';

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
            this.currentStory = story;
            markStoryRead(storyId);
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
                    speakerHtml + clickableText +
                '</p>';
            });
        } else if (story.text) {
            // Fallback: single text field
            html += '<p class="story-paragraph narration">' + self.makeClickable(story.text) + '</p>';
        }

        html += '</div>';
        container.innerHTML = html;

        // Back button
        const backBtn = document.getElementById('reader-back-btn');
        if (backBtn) {
            backBtn.addEventListener('click', function() {
                self.closeStory();
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
                const dictEntry = wordDB[cleanWord];
                const english = dictEntry ? dictEntry.en : '';

                return '<span class="word" data-word="' + self.escapeHtml(cleanWord) + '" ' +
                    'onclick="showWord(' + JSON.stringify(token) + ', ' + JSON.stringify(english) + ')">' +
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
    }
};

// ============================================
// AUTO-INIT
// ============================================

loadDictionary();

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