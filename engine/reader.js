// ============================================
// WORD DATABASE (for the reader)
// ============================================
let wordDB = {};

async function loadDictionary() {
    try {
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
// =============================================
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
        btn.style.background = '1B4B5A';
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
// READER ENGINE — Dynamic JSON Story Loader
// ============================================

window.Reader = {
    storiesBasePath: 'content/stories/',
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
            const manifest = await this.loadJSON(this.storiesBasePath + 'manifest.json');
            this.stories = manifest.stories || [];
            console.log('Reader: loaded', this.stories.length, 'stories from manifest');
            this.buildLibraryUI(libraryEl);
        } catch (e) {
            libraryEl.innerHTML = '<p class="text-muted">No stories found. Run build-manifest.py</p>';
            console.error('Reader: failed to load manifest', e);
        }
    },

    buildLibraryUI(container) {
        if (!this.stories.length) {
            container.innerHTML = '<p class="text-muted">No stories in manifest yet.</p>';
            return;
        }

        const byLevel = {};
        this.stories.forEach(function(s) {
            const level = s.level || 'Unknown';
            if (!byLevel[level]) byLevel[level] = [];
            byLevel[level].push(s);
        });

        let html = '';
        const levels = Object.keys(byLevel).sort();
        const self = this;

        levels.forEach(function(level) {
            html += '<div class="story-level-group">' +
                '<h3 class="story-level-title">' + self.escapeHtml(level) + '</h3>' +
                '<div class="story-grid">';

            byLevel[level].forEach(function(story) {
                html += '<button ' +
                    'class="story-card" ' +
                    'data-story-id="' + self.escapeHtml(story.id) + '">' +
                    '<div class="story-card-title">' + self.escapeHtml(story.title) + '</div>' +
                    '<div class="story-card-meta">' +
                        self.escapeHtml(story.source || '') +
                    '</div>' +
                '</button>';
            });

            html += '</div></div>';
        });

        container.innerHTML = html;

        // Event delegation — click any story card
        container.addEventListener('click', function(e) {
            const card = e.target.closest('.story-card');
            if (!card) return;
            const storyId = card.getAttribute('data-story-id');
            if (storyId) self.loadStory(storyId);
        });
    },

    async loadStory(storyId) {
        const storyMeta = this.stories.find(s => s.id === storyId);
        if (!storyMeta) {
            console.error('Story not found in manifest:', storyId);
            return;
        }

        console.log('Reader: loading story', storyId, 'from', storyMeta.path);

        try {
            const story = await this.loadJSON(this.storiesBasePath + storyMeta.path);
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

    async loadJSON(url) {
        const res = await fetch(url);
        if (!res.ok) throw new Error('HTTP ' + res.status + ': ' + url);
        return res.json();
    },

    closeStory() {
        const contentEl = document.getElementById('reader-content');
        const libraryEl = document.getElementById('reader-library');
        if (contentEl) {
            contentEl.innerHTML = '';
            contentEl.classList.add('hidden');
        }
        if (libraryEl) libraryEl.classList.remove('hidden');
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