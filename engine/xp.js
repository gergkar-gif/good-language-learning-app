// ============================================
// XP SYSTEM
// ============================================
let xpData = {
    total: 0,
    history: {},
    dailyNewWords: {}
};

const NEW_WORDS_DAILY_CAP = 20;
const STREAK_WINDOW_DAYS = 3;
const STREAK_THRESHOLD = 50;
const EARLY_REVIEW_XP = 0.2;

function getTodayString() {
    return new Date().toISOString().split('T')[0];
}

function loadXP() {
    const saved = localStorage.getItem('spanishApp_xp');
    if (saved) {
        xpData = JSON.parse(saved);
    }
}

function saveXP() {
    localStorage.setItem('spanishApp_xp', JSON.stringify(xpData));
    updateXPHeader();
}

function getDailyNewWords(dateStr) {
    return xpData.dailyNewWords[dateStr] || 0;
}

function canAddNewWord() {
    return getDailyNewWords(getTodayString()) < NEW_WORDS_DAILY_CAP;
}

function recordNewWord() {
    const today = getTodayString();
    if (!xpData.dailyNewWords[today]) {
        xpData.dailyNewWords[today] = 0;
    }
    xpData.dailyNewWords[today]++;
    saveXP();
}

function awardXP(amount, reason) {
    const today = getTodayString();
    if (!xpData.history[today]) {
        xpData.history[today] = 0;
    }
    xpData.history[today] += amount;
    xpData.total += amount;
    saveXP();
    
    showXPNotification(amount, reason);
}

function showXPNotification(amount, reason) {
    const notif = document.createElement('div');
    notif.textContent = (amount > 0 ? '+' : '') + amount + ' XP — ' + reason;
    notif.style.cssText = `
        position: fixed;
        top: 80px;
        left: 50%;
        transform: translateX(-50%);
        background: #E4572E;
        color: white;
        padding: 10px 20px;
        border-radius: 20px;
        font-weight: bold;
        z-index: 1000;
        animation: fadeUp 2s ease-out forwards;
    `;
    document.body.appendChild(notif);
    setTimeout(() => notif.remove(), 2000);
}

function calculateReviewXP(card, rating) {
    if (rating === 'again') {
        return { xp: 0, reason: 'Again (0 XP)' };
    }
    
    const now = new Date();
    const dueDate = new Date(card.nextReview);
    const isEarly = now < dueDate;
    
    if (isEarly) {
        return { xp: EARLY_REVIEW_XP, reason: 'Early review (0.2 XP)' };
    }
    
    const daysSinceReview = card.reviews === 0 ? 0 : Math.max(1, Math.floor((now - new Date(card.lastReviewed || card.added)) / (1000 * 60 * 60 * 24)));
    
    let baseXP = 10;
    const intervalBonus = Math.min(daysSinceReview, 20);
    const ratingMult = { hard: 0.8, good: 1.0, easy: 1.2 };
    const mult = ratingMult[rating] || 1.0;
    
    const totalXP = Math.round((baseXP + intervalBonus) * mult);
    
    let reason = '';
    if (rating === 'hard') reason = 'Hard recall (' + totalXP + ' XP)';
    else if (rating === 'good') reason = 'Good recall (' + totalXP + ' XP)';
    else if (rating === 'easy') reason = 'Easy recall (' + totalXP + ' XP)';
    
    return { xp: totalXP, reason: reason };
}

function getStreakStatus() {
    const today = new Date();
    let windowXP = 0;
    
    for (let i = 0; i < STREAK_WINDOW_DAYS; i++) {
        const d = new Date(today);
        d.setDate(d.getDate() - i);
        const dateStr = d.toISOString().split('T')[0];
        windowXP += xpData.history[dateStr] || 0;
    }
    
    return {
        active: windowXP >= STREAK_THRESHOLD,
        xp: windowXP,
        threshold: STREAK_THRESHOLD,
        days: STREAK_WINDOW_DAYS
    };
}

function updateXPHeader() {
    const streak = getStreakStatus();
    const xpEl = document.getElementById('header-xp');
    const streakEl = document.getElementById('header-streak');
    
    if (xpEl) xpEl.textContent = xpData.total + ' XP';
    if (streakEl) {
        if (streak.active) {
            streakEl.textContent = '🔥 ' + streak.days + 'd streak';
            streakEl.style.color = '#E4572E';
        } else {
            streakEl.textContent = streak.xp + '/' + streak.threshold + ' XP';
            streakEl.style.color = '#8FB4BA';
        }
    }
}