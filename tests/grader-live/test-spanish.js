// ============================================
// SPANISH B2 GRADER TEST SUITE
// ============================================
const path = require('path');
const fs = require('fs');
const { runComparisonSuite } = require('./test-suite-runner');

const fixturesDir = path.join(__dirname, 'fixtures');

const cases = [
    {
        name: 'Spanish B2 Strong Production',
        type: 'strong',
        data: JSON.parse(fs.readFileSync(path.join(fixturesDir, 'es-strong.json'), 'utf8'))
    },
    {
        name: 'Spanish B2 Average Production',
        type: 'average',
        data: JSON.parse(fs.readFileSync(path.join(fixturesDir, 'es-average.json'), 'utf8'))
    },
    {
        name: 'Spanish B2 Weak Production',
        type: 'weak',
        data: JSON.parse(fs.readFileSync(path.join(fixturesDir, 'es-weak.json'), 'utf8'))
    }
];

runComparisonSuite(cases, 'Spanish')
    .then(() => {
        console.log('\n[SUCCESS] Spanish Grader Suite completed successfully.');
        process.exit(0);
    })
    .catch(err => {
        console.error('\n[FAILURE] Spanish Grader Suite failed:', err.message);
        process.exit(1);
    });
