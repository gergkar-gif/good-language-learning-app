// ============================================
// TEST SUITE RUNNER UTILITY
// ============================================
const fs = require('fs');
const path = require('path');
const { GraderEngine } = require('../../engine/grader');

function printResult(name, result) {
    console.log(`\n--------------------------------------------`);
    console.log(`CASE: ${name}`);
    console.log(`Overall Score: ${result.overallScore} / 100`);
    console.log(`Task Completion: ${(result.taskCompletion * 100).toFixed(0)}%`);
    console.log(`Dimensions:`);
    for (const [dim, val] of Object.entries(result.dimensions || {})) {
        console.log(`  - ${dim}: ${(val * 100).toFixed(0)}%`);
    }
    console.log(`Demonstrated Skills: ${(result.demonstratedSkills || []).map(s => `${s.skillId} (${(s.confidence * 100).toFixed(0)}%)`).join(', ') || 'none'}`);
    console.log(`Weak Skills: ${(result.weakSkills || []).map(s => `${s.skillId} (${(s.confidence * 100).toFixed(0)}%)`).join(', ') || 'none'}`);
    console.log(`Errors: ${(result.errors || []).length}`);
    (result.errors || []).forEach(e => {
        console.log(`  * [${e.category}/${e.severity}] "${e.text}": ${e.explanation} ${e.skillId ? `(Skill: ${e.skillId})` : ''}`);
    });
    console.log(`Strengths: ${(result.feedback && result.feedback.strengths) ? result.feedback.strengths.join('; ') : 'none'}`);
    console.log(`Priorities: ${(result.feedback && result.feedback.priorities) ? result.feedback.priorities.join('; ') : 'none'}`);
    if (result.localStats) {
        console.log(`Local Stats: ${result.localStats.wordCount} words, ${result.localStats.sentenceCount} sentences, ${result.localStats.avgSentenceLength} words/sentence`);
    }
}

async function runComparisonSuite(cases, languageLabel) {
    console.log(`\n============================================`);
    console.log(`RUNNING ${languageLabel.toUpperCase()} GRADER SUITE`);
    console.log(`Endpoint: ${process.env.GRADER_ENDPOINT || process.env.OMNIROUTE_URL || 'http://localhost:20128'}`);
    console.log(`============================================`);

    const grader = new GraderEngine();
    const results = [];

    for (const c of cases) {
        console.log(`\nEvaluating: ${c.name}...`);
        try {
            const result = await grader.grade(
                c.data.cefrLevel,
                c.data.taskType,
                c.data.taskInstructions,
                c.data.targetSkills,
                c.data.learnerProduction,
                0
            );
            results.push({ name: c.name, type: c.type, result });
            printResult(c.name, result);
        } catch (err) {
            console.error(`FAILED ${c.name}:`, err.message);
            results.push({ name: c.name, type: c.type, error: err.message });
        }
    }

    // Comparison analysis
    console.log(`\n============================================`);
    console.log(`${languageLabel.toUpperCase()} SUMMARY & ORDERING CHECK`);
    console.log(`============================================`);

    const strongCase = results.find(r => r.type === 'strong' && r.result);
    const avgCase = results.find(r => r.type === 'average' && r.result);
    const weakCase = results.find(r => r.type === 'weak' && r.result);

    if (strongCase && avgCase && weakCase) {
        const sScore = strongCase.result.overallScore;
        const aScore = avgCase.result.overallScore;
        const wScore = weakCase.result.overallScore;

        console.log(`Strong Score:  ${sScore}`);
        console.log(`Average Score: ${aScore}`);
        console.log(`Weak Score:    ${wScore}`);

        const isOrdered = sScore > aScore && aScore > wScore;
        console.log(`\nMonotonic ordering (Strong > Average > Weak): ${isOrdered ? 'PASS' : 'FAIL'}`);
        console.log(`Strong vs Average Gap: ${(sScore - aScore).toFixed(1)} points`);
        console.log(`Average vs Weak Gap:   ${(aScore - wScore).toFixed(1)} points`);

        if (!isOrdered) {
            throw new Error(`Score ordering failure: Strong=${sScore}, Average=${aScore}, Weak=${wScore}`);
        }
    } else {
        throw new Error(`One or more test cases did not complete successfully`);
    }

    return results;
}

module.exports = {
    runComparisonSuite,
    printResult
};
