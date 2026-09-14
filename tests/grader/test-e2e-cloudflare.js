const { GraderEngine } = require('../../engine/grader');

async function runE2E() {
    console.log('Testing GraderEngine with production Cloudflare Worker...');
    const grader = new GraderEngine({
        endpoint: 'https://parlour-grader.gergkar.workers.dev/grade',
        timeout: 30000
    });

    const production = 'El verano pasado fui de vacaciones a Granada con mi familia. La ciudad era hermosa y la Alhambra fue impresionante, aunque hacía demasiado calor.';
    const context = {
        language: 'es',
        target_cefr: 'B1',
        activity_type: 'writing_studio',
        prompt: 'Describe un viaje memorable que hiciste en el pasado.'
    };

    const start = Date.now();
    const result = await grader.grade(production, context);
    const elapsed = ((Date.now() - start) / 1000).toFixed(2);

    console.log(`Grading completed in ${elapsed}s:`);
    console.log('Overall Score:', result.overallScore);
    console.log('Task Completion:', result.taskCompletion);
    console.log('Dimensions:', result.dimensions);
    console.log('Demonstrated Skills:', result.demonstratedSkills);
    console.log('Weak Skills:', result.weakSkills);
    console.log('Errors:', result.errors);
    console.log('Feedback:', result.feedback);
    console.log('Local Stats:', result.localStats);
}

runE2E();
