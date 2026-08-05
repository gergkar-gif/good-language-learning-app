// ============================================
// PROGRESS TRACKING ENGINE
// ============================================
const PROGRESS_KEY = 'spanishMastery_progress';

const EMOJI_MAP = {
    "Greetings & Introductions": "👋",
    "Personal Information": "🪪",
    "Family": "👨‍👩‍👧‍👦",
    "Describing People": "🎨",
    "Describing a Home": "🏠",
    "Where Things Are": "📍",
    "Daily Routine": "🌅",
    "Time & Plans": "⏰",
    "Food & Drink": "🍽️",
    "Shopping": "🛒",
    "Hobbies": "⚽",
    "Describing Your Town": "🏙️",
    "Directions": "🧭",
    "Weather": "🌤️",
    "Work & Study": "💼",
    "Health": "🏥",
    "Future Plans": "✈️",
    "Review 1": "📝",
    "Review 2": "📝",
    "A1 Final Review": "🎓"
};

function getProgress() {
    try {
        return JSON.parse(localStorage.getItem(PROGRESS_KEY) || '{}');
    } catch (e) {
        return {};
    }
}

function saveProgress(progress) {
    localStorage.setItem(PROGRESS_KEY, JSON.stringify(progress));
}

function markLessonComplete(lessonId) {
    const progress = getProgress();
    if (!progress[lessonId]) {
        progress[lessonId] = { completedAt: new Date().toISOString() };
        saveProgress(progress);
        if (typeof addXP === 'function') addXP(50, 'Completed ' + lessonId);
        renderCurriculum();
    }
}

function isLessonComplete(lessonId) {
    return !!getProgress()[lessonId];
}

function getLevelProgress(levelKey) {
    const data = window._curriculumData;
    if (!data || !data.levels || !data.levels[levelKey]) return { completed: 0, total: 0 };
    const lessons = data.levels[levelKey].lessons || [];
    const progress = getProgress();
    const completed = lessons.filter(function(l) { return progress[l.id]; }).length;
    return { completed: completed, total: lessons.length };
}

function renderA1Lessons(lessons) {
    const container = document.getElementById('a1-lessons');
    if (!container || !lessons) return;
    const progress = getProgress();
    const completed = lessons.filter(function(l) { return progress[l.id]; }).length;
    const total = lessons.length;
    const headerText = document.getElementById('a1-progress-text');
    if (headerText) {
        headerText.textContent = completed + '/' + total + ' completed';
    }
    container.innerHTML = lessons.map(function(lesson) {
        const done = progress[lesson.id];
        const emoji = EMOJI_MAP[lesson.title] || '📚';
        const check = done ? '<span style="margin-left:8px;color:#4CAF50;">✓</span>' : '';
        const opacity = done ? 'opacity:0.75;' : '';
        const border = done ? 'border-left:4px solid #4CAF50;' : '';
        return '<div class="card" onclick="startLesson(\'' + lesson.id + '\')" style="' + opacity + border + '">' +
            '<h3>' + emoji + ' ' + lesson.title + check + '</h3>' +
            '<p>' + (lesson.goal || '') + '</p><span class="level-badge">A1</span></div>';
    }).join('');
}

function renderCurriculum() {
    if (window._curriculumData) {
        var a1 = window._curriculumData.levels && window._curriculumData.levels.A1 && window._curriculumData.levels.A1.lessons;
        if (a1) renderA1Lessons(a1);
        return;
    }
    fetch('content/curriculum/curriculum.json')
        .then(function(r) {
            if (!r.ok) throw new Error('Network response was not ok');
            return r.json();
        })
        .then(function(data) {
            window._curriculumData = data;
            var a1 = data.levels && data.levels.A1 && data.levels.A1.lessons;
            if (a1) renderA1Lessons(a1);
        })
        .catch(function(err) {
            console.error('Failed to load curriculum:', err);
            var headerText = document.getElementById('a1-progress-text');
            if (headerText) headerText.textContent = '20 lessons';
        });
}

window.SpanishMastery = window.SpanishMastery || {};
window.SpanishMastery.progress = {
    getProgress: getProgress,
    saveProgress: saveProgress,
    markLessonComplete: markLessonComplete,
    isLessonComplete: isLessonComplete,
    getLevelProgress: getLevelProgress,
    renderCurriculum: renderCurriculum
};