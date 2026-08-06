// ============================================
// CURRICULUM RENDERER
// ============================================

const CURRICULUM_EMOJIS = {
    "Greetings & Introductions":"👋",
    "Personal Information":"🪪",
    "Family":"👨‍👩‍👧‍👦",
    "Describing People":"🎨",
    "Describing a Home":"🏠",
    "Where Things Are":"📍",
    "Daily Routine":"🌅",
    "Time & Plans":"⏰",
    "Food & Drink":"🍽️",
    "Shopping":"🛒",
    "Hobbies":"⚽",
    "Describing Your Town":"🏙️",
    "Directions":"🧭",
    "Weather":"🌤️",
    "Work & Study":"💼",
    "Health":"🏥",
    "Future Plans":"✈️",
    "Review 1":"📝",
    "Review 2":"📝",
    "A1 Final Review":"🎓"
};

async function renderCurriculum() {

    if (!window._curriculumData) {
        const res = await fetch("content/es/curriculum/curriculum.json");
        window._curriculumData = await res.json();
    }

    const root = document.getElementById("learn-content");
    if (!root) return;

    const progress = getProgress();

    root.innerHTML = "";

    Object.entries(window._curriculumData.levels).forEach(([level,data]) => {

        const lessons = data.lessons || [];
        const completed = lessons.filter(l => progress[l.id]).length;

        let html = `
            <div class="level-section">
                <div onclick="toggleLevel('${level.toLowerCase()}')" class="level-header">
                    <div>
                        <h3>${data.title || level}</h3>
                        <p>${completed}/${lessons.length} completed</p>
                    </div>
                    <span id="${level.toLowerCase()}-arrow">▼</span>
                </div>

                <div id="${level.toLowerCase()}-lessons">
        `;

        lessons.forEach(lesson => {
            const done = !!progress[lesson.id];
            html += `
                <div class="card"
                     onclick="startLesson('${lesson.id}')"
                     style="${done ? "opacity:.7;border-left:4px solid #4CAF50;" : ""}">
                    <h3>${CURRICULUM_EMOJIS[lesson.title] || "📚"} ${lesson.title} ${done ? "✓" : ""}</h3>
                    <p>${lesson.goal || ""}</p>
                    ${UI.badge(level)}
                </div>
            `;
        });

        html += "</div></div>";

        UI.append("learn-content", html);
    });
}