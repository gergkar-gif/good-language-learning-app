// ==========================================================
// Parlour Service Worker (Offline Support & PWA App Shell)
// ==========================================================

const CACHE_VERSION = 'v2026-09-24u';
const SHELL_CACHE_NAME = `parlour-shell-${CACHE_VERSION}`;
const CONTENT_CACHE_NAME = `parlour-content-${CACHE_VERSION}`;

// Core application shell assets cached immediately on installation
const PRECACHE_ASSETS = [
    './',
    'index.html',
    'manifest.webmanifest',
    'assets/icons/favicon.svg',

    // Stylesheets
    'styles/base.css',
    'styles/geometry.css',
    'styles/components.css',
    'styles/layout.css',
    'styles/utilities.css',
    'styles/verbs.css',
    'styles/workshop.css',
    'styles/study-plan.css',

    // Core Engine & Submodules
    'imports/verbs/verb-list.js',
    'engine/lang.js',
    'engine/xp.js',
    'engine/morphology/hungarian.js',
    'engine/morphology/spanish.js',
    'engine/lexicon.js',
    'engine/srs.js',
    'engine/content-loader.js',
    'engine/ui.js',
    'engine/art.js',
    'engine/theme.js',
    'engine/sound.js',
    'engine/geo.js',
    'engine/page-header.js',
    'engine/speech.js',
    'engine/tts.js',
    'engine/speech-input.js',
    'engine/reader.js',
    'engine/drillHistory.js',
    'engine/verbs/stats.js',
    'engine/verbs/leaderboard.js',
    'engine/verbs/table.js',
    'engine/verbs/speed.js',
    'engine/verbs.js',
    'engine/drills/grammar-runner.js',
    'engine/drills/grammar.js',
    'engine/drills/translation-runner.js',
    'engine/drills/translation.js',
    'engine/drills/vocabulary.js',
    'engine/drills/listening-runner.js',
    'engine/drills/listening.js',
    'engine/canDoPrompt.js',
    'engine/drills/speaking-runner.js',
    'engine/drills/speaking.js',
    'engine/grader/local-grader.js',
    'engine/grader/grader-prompt.js',
    'engine/grader/schema.js',
    'engine/grader/grader-engine.js',
    'engine/grader/index.js',
    'engine/drills/writing.js',
    'engine/drills/hu-suffix.js',
    'engine/drills/hu-prefix.js',
    'engine/drills/hu-morphology.js',
    'engine/drills/hu-verb.js',
    'engine/drills/hu-verb-studio.js',
    'engine/workshop.js',
    'engine/lessons.js',
    'engine/progress.js',
    'engine/learnerPath.js',
    'engine/recycle.js',
    'engine/leveltest.js',
    'engine/diagnostic.js',
    'engine/learnerModel.js',
    'engine/recommend.js',
    'engine/recommendationEngine.js',
    'engine/studyPlan.js',
    'engine/journey.js',
    'engine/decks/match.js',
    'engine/decks/learn.js',
    'engine/decks.js',
    'engine/studyPlanRunner.js',
    'engine/curriculum.js',
    'engine/library.js',
    'engine/guide.js',
    'engine/home.js',
    'engine/sync.js',
    'engine/init.js',
    'engine/bugreport.js',

    // Core manifests & tests
    'content/es-latam/curriculum/curriculum.json',
    'content/es-es/curriculum/curriculum.json',
    'content/hu/curriculum/curriculum.json',
    'content/es-latam/stories/manifest.json',
    'content/es-es/stories/manifest.json',
    'content/hu/stories/manifest.json',
    'content/es-latam/decks/decks.json',
    'content/es-es/decks/decks.json',
    'content/hu/decks/decks.json',
    'content/es-latam/tests/diagnostic-test.json',
    'content/es-es/tests/diagnostic-test.json',
    'content/hu/tests/diagnostic-test.json'
];

// ----------------------------------------------------------
// 1. INSTALLATION
// ----------------------------------------------------------
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(SHELL_CACHE_NAME).then(cache => {
            return cache.addAll(PRECACHE_ASSETS);
        }).then(() => {
            return self.skipWaiting();
        }).catch(err => {
            console.error('ServiceWorker precache failed:', err);
        })
    );
});

// ----------------------------------------------------------
// 2. ACTIVATION & CACHE CLEANUP
// ----------------------------------------------------------
self.addEventListener('activate', event => {
    const validCaches = [SHELL_CACHE_NAME, CONTENT_CACHE_NAME];
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys.map(key => {
                    if (!validCaches.includes(key)) {
                        return caches.delete(key);
                    }
                })
            );
        }).then(() => {
            return self.clients.claim();
        })
    );
});

// ----------------------------------------------------------
// 3. FETCH STRATEGIES
// ----------------------------------------------------------
self.addEventListener('fetch', event => {
    const request = event.request;

    // Only process GET requests
    if (request.method !== 'GET') return;

    const url = new URL(request.url);

    // Bypass external requests (Cloudflare Worker sync, Resend, AI APIs)
    if (url.origin !== self.location.origin) {
        return;
    }

    // A. Navigation requests: return cached index.html if network is unreachable
    if (request.mode === 'navigate') {
        event.respondWith(
            fetch(request).catch(() => {
                return caches.match('./index.html', { ignoreSearch: true })
                    .then(res => res || caches.match('index.html', { ignoreSearch: true }));
            })
        );
        return;
    }

    // B. Dynamic Content (lessons, grammar, stories, dictionary)
    // Strategy: Stale-While-Revalidate (Instant response from cache, background refresh)
    if (url.pathname.includes('/content/')) {
        event.respondWith(
            caches.match(request, { ignoreSearch: true }).then(cachedResponse => {
                const fetchPromise = fetch(request).then(networkResponse => {
                    if (networkResponse && networkResponse.status === 200) {
                        const clone = networkResponse.clone();
                        caches.open(CONTENT_CACHE_NAME).then(cache => {
                            cache.put(request, clone);
                        });
                    }
                    return networkResponse;
                }).catch(() => cachedResponse);

                return cachedResponse || fetchPromise;
            })
        );
        return;
    }

    // C. App Shell (HTML, CSS, JS, icons)
    // Strategy: Stale-While-Revalidate with Precache
    event.respondWith(
        caches.match(request, { ignoreSearch: true }).then(cachedResponse => {
            const fetchPromise = fetch(request).then(networkResponse => {
                if (networkResponse && networkResponse.status === 200) {
                    const responseClone = networkResponse.clone();
                    caches.open(SHELL_CACHE_NAME).then(cache => {
                        cache.put(request, responseClone);
                    });
                }
                return networkResponse;
            }).catch(() => {
                // Offline and no network - return cachedResponse if present
            });

            return cachedResponse || fetchPromise;
        })
    );
});

// ----------------------------------------------------------
// 4. MESSAGE EVENT
// ----------------------------------------------------------
self.addEventListener('message', event => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
});
