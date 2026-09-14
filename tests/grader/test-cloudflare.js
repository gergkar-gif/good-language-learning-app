async function testWorker() {
    console.log('Sending request to https://parlour-grader.gergkar.workers.dev/grade ...');
    const start = Date.now();
    try {
        const res = await fetch('https://parlour-grader.gergkar.workers.dev/grade', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                prompt: 'You are a grader. Evaluate this student text: "Hola, me llamo Carlos y vivo en Madrid." Return valid JSON with keys: cefr_estimate, strengths, suggestions.'
            })
        });
        const elapsed = ((Date.now() - start) / 1000).toFixed(2);
        console.log(`HTTP ${res.status} in ${elapsed}s`);
        const json = await res.json();
        console.log('Response:');
        console.log(JSON.stringify(json, null, 2));
    } catch (err) {
        console.error('Error:', err);
    }
}

testWorker();
