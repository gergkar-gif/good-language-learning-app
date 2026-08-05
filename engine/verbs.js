// ============================================
// VERB DRILL SYSTEM
// ============================================
let currentVerb = null;
let currentTensePath = 'indicativo.presente';
let includeVosotros = false;

const ALL_TENSE_OPTIONS = [
    'indicativo.presente',
    'indicativo.preterito',
    'indicativo.imperfecto',
    'indicativo.futuro',
    'indicativo.condicional',
    'subjuntivo.presente',
    'subjuntivo.imperfecto',
    'subjuntivo.futuro'
];

const drillVerbs = (typeof ALL_VERBS !== 'undefined') ? ALL_VERBS : ['hablar', 'comer', 'vivir'];

for (let i = drillVerbs.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [drillVerbs[i], drillVerbs[j]] = [drillVerbs[j], drillVerbs[i]];
}

let currentVerbIndex = 0;

function changeTense() {
    const select = document.getElementById('tense-select');
    currentTensePath = select.value;
    if (currentTensePath === 'all') {
        pickRandomTense();
    }
    if (currentVerb) {
        updateDrillDisplay();
        clearDrillInputs();
    }
}

function toggleVosotros() {
    includeVosotros = document.getElementById('vosotros-toggle').checked;
    const switchEl = document.getElementById('vosotros-switch');
    const knob = switchEl.querySelector('span');
    const row = document.getElementById('vosotros-row');

    if (includeVosotros) {
        switchEl.style.background = '#1B4B5A';
        knob.style.left = '18px';
        row.style.display = 'flex';
    } else {
        switchEl.style.background = '#DCE6E8';
        knob.style.left = '2px';
        row.style.display = 'none';
    }

    clearDrillInputs();
}

function pickRandomTense() {
    const randomIndex = Math.floor(Math.random() * ALL_TENSE_OPTIONS.length);
    currentTensePath = ALL_TENSE_OPTIONS[randomIndex];
}

function getTenseDisplayName(path) {
    const map = {
        'indicativo.presente': 'Presente (Indicative)',
        'indicativo.preterito': 'Pretérito (Indicative)',
        'indicativo.imperfecto': 'Imperfecto (Indicative)',
        'indicativo.futuro': 'Futuro (Indicative)',
        'indicativo.condicional': 'Condicional (Indicative)',
        'subjuntivo.presente': 'Presente (Subjunctive)',
        'subjuntivo.imperfecto': 'Imperfecto (Subjunctive)',
        'subjuntivo.futuro': 'Futuro (Subjunctive)'
    };
    return map[path] || path;
}

async function loadVerb(verbName) {
    try {
        const response = await fetch('imports/verbs/' + verbName + '.json');
        currentVerb = await response.json();
        if (document.getElementById('tense-select').value === 'all') {
            pickRandomTense();
        }
        updateDrillDisplay();
        clearDrillInputs();
    } catch (error) {
        console.error('Failed to load verb:', error);
        alert('Could not load verb: ' + verbName);
    }
}

function updateDrillDisplay() {
    const titleEl = document.getElementById('drill-title');
    const meaningEl = document.getElementById('drill-meaning');
    if (titleEl) {
        titleEl.textContent = currentVerb.infinitivo.toUpperCase() + ' — ' + getTenseDisplayName(currentTensePath);
    }
    if (meaningEl && currentVerb.english) {
        meaningEl.textContent = currentVerb.english.infinitivo || '';
    }
}

function clearDrillInputs() {
    const max = includeVosotros ? 6 : 6;
    for (let i = 1; i <= max; i++) {
        const input = document.getElementById('v' + i);
        if (input) {
            input.value = '';
            input.classList.remove('correct', 'wrong');
        }
    }
    const resultDiv = document.getElementById('drill-result');
    if (resultDiv) resultDiv.textContent = '';
}

function nextVerb() {
    currentVerbIndex = (currentVerbIndex + 1) % drillVerbs.length;
    loadVerb(drillVerbs[currentVerbIndex]);
}

function checkDrill() {
    if (!currentVerb) {
        alert('Loading verb data... please wait.');
        return;
    }
    
    const parts = currentTensePath.split('.');
    let tenseData = currentVerb;
    for (const part of parts) {
        tenseData = tenseData[part];
        if (!tenseData) break;
    }
    
    if (!tenseData) {
        alert('Tense not available for this verb: ' + getTenseDisplayName(currentTensePath));
        return;
    }
    
    const persons = includeVosotros
        ? ['yo', 'tu', 'ud', 'nosotros', 'vosotros', 'uds']
        : ['yo', 'tu', 'ud', 'nosotros', 'uds'];
    const total = persons.length;
    let correct = 0;

    for (let i = 0; i < total; i++) {
        const inputId = includeVosotros ? (i + 1) : (i < 4 ? i + 1 : i + 2);
        const input = document.getElementById('v' + inputId).value.toLowerCase().trim();
        const el = document.getElementById('v' + inputId);
        el.classList.remove('correct', 'wrong');
        
        let correctAnswer = tenseData[persons[i]] || '';
        const normalizedInput = input.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
        const normalizedAnswer = correctAnswer.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
        
        if (normalizedInput === normalizedAnswer && input !== '') {
            correct++;
            el.classList.add('correct');
            if (input !== correctAnswer.toLowerCase()) {
                el.value = correctAnswer;
            }
        } else {
            el.classList.add('wrong');
        }
    }
    
    const resultDiv = document.getElementById('drill-result');
    if (correct === total) {
        resultDiv.textContent = '✓ Perfect! ' + total + '/' + total;
        resultDiv.style.color = '#3E8E5B';
    } else {
        resultDiv.textContent = correct + '/' + total + ' correct. Try again!';
        resultDiv.style.color = '#B8412F';
    }
}
