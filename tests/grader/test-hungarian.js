// ============================================
// HUNGARIAN B2 GRADER TEST SUITE
// ============================================
const path = require('path');
const fs = require('fs');
const { runComparisonSuite } = require('./test-suite-runner');

const fixturesDir = path.join(__dirname, 'fixtures');

const cases = [
    {
        name: 'Hungarian B2 Strong Production',
        type: 'strong',
        data: JSON.parse(fs.readFileSync(path.join(fixturesDir, 'hu-strong.json'), 'utf8'))
    },
    {
        name: 'Hungarian B2 Average Production',
        type: 'average',
        data: JSON.parse(fs.readFileSync(path.join(fixturesDir, 'hu-average.json'), 'utf8'))
    },
    {
        name: 'Hungarian B2 Weak Production',
        type: 'weak',
        data: JSON.parse(fs.readFileSync(path.join(fixturesDir, 'hu-weak.json'), 'utf8'))
    }
];

runComparisonSuite(cases, 'Hungarian')
    .then(() => {
        console.log('\n[SUCCESS] Hungarian Grader Suite completed successfully.');
        process.exit(0);
    })
    .catch(err => {
        console.error('\n[FAILURE] Hungarian Grader Suite failed:', err.message);
        process.exit(1);
    });
