#!/usr/bin/env python3
"""Inspect the dynamics-directions-tempo probe XMLs with element-level measurements."""
import xml.etree.ElementTree as ET
import os, json

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'xml')

def load(name):
    return ET.parse(os.path.join(D, name)).getroot()

def report(title, facts):
    print('==== %s' % title)
    for f in facts: print('  ' + f)

# p01: basic dynamics
r = load('p01_dynamics_basic.xml')
dyns = r.findall('.//dynamics')
children = [c.tag for d in dyns for c in d]
report('p01_dynamics_basic', [
    'dynamics elements: %d' % len(dyns),
    'children in order: %s' % children,
])

# p02: special dynamics
r = load('p02_dynamics_special.xml')
dyns = r.findall('.//dynamics')
children = [c.tag for d in dyns for c in d]
others = [o.text for o in r.findall('.//other-dynamics')]
report('p02_dynamics_special', [
    'dynamics elements: %d' % len(dyns),
    'children in order: %s' % children,
    'other-dynamics texts: %s' % others,
])

# p03: words
r = load('p03_words_directions.xml')
words = r.findall('.//direction-type/words')
placements = [(w.text, d.get('placement')) for d in r.findall('.//direction') for w in d.findall('direction-type/words')]
report('p03_words_directions', [
    'words elements: %d' % len(words),
    '(text, placement): %s' % placements,
])

# p04: rehearsal marks
r = load('p04_rehearsal_marks.xml')
rehs = r.findall('.//rehearsal')
per_measure = {}
for m in r.findall('.//measure'):
    n = m.get('number')
    got = m.findall('.//rehearsal')
    if got: per_measure[n] = [(x.text, x.get('font-weight')) for x in got]
report('p04_rehearsal_marks', [
    'rehearsal elements: %d' % len(rehs),
    'by measure (text, font-weight): %s' % per_measure,
])

# p05: metronome basic
r = load('p05_metronome_basic.xml')
metros = r.findall('.//metronome')
facts = ['metronome elements: %d' % len(metros)]
for me in metros:
    facts.append('metronome children: %s' % [(c.tag, c.text) for c in me])
facts.append('sound tempo values: %s' % [s.get('tempo') for s in r.findall('.//sound') if s.get('tempo')])
report('p05_metronome_basic', facts)

# p06: dotted beat unit
r = load('p06_metronome_dotted.xml')
metros = r.findall('.//metronome')
facts = ['metronome elements: %d' % len(metros)]
for me in metros:
    facts.append('metronome children: %s' % [(c.tag, c.text) for c in me])
facts.append('sound tempo values: %s' % [s.get('tempo') for s in r.findall('.//sound') if s.get('tempo')])
report('p06_metronome_dotted', facts)

# p07: metric modulation attempt
r = load('p07_metric_modulation.xml')
metros = r.findall('.//metronome')
facts = ['metronome elements: %d' % len(metros)]
for me in metros:
    facts.append('metronome children: %s' % [(c.tag, c.text) for c in me])
facts.append('beat-unit-tied/metronome-relation present: %d/%d' % (
    len(r.findall('.//metronome-tied')), len(r.findall('.//metronome-relation'))))
facts.append('sound tempo values: %s' % [s.get('tempo') for s in r.findall('.//sound') if s.get('tempo')])
report('p07_metric_modulation', facts)

# p08: mid-piece Q
r = load('p08_q_midpiece.xml')
facts = []
for m in r.findall('.//measure'):
    n = m.get('number')
    seq = []
    for child in m:
        if child.tag == 'note':
            step = child.find('pitch/step')
            seq.append('note:%s' % (step.text if step is not None else 'rest'))
        elif child.tag == 'direction':
            t = child.find('sound')
            mt = child.find('direction-type/metronome')
            if t is not None and t.get('tempo'):
                pm = mt.find('per-minute').text if mt is not None else '?'
                bu = mt.find('beat-unit').text if mt is not None else '?'
                seq.append('Qdir:%s=%s(sound=%s)' % (bu, pm, t.get('tempo')))
    facts.append('measure %s stream: %s' % (n, ' '.join(seq)))
report('p08_q_midpiece', facts)

# p09: tempo text
r = load('p09_tempo_text.xml')
facts = []
for d in r.findall('.//direction'):
    ws = [w.text for w in d.findall('direction-type/words')]
    me = d.find('direction-type/metronome')
    snd = d.find('sound')
    if ws or me is not None:
        facts.append('direction words=%s metronome=%s sound-tempo=%s' % (
            ws, [(c.tag, c.text) for c in me] if me is not None else None,
            snd.get('tempo') if snd is not None else None))
report('p09_tempo_text', facts)

# p10: rit/accel as text
r = load('p10_rit_accel_text.xml')
words = [(w.text, d.get('placement')) for d in r.findall('.//direction') for w in d.findall('direction-type/words')]
sounds = [s.attrib for s in r.findall('.//sound')]
report('p10_rit_accel_text', [
    'words (text, placement): %s' % words,
    'sound elements: %s' % sounds,
])

# p11: capo decorations
r = load('p11_dacapo_segno_decos.xml')
facts = []
for m in r.findall('.//measure'):
    n = m.get('number')
    for d in m.findall('direction'):
        dts = [c.tag + (':' + c.text if c.text else '') for dt in d.findall('direction-type') for c in dt]
        snd = d.find('sound')
        if dts or snd is not None:
            facts.append('m%s direction-types=%s sound=%s' % (n, dts, snd.attrib if snd is not None else None))
report('p11_dacapo_segno_decos', facts)

# p12: sound-only directives
r = load('p12_sound_directives.xml')
facts = []
for m in r.findall('.//measure'):
    n = m.get('number')
    for d in m.findall('direction'):
        snd = d.find('sound')
        dts = [c.tag for dt in d.findall('direction-type') for c in dt]
        if snd is not None:
            facts.append('m%s sound=%s (direction-types=%s)' % (n, snd.attrib, dts))
report('p12_sound_directives', facts)

# p13: tempofont
r = load('p13_tempofont.xml')
facts = []
for d in r.findall('.//direction'):
    for dt in d.findall('direction-type'):
        for c in dt:
            if c.tag in ('words', 'metronome'):
                facts.append('%s text=%r font-family=%r' % (c.tag, c.text, c.get('font-family')))
report('p13_tempofont', facts)

# p14: sound tempo arithmetic
r = load('p14_sound_tempo_values.xml')
facts = []
for m in r.findall('.//measure'):
    n = m.get('number')
    for d in m.findall('direction'):
        snd = d.find('sound')
        me = d.find('direction-type/metronome')
        if snd is not None and snd.get('tempo'):
            facts.append('m%s metronome=%s sound-tempo=%s' % (
                n, [(c.tag, c.text) for c in me] if me is not None else None, snd.get('tempo')))
report('p14_sound_tempo_values', facts)
