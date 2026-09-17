// ============================================
// PARLOUR GRADER ENGINE
// ============================================
// Dedicated formative production grader:
// - Language-agnostic (Spanish, Hungarian, and future courses)
// - Dual evaluation: instant deterministic local metrics + AI formative grading
// - Multi-endpoint abstraction:
//     * Local dev: OmniRoute on http://localhost:20128 (model: "auto")
//     * Production: Cloudflare Worker on https://parlour-grader.gergkar.workers.dev
// - Resilient transport: timeout, exponential backoff, JSON repair, diagnostic retention
// - Graceful degradation: never crashes Parlour if AI is offline or quota exhausted

(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        define(['./local-grader', './grader-prompt', './schema'], factory);
    } else if (typeof module === 'object' && module.exports) {
        const LocalGrader = require('./local-grader');
        const { buildGraderPrompt } = require('./grader-prompt');
        const { validateAndCleanResult } = require('./schema');
        module.exports = factory(LocalGrader, { buildGraderPrompt }, { validateAndCleanResult });
    } else {
        root.GraderEngine = factory(root.LocalGrader, root.GraderPrompt, root.GraderSchema);
    }
})(typeof self !== 'undefined' ? self : this, function (LocalGrader, GraderPrompt, GraderSchema) {
    'use strict';

    const isNode = typeof process !== 'undefined' && process.versions != null && process.versions.node != null;

    const DEFAULT_PROD_ENDPOINT = 'https://parlour-grader.gergkar.workers.dev/grade';
    const DEFAULT_LOCAL_ENDPOINT = 'http://localhost:20128/v1/chat/completions';

    class GraderEngine {
        constructor(options) {
            const opts = options || {};

            if (isNode) {
                this.endpoint = opts.endpoint || process.env.GRADER_ENDPOINT || process.env.OMNIROUTE_URL || DEFAULT_LOCAL_ENDPOINT;
                this.apiKey = opts.apiKey || process.env.GRADER_API_KEY || process.env.OMNIROUTE_API_KEY || 'parlour-local';
                this.maxRetries = Number(opts.maxRetries != null ? opts.maxRetries : (process.env.OMNIROUTE_MAX_RETRIES || 1));
                this.timeout = Number(opts.timeout || process.env.OMNIROUTE_TIMEOUT || 35000);
                this.model = opts.model || process.env.GRADER_MODEL || 'auto';
            } else {
                // In browser
                const devOverride = (typeof localStorage !== 'undefined') ? localStorage.getItem('grader_endpoint') : null;
                const devKey = (typeof localStorage !== 'undefined') ? localStorage.getItem('grader_api_key') : null;

                this.endpoint = opts.endpoint || devOverride || DEFAULT_PROD_ENDPOINT;
                this.apiKey = opts.apiKey || devKey || (this.isLocalDev() ? 'parlour-local' : null);
                this.maxRetries = Number(opts.maxRetries != null ? opts.maxRetries : 1);
                this.timeout = Number(opts.timeout || 35000);
                this.model = opts.model || 'auto';
            }

            // Normalise URL
            if (this.endpoint.endsWith('/')) {
                this.endpoint = this.endpoint.slice(0, -1);
            }
            if (this.endpoint === 'http://localhost:20128') {
                this.endpoint = DEFAULT_LOCAL_ENDPOINT;
            }
        }

        isLocalDev() {
            return typeof this.endpoint === 'string' && (
                this.endpoint.includes('localhost') ||
                this.endpoint.includes('127.0.0.1')
            );
        }

        /**
         * Universal grading method.
         * Accepts:
         *   grade(productionText, context)
         * or prototype signature:
         *   grade(cefrLevel, taskType, taskInstructions, targetSkills, learnerProduction, retryCount)
         */
        async grade(arg1, arg2, arg3, arg4, arg5, arg6) {
            let productionText = '';
            let context = {};
            let retryCount = 0;

            if (typeof arg1 === 'string' && (arg2 && typeof arg2 === 'object') && !arg3) {
                // Modern API: grade(productionText, context)
                productionText = arg1;
                context = Object.assign({}, arg2);
                retryCount = context.retryCount || 0;
            } else {
                // Prototype / positional signature:
                // grade(cefrLevel, taskType, taskInstructions, targetSkills, learnerProduction, retryCount)
                context = {
                    cefrLevel: arg1,
                    taskType: arg2,
                    taskInstructions: arg3,
                    targetSkills: arg4
                };
                productionText = arg5 || '';
                retryCount = typeof arg6 === 'number' ? arg6 : 0;
            }

            const cefrLevel = (context.cefrLevel || 'B2').toUpperCase();
            const taskType = context.taskType || 'extended_production';
            const taskInstructions = context.taskInstructions || 'Complete the task appropriately in the target language.';
            const targetSkills = context.targetSkills || [];
            const language = context.language || (typeof Lang !== 'undefined' ? Lang.code() : 'es');
            const modality = context.modality || (context.isSpeaking || (taskType && String(taskType).toLowerCase().includes('oral')) ? 'oral' : 'written');
            const taskCompletionPrimary = !!context.taskCompletionPrimary;

            // 1. Instant deterministic local analysis
            const localStats = LocalGrader
                ? LocalGrader.analyze(productionText, { cefrLevel, modality })
                : { wordCount: productionText.split(/\s+/).length, targetWordCountMet: true };

            // 2. Perform AI formative evaluation
            try {
                const aiResult = await this._callAiGrader({
                    cefrLevel,
                    taskType,
                    taskInstructions,
                    targetSkills,
                    learnerProduction: productionText,
                    language,
                    modality,
                    taskCompletionPrimary,
                    retryCount
                });

                // Attach deterministic metrics & metadata
                aiResult.localStats = localStats;
                aiResult.aiEvaluated = true;
                aiResult.meta = {
                    evaluatedAt: new Date().toISOString(),
                    cefrLevel,
                    taskType,
                    language,
                    modality
                };

                return aiResult;
            } catch (error) {
                // If caller explicitly wants throw on error (e.g. unit tests or diagnostic suites)
                if (context.throwOnError || isNode) {
                    throw error;
                }

                // Graceful client-side fallback: never crash Parlour UI on AI network failure or quota exhaustion
                console.warn('AI Grading unavailable; providing local assessment:', error.message);
                return this._fallbackAssessment(productionText, cefrLevel, localStats, error.message);
            }
        }

        async _callAiGrader(params) {
            const {
                cefrLevel,
                taskType,
                taskInstructions,
                targetSkills,
                learnerProduction,
                language,
                modality,
                taskCompletionPrimary,
                retryCount
            } = params;

            let prompt = GraderPrompt.buildGraderPrompt(
                cefrLevel,
                taskType,
                taskInstructions,
                targetSkills,
                learnerProduction,
                { language, modality, taskType, taskCompletionPrimary }
            );

            if (retryCount > 0) {
                prompt += `\n\nRETRY OUTPUT REQUIREMENT:\nThis is a retry after invalid model output. Return ONLY a compact, valid JSON object.\nDo not include Markdown fences or extra commentary. Never use unescaped double quotes inside string values (use single quotes 'word' or backticks instead). Keep all fields concise.`;
            }

            const isChatCompletions = this.endpoint.endsWith('/chat/completions') || this.isLocalDev();
            let response;
            let timeoutId;

            try {
                const controller = new AbortController();
                timeoutId = setTimeout(() => controller.abort(), this.timeout);

                const headers = { 'Content-Type': 'application/json' };
                if (this.apiKey) {
                    headers['Authorization'] = `Bearer ${this.apiKey}`;
                }

                let body;
                if (isChatCompletions) {
                    body = JSON.stringify({
                        model: this.model,
                        messages: [
                            {
                                role: 'system',
                                content: 'You are an expert CEFR-aligned language-learning grader. Return only valid JSON.'
                            },
                            { role: 'user', content: prompt }
                        ],
                        temperature: 0,
                        max_tokens: 3000,
                        response_format: { type: 'json_object' }
                    });
                } else {
                    // Custom Cloudflare Worker /grade endpoint
                    body = JSON.stringify({
                        cefrLevel,
                        taskType,
                        taskInstructions,
                        targetSkills,
                        learnerProduction,
                        language,
                        modality,
                        prompt
                    });
                }

                response = await fetch(this.endpoint, {
                    method: 'POST',
                    headers,
                    body,
                    signal: controller.signal
                });
            } catch (networkError) {
                if (networkError.name === 'AbortError') {
                    throw new Error(`Grader request timed out after ${this.timeout}ms`);
                }
                if (retryCount < this.maxRetries) {
                    await this._sleep(this._backoff(retryCount));
                    return this._callAiGrader(Object.assign({}, params, { retryCount: retryCount + 1 }));
                }
                throw networkError;
            } finally {
                clearTimeout(timeoutId);
            }

            if (!response.ok) {
                const errorText = await response.text().catch(() => '');
                if ((response.status === 429 || response.status >= 500) && retryCount < this.maxRetries) {
                    await this._sleep(this._backoff(retryCount));
                    return this._callAiGrader(Object.assign({}, params, { retryCount: retryCount + 1 }));
                }
                throw new Error(`HTTP ${response.status}${errorText ? `: ${errorText.slice(0, 300)}` : ''}`);
            }

            let responseData;
            try {
                responseData = await response.json();
            } catch {
                throw new Error('Grader endpoint returned invalid non-JSON response');
            }

            // Extract content from either OpenAI chat completions or direct Cloudflare Worker shape
            let contentString = '';
            if (responseData && responseData.choices && responseData.choices[0] && responseData.choices[0].message) {
                contentString = responseData.choices[0].message.content;
            } else if (responseData && typeof responseData.content === 'string') {
                contentString = responseData.content;
            } else if (responseData && typeof responseData.overallScore === 'number') {
                // Direct assessment object already parsed by worker
                return GraderSchema.validateAndCleanResult(responseData);
            } else {
                throw new Error('Grader response structure unrecognized');
            }

            try {
                const parsedObject = this._parseJson(contentString);
                return GraderSchema.validateAndCleanResult(parsedObject);
            } catch (parseError) {
                parseError.rawContent = contentString;
                parseError.omniRouteData = responseData;
                if (retryCount < this.maxRetries) {
                    await this._sleep(this._backoff(retryCount));
                    return this._callAiGrader(Object.assign({}, params, { retryCount: retryCount + 1 }));
                }
                throw parseError;
            }
        }

        /**
         * Robust JSON parser that repairs common LLM output anomalies:
         * - Markdown fence stripping
         * - Outer brace slicing (ignoring surrounding conversational prose)
         * - Trailing comma cleanup
         */
        _parseJson(content) {
            let cleaned = String(content || '')
                .trim()
                .replace(/^```(?:json)?\s*/i, '')
                .replace(/\s*```$/i, '')
                .trim();

            const candidates = [cleaned];

            const firstBrace = cleaned.indexOf('{');
            const lastBrace = cleaned.lastIndexOf('}');
            if (firstBrace !== -1 && lastBrace > firstBrace) {
                candidates.push(cleaned.slice(firstBrace, lastBrace + 1));
            }

            // Remove trailing commas before } or ]
            candidates.push(cleaned.replace(/,\s*([}\]])/g, '$1'));

            if (firstBrace !== -1 && lastBrace > firstBrace) {
                candidates.push(cleaned.slice(firstBrace, lastBrace + 1).replace(/,\s*([}\]])/g, '$1'));
            }

            // Also generate repaired versions for unescaped quotes inside JSON string values
            const repaired = [];
            for (const cand of candidates) {
                const fixed = this._repairUnescapedQuotes(cand);
                if (fixed !== cand) {
                    repaired.push(fixed);
                }
            }
            candidates.push(...repaired);

            for (const cand of candidates) {
                try {
                    return JSON.parse(cand);
                } catch (e) {}
            }

            throw new Error('Failed to parse grader JSON: no valid JSON object found');
        }

        /**
         * Repairs unescaped internal double quotes within JSON string values
         * (e.g. "explanation": "The verb "hacer" is irregular." -> "explanation": "The verb 'hacer' is irregular.")
         */
        _repairUnescapedQuotes(jsonStr) {
            const lines = String(jsonStr || '').split(/\r?\n/);
            const fixedLines = lines.map(line => {
                // Match property line:  "key": "value..."
                const propMatch = line.match(/^(\s*"[a-zA-Z0-9_]+"\s*:\s*")(.*)("(?:\s*,)?\s*)$/);
                if (propMatch) {
                    const prefix = propMatch[1];
                    const middle = propMatch[2];
                    const suffix = propMatch[3];
                    const fixedMiddle = middle.replace(/(?<!\\)"/g, "'");
                    return prefix + fixedMiddle + suffix;
                }

                // Match array string items on their own line:  "value..."
                const arrayStrMatch = line.match(/^(\s*")(.*)("(?:\s*,)?\s*)$/);
                if (arrayStrMatch) {
                    const prefix = arrayStrMatch[1];
                    const middle = arrayStrMatch[2];
                    const suffix = arrayStrMatch[3];
                    const fixedMiddle = middle.replace(/(?<!\\)"/g, "'");
                    return prefix + fixedMiddle + suffix;
                }

                // Match single-line array with strings: "key": ["val1", "val2"...]
                const inlineArrayMatch = line.match(/^(\s*"[a-zA-Z0-9_]+"\s*:\s*\[)(.*)(\](?:\s*,)?\s*)$/);
                if (inlineArrayMatch) {
                    const prefix = inlineArrayMatch[1];
                    const content = inlineArrayMatch[2];
                    const suffix = inlineArrayMatch[3];
                    const fixedContent = content.replace(/"(.*?)"(?=\s*(?:,|$))/g, (m, inner) => {
                        const fixedInner = inner.replace(/(?<!\\)"/g, "'");
                        return `"${fixedInner}"`;
                    });
                    return prefix + fixedContent + suffix;
                }

                return line;
            });
            return fixedLines.join('\n');
        }

        _fallbackAssessment(productionText, cefrLevel, localStats, reason) {
            const hasMinWords = localStats.wordCount >= (localStats.targetRange ? localStats.targetRange.min : 30);
            const baseScore = hasMinWords ? 70 : 50;

            return {
                overallScore: baseScore,
                taskCompletion: hasMinWords ? 0.75 : 0.5,
                dimensions: {
                    grammar: 0.7,
                    vocabulary: 0.7,
                    coherence: 0.7,
                    complexity: 0.7,
                    naturalness: 0.7
                },
                errors: [],
                demonstratedSkills: [],
                weakSkills: [],
                feedback: {
                    strengths: [
                        localStats.lengthFeedback,
                        `Produced ${localStats.wordCount} words across ${localStats.sentenceCount} sentences.`
                    ],
                    priorities: [
                        'AI detailed evaluation is temporarily unavailable; practice continued locally.'
                    ]
                },
                localStats,
                aiEvaluated: false,
                offline: true,
                warning: reason
            };
        }

        _backoff(retryCount) {
            return Math.min(8000, 1000 * Math.pow(2, retryCount));
        }

        _sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }
    }

    return GraderEngine;
});
