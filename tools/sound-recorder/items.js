// The recording list for lesson.a1.01's sound tables, shared by index.html
// (recording) and review.html (checking the processed clips). `id` becomes the file
// name (tools/sound-recorder/recordings/<id>.wav).
const VOWEL_HINT = 'Just the sound, not a word — about half a second.';
const LONG_HINT = 'Just the sound, held clearly longer than the short one.';
const GROUPS = [
  ['Vowels on their own', [
    ['vowel-a', 'a', VOWEL_HINT], ['vowel-a-long', 'á', LONG_HINT],
    ['vowel-e', 'e', VOWEL_HINT], ['vowel-e-long', 'é', LONG_HINT],
    ['vowel-i', 'i', VOWEL_HINT], ['vowel-i-long', 'í', LONG_HINT],
    ['vowel-o', 'o', VOWEL_HINT], ['vowel-o-long', 'ó', LONG_HINT],
    ['vowel-oe', 'ö', VOWEL_HINT], ['vowel-oe-long', 'ő', LONG_HINT],
    ['vowel-u', 'u', VOWEL_HINT], ['vowel-u-long', 'ú', LONG_HINT],
    ['vowel-ue', 'ü', VOWEL_HINT], ['vowel-ue-long', 'ű', LONG_HINT],
  ]],
  ['Words', [
    ['word-hat', 'hat'], ['word-hat-long', 'hát'], ['word-lat', 'lát'],
    ['word-szel', 'szel'], ['word-szel-long', 'szél'], ['word-resz', 'rész'],
    ['word-irt', 'irt'], ['word-irt-long', 'írt'], ['word-viz', 'víz'],
    ['word-kor', 'kor'], ['word-kor-long', 'kór'], ['word-to', 'tó'],
    ['word-tor', 'tör'], ['word-tor-long', 'tőr'], ['word-bor-long', 'bőr'],
    ['word-hurok', 'hurok'], ['word-hurok-long', 'húrok'], ['word-kut', 'kút'],
    ['word-ut', 'üt'], ['word-ur-long', 'űr'], ['word-tuz', 'tűz'],
  ].map(([id, say]) => [id, say, 'Normal pace, one clear take.'])],
  ['Consonants you can hold', [
    ['held-sz', 'sz', 'Hold it about a second: “ssss” — no vowel before or after.'],
    ['held-s', 's', 'Hold it about a second: “shhh” — no vowel before or after.'],
    ['held-zs', 'zs', 'Hold it about a second: the s in “measure” — no vowel.'],
  ]],
  ['Consonant words', [
    ['word-szia', 'szia'], ['word-so', 'só'], ['word-zseb', 'zseb'], ['word-csak', 'csak'],
    ['word-cel', 'cél'], ['word-gyar', 'gyár'], ['word-nyar', 'nyár'], ['word-tyuk', 'tyúk'],
    ['word-kiraly', 'király'], ['word-jo', 'jó'],
  ].map(([id, say]) => [id, say, 'Normal pace, one clear take.'])],
];
const ITEMS = GROUPS.flatMap(([group, items]) => items.map(([id, say, hint]) => ({ id, say, hint, group })));

