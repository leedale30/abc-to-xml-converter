#!/usr/bin/env python3
"""Inspect the structure-repeats probe XML output. Measured facts only, via ElementTree."""
import xml.etree.ElementTree as ET
import os, json, sys

HERE = os.path.dirname(os.path.abspath(__file__))
XML = os.path.join(HERE, 'xml')

def load(name):
    return ET.parse(os.path.join(XML, name)).getroot()

def report(title, lines):
    print('=== %s ===' % title)
    for l in lines:
        print('  ' + l)

# ---------- repeats_basic ----------
r = load('repeats_basic.xml')
lines = []
reps = r.findall('.//repeat')
lines.append('repeat elements: %d  directions: %s' %
             (len(reps), [x.get('direction') for x in reps]))
bls = r.findall('.//barline')
lines.append('barlines: %s' % [(b.get('location'),
                                (b.find('bar-style').text if b.find('bar-style') is not None else None),
                                (b.find('repeat').get('direction') if b.find('repeat') is not None else None))
                               for b in bls])
report('repeats_basic', lines)

# ---------- voltas ----------
r = load('voltas.xml')
lines = []
ends = r.findall('.//ending')
lines.append('ending elements: %d  -> %s' %
             (len(ends), [(e.get('number'), e.get('type')) for e in ends]))
reps = r.findall('.//repeat')
lines.append('repeat elements: %d  -> %s' % (len(reps), [x.get('direction') for x in reps]))
report('voltas', lines)

# ---------- dcds_decorations ----------
r = load('dcds_decorations.xml')
lines = []
lines.append('segno elements: %d  coda elements: %d' %
             (len(r.findall('.//segno')), len(r.findall('.//coda'))))
words = [w.text for w in r.findall('.//direction//words')]
lines.append('words texts: %s' % words)
snds = r.findall('.//sound')
lines.append('sound elements: %d  attrs: %s' % (len(snds), [dict(s.attrib) for s in snds]))
other = r.findall('.//other-articulation') + r.findall('.//other-direction')
lines.append('other-articulation/other-direction: %d' % len(other))
report('dcds_decorations', lines)

# ---------- dcds_directives ----------
r = load('dcds_directives.xml')
lines = []
snds = r.findall('.//sound')
lines.append('sound elements: %d  attrs: %s' % (len(snds), [dict(s.attrib) for s in snds]))
# which measure each sound sits in
permeasure = []
for m in r.findall('.//measure'):
    n = len(m.findall('.//sound'))
    if n: permeasure.append((m.get('number'), [dict(s.attrib) for s in m.findall('.//sound')]))
lines.append('sounds per measure: %s' % permeasure)
report('dcds_directives', lines)

# ---------- barline_styles ----------
r = load('barline_styles.xml')
lines = []
bls = r.findall('.//barline')
lines.append('barlines: %s' % [(b.get('location'),
                                b.find('bar-style').text if b.find('bar-style') is not None else None)
                               for b in bls])
report('barline_styles', lines)

# ---------- barnumbers ----------
r = load('barnumbers.xml')
lines = []
mns = r.findall('.//print/measure-numbering')
lines.append('print/measure-numbering elements: %d  values: %s' %
             (len(mns), [m.text for m in mns]))
prints = r.findall('.//print')
lines.append('print elements: %d (in measures %s)' %
             (len(prints), [m.get('number') for m in r.findall('.//measure') if m.find('print') is not None]))
report('barnumbers', lines)

# ---------- metre_change ----------
r = load('metre_change.xml')
lines = []
times = r.findall('.//attributes/time')
lines.append('time elements: %d -> %s' %
             (len(times), [(t.find('beats').text, t.find('beat-type').text) for t in times]))
for m in r.findall('.//measure'):
    t = m.find('.//attributes/time')
    if t is not None:
        lines.append('measure %s carries time %s/%s' %
                     (m.get('number'), t.find('beats').text, t.find('beat-type').text))
report('metre_change', lines)

# ---------- anacrusis ----------
r = load('anacrusis.xml')
lines = []
div = int(r.find('.//attributes/divisions').text)
for m in r.findall('.//measure'):
    dur = sum(int(n.find('duration').text) for n in m.findall('note') if n.find('duration') is not None)
    lines.append('measure %s: implicit=%s  total note duration=%d (divisions=%d, full bar=%d)' %
                 (m.get('number'), m.get('implicit'), dur, div, div * 4))
report('anacrusis', lines)
