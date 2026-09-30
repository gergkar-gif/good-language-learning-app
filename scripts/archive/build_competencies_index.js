const fs = require('fs');
const path = require('path');

const repoRoot = path.resolve('c:/Users/Admin/My Drive/Werk/7 - Other projects/spanish-app/spanish-mastery');
const curriculumPath = path.join(repoRoot, 'content/es/curriculum/curriculum.json');
const lessonsDir = path.join(repoRoot, 'content/es/lessons');
const outputPath = path.join(repoRoot, 'content/es/indexes/competencies-index.json');
const scriptCopyPath = path.join(repoRoot, 'scripts/build_competencies_index.js');

if (!fs.existsSync(curriculumPath)) {
    console.error('Curriculum not found at:', curriculumPath);
    process.exit(1);
}

const curriculum = JSON.parse(fs.readFileSync(curriculumPath, 'utf8'));

// Build lessonId -> unit mapping
const lessonToUnit = {};
Object.keys(curriculum.levels || {}).forEach(lvlKey => {
    const lvl = curriculum.levels[lvlKey];
    (lvl.units || []).forEach(unit => {
        (unit.lessons || []).forEach(les => {
            lessonToUnit[les.id] = {
                level: lvlKey,
                unitId: unit.id,
                unitLabel: unit.label,
                unitTitle: unit.title,
                lessonId: les.id,
                lessonTitle: les.title,
                lessonGoal: les.goal
            };
        });
    });
});

function walk(dir) {
    let results = [];
    fs.readdirSync(dir).forEach(file => {
        const full = path.join(dir, file);
        if (fs.statSync(full).isDirectory()) results = results.concat(walk(full));
        else if (file.endsWith('.json')) results.push(full);
    });
    return results;
}

const lessonFiles = walk(lessonsDir);
const competencies = [];

lessonFiles.forEach(f => {
    try {
        const les = JSON.parse(fs.readFileSync(f, 'utf8'));
        const lId = les.id;
        if (!lId) return;

        const uInfo = lessonToUnit[lId] || {
            level: les.level || 'A1',
            unitId: 'unit.' + (les.level ? les.level.toLowerCase() : 'a1') + '.01',
            unitLabel: '1',
            unitTitle: 'General Practice',
            lessonId: lId,
            lessonTitle: les.title || 'Lesson',
            lessonGoal: les.goal || ''
        };

        const checklist = (les.sections || []).find(s => s.type === 'checklist');
        const items = (checklist && Array.isArray(checklist.items)) ? checklist.items : [];

        items.forEach((text, idx) => {
            if (!text || typeof text !== 'string') return;
            const cleanText = text.trim();
            if (!cleanText) return;

            competencies.push({
                id: `${lId}.c${idx + 1}`,
                text: cleanText,
                lessonId: lId,
                lessonTitle: uInfo.lessonTitle,
                level: uInfo.level,
                unitId: uInfo.unitId,
                unitLabel: uInfo.unitLabel,
                unitTitle: uInfo.unitTitle
            });
        });
    } catch (err) {
        console.warn('Failed parsing lesson:', f, err.message);
    }
});

// Ensure indexes directory exists
const indexDir = path.dirname(outputPath);
if (!fs.existsSync(indexDir)) {
    fs.mkdirSync(indexDir, { recursive: true });
}

fs.writeFileSync(outputPath, JSON.stringify(competencies, null, 2), 'utf8');
console.log(`Generated ${competencies.length} competencies -> ${outputPath}`);

// Copy script to repo scripts/ folder as well for repo completeness
const selfContent = fs.readFileSync(__filename, 'utf8');
fs.writeFileSync(scriptCopyPath, selfContent, 'utf8');
console.log(`Saved copy of builder to ${scriptCopyPath}`);
