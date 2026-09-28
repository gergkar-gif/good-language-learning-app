#!/usr/bin/env python3
"""Turn raw takes from tools/sound-recorder/recordings/ into lesson-ready MP3s.

For each <id>.wav: high-pass (rumble), find the spoken part, cut everything
else — including the lip smack / breath / key click that sits a little
before or after the word — fade the edges, level every clip to the same
loudness, and write content/hu/audio/sounds/<id>.mp3.

The lesson files get a light "studio" voice chain (see studio()): gentle EQ
and 2:1 compression, no reverb, no de-essing (sz/s/cs are the lesson).
A plain version (rumble filter + levelling only) goes to plain/ so the two
can be A/B'd on review.html.

Finding the spoken part: 5 ms energy frames are grouped into segments
(split on 30 ms of quiet). The segment with the most energy is the core
(not the loudest frame: a final t/k release can out-peak the vowel). The core is widened backwards only across near-touching segments
(an sz hiss or a stop burst runs straight into the vowel; a smack is
separated from it by a gap), and — for words only — forwards across a
short closure, so a final t/k release is kept. Isolated vowels and held
consonants never widen forwards.

When the automatic cut is wrong, put {"<id>": {"start_ms": .., "end_ms": ..}}
in trim-overrides.json (raw-take milliseconds, either key optional).

Writes review.json (cut points + a waveform envelope per take) for
review.html.

    python tools/sound-recorder/process.py
"""

import array
import json
import math
import wave
from pathlib import Path

import lameenc

HERE = Path(__file__).resolve().parent
RAW = HERE / 'recordings'
OUT = HERE.parents[1] / 'content' / 'hu' / 'audio' / 'sounds'
OVERRIDES = HERE / 'trim-overrides.json'

FRAME_MS = 5
SPLIT_GAP_MS = 30        # quiet this long splits two segments
BACK_GAP_MS = 60         # widen backwards only across gaps this short
FORWARD_GAP_MS = 200     # words: keep a final stop release after a closure this long
MIN_TAIL_PEAK = 0.12     # ...if that release is at least this loud (x core peak)
PRE_PAD_MS, POST_PAD_MS = 25, 60
FADE_IN_MS, FADE_OUT_MS = 12, 40
TARGET_DBFS = -18.0      # loudness of the voiced part
PEAK_CEILING = 10 ** (-1.0 / 20)
PLAIN = HERE / 'plain'


def read(path):
    with wave.open(str(path)) as w:
        rate = w.getframerate()
        samples = array.array('h', w.readframes(w.getnframes()))
    return [s / 32768 for s in samples], rate


def high_pass(x, rate, cutoff=70.0):
    rc = 1 / (2 * math.pi * cutoff)
    alpha = rc / (rc + 1 / rate)
    out, prev_x, prev_y = [], 0.0, 0.0
    for v in x:
        prev_y = alpha * (prev_y + v - prev_x)
        prev_x = v
        out.append(prev_y)
    return out


def biquad(x, b0, b1, b2, a0, a1, a2):
    b0, b1, b2, a1, a2 = b0 / a0, b1 / a0, b2 / a0, a1 / a0, a2 / a0
    out, x1, x2, y1, y2 = [], 0.0, 0.0, 0.0, 0.0
    for v in x:
        y = b0 * v + b1 * x1 + b2 * x2 - a1 * y1 - a2 * y2
        x2, x1, y2, y1 = x1, v, y1, y
        out.append(y)
    return out


# RBJ audio-EQ-cookbook filters.
def hp_biquad(x, rate, f, q=0.707):
    w = 2 * math.pi * f / rate
    alpha, c = math.sin(w) / (2 * q), math.cos(w)
    return biquad(x, (1 + c) / 2, -(1 + c), (1 + c) / 2, 1 + alpha, -2 * c, 1 - alpha)


def peaking(x, rate, f, gain_db, q):
    A, w = 10 ** (gain_db / 40), 2 * math.pi * f / rate
    alpha, c = math.sin(w) / (2 * q), math.cos(w)
    return biquad(x, 1 + alpha * A, -2 * c, 1 - alpha * A, 1 + alpha / A, -2 * c, 1 - alpha / A)


def high_shelf(x, rate, f, gain_db):
    A, w = 10 ** (gain_db / 40), 2 * math.pi * f / rate
    c, alpha = math.cos(w), math.sin(w) / 2 * math.sqrt(2)
    sq = 2 * math.sqrt(A) * alpha
    return biquad(x, A * ((A + 1) + (A - 1) * c + sq), -2 * A * ((A - 1) + (A + 1) * c),
                  A * ((A + 1) + (A - 1) * c - sq), (A + 1) - (A - 1) * c + sq,
                  2 * ((A - 1) - (A + 1) * c), (A + 1) - (A - 1) * c - sq)


def compress(x, rate, ratio=2.0, below_peak_db=12, attack_ms=5, release_ms=80):
    """Feed-forward peak compressor; threshold sits below the clip's own peak."""
    att, rel = math.exp(-1 / (rate * attack_ms / 1000)), math.exp(-1 / (rate * release_ms / 1000))
    env, envs = 0.0, []
    for v in x:
        a = abs(v)
        env = att * env + (1 - att) * a if a > env else rel * env + (1 - rel) * a
        envs.append(env)
    threshold = max(envs) * 10 ** (-below_peak_db / 20)
    return [v * ((e / threshold) ** (1 / ratio - 1) if e > threshold else 1.0) for v, e in zip(x, envs)]


def studio(x, rate):
    x = hp_biquad(x, rate, 90)            # rumble, handling thumps
    x = peaking(x, rate, 300, -2.5, 1.0)  # small-room boxiness
    x = peaking(x, rate, 4000, 2.0, 1.0)  # presence, kept modest for sz/s/cs
    return high_shelf(x, rate, 10000, 1.5)  # air


def frame_rms(x, n):
    return [math.sqrt(sum(v * v for v in x[i:i + n]) / n) for i in range(0, len(x) - n + 1, n)]


def segments(rms):
    floor = sorted(rms)[len(rms) // 20]
    loud = max(rms)
    threshold = max(floor * 4, loud * 0.05)
    active = [i for i, v in enumerate(rms) if v > threshold]
    split = SPLIT_GAP_MS // FRAME_MS
    segs, start, prev = [], active[0], active[0]
    for i in active[1:]:
        if i - prev > split:
            segs.append([start, prev])
            start = i
        prev = i
    segs.append([start, prev])
    return [(s, e, max(rms[s:e + 1]) / loud, sum(v * v for v in rms[s:e + 1])) for s, e in segs]


def find_cut(rms, is_word):
    segs = segments(rms)
    core = max(range(len(segs)), key=lambda k: segs[k][3])
    start, end = segs[core][0], segs[core][1]
    k = core - 1
    while k >= 0 and start - segs[k][1] <= BACK_GAP_MS // FRAME_MS:
        start = segs[k][0]
        k -= 1
    if is_word:
        k = core + 1
        while (k < len(segs) and segs[k][0] - end <= FORWARD_GAP_MS // FRAME_MS
               and segs[k][2] >= MIN_TAIL_PEAK):
            end = segs[k][1]
            k += 1
    return start * FRAME_MS, (end + 1) * FRAME_MS


def finish(clip, rate, voiced_threshold):
    n = rate * FRAME_MS // 1000
    clip = list(clip)
    fin, fout = FADE_IN_MS * rate // 1000, FADE_OUT_MS * rate // 1000
    for i in range(min(fin, len(clip))):
        clip[i] *= 0.5 - 0.5 * math.cos(math.pi * i / fin)
    for i in range(min(fout, len(clip))):
        clip[-1 - i] *= 0.5 - 0.5 * math.cos(math.pi * i / fout)
    frames = frame_rms(clip, n)
    voiced = [v for v in frames if v > max(frames) * voiced_threshold]
    loudness = math.sqrt(sum(v * v for v in voiced) / len(voiced))
    gain = 10 ** (TARGET_DBFS / 20) / loudness
    gain = min(gain, PEAK_CEILING / max(abs(v) for v in clip))
    return array.array('h', (int(max(-1, min(1, v * gain)) * 32767) for v in clip)), gain


def write_mp3(path, pcm, rate):
    enc = lameenc.Encoder()
    enc.set_bit_rate(96)
    enc.set_in_sample_rate(rate)
    enc.set_channels(1)
    enc.set_quality(2)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(enc.encode(pcm.tobytes()) + enc.flush())


def process(item_id, overrides):
    raw, rate = read(RAW / f'{item_id}.wav')
    x = high_pass(raw, rate)
    n = rate * FRAME_MS // 1000
    rms = frame_rms(x, n)
    auto_start, auto_end = find_cut(rms, item_id.startswith('word-'))
    manual = overrides.get(item_id, {})
    start_ms = manual.get('start_ms', auto_start)
    end_ms = manual.get('end_ms', auto_end)
    a = max(0, (start_ms - PRE_PAD_MS) * rate // 1000)
    b = min(len(x), (end_ms + POST_PAD_MS) * rate // 1000)

    plain, gain = finish(x[a:b], rate, 0.25)
    write_mp3(PLAIN / f'{item_id}.mp3', plain, rate)
    # EQ runs on the whole take so filter start-up never lands inside the clip.
    polished, _ = finish(compress(studio(raw, rate)[a:b], rate), rate, 0.25)
    write_mp3(OUT / f'{item_id}.mp3', polished, rate)

    return {
        'id': item_id,
        'rawMs': len(x) * 1000 // rate,
        'cut': [max(0, start_ms - PRE_PAD_MS), min(len(x) * 1000 // rate, end_ms + POST_PAD_MS)],
        'manual': bool(manual),
        'gainDb': round(20 * math.log10(gain), 1),
        'envelope': [round(v / max(rms), 3) for v in rms],
    }


def main():
    overrides = json.loads(OVERRIDES.read_text(encoding='utf-8')) if OVERRIDES.exists() else {}
    report = [process(p.stem, overrides) for p in sorted(RAW.glob('*.wav'))]
    (HERE / 'review.json').write_text(json.dumps(report), encoding='utf-8')
    for r in report:
        print(f"{r['id']:22} keep {r['cut'][0]:5d}-{r['cut'][1]:5d} ms of {r['rawMs']:5d}"
              f"  gain {r['gainDb']:+5.1f} dB{'  (manual)' if r['manual'] else ''}")


if __name__ == '__main__':
    main()
