# Changelog

## [Unreleased]

### Architecture
- Split monolithic `script.js` into `engine/` modules: `xp.js`, `srs.js`, `reader.js`, `verbs.js`, `lessons.js`, `init.js`.
- Established folder structure: `engine/`, `content/`, `imports/`, `generated/`, `assets/`, `scripts/`, `docs/`.

### Known Issues
- `wordDB` dictionary not loading correctly (review cards show "unknown").
