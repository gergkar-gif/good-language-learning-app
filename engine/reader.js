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

// ============================================
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
