#!/usr/bin/env python3
"""Inspector for pitch-staff census probes: dumps measured facts per XML file."""
import sys, glob, os
import xml.etree.ElementTree as ET

def facts(path):
    tree = ET.parse(path)
    root = tree.getroot()
    out = []
    parts = root.findall('part')
    out.append('parts=%d' % len(parts))
    for ip, part in enumerate(parts):
        pid = part.get('id')
        # clefs
        for c in part.iter('clef'):
            sign = c.findtext('sign'); line = c.findtext('line')
            coc = c.findtext('clef-octave-change')
            out.append('%s clef sign=%s line=%s octave-change=%s' % (pid, sign, line, coc))
        # keys
        for k in part.iter('key'):
            fifths = k.findtext('fifths'); mode = k.findtext('mode')
            steps = [e.text for e in k.findall('key-step')]
            alts = [e.text for e in k.findall('key-alter')]
            koct = [(e.get('number'), e.text) for e in k.findall('key-octave')]
            s = '%s key fifths=%s mode=%s' % (pid, fifths, mode)
            if steps: s += ' key-steps=%s key-alters=%s key-octaves=%s' % (steps, alts, koct)
            out.append(s)
        # times
        for t in part.iter('time'):
            out.append('%s time symbol=%s beats=%s beat-type=%s' %
                       (pid, t.get('symbol'), t.findtext('beats'), t.findtext('beat-type')))
        # staff-details / transpose
        for sd in part.iter('staff-details'):
            tun = [(st.findtext('tuning-step'), st.findtext('tuning-octave')) for st in sd.findall('staff-tuning')]
            out.append('%s staff-details staff-lines=%s staff-tunings=%d %s' %
                       (pid, sd.findtext('staff-lines'), len(tun), tun if tun else ''))
        for tr in part.iter('transpose'):
            out.append('%s transpose chromatic=%s diatonic=%s' %
                       (pid, tr.findtext('chromatic'), tr.findtext('diatonic')))
        # notes: pitch/unpitched/accidental/notehead
        pitches, unp, accs, nheads, others = [], [], [], [], []
        for n in part.iter('note'):
            p = n.find('pitch')
            if p is not None:
                pitches.append('%s%s%s' % (p.findtext('step'),
                                           '(%s)' % p.findtext('alter') if p.find('alter') is not None else '',
                                           p.findtext('octave')))
            u = n.find('unpitched')
            if u is not None:
                unp.append('%s%s' % (u.findtext('display-step'), u.findtext('display-octave')))
            a = n.find('accidental')
            if a is not None:
                accs.append(a.text + ('[paren]' if a.get('parentheses') == 'yes' else ''))
            nh = n.find('notehead')
            if nh is not None:
                nheads.append(nh.text + ('[filled=%s]' % nh.get('filled') if nh.get('filled') else ''))
        for oa in part.iter('other-articulation'):
            others.append(oa.text)
        out.append('%s pitches(n=%d)=%s' % (pid, len(pitches), pitches[:16]))
        if unp: out.append('%s unpitched(n=%d)=%s' % (pid, len(unp), unp[:16]))
        out.append('%s accidentals(n=%d)=%s' % (pid, len(accs), accs))
        if nheads: out.append('%s noteheads(n=%d)=%s' % (pid, len(nheads), nheads))
        if others: out.append('%s other-articulations(n=%d)=%s' % (pid, len(others), others))
        # instrument refs (percussion)
        insts = set(i.get('id') for i in part.iter('instrument'))
        if insts: out.append('%s note-instrument-ids=%s' % (pid, sorted(insts)))
    # score-part midi-unpitched
    for sp in root.iter('score-part'):
        for mi in sp.iter('midi-instrument'):
            mu = mi.findtext('midi-unpitched')
            if mu: out.append('score-part %s midi-instrument %s midi-unpitched=%s' % (sp.get('id'), mi.get('id'), mu))
    return out

for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__) or '.', 'xml', '*.xml'))):
    print('===== %s =====' % os.path.basename(f))
    for line in facts(f):
        print('  ' + line)
