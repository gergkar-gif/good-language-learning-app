// ==========================================================
// Unit Tests: SEO, Google Discoverability & Sitemap Validation
// ==========================================================
const assert = require('assert');
const fs = require('fs');
const path = require('path');

function assertZeroEmojis(str, contextName) {
    const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{1F1E6}-\u{1F1FF}]/u;
    assert(!emojiRegex.test(str), `Emoji detected in ${contextName}`);
}

const rootDir = path.resolve(__dirname, '../../');

console.log('--- Test 1: robots.txt Integrity ---');
const robotsPath = path.join(rootDir, 'robots.txt');
assert(fs.existsSync(robotsPath), 'robots.txt must exist at workspace root');
const robotsContent = fs.readFileSync(robotsPath, 'utf8');
assertZeroEmojis(robotsContent, 'robots.txt');
assert(robotsContent.includes('User-agent: *'), 'robots.txt must specify User-agent: *');
assert(robotsContent.includes('Allow: /'), 'robots.txt must allow crawling');
assert(robotsContent.includes('Sitemap: https://parlour.me.uk/sitemap.xml'), 'robots.txt must point to sitemap.xml');
console.log('[PASS] robots.txt is valid and points to sitemap.xml.');

console.log('\n--- Test 2: sitemap.xml Integrity ---');
const sitemapPath = path.join(rootDir, 'sitemap.xml');
assert(fs.existsSync(sitemapPath), 'sitemap.xml must exist at workspace root');
const sitemapContent = fs.readFileSync(sitemapPath, 'utf8');
assertZeroEmojis(sitemapContent, 'sitemap.xml');
assert(sitemapContent.includes('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'), 'sitemap.xml must have valid urlset namespace');
assert(sitemapContent.includes('<loc>https://parlour.me.uk/</loc>'), 'sitemap.xml must list root domain');
assert(sitemapContent.includes('<loc>https://parlour.me.uk/privacy.html</loc>'), 'sitemap.xml must list privacy.html');
console.log('[PASS] sitemap.xml is valid and lists canonical URLs.');

console.log('\n--- Test 3: index.html Metadata & Structured Data ---');
const indexPath = path.join(rootDir, 'index.html');
const indexHtml = fs.readFileSync(indexPath, 'utf8');
assertZeroEmojis(indexHtml, 'index.html');

// Canonical and robots
assert(indexHtml.includes('<link rel="canonical" href="https://parlour.me.uk/">'), 'index.html must specify canonical URL');
assert(indexHtml.includes('<meta name="robots" content="index, follow">'), 'index.html must permit indexing');

// Open Graph
assert(indexHtml.includes('<meta property="og:title" content="Parlour — A place for language">'), 'index.html must have og:title');
assert(indexHtml.includes('<meta property="og:url" content="https://parlour.me.uk/">'), 'index.html must have og:url');
assert(indexHtml.includes('<meta property="og:type" content="website">'), 'index.html must have og:type');

// Twitter
assert(indexHtml.includes('<meta name="twitter:card" content="summary">'), 'index.html must have twitter:card');

// Schema.org JSON-LD
const jsonLdMatch = indexHtml.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/);
assert(jsonLdMatch, 'index.html must contain JSON-LD structured data script');
let schemaData;
try {
    schemaData = JSON.parse(jsonLdMatch[1]);
} catch (e) {
    assert.fail(`JSON-LD in index.html is invalid JSON: ${e.message}`);
}
assert.strictEqual(schemaData['@context'], 'https://schema.org', 'Schema context must be schema.org');
assert(Array.isArray(schemaData['@graph']), 'Schema must contain @graph entries');
const webAppEntry = schemaData['@graph'].find(item => item['@type'] === 'WebApplication');
assert(webAppEntry, 'Schema must define WebApplication');
assert.strictEqual(webAppEntry.name, 'Parlour', 'WebApplication name must be Parlour');

// noscript fallback
assert(indexHtml.includes('<noscript>'), 'index.html must include noscript fallback for crawlers');
console.log('[PASS] index.html SEO, social meta, and structured data verified.');

console.log('\n--- Test 4: privacy.html SEO Metadata ---');
const privacyPath = path.join(rootDir, 'privacy.html');
const privacyHtml = fs.readFileSync(privacyPath, 'utf8');
assertZeroEmojis(privacyHtml, 'privacy.html');
assert(privacyHtml.includes('<link rel="canonical" href="https://parlour.me.uk/privacy.html">'), 'privacy.html must specify canonical URL');
assert(privacyHtml.includes('<meta name="robots" content="index, follow">'), 'privacy.html must specify robots directive');
console.log('[PASS] privacy.html SEO metadata verified.');

console.log('\n==========================================================');
console.log('ALL SEO & DISCOVERABILITY TESTS PASSED [Zero Emojis Enforced]');
console.log('==========================================================');
