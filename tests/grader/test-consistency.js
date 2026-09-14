// ============================================
// REPEATABILITY & CONSISTENCY TEST
// ============================================
const path = require('path');
const fs = require('fs');
const { GraderEngine } = require('../../engine/grader');

const fixturesDir = path.join(__dirname, 'fixtures');
const input = JSON.parse(fs.readFileSync(path.join(fixturesDir, 'es-strong.json'), 'utf8'));

async function main() {
    const runs = Number(process.env.CONSISTENCY_RUNS || 3);
    const grader = new GraderEngine();
    const scores = [];

    console.log(`\n============================================`);
    console.log(`RUNNING CONSISTENCY TEST (${runs} runs on Strong Spanish B2)`);
    console.log(`============================================`);

    for (let i = 1; i <= runs; i++) {
        process.stdout.write(`Run ${i}/${runs}... `);
        const start = Date.now();
        const result = await grader.grade(
            input.cefrLevel,
            input.taskType,
            input.taskInstructions,
            input.targetSkills,
            input.learnerProduction,
            0
        );
        const duration = ((Date.now() - start) / 1000).toFixed(1);
        scores.push(result.overallScore);
        console.log(`Score: ${result.overallScore} (${duration}s)`);
    }

    const min = Math.min(...scores);
    const max = Math.max(...scores);
    const mean = scores.reduce((a, b) => a + b, 0) / scores.length;
    const range = max - min;

    console.log(`\n--------------------------------------------`);
    console.log(`RESULTS:`);
    console.log(`Scores: ${scores.join(', ')}`);
    console.log(`Mean:   ${mean.toFixed(1)}`);
    console.log(`Range:  ${range.toFixed(1)} points`);

    if (range > 15) {
        throw new Error(`Variance too high: range is ${range} points (expected <= 15 points)`);
    }

    console.log(`\n[SUCCESS] Consistency test passed with tight score range (${range.toFixed(1)} pts).`);
}

main()
    .then(() => process.exit(0))
    .catch(err => {
        console.error('\n[FAILURE] Consistency test failed:', err.message);
        process.exit(1);
    });
