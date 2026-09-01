#!/usr/bin/env python3
"""Inspect the abcplus-extensions probe XML outputs with ElementTree (no regex verdicts)."""
import xml.etree.ElementTree as ET
import os, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')

def load(name):
    return ET.parse(os.path.join(OUT, name)).getroot()

def show(title):
    print('\n=== %s ===' % title)

# p01 vel:
r = load('p01_vel_pernote.xml')
show('p01 vel:')
ods = r.findall('.//direction/direction-type/other-direction')
snds = r.findall('.//direction/sound')
print('other-direction texts:', [o.text for o in ods])
print('direction/sound dynamics attrs:', [s.get('dynamics') for s in snds])
dirs = r.findall('.//direction')
for d in dirs:
    od = d.find('direction-type/other-direction')
    if od is not None:
        print('direction placement=%s, has sound=%s' % (d.get('placement'), d.find('sound') is not None))

# p02/p03 harp
for f, tag in [('p02_harp_pedals_deco.xml','p02 harp deco'), ('p03_harp_pedals_directive.xml','p03 harp directive')]:
    r = load(f); show(tag)
    hps = r.findall('.//harp-pedals')
    print('harp-pedals count:', len(hps))
    for hp in hps:
        tunings = hp.findall('pedal-tuning')
        print('pedal-tuning count:', len(tunings))
        print('steps/alters:', [(t.findtext('pedal-step'), t.findtext('pedal-alter')) for t in tunings])

# p04/p05 accordion
for f, tag in [('p04_accordion_deco.xml','p04 accordion deco'), ('p05_accordion_directive.xml','p05 accordion directive')]:
    r = load(f); show(tag)
    ars = r.findall('.//accordion-registration')
    print('accordion-registration count:', len(ars))
    for ar in ars:
        print('children:', [(c.tag, c.text) for c in ar])

# p06 per-voice MIDI program
r = load('p06_midi_program_pervoice.xml'); show('p06 per-voice MIDI program')
for sp in r.findall('part-list/score-part'):
    mi = sp.find('midi-instrument')
    print(sp.findtext('part-name'), '-> midi-program:', mi.findtext('midi-program') if mi is not None else None,
          'midi-channel:', mi.findtext('midi-channel') if mi is not None else None)

# p07 channel + control
r = load('p07_midi_channel_control.xml'); show('p07 channel/control')
for sp in r.findall('part-list/score-part'):
    mi = sp.find('midi-instrument')
    if mi is not None:
        print(sp.findtext('part-name'), {c.tag: c.text for c in mi})

# p08 bank forms
r = load('p08_midi_bank_forms.xml'); show('p08 bank/vol/pan forms')
for sp in r.findall('part-list/score-part'):
    mi = sp.find('midi-instrument')
    print(sp.findtext('part-name'), {c.tag: c.text for c in mi} if mi is not None else None)

# p09 mid-tune change
r = load('p09_midi_midtune_change.xml'); show('p09 mid-tune instrument change')
for d in r.findall('.//direction'):
    w = d.find('direction-type/words')
    snd = d.find('sound')
    if w is not None and snd is not None:
        mi = snd.find('midi-instrument')
        print('words:', w.text, '| sound/midi-instrument children:',
              {c.tag: c.text for c in mi} if mi is not None else None)
# header instrument for the part
for sp in r.findall('part-list/score-part'):
    mi = sp.find('midi-instrument')
    print('part-list midi-program:', mi.findtext('midi-program') if mi is not None else None)

# p10 MIDI= form
r = load('p10_midi_equals_form.xml'); show('p10 MIDI= form')
for sp in r.findall('part-list/score-part'):
    mi = sp.find('midi-instrument')
    print(sp.findtext('part-name'), '-> midi-program:', mi.findtext('midi-program') if mi is not None else None)

# p11 instrument sounds
r = load('p11_instrument_sounds.xml'); show('p11 instrument-sound mapping')
for sp in r.findall('part-list/score-part'):
    snd = sp.find('score-instrument/instrument-sound')
    print(sp.findtext('part-name'), '->', snd.text if snd is not None else None)

# p12-p17 score semantics
for f, tag in [('p12_score_bracket.xml','p12 [V1 V2] bracket'),
               ('p13_score_paren.xml','p13 (V1 V2) paren'),
               ('p14_score_brace_grand.xml','p14 {RH LH} one named'),
               ('p15_score_brace_rejected.xml','p15 {V1 V2} both named'),
               ('p16_score_star_grand.xml','p16 {* V1 V2}'),
               ('p17_score_badvoice.xml','p17 bad voice id')]:
    r = load(f); show(tag)
    pl = r.find('part-list')
    sps = pl.findall('score-part')
    pgs = pl.findall('part-group')
    print('score-part count:', len(sps), '| ids:', [sp.get('id') for sp in sps])
    print('part-groups:', [(pg.get('type'), pg.get('number'), pg.findtext('group-symbol')) for pg in pgs])
    parts = r.findall('part')
    for p in parts:
        m1 = p.find('measure')
        staves = m1.findtext('attributes/staves') if m1 is not None else None
        clefs = [c.findtext('sign') for c in m1.findall('attributes/clef')] if m1 is not None else []
        nvoices = sorted(set(n.findtext('voice') for n in m1.findall('note'))) if m1 is not None else []
        print('part', p.get('id'), 'staves:', staves, 'clefs:', clefs, 'voices in m1:', nvoices,
              'notes in m1:', len(m1.findall('note')) if m1 is not None else 0)

# p18 measurenb
r = load('p18_measurenb.xml'); show('p18 measurenb')
nums = [m.get('number') for m in r.findall('part/measure')]
print('measure numbers:', nums)

# p19-21 measure numbering
for f, tag in [('p19_measurenumbering.xml','p19 measurenumbering yes'),
               ('p20_measurenumbering_default.xml','p20 default (no directive)'),
               ('p21_barnumbers.xml','p21 barnumbers 1')]:
    r = load(f); show(tag)
    mns = r.findall('.//print/measure-numbering')
    prints = r.findall('.//print')
    msrs = r.findall('part/measure')
    print('measure count:', len(msrs), '| print count:', len(prints),
          '| measure-numbering texts:', [m.text for m in mns])

# p22 swing/mute
r = load('p22_swing_mute.xml'); show('p22 swing/mute')
for s in r.findall('.//sound'):
    at = dict(s.attrib)
    if at: print('sound attrs:', at)

# p23 tempofont
r = load('p23_tempofont.xml'); show('p23 tempofont')
for m in r.findall('.//metronome'):
    print('metronome attrs:', dict(m.attrib), 'beat-unit:', m.findtext('beat-unit'), 'per-minute:', m.findtext('per-minute'))
for w in r.findall('.//direction/direction-type/words'):
    print('words:', w.text, dict(w.attrib))

# p24 linked-tab
r = load('p24_linked_tab.xml'); show('p24 linked-tab')
pl = r.find('part-list')
print('score-parts:', [(sp.get('id'), sp.findtext('part-name')) for sp in pl.findall('score-part')])
for p in r.findall('part'):
    m1 = p.find('measure')
    staves = m1.findtext('attributes/staves')
    clefs = [(c.findtext('sign'), c.findtext('line')) for c in m1.findall('attributes/clef')]
    tabs = m1.findall('.//notations/technical')
    print('part', p.get('id'), 'staves:', staves, 'clefs:', clefs,
          'notes:', len(m1.findall('note')),
          'string/fret pairs in m1:', [(t.findtext('string'), t.findtext('fret')) for t in tabs])
