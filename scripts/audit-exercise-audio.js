// Prints what every lesson exercise would say aloud once settled (ROADMAP 122),
// one file per course, so the cleaning rules in engine/exercise-audio.js can
// be skimmed against real content before shipping.
//
//   node scripts/audit-exercise-audio.js [out-dir] [content-dir]
//
// Each line: <id> | <type> | <spoken text, or "(silent)"> | <source text>.
// Silent lines are listed first in each file: they're where a rule may be
// too strict. Spoken lines that contain English are where it's too loose.

const fs = require('fs');
const path = require('path');
const ExerciseAudio = require('../engine/exercise-audio.js');

const outDir = process.argv[2] || path.join(__dirname, '..', 'generated', 'audit-exercise-audio');
const root = process.argv[3] || path.join(__dirname, '..', 'content');
fs.mkdirSync(outDir, { recursive: true });

function walk(dir, files = []) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
        const full = path.join(dir, entry.name);
        if (entry.isDirectory()) walk(full, files);
        else if (entry.name.endsWith('.json')) files.push(full);
    }
    return files;
}

// Same split as splitOptionGloss() in engine/lessons.js: "text [gloss]".
function optionText(option) {
    return String(option || '').replace(/\s*\[[^\]]*\]\s*$/, '').trim();
}

function spokenFor(ex, lang) {
    switch (ex.type) {
        case 'fill-blank':
            return { spoken: ExerciseAudio.fillBlank(ex.sentence, ex.answer || (ex.answers || [])[0], lang), source: ex.sentence };
        case 'multiple-choice':
        case 'dialogue-complete': {
            if (!Array.isArray(ex.options)) return null;
            const i = Array.isArray(ex.correct) ? ex.correct[0] : ex.correct;
            const option = optionText(ex.options[i]);
            const spoken = ex.type === 'dialogue-complete'
                ? ExerciseAudio.stripAsides(option)
                : ExerciseAudio.forChoice(ex.question, option, lang);
            return { spoken, source: (ex.question || '') + ' → ' + option };
        }
        case 'sentence-builder': {
            const solution = (ex.solutions && ex.solutions[0]) || ex.solution || [];
            return { spoken: ExerciseAudio.stripAsides(solution.join(' ')), source: solution.join(' ') };
        }
        default:
            return null;
    }
}

const summary = [];
for (const course of fs.readdirSync(root)) {
    const dir = path.join(root, course, 'exercises');
    if (!fs.existsSync(dir)) continue;
    const silent = [], spoken = [];
    for (const file of walk(dir)) {
        let data;
        try { data = JSON.parse(fs.readFileSync(file, 'utf8')); } catch { continue; }
        const list = Array.isArray(data) ? data : data.exercises;
        if (!Array.isArray(list)) continue;
        for (const ex of list) {
            if (!ex || typeof ex !== 'object') continue;
            const r = spokenFor(ex, course);
            if (!r) continue;
            const line = [ex.id, ex.type, r.spoken || '(silent)', r.source].join(' | ').replace(/\n/g, ' ');
            (r.spoken ? spoken : silent).push(line);
        }
    }
    fs.writeFileSync(path.join(outDir, course + '.txt'),
        `# ${course}: ${spoken.length} spoken, ${silent.length} silent\n\n## Silent\n${silent.join('\n')}\n\n## Spoken\n${spoken.join('\n')}\n`);
    summary.push(`${course}: ${spoken.length} spoken, ${silent.length} silent`);
}
console.log(summary.join('\n'));
console.log('Written to ' + outDir);
