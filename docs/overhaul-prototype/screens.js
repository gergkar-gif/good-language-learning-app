/* Parlour overhaul prototype: rough pass. Placeholder content, not app data. */
(function () {
  var $ = function (id) { return document.getElementById(id); };

  /* ---------- nav icons ---------- */
  var ICON = {
    home: '<path class="nl" style="stroke-width:1.5" d="M8 3V29"/><path class="n" d="M8 7V29H24z"/><path class="nl" style="stroke-width:1.2" d="M8 5A24 24 0 0 1 30 29"/><circle class="o" cx="12.5" cy="23" r="2.2"/>',
    lessons: '<path class="n" d="M3 26a10 10 0 0 1 20 0z"/><path class="nl" d="M13 16 27 5M23 26 27 5M3 26.8h26"/><circle class="o" cx="27" cy="5.5" r="3.4"/>',
    library: '<rect class="n" x="3" y="10" width="4.5" height="18"/><rect class="n" x="10" y="3" width="4.5" height="25"/><rect class="nl" x="17.8" y="13" width="3.9" height="15"/><rect class="n" x="24" y="8" width="4.5" height="20"/><circle class="o" cx="19.5" cy="9" r="4.2"/>',
    workshop: '<path class="nl" d="M2 26 30 12" style="stroke-width:2.2"/><circle class="n" cx="15" cy="19" r="5.6"/><rect class="o" x="21" y="3" width="8" height="8"/>',
    decks: '<rect class="nl" x="11" y="3" width="16" height="20"/><rect class="nl" x="6.5" y="7.5" width="16" height="20"/><rect class="n" x="2" y="12" width="16" height="17"/><path class="ol" d="M27 3v20"/>',
    journey: '<circle class="n" cx="5" cy="26" r="3"/><path class="nl" d="M5 26C14 26 13 12 24 11" style="stroke-width:2"/><rect class="o" x="22" y="6" width="7" height="7"/>'
  };
  var NAV = [['home', 'Home'], ['lessons', 'Lessons'], ['library', 'Library'], ['workshop', 'Workshop'], ['decks', 'Decks'], ['journey', 'Journey']];

  /* ---------- hero art (one gesture per page) ---------- */
  function hero(inner) { return '<svg class="hero" viewBox="0 0 252 184" preserveAspectRatio="xMaxYMin meet" aria-hidden="true">' + inner + '</svg>'; }
  var HERO = {
    // Home: the app's door. Vermilion half-disc, navy door, outlined open leaf, knob.
    home: hero('<circle class="sand" cx="184" cy="72" r="64"/><path class="navs" stroke-width="1.2" d="M128 62A108 108 0 0 1 236 170"/><path class="navf" d="M128 62V170H202z"/><path class="navs" stroke-width="2" d="M128 40V170M128 62H236"/><path class="navs" stroke-width="1.2" d="M202 170 116 46"/><g class="rise"><circle class="vf" cx="149" cy="142" r="6"/></g><path class="navs" stroke-width="1.2" d="M20 170h232"/>'),
    lessons: hero('<circle class="sand" cx="176" cy="52" r="70"/><path class="navf" d="M44 170a72 72 0 0 1 144 0z"/><path class="navs" stroke-width="1.2" d="M96 118 204 44M188 170 204 44M20 170h232"/><g class="rise"><circle class="vf" cx="204" cy="44" r="8"/></g>'),
    library: hero('<circle class="sand" cx="176" cy="64" r="58"/><rect class="navf" x="96" y="92" width="15" height="78"/><rect class="navf" x="118" y="48" width="15" height="122"/><rect class="navs" stroke-width="1.5" x="141" y="106" width="13" height="64"/><rect class="navf" x="161" y="76" width="15" height="94"/><path class="navs" d="M76 170h176"/><g class="rise"><circle class="vf" cx="150" cy="60" r="9"/></g>'),
    workshop: hero('<circle class="sand" cx="178" cy="58" r="62"/><path class="navs" stroke-width="2" d="M48 162 232 88"/><circle class="navf" cx="132" cy="124" r="22"/><g class="rise"><rect class="vf" x="188" y="56" width="20" height="20"/></g>'),
    decks: hero('<circle class="sand" cx="182" cy="52" r="58"/><rect class="navs" stroke-width="1.5" x="128" y="22" width="66" height="102"/><rect class="navs" stroke-width="1.5" x="108" y="46" width="66" height="102"/><rect class="navf" x="88" y="70" width="66" height="100"/><g class="rise"><path class="vs" stroke-width="2.5" d="M194 22v102"/></g><path class="navs" d="M60 170h192"/>'),
    journey: hero('<circle class="sand" cx="176" cy="64" r="64"/><circle class="navf" cx="72" cy="162" r="7"/><path class="navs" stroke-width="2" d="M72 162C124 162 122 76 208 66"/><g class="rise"><rect class="vf" x="206" y="52" width="16" height="16"/></g>')
  };

  /* ---------- level marks ---------- */
  var LVL = {
    A1: '<circle class="sand" cx="32" cy="30" r="24"/><path class="navf" d="M12 48a20 20 0 0 1 40 0z"/><path class="navs" stroke-width="1.2" d="M4 48h56"/><circle class="acc" cx="47" cy="15" r="5"/>',
    A2: '<circle class="sand" cx="26" cy="32" r="22"/><circle class="navf" cx="40" cy="35" r="16"/><path class="navs" stroke-width="1.2" d="M6 58 58 8"/><circle class="acc" cx="13" cy="14" r="4.5"/>',
    B1: '<circle class="sand" cx="32" cy="32" r="26"/><path class="navf" d="M32 32V6A26 26 0 0 1 58 32z"/><rect class="acc" x="38" y="38" width="11" height="11"/>',
    B2: '<circle class="sand" cx="32" cy="34" r="24"/><path class="navf" d="M12 54V16l34 38z"/><path class="navs" stroke-width="1.2" d="M32 4v56"/><circle class="acc" cx="47" cy="20" r="5"/>',
    C1: '<circle class="sand" cx="32" cy="32" r="26"/><path class="navs" stroke-width="6" d="M13 32A19 19 0 0 1 51 32"/><circle class="navf" cx="32" cy="45" r="7"/><path class="navs" stroke-width="1.2" d="M6 58 58 6"/><circle class="acc" cx="51" cy="32" r="4.5"/>'
  };
  function lvlIcon(k, state) {
    return '<svg class="' + (state || 'todo') + '" viewBox="0 0 64 64" aria-hidden="true">' + LVL[k] + '</svg>';
  }
    /* ---------- generated unit compositions ----------
     Deterministic from the unit id. Rules keep every result balanced:
     one sand disc, one or two navy forms, at most one hairline, exactly one
     vermilion accent placed roughly opposite the main navy form. */
  function rng(seed) {
    var h = 1779033703 ^ seed.length;
    for (var i = 0; i < seed.length; i++) { h = Math.imul(h ^ seed.charCodeAt(i), 3432918353); h = (h << 13) | (h >>> 19); }
    return function () {
      h = Math.imul(h ^ (h >>> 16), 2246822507); h = Math.imul(h ^ (h >>> 13), 3266489909);
      return ((h ^= h >>> 16) >>> 0) / 4294967296;
    };
  }
  function f(n) { return Math.round(n * 10) / 10; }
  function form(kind, cx, cy, r) {
    var a = f(cx - r), b = f(cx + r);
    switch (kind) {
      case 0: return '<path class="navf" d="M' + a + ' ' + cy + 'A' + r + ' ' + r + ' 0 0 1 ' + b + ' ' + cy + 'z"/>';
      case 1: return '<path class="navf" d="M' + cx + ' ' + cy + 'V' + f(cy - r) + 'A' + r + ' ' + r + ' 0 0 1 ' + b + ' ' + cy + 'z"/>';
      case 2: return '<circle class="navf" cx="' + f(cx + r * .32) + '" cy="' + f(cy - r * .3) + '" r="' + f(r * .48) + '"/>';
      case 3: return '<circle class="navs" stroke-width="' + f(r * .22) + '" cx="' + cx + '" cy="' + cy + '" r="' + f(r * .58) + '"/>';
      case 4: return '<path class="navf" d="M' + f(cx - r * .7) + ' ' + f(cy + r * .7) + 'V' + f(cy - r * .7) + 'L' + f(cx + r * .7) + ' ' + f(cy + r * .7) + 'z"/>';
      case 5: return '<rect class="navf" x="' + a + '" y="' + f(cy - r * .58) + '" width="' + f(r * 2) + '" height="' + f(r * .4) + '"/>';
      case 6: return '<circle class="navf" cx="' + f(cx + r * .42) + '" cy="' + f(cy - r * .18) + '" r="' + f(r * .62) + '"/>';
      default: return '<path class="navf" d="M' + cx + ' ' + cy + 'H' + a + 'A' + r + ' ' + r + ' 0 0 1 ' + cx + ' ' + f(cy - r) + 'z"/><path class="navf" d="M' + cx + ' ' + cy + 'H' + b + 'A' + r + ' ' + r + ' 0 0 1 ' + cx + ' ' + f(cy + r) + 'z"/>';
    }
  }
  function unitMark(seed) {
    var R = rng(String(seed)), pick = function (n) { return Math.floor(R() * n); };
    var r = 21 + pick(5), cx = 32 + pick(5) - 2, cy = 32 + pick(5) - 2;
    var rot = pick(4) * 90, kind = pick(8), out = '<circle class="sand" cx="' + cx + '" cy="' + cy + '" r="' + r + '"/>';
    var main = '<g transform="rotate(' + rot + ' ' + cx + ' ' + cy + ')">' + form(kind, cx, cy, r) + '</g>';
    var extra = '', roll = R();
    if (roll < .34) {                       // a hairline axis
      var t = pick(3), lx = f(cx + (R() - .5) * r * .8);
      extra = t === 0 ? '<path class="navs" stroke-width="1.2" d="M' + lx + ' ' + (cy - r - 6) + 'V' + (cy + r + 6) + '"/>'
        : t === 1 ? '<path class="navs" stroke-width="1.2" d="M' + (cx - r - 6) + ' ' + f(cy + (R() - .5) * r * .8) + 'H' + (cx + r + 6) + '"/>'
        : '<path class="navs" stroke-width="1.2" d="M' + (cx - r) + ' ' + (cy + r) + 'L' + (cx + r) + ' ' + (cy - r) + '"/>';
    } else if (roll < .6 && kind !== 2 && kind !== 6) {   // a second, smaller navy form on the other side (never beside a navy disc)
      extra = '<g transform="rotate(' + ((rot + 180) % 360) + ' ' + cx + ' ' + cy + ')">' + form([0, 1, 4][pick(3)], cx, cy, f(r * .42)) + '</g>';
    }
    var ang = (rot + 180 + (R() - .5) * 70) * Math.PI / 180, d = r * (.7 + R() * .28);
    var ax = f(cx + d * Math.sin(ang)), ay = f(cy - d * Math.cos(ang));
    var acc = R() < .5 ? '<circle class="acc" cx="' + ax + '" cy="' + ay + '" r="' + f(4 + R() * 1.6) + '"/>'
      : '<rect class="acc" x="' + f(ax - 4.5) + '" y="' + f(ay - 4.5) + '" width="9" height="9"/>';
    return '<svg viewBox="0 0 64 64" aria-hidden="true">' + out + extra + main + acc + '</svg>';
  }
  function unitIcon(seed) { return unitMark(seed); }
  function thumb(inner) { return '<svg class="thumb" viewBox="0 0 72 56" aria-hidden="true">' + inner + '</svg>'; }
  var TH = {
    ochre: thumb('<circle cx="30" cy="30" r="22" class="ta"/><rect x="40" y="16" width="20" height="30" class="navf"/>'),
    sand: thumb('<circle cx="40" cy="26" r="24" class="sand"/><path class="navf" d="M12 52V22h26z"/>'),
    half: thumb('<path class="navf" d="M10 50A26 26 0 0 1 62 50z"/><path class="tas" stroke-width="1.5" d="M36 10v40"/><circle class="ta" cx="36" cy="10" r="5"/>'),
    beam: thumb('<path class="navs" stroke-width="1.5" d="M6 44 66 20"/><circle class="navf" cx="34" cy="32" r="8"/><rect class="ta" x="50" y="8" width="10" height="10"/>'),
    cards: thumb('<rect class="navs" stroke-width="1.5" x="24" y="6" width="34" height="38"/><rect class="navf" x="10" y="16" width="34" height="34"/>'),
    bars: thumb('<rect class="navf" x="10" y="20" width="8" height="32"/><rect class="navf" x="24" y="8" width="8" height="44"/><rect class="navs" stroke-width="1.5" x="39" y="24" width="8" height="28"/><circle class="ta" cx="56" cy="20" r="7"/>'),
    wave: thumb('<path class="navs" stroke-width="2.5" d="M10 28v0M18 18v20M26 10v36M34 20v16M42 14v28M50 22v12"/><circle class="ta" cx="62" cy="28" r="5"/>'),
    disc: thumb('<circle cx="36" cy="28" r="22" class="sand"/><circle cx="30" cy="30" r="10" class="navf"/><rect class="ta" x="46" y="10" width="9" height="9"/>')
  };

  function head(title, lede, art) { return '<header class="head"><h1>' + title + '</h1>' + (lede ? '<p class="lede">' + lede + '</p>' : '') + art + '</header>'; }
  function row(go, name, desc, fact, th, due) {
    return '<button class="row' + (due ? ' due' : '') + '" data-go="' + go + '"><span><span class="name">' + name + '</span><span class="desc">' + desc + '</span></span><span class="fact">' + (fact || '') + '</span>' + th + '</button>';
  }
  function track(pct) { return '<div class="track' + (pct >= 100 ? ' done' : '') + '"><i style="width:' + pct + '%"></i>' + (pct > 0 && pct < 100 ? '<b style="left:' + pct + '%"></b>' : '') + '</div>'; }
  var CHK = '<svg viewBox="0 0 20 20"><path d="M3 10.5l4.5 4.5L17 5"/></svg>';
  var CRS = '<svg viewBox="0 0 20 20"><path d="M4 4l12 12M16 4L4 16"/></svg>';
  var ARROW = '<svg viewBox="0 0 22 22"><path d="M13 4l-7 7 7 7"/></svg>';
  var XICON = '<svg viewBox="0 0 22 22"><path d="M5 5l12 12M17 5L5 17"/></svg>';

  /* ---------- screens ---------- */
  var S = {};

  S.home = { tab: 'home', label: 'Home', html: function () {
    return head('Hola, Gergely.', '', HERO.home) +
      '<section class="pad" style="padding-top:8px"><p class="serif muted" style="font-size:1.05rem">Continue learning</p>' +
      '<h2 class="serif" style="font-size:clamp(1.55rem,7vw,1.9rem);line-height:1.1;margin-top:14px">B1 · Unit 8 · Lesson 3</h2>' +
      '<p class="muted small" style="margin-top:6px;font-size:15px">Ordering at a café. Step 9 of 25.</p>' +
      '<div class="actline"><button class="btn" data-go="lesson">Resume lesson</button><span class="rule"></span></div>' +
      '<div class="tos"><span class="tos-l">Short on time?</span><span class="tos-b"><button data-go="plan">5 min</button><button data-go="plan">10 min</button><button data-go="plan">20 min</button><button data-go="plan">30 min</button></span></div></section>' +
      '<h2 class="sec">Explore</h2><div class="rows">' +
      row('decks/review', 'Review', 'Words that have come due', '<span class="figure">12</span><small>due today</small>', TH.ochre, 1) +
      row('library', 'Read', 'Stories and your own texts', '<small class="ot">3 new</small>', TH.sand, 1) +
      row('workshop', 'Practise', 'Speak, write, drill a skill', '', TH.half) + '</div>' +
      '<section class="pad" style="padding-top:40px"><p class="serif" style="font-size:2.6rem;line-height:1;letter-spacing:-.02em">12<span style="font-size:1.3rem;margin-left:4px">days</span></p>' +
      '<div class="dots"><i></i><i></i><i></i><i></i><i class="off"></i><hr></div></section>' +
      '<a class="how" href="#home">How Parlour works</a>';
  } };

  S.lessons = { tab: 'lessons', label: 'Lessons: levels', html: function () {
    var L = [['A1', 'Fundamentals', 'Survival skills', 115, 115], ['A2', 'Basic', 'Everyday needs', 120, 120], ['B1', 'Intermediate', 'Opinions and stories', 41, 144], ['B2', 'Upper Intermediate', 'Argument and nuance', 0, 36], ['C1', 'Advanced', 'Coming later', 0, 0]];
    return head('Lessons', 'Five levels, one path forward.', HERO.lessons) +
      '<div class="rows" style="margin-top:34px;border-top:1px solid var(--hair)">' + L.map(function (l) {
        var pct = l[4] ? Math.round(100 * l[3] / l[4]) : 0;
        return '<button class="lvl" data-go="lessons/path">' + lvlIcon(l[0], pct >= 100 ? 'done' : l[0] === 'B1' ? 'now' : 'todo') + '<span><span class="code">' + l[0] + '</span><span class="nm">' + l[1] + '</span><span class="desc" style="margin-top:2px">' + l[2] + '</span>' +
          '<span class="meta">' + track(pct) + '<span>' + (l[4] ? (pct >= 100 ? '<span class="cmp">Complete</span>' : l[3] + ' / ' + l[4]) : 'Soon') + '</span></span></span></button>';
      }).join('') + '</div>';
  } };

  S['lessons/path'] = { tab: 'lessons', label: 'Lessons: unit path', html: function () {
    var U = [['Greetings and introductions', 5, 5, 0], ['Meeting someone new', 5, 5, 1], ['Naming things', 5, 5, 2], ['Describing people', 5, 5, 3], ['Family', 5, 5, 0], ['Daily routine', 5, 3, 1], ['At home', 5, 0, 2], ['At the supermarket', 5, 0, 3]];
    var STEP = 140, top = 62, h = top * 2 + STEP * (U.length - 1) - 40, d = '', pos = [];
    U.forEach(function (u, i) { var x = i % 2 ? 68 : 32, y = top + i * STEP; pos.push([x, y]); d += (i ? 'C ' + x + ' ' + (y - STEP * .55) + ' ' + pos[i - 1][0] + ' ' + (y - STEP * .45) + ' ' + x + ' ' + y + ' ' : 'M ' + x + ' ' + y + ' '); });
    var nodes = U.map(function (u, i) {
      var x = pos[i][0], y = pos[i][1], right = i % 2, done = u[2] === u[1], now = !done && u[2] > 0, state = done ? 'done' : now ? 'now' : 'todo';
      var lab = '<div class="ut ' + state + '" style="top:' + y + 'px;' + (right ? 'right:calc(' + (100 - x) + '% + 72px);text-align:right' : 'left:calc(' + x + '% + 72px)') + '"><span class="un">' + (i < 9 ? '0' : '') + (i + 1) + '</span><h3>' + u[0] + '</h3><p>' + (done ? 'Complete · ' + u[1] + ' lessons' : u[2] + ' of ' + u[1] + ' lessons') + '</p></div>';
      var disc = '<div class="ud ' + state + '" style="top:' + y + 'px;left:' + x + '%">' + unitIcon('b1-' + (i + 1)) + '</div>';
      return disc + lab;
    }).join('');
    return '<a class="backl" href="#lessons" data-go="lessons">‹ Lessons</a>' + head('B1', 'Intermediate. Opinions and stories.', HERO.lessons) +
      '<div class="path" style="height:' + h + 'px;margin-top:12px"><svg class="line" viewBox="0 0 100 ' + h + '" preserveAspectRatio="none" aria-hidden="true"><path d="' + d + '" fill="none" stroke="var(--navy)" stroke-width="1.5" vector-effect="non-scaling-stroke" opacity=".85"/></svg>' + nodes + '</div>';
  } };


  S.gallery = { tab: 'lessons', label: 'Unit marks: generated gallery', html: function () {
    var cells = '';
    for (var n = 1; n <= 40; n++) cells += '<div class="gc">' + unitIcon('b1-' + n) + '<span>' + (n < 10 ? '0' : '') + n + '</span></div>';
    return '<a class="backl" href="#lessons" data-go="lessons">\u2039 Lessons</a>' + head('Unit marks', 'Forty units, forty compositions. Each is generated from its id.', '') + '<div class="gal">' + cells + '</div>';
  } };

  function xbar(pct, count) {
    return '<div class="xbar"><button class="icobtn" data-go="home" aria-label="Close">' + XICON + '</button>' + track(pct) + '<span class="count">' + count + '</span></div>';
  }
  function opts(state) {
    var O = [['A', 'leche'], ['B', 'azúcar'], ['C', 'agua'], ['D', 'miel']];
    return '<div class="opts">' + O.map(function (o, i) {
      var cls = '', mk = '';
      if (state === 'choosing' && i === 0) cls = ' sel';
      if (state === 'correct' && i === 0) { cls = ' ok'; mk = CHK; }
      if (state === 'wrong') { if (i === 1) { cls = ' bad'; mk = CRS; } if (i === 0) { cls = ' ok'; mk = CHK; } }
      return '<button class="opt' + cls + '"><span class="k">' + o[0] + '</span><span>' + o[1] + '</span><span class="mk" style="color:' + (cls === ' bad' ? 'var(--brick)' : 'var(--pine)') + '">' + (mk ? mk.replace('<svg', '<svg width="20" height="20" style="stroke:currentColor;fill:none;stroke-width:2.4"') : '') + '</span></button>';
    }).join('') + '</div>';
  }
  function exercise(state) {
    var blank = state === 'correct' ? '<span class="blank ok">leche</span>' : state === 'wrong' ? '<span class="blank bad">azúcar</span>' : '<span class="blank">' + (state === 'choosing' ? 'leche' : '&nbsp;') + '</span>';
    var fb = '';
    if (state === 'correct') fb = '<div class="fb ok"><div><h3>' + CHK + 'Correct</h3><p>leche means milk.</p></div><button class="btn ok" data-go="lesson/done">Continue</button></div>';
    if (state === 'wrong') fb = '<div class="fb bad"><div><h3>' + CRS + 'Not quite</h3><p>The answer is leche (milk).</p></div><button class="btn bad" data-go="lesson/done">Continue</button></div>';
    var art = '<svg class="xart" viewBox="0 0 110 120" aria-hidden="true"><circle class="sand" cx="72" cy="42" r="40"/><path class="navf" d="M40 112a30 30 0 0 1 60 0z"/><path class="tas" stroke-width="1.5" d="M70 62v50"/><circle class="ta" cx="70" cy="62" r="6"/></svg>';
    return '<div class="xwrap">' + xbar(36, '9 / 25') + '<div class="xq">' + art + '<p class="lab">Choose the missing word</p><p class="sent">Quisiera un café con ' + blank + ', por favor.</p></div>' + opts(state) + '<div style="height:24px"></div>' +
      (fb || '<div class="pad" style="margin-top:auto;padding-bottom:24px;padding-top:24px"><button class="btn" ' + (state === 'idle' ? 'disabled' : '') + ' style="width:100%;text-align:center">Check</button></div>') + '</div>';
  }
  S.lesson = { tab: 'lessons', x: 1, label: 'Lesson: choosing', html: function () { return exercise('choosing'); } };
  S['lesson/correct'] = { tab: 'lessons', x: 1, label: 'Lesson: correct', html: function () { return exercise('correct'); } };
  S['lesson/wrong'] = { tab: 'lessons', x: 1, label: 'Lesson: incorrect', html: function () { return exercise('wrong'); } };
  S['lesson/done'] = { tab: 'lessons', label: 'Lesson: complete', html: function () {
    var art = hero('<circle class="sand" cx="150" cy="46" r="80"/><path class="navf" d="M60 170a72 72 0 0 1 144 0z"/><path class="navs" d="M30 170h222"/><g class="rise"><path class="ps" stroke-width="1.5" d="M132 66v104"/><circle class="pf" cx="132" cy="66" r="9"/></g>');
    return head('Lesson<br>complete.', 'Ordering at a café', art) +
      '<div class="fin"><div class="stats3" style="margin:96px 0 0;max-width:none"><div><p class="n">+42</p><p class="l">XP earned</p></div><div><p class="n">9 / 10</p><p class="l">answered right</p></div><div><p class="n">3</p><p class="l">new words</p></div></div>' +
      '<div class="actline"><button class="btn" data-go="home">Continue</button><span class="rule"></span></div><a class="how" style="margin-left:0" href="#decks/review" data-go="decks/review">Review the new words</a></div>';
  } };

    /* ---------- Library: rooms, shelves, story rows ---------- */
  var CHEV = '<svg class="chev" viewBox="0 0 20 20" aria-hidden="true"><path d="M5 8l5 5 5-5"/></svg>';
  var TICK = '<svg class="rd" viewBox="0 0 20 20" aria-label="Read"><path d="M3 10.5l4.5 4.5L17 5"/></svg>';
  function libTabs(active) {
    var T = [['library', 'Parlour'], ['library/saved', 'Saved'], ['library/texts', 'My texts']];
    return '<div class="tabs" role="tablist">' + T.map(function (t) { return '<button role="tab" data-go="' + t[0] + '" aria-selected="' + (t[0] === active) + '">' + t[1] + '</button>'; }).join('') + '</div>';
  }
  function storyRow(id, part, title, sub, o) {
    o = o || {};
    var meta = [];
    if (o.reach) meta.push('<span class="ot">Within reach</span>');
    if (o.quiz) meta.push('<span class="cmp">Quiz ' + o.quiz + '</span>');
    if (o.fam) meta.push('<span>' + o.fam + '% familiar</span>');
    return '<button class="sr" data-go="library/read"><span class="cv">' + unitMark(id) + '</span><span class="sb">' +
      '<span class="name">' + (part ? '<span class="part">' + part + '</span>' : '') + title + '</span>' +
      (sub ? '<span class="desc">' + sub + '</span>' : '') +
      (meta.length ? '<span class="smeta">' + meta.join('<i></i>') + '</span>' : '') +
      (o.prog ? '<span class="sprog">' + track(o.prog) + '<span>' + o.prog + '%</span></span>' : '') +
      '</span><span class="ss">' + (o.read ? TICK : '') + '</span></button>';
  }
  function shelf(title, count, rows) {
    return '<div class="shelf"><button class="shelf-h"><h3>' + title + ' <span>' + count + '</span></h3>' + CHEV + '</button><div class="shelf-b">' + rows + '</div></div>';
  }
  function roomRow(code, name, count, state, open) {
    return '<button class="lvl room-h' + (open ? ' open' : '') + '" data-go="library">' + lvlIcon(code, state) + '<span><span class="code">' + code + '</span><span class="nm">' + name + '</span>' +
      '<span class="meta"><span>' + count + '</span>' + CHEV + '</span></span></button>';
  }

  S.library = { tab: 'library', label: 'Library: Parlour (rooms and shelves)', html: function () {
    var orig = storyRow('lib-b1-o1', 'Part 1', 'Un día en el mercado', 'Unit 6 · Café and Market', { read: 1, quiz: '4/5', fam: 91 }) +
      storyRow('lib-b1-o2', 'Part 2', 'La llave perdida', 'Unit 6 · Café and Market', { read: 1, fam: 88 }) +
      storyRow('lib-b1-o3', 'Part 3', 'El tren de las ocho', 'Unit 7 · Getting around', { prog: 40, fam: 84 }) +
      storyRow('lib-b1-o4', 'Part 4', 'Una carta sin remitente', 'Unit 7 · Getting around', { reach: 1, fam: 79 });
    var latam = storyRow('lib-b1-l1', 'Part 1', 'Carnaval en Barranquilla', 'Latin America track', { fam: 72 }) +
      storyRow('lib-b1-l2', 'Part 2', 'Mercado de San Telmo', 'Latin America track', { fam: 70 });
    var classics = storyRow('lib-b1-c1', '', 'Lazarillo de Tormes', 'Anonymous · adapted', { fam: 61 }) +
      storyRow('lib-b1-c2', '', 'Rinconete y Cortadillo', 'Cervantes · adapted', { fam: 58 });
    return head('Library', 'Stories to read, and your own texts.', HERO.library) + libTabs('library') +
      '<div class="rows lvls" style="border-top:0">' +
      roomRow('A1', 'Fundamentals', '6 / 20 read', 'todo') + roomRow('A2', 'Basic', '4 / 24 read', 'todo') +
      roomRow('B1', 'Intermediate', '5 / 30 read \u00b7 you\u2019re here', 'now', 1) +
      '<div class="room-b"><div class="searchw"><input class="fi" type="search" placeholder="Search titles\u2026" aria-label="Search B1 stories"></div>' +
      shelf('Original', '(5 / 24 read)', orig) + shelf('Latin America', '(0 / 12)', latam) + shelf('Classics', '(0 / 10)', classics) + '</div>' +
      roomRow('B2', 'Upper Intermediate', '0 / 12 read', 'todo') + roomRow('C1', 'Advanced', 'Coming soon', 'todo') + '</div>';
  } };

  S['library/saved'] = { tab: 'library', label: 'Library: Saved', html: function () {
    var r = function (id, title, sub, o) { return '<div class="sr-wrap">' + storyRow(id, '', title, sub, o) + '<button class="linkbtn">Remove from Saved</button></div>'; };
    return head('Library', 'Stories to read, and your own texts.', HERO.library) + libTabs('library/saved') +
      '<div class="rows" style="border-top:0">' + r('lib-s1', 'El tren de las ocho', 'B1 \u00b7 Original', { prog: 40, fam: 84 }) + r('lib-s2', 'Lazarillo de Tormes', 'B1 \u00b7 Anonymous', { fam: 61 }) + r('lib-s3', 'La llave perdida', 'B1 \u00b7 Original', { read: 1, fam: 88 }) + '</div>' +
      '<p class="empty pad">Save a story from its page and it will wait for you here.</p>';
  } };

  S['library/texts'] = { tab: 'library', label: 'Library: My texts', html: function () {
    var t = function (title, meta, fam, go) { return '<div class="tx"><button class="tx-main" data-go="' + (go || 'library/read') + '"><span class="name">' + title + '</span><span class="desc">' + meta + '</span></button><span class="tx-fam">' + fam + '% familiar</span><span class="tx-act"><button class="linkbtn" data-go="library/editor">Edit</button><button class="linkbtn danger">Delete</button></span></div>'; };
    return head('Library', 'Stories to read, and your own texts.', HERO.library) + libTabs('library/texts') +
      '<div class="pad" style="padding-top:26px"><p class="muted" style="max-width:26em;font-size:15px">Bring in any Spanish text and read it with the same dictionary and word tools.</p>' +
      '<div class="actline"><button class="btn" data-go="library/editor">Add text</button><span class="rule"></span></div></div>' +
      '<div class="rows" style="margin-top:28px">' + t('Correo de Lucía', '212 words \u00b7 ~2 min \u00b7 Estimated B1', 72) + t('Noticia sobre el metro', '640 words \u00b7 ~5 min \u00b7 Estimated B2', 48) + t('Receta de mi abuela', '180 words \u00b7 ~2 min \u00b7 Estimated A2', 90) + '</div>';
  } };

  S['library/editor'] = { tab: 'library', label: 'Library: My text (add and analyse)', html: function () {
    var group = function (label, n, items, ot) { return '<div class="vg"><p class="vg-t">' + label + ' <span' + (ot ? ' class="ot"' : '') + '>(' + n + ')</span></p>' + items.map(function (i) { return '<label class="vi"><span class="cb' + (i[2] ? ' on' : '') + '"></span><span class="serif">' + i[0] + '</span><span class="muted small">' + i[1] + '</span></label>'; }).join('') + '</div>'; };
    return '<a class="backl" href="#library/texts" data-go="library/texts">\u2039 My texts</a>' +
      '<div class="pad"><h1 class="serif" style="font-size:2.2rem;line-height:1.05;margin-top:22px;letter-spacing:-.02em">Add text</h1>' +
      '<label class="fl" for="t1">Title</label><input id="t1" class="fi" value="Correo de Luc\u00eda">' +
      '<label class="fl" for="t2">Paste your text</label><textarea id="t2" class="fi ta-area" rows="5">Querida Marta: Te escribo desde la playa. Ayer fuimos al mercado y compramos fruta fresca para toda la semana\u2026</textarea>' +
      '<div class="actline" style="margin-top:16px"><button class="btn ghost">Analyse text</button></div>' +
      '<div class="ana"><p class="ana-h">Estimated level: <b>B1</b></p><p class="muted">212 words \u00b7 ~2 min read</p><p class="serif" style="font-size:1.6rem;margin-top:14px">72% <span style="font-size:1rem" class="muted">familiar</span></p>' + track(72) +
      '<div class="ana-b"><span>Familiar <b>118</b></span><span>New <b class="ot">34</b></span><span>In decks <b>21</b></span><span>Due <b class="ot">9</b></span></div></div>' +
      '<h2 class="sec" style="padding:32px 0 6px">Inspect vocabulary</h2>' +
      group('New', 34, [['la playa', 'beach', 1], ['fresco', 'fresh', 1], ['la semana', 'week', 0]], 1) + group('Due', 9, [['comprar', 'to buy', 0], ['el mercado', 'market', 0]], 1) +
      '<div class="actline" style="margin-top:18px"><button class="btn ghost">Add selected words to deck</button></div>' +
      '<div class="actline" style="margin-top:30px;gap:10px;flex-wrap:wrap"><button class="btn" data-go="library/texts">Save</button><button class="btn ghost" data-go="library/read">Save and read</button><button class="linkbtn danger" style="margin-left:auto">Delete text</button></div></div>';
  } };

  S['library/read'] = { tab: 'library', label: 'Library: reader (story)', html: function () {
    return '<div class="rbar"><i style="width:38%"></i><b style="left:38%"></b></div><a class="backl" href="#library" data-go="library" style="margin-top:18px">\u2039 Library</a>' +
      '<div class="reader"><h1 class="serif" style="font-size:2.2rem;line-height:1.05;margin-top:22px;letter-spacing:-.02em">El tren de las ocho</h1>' +
      '<div class="rhead"><span class="muted small">B1 \u00b7 Part 3 \u00b7 4 min</span><span class="ract"><button class="sqb" aria-label="Save story">Save</button><button class="sqb" aria-label="Smaller text">A\u2212</button><button class="sqb" aria-label="Larger text">A+</button></span></div>' +
      '<p>Todas las ma\u00f1anas, Marta baja a la <span class="w new">estaci\u00f3n</span> de la esquina. Compra un caf\u00e9 con <span class="w new sel">leche</span> y un pan <span class="w rev">tostado</span>, y espera junto a la ventana.</p>' +
      '<p>Le gusta ver pasar a la gente antes de empezar el trabajo.</p></div>' +
      '<div class="pop"><p class="word">leche</p><p class="g">milk \u00b7 la leche</p><div class="btns"><button class="btn ghost">Listen</button><button class="btn">Add to deck</button></div></div>' +
      '<div class="pad" style="margin-top:34px"><p class="serif" style="font-size:1.25rem">Finished?</p><div class="actline"><button class="btn">Take the quiz</button><span class="rule"></span></div></div>';
  } };

  S.workshop = { tab: 'workshop', label: 'Workshop', html: function () {
    return head('Workshop', 'Sharpen every skill.', HERO.workshop) + '<div class="rows" style="margin-top:34px">' +
      row('workshop/verb', 'Verb Driller', 'Conjugation tables and speed drills', '', TH.bars) +
      row('workshop/verb', 'Grammar Driller', 'Practise by skill, from every lesson', '', TH.half) +
      row('workshop/verb', 'Translation Driller', 'Real sentences, either direction', '', TH.beam) +
      row('workshop/verb', 'Vocabulary Driller', 'Meaning and context', '', TH.disc) +
      row('workshop/verb', 'Listening Driller', 'Decode spoken Spanish, by ear', '', TH.wave) + '</div>';
  } };
  S['workshop/verb'] = { tab: 'workshop', label: 'Workshop: choose tense', html: function () {
    var T = [['Presente', 'Regular and irregular', 1], ['Pretérito perfecto', 'Regular and irregular'], ['Pretérito indefinido', 'Regular and irregular'], ['Pretérito imperfecto', 'Regular and irregular'], ['Futuro', 'Regular and irregular'], ['All tenses', 'Mixed practice']];
    var art = HERO.workshop;
    return '<a class="backl" href="#workshop" data-go="workshop">‹ Workshop</a>' + head('Verb Driller', 'Conjugation tables and speed drills.', art.replace('<circle class="sand" cx="160" cy="64" r="74"/>', '<circle class="sand" cx="160" cy="64" r="74"/>')) +
      '<h2 class="sec" style="padding-top:26px">Choose a tense</h2><div class="tenses">' + T.map(function (t) { return '<button class="tense' + (t[2] ? ' on' : '') + '" data-go="workshop/drill"><span class="name">' + t[0] + '</span><span class="desc">' + t[1] + '</span></button>'; }).join('') + '</div>';
  } };
  S['workshop/drill'] = { tab: 'workshop', x: 1, label: 'Workshop: driller', html: function () {
    var P = [['yo', 'hablo', 'ok'], ['tú', 'hablas', 'ok'], ['él / ella / usted', 'habla', 'ok'], ['nosotros / -as', 'hablam', 'act'], ['vosotros / -as', ''], ['ellos / ellas / ustedes', '']];
    return '<div class="xwrap">' + xbar(30, '3 / 10') + '<div class="xq" style="min-height:0"><p class="lab">Conjugate the verb</p><p class="sent" style="font-size:2.6rem;margin-top:10px">hablar</p><p class="muted" style="margin-top:4px">to speak · Presente</p></div>' +
      '<div class="conj">' + P.map(function (p) { return '<div class="r"><span class="who">' + p[0] + '</span><span class="fld ' + (p[2] || '') + '">' + p[1] + '</span></div>'; }).join('') + '</div>' +
      '<div class="pad" style="margin-top:auto;padding-top:24px;padding-bottom:24px"><button class="btn" style="width:100%;text-align:center">Check</button></div></div>';
  } };

  S.decks = { tab: 'decks', label: 'Decks', html: function () {
    var D = [['A1 Core Vocabulary', '235 words', 72, 18, TH.cards], ['Verbs: present tense', '128 words', 54, 7, TH.half], ['Travel and transport', '96 words', 81, 3, TH.disc], ['False friends', '64 words', 66, 4, TH.beam]];
    return head('Decks', 'Master vocabulary with spaced repetition.', HERO.decks) +
      '<div class="allwords"><div><p class="muted small" style="margin-bottom:8px">All my words</p><p class="big">32<span>due</span></p></div><div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:flex-end"><button class="btn" data-go="decks/review">Review</button><button class="btn ghost">Browse</button></div></div>' +
      '<h2 class="sec" style="padding-top:28px">My decks</h2><div class="rows">' + D.map(function (d) {
        return '<button class="row due" data-go="decks/review"><span><span class="name">' + d[0] + '</span><span class="desc">' + d[1] + '</span><span style="display:block;margin-top:10px;max-width:11em">' + track(d[2]) + '</span></span><span class="fact"><span class="figure">' + d[3] + '</span><small>due today</small></span>' + d[4] + '</button>';
      }).join('') +
      '<button class="row"><span><span class="name">Create a new deck</span><span class="desc">Build your own vocabulary set</span></span><span></span>' + thumb('<circle class="navs" stroke-width="1.5" cx="36" cy="28" r="16"/><path class="navs" stroke-width="1.5" d="M36 20v16M28 28h16"/>') + '</button></div>';
  } };
  function flash(back) {
    var art = '<svg class="fa" viewBox="0 0 120 100" preserveAspectRatio="xMaxYMax meet" aria-hidden="true"><circle class="sand" cx="90" cy="60" r="52"/><path class="navf" d="M30 100a34 34 0 0 1 68 0z"/><path class="tas" stroke-width="1.5" d="M64 40v60"/><circle class="ta" cx="64" cy="40" r="6"/></svg>';
    return '<div class="xwrap">' + xbar(48, '12 / 25') + '<div class="flash">' + art + '<p class="w1">caminar</p><p class="w2">verbo</p>' + (back ? '<p class="w3">to walk</p>' : '') + '</div>' +
      (back ? '<div class="grade"><button class="g1"><span>Again<small>&lt; 1 min</small></span></button><button class="g2"><span>Hard<small>&lt; 10 min</small></span></button><button class="g3"><span>Good<small>3 d</small></span></button><button class="g4"><span>Easy<small>7 d</small></span></button></div>' :
        '<div class="pad" style="padding-top:14px"><button class="btn ghost" data-go="decks/answer" style="width:100%;text-align:center">Show answer</button></div>') + '</div>';
  }
  S['decks/review'] = { tab: 'decks', x: 1, label: 'Decks: review (front)', html: function () { return flash(false); } };
  S['decks/answer'] = { tab: 'decks', x: 1, label: 'Decks: review (answer)', html: function () { return flash(true); } };

  S.journey = { tab: 'journey', label: 'Journey', html: function () {
    // The ridge is the whole course (A1 to C1, equal bands). The yellow marker is the learner's true place on it.
    var x0 = 14, y0 = 200, x1 = 336, y1 = 52;
    var pt = function (t) { return [x0 + (x1 - x0) * t, y0 + (y1 - y0) * t]; };
    var BANDS = ['A1', 'A2', 'B1', 'B2', 'C1'], DONE = 2, IN = 2, FRAC = 41 / 144;
    var t = (IN + FRAC) / BANDS.length, me = pt(t), top = pt(1);
    var lines = '', dots = '', labels = '';
    for (var i = 1; i < BANDS.length; i++) {
      var g = pt(i / BANDS.length), passed = i / BANDS.length < t, isDone = i <= DONE;
      lines += '<path d="M' + g[0] + ' ' + g[1] + 'V' + y0 + '" stroke="' + (passed ? 'var(--cream)' : 'var(--muted)') + '" stroke-width="1" opacity="' + (passed ? '.55' : '.45') + '" fill="none"/>';
      dots += isDone ? '<circle cx="' + g[0] + '" cy="' + g[1] + '" r="5.5" fill="var(--pine)"/>' : '<circle cx="' + g[0] + '" cy="' + g[1] + '" r="4.5" fill="var(--cream)" stroke="var(--muted)" stroke-width="1.5"/>';
    }
    BANDS.forEach(function (b, i) {
      var m = pt((i + .5) / BANDS.length), st = i < DONE ? 'done' : i === IN ? 'now' : 'todo';
      labels += '<text x="' + m[0] + '" y="' + (m[1] - 16) + '" text-anchor="middle" class="mt-l ' + st + '">' + b + '</text>';
    });
    var svg = '<svg class="mt" viewBox="0 0 360 236" role="img" aria-label="Level B1, 41 of 144 lessons done, on the way from A1 to C1">' +
      '<circle class="sand" cx="262" cy="86" r="64"/>' +
      '<path d="M' + me[0] + ' ' + me[1] + 'L' + x1 + ' ' + y1 + 'V' + y0 + 'H' + me[0] + 'z" fill="var(--sand)" opacity=".7"/>' +
      '<path d="M' + me[0] + ' ' + me[1] + 'L' + x1 + ' ' + y1 + 'V' + y0 + '" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 5"/>' +
      '<path d="M' + x0 + ' ' + y0 + 'L' + me[0] + ' ' + me[1] + 'V' + y0 + 'z" fill="var(--navy)"/>' +
      lines + '<path d="M8 ' + y0 + 'H352" stroke="var(--navy)" stroke-width="1.2" fill="none"/>' +
      '<path d="M' + top[0] + ' ' + top[1] + 'V' + (top[1] - 26) + '" stroke="var(--muted)" stroke-width="1.2" fill="none"/><rect x="' + (top[0] - 5) + '" y="' + (top[1] - 36) + '" width="10" height="10" fill="var(--cream)" stroke="var(--muted)" stroke-width="1.5"/>' +
      dots + labels +
      '<circle cx="' + me[0] + '" cy="' + me[1] + '" r="9.5" fill="var(--vermilion)" stroke="var(--cream)" stroke-width="2.5"/></svg>';
    var m = function (label, val, go, cls) { return '<button class="jm" data-go="' + go + '"><span class="jm-l">' + label + '</span><span class="jm-v' + (cls ? ' ' + cls : '') + '">' + val + '</span>' + CHEV + '</button>'; };
    var days = ''; [1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,2].forEach(function (a) { days += '<i class="' + (a === 1 ? 'on' : a === 2 ? 'today' : '') + '"></i>'; });
    return head('Journey', 'Where you are, and where you are going.', HERO.journey) +
      '<section class="pad" style="padding-top:8px"><div class="streakline"><span class="jbig">12<span> days in a row</span></span><span class="muted small">Best 31 \u00b7 Rank 14</span></div>' +
      '<div class="dgrid" role="img" aria-label="22 active days of the last 30">' + days + '</div><p class="muted small" style="margin-top:12px">22 active of the last 30 days. <button class="linkbtn">Import a streak</button></p></section>' +
      '<div class="mtw" style="margin-top:38px">' + svg + '</div>' +
      '<p class="jsum">B1 \u00b7 41 of 144 lessons \u00b7 412 of 1,204 overall</p>' +
      '<div class="rows jmrows" style="margin-top:30px">' +
      m('Can-Do Passport', '126 verified', 'journey/passport', 'pv') + m('Grammar and vocabulary', '34 / 52', 'journey/knowledge') + m('Skills', '4 measured', 'journey/skills') +
      m('Milestones', '3 to go', 'journey/milestones') + m('Account and appearance', '', 'journey/account') + '</div>';
  } };

  function jsub(title, lede, body) {
    return '<a class="backl" href="#journey" data-go="journey">\u2039 Journey</a><header class="head" style="min-height:0;padding-bottom:6px"><h1>' + title + '</h1>' + (lede ? '<p class="lede">' + lede + '</p>' : '') + '</header>' + body;
  }
  S['journey/knowledge'] = { tab: 'journey', label: 'Journey: grammar and vocabulary', html: function () {
    return jsub('Grammar and vocabulary', '', '<div class="rows jrows" style="margin-top:22px">' +
      '<div class="jbl"><span class="jbig">34<span> of 52 grammar points</span></span>' + track(65) + '<span class="desc">Next: <button class="linkbtn">Past tenses</button> \u00b7 <button class="linkbtn">Reflexive verbs</button></span></div>' +
      '<div class="jbl"><span class="jbig">1,340<span> of 3,100 words met</span></span>' + track(43) + '<span class="desc">At this pace, the level\u2019s words are met by March.</span>' +
      '<span class="jchips"><span><b>412</b> in active review</span><i></i><span><b>5</b> of 30 stories read</span></span></div></div>');
  } };
  S['journey/skills'] = { tab: 'journey', label: 'Journey: skills', html: function () {
    var stat = function (label, pct, value) { return '<div class="jr"><span class="jr-l">' + label + '</span>' + track(pct) + '<span class="jr-v">' + value + '</span></div>'; };
    return jsub('Skills', 'What you have practised, by skill.', '<div class="rows jrows" style="margin-top:22px">' + stat('Reading', 60, '12 / 20') + stat('Listening', 40, '8 / 20') + stat('Writing', 33, '5 / 15') + stat('Speaking', 81, '81% \u00b7 14 attempts') + '<div class="jr muted-row"><span class="jr-l">Pronunciation</span><span class="jr-n">Not measured yet</span></div></div>');
  } };
  S['journey/milestones'] = { tab: 'journey', label: 'Journey: milestones', html: function () {
    var ms = function (label, done, sub) { return '<li class="ms' + (done ? ' done' : '') + '"><span class="tk">' + (done ? TICK : '') + '</span><span><span class="name" style="font-size:1.1rem">' + label + '</span>' + (sub ? '<span class="desc">' + sub + '</span>' : '') + '</span></li>'; };
    return jsub('Milestones', '', '<ul class="mslist" style="margin-top:22px">' + ms('Finish A2', 1, 'Reached in March') + ms('Read 10 stories', 0, '5 of 10') + ms('A 30-day streak', 0, '12 of 30 days') + ms('Finish B1', 0, '103 lessons to go') + '</ul>');
  } };
  S['journey/account'] = { tab: 'journey', label: 'Journey: account and appearance', html: function () {
    return jsub('Account and appearance', '', '<h2 class="sec" style="padding-top:26px">Account</h2><div class="pad acct"><p class="muted small" style="max-width:26em">Back up your progress so it isn\u2019t stuck on one device.</p>' +
      '<div class="actline" style="margin-top:14px"><button class="btn ghost">Continue with Google</button></div>' +
      '<p class="muted small" style="margin:18px 0 10px">Or sign in with email</p><input class="fi" type="email" placeholder="you@example.com" aria-label="Email"><div class="actline" style="margin-top:12px"><button class="btn">Send me a login link</button></div></div>' +
      '<h2 class="sec">Appearance</h2><div class="pad"><div class="tabs" style="margin:0" role="radiogroup"><button role="radio" aria-selected="false">System</button><button role="radio" aria-selected="true">Light</button><button role="radio" aria-selected="false">Dark</button></div></div>');
  } };

  S['journey/passport'] = { tab: 'journey', label: 'Journey: Can-Do Passport', html: function () {
    var rowc = function (text, lesson, st) {
      var b = st === 'v' ? '<span class="cmp"><svg class="rd sm" viewBox="0 0 20 20"><path d="M3 10.5l4.5 4.5L17 5"/></svg>Verified</span>' : st === 'g' ? '<span class="ot">Confidence gap</span>' : '<span class="ot">Needs review</span>';
      return '<li class="cd"><span class="cd-t">\u201c' + text + '\u201d</span><span class="desc">' + lesson + '</span><span class="cd-b">' + b + '<span class="cd-a"><button class="linkbtn">Speak</button><button class="linkbtn">Write</button></span></span></li>';
    };
    return '<a class="backl" href="#journey" data-go="journey">\u2039 Journey</a>' + head('Can-Do Passport', 'What you can do in Spanish, and how sure we are.', HERO.journey) +
      '<div class="tabs" role="tablist"><button role="tab" aria-selected="false">A1</button><button role="tab" aria-selected="false">A2</button><button role="tab" aria-selected="true">B1</button><button role="tab" aria-selected="false">B2</button><button role="tab" aria-selected="false">C1</button></div>' +
      '<div class="pad" style="padding-top:22px"><p class="jchips"><span class="cmp">126 verified</span><i></i><span class="ot">8 confidence gaps</span><i></i><span class="ot">3 need review</span></p></div>' +
      '<h2 class="sec" style="padding-top:26px">Unit 6 \u00b7 Caf\u00e9 and Market</h2><ul class="cdlist">' +
      rowc('I can order food and drink in a caf\u00e9', 'Ordering at a caf\u00e9', 'v') + rowc('I can ask what something costs', 'At the market', 'v') + rowc('I can complain politely about a mistake', 'When things go wrong', 'g') + '</ul>' +
      '<h2 class="sec" style="padding-top:26px">Unit 7 \u00b7 Getting around</h2><ul class="cdlist">' + rowc('I can ask for and follow directions', 'Finding the station', 'v') + rowc('I can buy a train ticket', 'At the ticket office', 'r') + '</ul>';
  } };

  /* ---------- the remaining screens ---------- */
  var ARW = '<svg viewBox="0 0 22 14" width="22" height="14" aria-hidden="true"><path d="M0 7h19M13 1l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2"/></svg>';
  function wc(go, name, desc) { return '<button class="wc" data-go="' + go + '"><span><span class="name">' + name + '</span>' + (desc ? '<span class="desc">' + desc + '</span>' : '') + '</span>' + ARW + '</button>'; }
  function kws(list) { return '<div class="chips">' + list.map(function (k) { return '<span class="kw' + (k[1] ? ' ok' : '') + '">' + (k[1] ? '\u2713 ' : '') + k[0] + '</span>'; }).join('') + '</div>'; }
  function keys() { return '<div class="akeys">' + ['\u00e1', '\u00e9', '\u00ed', '\u00f3', '\u00fa', '\u00f1', '\u00bf', '\u00a1'].map(function (k) { return '<button class="key">' + k + '</button>'; }).join('') + '</div>'; }
  function crit(label, pct, val) { return '<div class="jr"><span class="jr-l">' + label + '</span>' + track(pct) + '<span class="jr-v">' + val + '</span></div>'; }
  function play() { return '<button class="play" aria-label="Listen"><svg viewBox="0 0 96 96"><circle class="navf" cx="48" cy="48" r="46"/><path d="M38 30l30 18-30 18z" fill="var(--cream)"/></svg></button>'; }
  function wave(done) { var h = [10, 22, 34, 16, 40, 26, 12, 30, 44, 20, 36, 14, 28, 38, 18, 24, 32, 12, 26, 34], o = ''; h.forEach(function (v, i) { o += '<rect x="' + (i * 12) + '" y="' + (24 - v / 2) + '" width="4" height="' + v + '" fill="' + (i < done ? 'var(--navy)' : 'var(--hair)') + '"/>'; }); return '<svg class="wave" viewBox="0 0 236 48" aria-hidden="true">' + o + '</svg>'; }
  function pad(x) { return '<div class="pad" style="padding-top:22px">' + x + '</div>'; }

  /* welcome (first open, no navigation) */
  S.welcome = { tab: 'home', nonav: 1, label: 'Welcome: language', html: function () {
    return head('Parlour', 'A place to learn a language properly, at your own pace.', HERO.home) +
      '<div class="pad" style="padding-top:34px"><p class="serif" style="font-size:1.5rem;line-height:1.15;margin-bottom:16px">What would you like to learn?</p>' + wc('welcome/variant', 'Spanish', 'A1 to B2 and beyond') + wc('welcome/start', 'Hungarian', 'A1 to B1') + '</div>';
  } };
  S['welcome/variant'] = { tab: 'home', nonav: 1, label: 'Welcome: which Spanish', html: function () {
    return '<a class="backl" href="#welcome" data-go="welcome">\u2039 Back</a>' + head('Which Spanish?', 'You can change this later.', HERO.home) +
      '<div class="pad" style="padding-top:34px">' + wc('welcome/start', 'Spain', 'Castilian vocabulary and vosotros') + wc('welcome/start', 'Latin America', 'Ustedes, and everyday words from the Americas') + '</div>';
  } };
  S['welcome/start'] = { tab: 'home', nonav: 1, label: 'Welcome: where to start', html: function () {
    return '<a class="backl" href="#welcome/variant" data-go="welcome/variant">\u2039 Back</a>' + head('Where do you start?', '', HERO.home) +
      '<div class="pad" style="padding-top:34px">' + wc('home', 'Start from the beginning', 'A1, the very first lesson') + wc('test', 'Find my level', 'A short check. About ten minutes.') + '</div>';
  } };

  /* study plan */
  S.plan = { tab: 'home', label: 'Study plan: short on time', html: function () {
    var it = function (m, t, d) { return '<div class="pl"><span class="pl-m"><b>' + m + '</b> min</span><span><span class="name">' + t + '</span><span class="desc">' + d + '</span></span></div>'; };
    return '<a class="backl" href="#home" data-go="home">\u2039 Home</a>' + head('Short on time?', 'Pick a time. We build a session that fits.', HERO.home) +
      '<div class="seg" role="radiogroup"><button role="radio" aria-checked="false">5 min</button><button role="radio" aria-checked="false">10 min</button><button role="radio" aria-checked="true" class="on">20 min</button><button role="radio" aria-checked="false">30 min</button></div>' +
      '<h2 class="sec">Your 20 minutes</h2><div class="rows">' + it(4, 'Review', '12 words that are due') + it(8, 'Lesson', 'B1 \u00b7 Unit 8 \u00b7 Lesson 3, from step 9') + it(5, 'Speaking', 'Ordering food and drink') + it(3, 'Reading', 'El tren de las ocho, part 3') + '</div>' +
      '<div class="pad" style="padding-top:16px"><div class="jr" style="border:0"><span class="jr-l">Total</span>' + track(100) + '<span class="jr-v">20 of 20 min</span></div>' +
      '<div class="actline"><button class="btn" data-go="lesson">Start</button><span class="rule"></span></div></div>';
  } };

  /* level test */
  S.test = { tab: 'lessons', label: 'Level test: readiness check', html: function () {
    var rc = function (ok, t, v) { return '<div class="rc"><span class="tk' + (ok ? ' ok' : '') + '">' + (ok ? TICK : '') + '</span><span class="name" style="font-size:1.1rem">' + t + '</span><span class="muted small">' + v + '</span></div>'; };
    return '<a class="backl" href="#lessons" data-go="lessons">\u2039 Lessons</a>' + head('B1 Readiness Check', 'See where you stand before the level test.', HERO.lessons) +
      '<div class="rows" style="margin-top:34px;border-top:1px solid var(--navy)">' + rc(0, 'Lessons finished', '41 of 144') + rc(1, 'Grammar covered', '52 of 52') + rc(1, 'Vocabulary met', '2,900 words') + '</div>' +
      '<h2 class="sec">What the test covers</h2><div class="rows">' + row('test', 'Part 1 \u00b7 Language in context', 'Grammar and vocabulary in short passages', '', TH.bars) + row('test', 'Part 2 \u00b7 Reading and writing', 'Answer questions, then write a short text', '', TH.sand) + row('test', 'Part 3 \u00b7 Speaking', 'A short spoken answer', '', TH.half) + '</div>' +
      '<div class="pad" style="padding-top:22px"><p class="muted small" style="max-width:26em">You can take it early. You will see which parts to revisit afterwards.</p><div class="actline"><button class="btn" data-go="test/writing">Take the test</button><span class="rule"></span></div></div>';
  } };
  S['test/writing'] = { tab: 'lessons', x: 1, label: 'Level test: written production', html: function () {
    return '<div class="xwrap">' + xbar(55, 'Part 2 of 3') + '<div class="pad" style="padding-top:28px"><p class="serif muted" style="font-size:1.05rem">Short written production</p>' +
      '<h2 class="serif" style="font-size:1.7rem;line-height:1.15;margin-top:10px;text-wrap:balance">Write to a friend about your weekend.</h2><p class="muted" style="margin-top:8px;font-size:15px">Use at least 80 words.</p>' +
      '<textarea class="fi ta-area" rows="7" style="margin-top:18px">El fin de semana fui a la playa con mi familia. Comimos paella y despu\u00e9s caminamos por el puerto\u2026</textarea>' +
      '<div class="cnt-row"><span>42 / 80 words</span></div>' + kws([['fin de semana', 1], ['fui', 1], ['porque', 0], ['despu\u00e9s', 1]]) + '</div>' +
      '<div class="pad" style="margin-top:auto;padding-top:22px;padding-bottom:24px"><button class="btn" style="width:100%;text-align:center" disabled>Next</button></div></div>';
  } };
  S['test/speaking'] = { tab: 'lessons', x: 1, label: 'Level test: spoken production', html: function () {
    return '<div class="xwrap">' + xbar(85, 'Part 3 of 3') + '<div class="pad" style="padding-top:28px"><p class="serif muted" style="font-size:1.05rem">Short spoken production</p>' +
      '<h2 class="serif" style="font-size:1.7rem;line-height:1.15;margin-top:10px;text-wrap:balance">Describe your morning routine.</h2><p class="muted" style="margin-top:8px;font-size:15px">Speak for about 30 seconds.</p></div>' +
      '<div class="recwrap"><button class="rec" aria-label="Stop recording"><svg viewBox="0 0 96 96"><circle cx="48" cy="48" r="46" fill="var(--vermilion)"/><rect x="34" y="34" width="28" height="28" fill="#fff"/></svg></button><p class="serif" style="font-size:1.6rem;margin-top:14px">0:12</p>' + wave(9) + '</div>' +
      '<div class="pad"><label class="fl" style="margin-top:0">What we heard</label><div class="fi" style="min-height:74px;color:var(--muted)">Me levanto a las siete y desayuno un caf\u00e9\u2026</div></div>' +
      '<div class="pad" style="margin-top:auto;padding-top:22px;padding-bottom:24px"><button class="btn ghost" style="width:100%;text-align:center" data-go="test/result">Finish the test</button></div></div>';
  } };
  S['test/result'] = { tab: 'lessons', label: 'Level test: result', html: function () {
    var art = hero('<circle class="sand" cx="150" cy="46" r="80"/><path class="navf" d="M60 170a72 72 0 0 1 144 0z"/><path class="navs" d="M30 170h222"/><g class="rise"><path class="ps" stroke-width="1.5" d="M132 66v104"/><circle class="pf" cx="132" cy="66" r="9"/></g>');
    return head('You passed<br>B1.', 'Ready for B2.', art) +
      '<div class="rows jrows" style="margin-top:96px">' + crit('Language', 86, '86%') + crit('Reading', 78, '78%') + crit('Writing', 72, '72%') + crit('Speaking', 80, '80%') + '</div>' +
      '<div class="pad" style="padding-top:8px"><div class="actline"><button class="btn" data-go="lessons">Continue to B2</button><span class="rule"></span></div><p style="margin-top:22px"><button class="linkbtn">Review your mistakes</button></p></div>';
  } };

  /* speaking and writing studios */
  S.speaking = { tab: 'workshop', x: 1, label: 'Speaking Studio: recording', html: function () {
    return '<div class="xwrap"><div class="xbar" style="grid-template-columns:24px 1fr"><button class="icobtn" data-go="workshop" aria-label="Close">' + XICON + '</button><span class="serif" style="font-size:1.15rem">Speaking Studio</span></div>' +
      '<div class="pad" style="padding-top:26px"><p class="serif muted" style="font-size:1.05rem">Task</p><h2 class="serif" style="font-size:1.7rem;line-height:1.15;margin-top:10px;text-wrap:balance">Ask for a table for two, and order a drink.</h2><p class="muted" style="margin-top:8px;font-size:15px">Aim for 45 seconds. B1.</p></div>' +
      '<div class="recwrap"><button class="rec" aria-label="Start recording"><svg viewBox="0 0 96 96"><circle cx="48" cy="48" r="46" fill="var(--vermilion)"/><circle cx="48" cy="48" r="14" fill="#fff"/></svg></button><p class="muted small" style="margin-top:14px">Tap to record</p></div>' +
      '<div class="pad" style="margin-top:auto;padding-bottom:24px;padding-top:18px"><button class="linkbtn" data-go="speaking/feedback">See an example result</button></div></div>';
  } };
  S['speaking/feedback'] = { tab: 'workshop', label: 'Speaking Studio: feedback', html: function () {
    return '<a class="backl" href="#speaking" data-go="speaking">\u2039 Speaking Studio</a><header class="head" style="min-height:0;padding-bottom:0"><h1>81%</h1><p class="lede">Clear and steady. Watch the past tense.</p></header>' +
      '<div class="rows jrows" style="margin-top:22px">' + crit('Pronunciation', 88, '88%') + crit('Fluency', 80, '80%') + crit('Grammar', 68, '68%') + crit('Vocabulary', 84, '84%') + '</div>' +
      '<h2 class="sec">To fix</h2><div class="rows"><div class="fx"><span class="bad-w">yo levant\u00e9 a las siete</span><span class="fix">me levant\u00e9 a las siete</span><span class="desc">Reflexive verbs need me, te, se.</span></div><div class="fx"><span class="bad-w">quiero un cerveza</span><span class="fix">quiero una cerveza</span><span class="desc">Cerveza is feminine.</span></div></div>' +
      '<div class="pad" style="padding-top:22px;display:flex;gap:10px;flex-wrap:wrap"><button class="btn ghost">Listen to yourself</button><button class="btn" data-go="speaking">Try again</button></div>';
  } };
  S.writing = { tab: 'workshop', x: 1, label: 'Writing Studio: task', html: function () {
    return '<div class="xwrap"><div class="xbar" style="grid-template-columns:24px 1fr"><button class="icobtn" data-go="workshop" aria-label="Close">' + XICON + '</button><span class="serif" style="font-size:1.15rem">Writing Studio</span></div>' +
      '<div class="pad" style="padding-top:26px"><p class="serif muted" style="font-size:1.05rem">Task \u00b7 B1</p><h2 class="serif" style="font-size:1.7rem;line-height:1.15;margin-top:10px;text-wrap:balance">Write an email complaining about a hotel room.</h2><p class="muted" style="margin-top:8px;font-size:15px">120 to 150 words.</p>' +
      '<textarea class="fi ta-area" rows="9" style="margin-top:18px">Estimado se\u00f1or: Le escribo para quejarme de la habitaci\u00f3n que reserv\u00e9 la semana pasada\u2026</textarea><div class="cnt-row"><span>23 / 120 words</span></div>' + kws([['quejarme', 1], ['reserva', 0], ['soluci\u00f3n', 0]]) + keys() + '</div>' +
      '<div class="pad" style="margin-top:auto;padding-top:22px;padding-bottom:24px"><button class="btn" style="width:100%;text-align:center" data-go="writing/feedback">Get feedback</button></div></div>';
  } };
  S['writing/feedback'] = { tab: 'workshop', label: 'Writing Studio: feedback', html: function () {
    return '<a class="backl" href="#writing" data-go="writing">\u2039 Writing Studio</a><header class="head" style="min-height:0;padding-bottom:0"><h1>B1</h1><p class="lede">A solid email. Two tenses to tidy.</p></header>' +
      '<div class="rows jrows" style="margin-top:22px">' + crit('Task', 84, '84%') + crit('Grammar', 66, '66%') + crit('Vocabulary', 78, '78%') + crit('Coherence', 80, '80%') + '</div>' +
      '<h2 class="sec">Your text</h2><div class="pad"><p class="serif" style="font-size:1.2rem;line-height:1.7">Estimado se\u00f1or: Le escribo para quejarme de la habitaci\u00f3n que <span class="bad-w">reservo</span> la semana pasada. Cuando <span class="bad-w">llegu\u00e9 estaba</span> sucia.</p>' +
      '<div class="fx" style="margin-top:12px;border-top:1px solid var(--hair)"><span class="bad-w">reservo</span><span class="fix">reserv\u00e9</span><span class="desc">Preterite, first person.</span></div><div class="fx"><span class="bad-w">llegu\u00e9 estaba</span><span class="fix">llegu\u00e9 y estaba</span><span class="desc">Join the two clauses.</span></div></div>';
  } };

  /* other lesson exercise types */
  S['lesson/type'] = { tab: 'lessons', x: 1, label: 'Lesson: type the word', html: function () {
    return '<div class="xwrap">' + xbar(44, '11 / 25') + '<div class="xq"><p class="lab">Type the missing word</p><p class="sent">Yo <span class="blank" style="min-width:5em">beb</span> agua todos los d\u00edas.</p><p class="muted" style="margin-top:12px;font-size:15px">beber, present tense</p></div>' +
      '<div class="pad" style="padding-top:8px"><input class="fi" value="bebo" aria-label="Your answer">' + keys() + '</div>' +
      '<div class="pad" style="margin-top:auto;padding-top:24px;padding-bottom:24px"><button class="btn" style="width:100%;text-align:center">Check</button></div></div>';
  } };
  S['lesson/listen'] = { tab: 'lessons', x: 1, label: 'Lesson: listen and type', html: function () {
    return '<div class="xwrap">' + xbar(52, '13 / 25') + '<div class="xq" style="min-height:0"><p class="lab">Listen and type what you hear</p></div>' +
      '<div class="recwrap">' + play() + '<p class="muted small" style="margin-top:14px"><button class="linkbtn">Slower</button></p></div>' +
      '<div class="pad" style="padding-top:8px"><input class="fi" placeholder="Type in Spanish\u2026" aria-label="Your answer">' + keys() + '</div>' +
      '<div class="pad" style="margin-top:auto;padding-top:24px;padding-bottom:24px"><button class="btn" style="width:100%;text-align:center" disabled>Check</button></div></div>';
  } };
  S['lesson/dialogue'] = { tab: 'lessons', x: 1, label: 'Lesson: dialogue', html: function () {
    var ln = function (who, t, me) { return '<div class="dl' + (me ? ' me' : '') + '"><span class="who2">' + who + '</span><span class="serif">' + t + '</span></div>'; };
    return '<div class="xwrap">' + xbar(60, '15 / 25') + '<div class="pad" style="padding-top:24px"><p class="serif muted" style="font-size:1.05rem">At the caf\u00e9</p>' + ln('Camarero', 'Buenas tardes. \u00bfQu\u00e9 va a tomar?') + ln('Marta', 'Un caf\u00e9 con leche, por favor.', 1) + ln('Camarero', '\u00bfAlgo para comer?') + '</div>' +
      '<p class="fl pad" style="margin-bottom:0">Your reply</p><div class="opts">' + [['A', 'S\u00ed, un pan tostado.'], ['B', 'No, gracias, nada m\u00e1s.'], ['C', 'Tengo veinte a\u00f1os.']].map(function (o, i) { return '<button class="opt' + (i === 1 ? ' sel' : '') + '"><span class="k">' + o[0] + '</span><span>' + o[1] + '</span><span></span></button>'; }).join('') + '</div>' +
      '<div class="pad" style="margin-top:auto;padding-top:24px;padding-bottom:24px"><button class="btn" style="width:100%;text-align:center">Check</button></div></div>';
  } };
  S['lesson/match'] = { tab: 'lessons', x: 1, label: 'Lesson: match pairs', html: function () {
    var L = [['leche', 'ok'], ['pan', 'sel'], ['agua', ''], ['az\u00facar', '']], R = [['bread', ''], ['sugar', ''], ['milk', 'ok'], ['water', '']];
    var b = function (w, st) { return '<button class="opt ' + st + '" style="grid-template-columns:1fr auto"><span>' + w + '</span><span class="mk" style="color:var(--pine)">' + (st === 'ok' ? CHK.replace('<svg', '<svg width="18" height="18" style="stroke:currentColor;fill:none;stroke-width:2.4"') : '') + '</span></button>'; };
    return '<div class="xwrap">' + xbar(64, '16 / 25') + '<div class="xq" style="min-height:0"><p class="lab">Match each word with its meaning</p></div><div class="mcols">' +
      '<div>' + L.map(function (x) { return b(x[0], x[1]); }).join('') + '</div><div>' + R.map(function (x) { return b(x[0], x[1]); }).join('') + '</div></div></div>';
  } };

  /* empty states */
  S['decks/empty'] = { tab: 'decks', label: 'Decks: empty', html: function () {
    var art = hero('<circle class="sand" cx="178" cy="70" r="70"/><rect class="navs" stroke-width="1.5" x="112" y="34" width="70" height="100"/><rect class="navs" stroke-width="1.5" x="140" y="58" width="70" height="100"/>');
    return head('Decks', 'Master vocabulary with spaced repetition.', art) +
      '<div class="pad" style="padding-top:64px"><h2 class="serif" style="font-size:1.8rem;line-height:1.1">No decks yet.</h2><p class="muted" style="margin-top:10px;max-width:24em;font-size:15px">Build your own vocabulary set, or add words as you read and they will collect here.</p>' +
      '<div class="actline" style="gap:10px;flex-wrap:wrap"><button class="btn">Create a deck</button><button class="btn ghost" data-go="library">Browse Parlour decks</button></div></div>';
  } };
  S['decks/caught-up'] = { tab: 'decks', label: 'Decks: all caught up', html: function () {
    var art = hero('<circle class="sand" cx="176" cy="46" r="70"/><path class="navf" d="M96 170A62 62 0 0 1 220 170z"/><path class="navs" d="M70 170h182"/><g class="rise"><path class="ps" stroke-width="1.5" d="M158 92v78"/><circle class="pf" cx="158" cy="92" r="8"/></g>');
    return head('All caught up.', 'Nothing is due right now.', art) +
      '<div class="pad" style="padding-top:96px"><p class="serif" style="font-size:1.4rem">Next review in 3 hours.</p><p class="muted" style="margin-top:8px;font-size:15px">Meanwhile, read a story or practise something new.</p>' +
      '<div class="actline" style="gap:10px;flex-wrap:wrap"><button class="btn" data-go="library">Read</button><button class="btn ghost" data-go="workshop">Practise</button></div></div>';
  } };

  /* sheets */
  S['sheet/deck'] = { tab: 'library', x: 1, label: 'Sheet: add word to deck', html: function () {
    var dk = function (n, c, on) { return '<label class="vi"><span class="cb' + (on ? ' on' : '') + '"></span><span class="serif">' + n + '</span><span class="muted small">' + c + '</span></label>'; };
    return '<div class="xwrap"><div class="dim"><div class="reader"><h1 class="serif" style="font-size:2.2rem;line-height:1.05;margin-top:40px;letter-spacing:-.02em">El tren de las ocho</h1><p>Compra un caf\u00e9 con <span class="w new sel">leche</span> y un pan tostado.</p></div></div>' +
      '<div class="sheet"><p class="serif" style="font-size:1.6rem;line-height:1">Add \u201cleche\u201d to a deck</p><p class="muted small" style="margin-top:6px">milk \u00b7 la leche</p><div style="margin-top:14px;border-top:1px solid var(--hair)">' + dk('A1 Core Vocabulary', '235 words', 1) + dk('Travel and transport', '96 words', 0) + dk('My words', '18 words', 0) + '</div>' +
      '<div class="actline" style="margin-top:18px;gap:10px;flex-wrap:wrap"><button class="btn">Add</button><button class="btn ghost">New deck</button><button class="linkbtn" style="margin-left:auto">Cancel</button></div></div></div>';
  } };
  S['sheet/streak'] = { tab: 'journey', x: 1, label: 'Sheet: import a streak', html: function () {
    return '<div class="xwrap"><div class="dim"><header class="head" style="min-height:0"><h1>Journey</h1></header></div>' +
      '<div class="sheet"><p class="serif" style="font-size:1.6rem;line-height:1">Import your streak</p><p class="muted" style="margin-top:8px;font-size:15px;max-width:26em">Switching from another app? Bring your streak over so your momentum carries on.</p>' +
      '<label class="fl" for="sk">Days</label><input id="sk" class="fi" type="number" value="45">' +
      '<div class="actline" style="margin-top:18px;gap:10px;flex-wrap:wrap"><button class="btn">Save streak</button><button class="linkbtn" style="margin-left:auto">Cancel</button></div></div></div>';
  } };

  
  /* ---------- shell ---------- */
  var order = ['home', 'lessons', 'lessons/path', 'gallery', 'lesson', 'lesson/correct', 'lesson/wrong', 'lesson/done', 'library', 'library/saved', 'library/texts', 'library/editor', 'library/read', 'workshop', 'workshop/verb', 'workshop/drill', 'decks', 'decks/review', 'decks/answer', 'journey', 'journey/passport', 'journey/knowledge', 'journey/skills', 'journey/milestones', 'journey/account', 'welcome', 'welcome/variant', 'welcome/start', 'plan', 'test', 'test/writing', 'test/speaking', 'test/result', 'speaking', 'speaking/feedback', 'writing', 'writing/feedback', 'lesson/type', 'lesson/listen', 'lesson/dialogue', 'lesson/match', 'decks/empty', 'decks/caught-up', 'sheet/deck', 'sheet/streak'];
  $('screen').innerHTML = order.map(function (k) { return '<option value="' + k + '">' + S[k].label + '</option>'; }).join('');

  function renderNav(tab) {
    $('nav').innerHTML = '<div class="brand"><b>Parlour</b><span>A place for language.</span></div><div class="items">' + NAV.map(function (n) {
      return '<button data-go="' + n[0] + '"' + (n[0] === tab ? ' aria-current="page"' : '') + '><svg viewBox="0 0 32 32" aria-hidden="true">' + ICON[n[0]] + '</svg>' + n[1] + '</button>';
    }).join('') + '</div>';
  }
  function go(key) {
    if (!S[key]) key = 'home';
    var s = S[key];
    renderNav(s.tab);
    $('nav').style.display = (s.nonav || s.x) ? 'none' : '';
    var p = $('page'); p.className = 'page' + (s.x ? ' x' : ''); p.innerHTML = s.html();
    $('scroller').scrollTop = 0; $('screen').value = key;
    if (location.hash !== '#' + key) history.replaceState(null, '', '#' + key);
  }
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-go]'); if (!t) return;
    e.preventDefault(); go(t.getAttribute('data-go'));
  });
  $('screen').addEventListener('change', function () { go(this.value); });

  var mode = 'auto', root = document.documentElement;
  function layout() {
    var w = window.innerWidth, l = mode === 'desktop' ? 'desktop' : mode === 'phone' ? 'phone' : (w >= 1024 ? 'desktop' : 'phone');
    root.dataset.layout = l; root.dataset.frame = (mode === 'phone' && w >= 500) ? '1' : '0';
  }
  $('layout').addEventListener('click', function () { mode = mode === 'auto' ? 'phone' : mode === 'phone' ? 'desktop' : 'auto'; this.textContent = 'Layout: ' + mode; layout(); });
  window.addEventListener('resize', layout);
  $('theme').addEventListener('click', function () { var d = root.getAttribute('data-theme') === 'dark'; if (d) root.removeAttribute('data-theme'); else root.setAttribute('data-theme', 'dark'); this.textContent = d ? 'Dark' : 'Light'; });
  layout();
  go((location.hash || '#home').slice(1));
})();
