// ============================================
// GRADER ENGINE PACKAGE ENTRY POINT
// ============================================

(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        define(['./local-grader', './grader-prompt', './schema', './grader-engine'], factory);
    } else if (typeof module === 'object' && module.exports) {
        const LocalGrader = require('./local-grader');
        const GraderPrompt = require('./grader-prompt');
        const GraderSchema = require('./schema');
        const GraderEngine = require('./grader-engine');
        module.exports = {
            LocalGrader,
            GraderPrompt,
            GraderSchema,
            GraderEngine
        };
    } else {
        // Browser globals already exposed by individual scripts
        root.ParlourGrader = {
            LocalGrader: root.LocalGrader,
            GraderPrompt: root.GraderPrompt,
            GraderSchema: root.GraderSchema,
            GraderEngine: root.GraderEngine
        };
    }
})(typeof self !== 'undefined' ? self : this, function (LocalGrader, GraderPrompt, GraderSchema, GraderEngine) {
    return {
        LocalGrader,
        GraderPrompt,
        GraderSchema,
        GraderEngine
    };
});
