// ============================================
// TAB SWITCHING
// ============================================
function showTab(tabName, event) {
    document.querySelectorAll('.tab').forEach(tab => {
        tab.classList.add('hidden');
    });
    document.getElementById(tabName).classList.remove('hidden');

    document.querySelectorAll('.nav button').forEach(btn => {
        btn.classList.remove('active');
    });
    if (event && event.target) {
        event.target.classList.add('active');
    } else {
        // If no event (called programmatically), activate first button
        document.querySelector('.nav button:first-child').classList.add('active');
    }

    if (tabName === 'drills' && !currentVerb) {
        // Initialize drills: load first verb if available
        if (drillVerbs && drillVerbs.length > 0) {
            loadVerb(drillVerbs[0]);
        }
    }
    if (tabName === 'review') {
        showNextCard();
    }
    if (tabName === 'reader') {
        updateReaderWordColors();
    }
}

// ============================================
// INIT
// ============================================
const style = document.createElement('style');
style.textContent = `
    @keyframes slideUp {
        from { transform: translateY(100%); }
        to { transform: translateY(0); }
    }
    @keyframes fadeUp {
        0% { opacity: 1; transform: translateX(-50%) translateY(0); }
        80% { opacity: 1; transform: translateX(-50%) translateY(-10px); }
        100% { opacity: 0; transform: translateX(-50%) translateY(-30px); }
    }
`;
document.head.appendChild(style);

function toggleLevel(levelId) {
    const lessonsDiv = document.getElementById(levelId + '-lessons');
    const arrow = document.getElementById(levelId + '-arrow');

    if (lessonsDiv.style.display === 'none') {
        lessonsDiv.style.display = 'block';
        arrow.textContent = '▼';
    } else {
        lessonsDiv.style.display = 'none';
        arrow.textContent = '▶';
    }
}

// Load everything
loadDictionary().then(() => {
    loadDeck();
    loadXP();
    updateXPHeader();
    updateReaderWordColors();
    if (typeof renderCurriculum === 'function') {
        renderCurriculum();
    }
});