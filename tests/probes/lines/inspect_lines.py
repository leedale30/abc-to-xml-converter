#!/usr/bin/env python3
"""Census inspector for the 'lines' domain probes.

Measures spanner-related elements in each probe's emitted MusicXML with
xml.etree (attribute-order independent). Prints one measured-fact block per
probe. No regex over raw XML.
"""
import os, sys, json
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
XMLDIR = os.path.join(HERE, 'xml')

def parents(root):
    return {c: p for p in root.iter() for c in p}

def summarize(path):
    tree = ET.parse(path)
    root = tree.getroot()
    par = parents(root)
    out = {}

    def anc_tag(el, tag):
        e = el
        while e is not None:
            if e.tag == tag: return True
            e = par.get(e)
        return False

    # glissando / slide
    for tag in ('glissando', 'slide'):
        els = list(root.iter(tag))
        out[tag] = [{'type': e.get('type'), 'line-type': e.get('line-type'),
                     'number': e.get('number'), 'in_notations': anc_tag(e, 'notations')}
                    for e in els]

    # pedal
    out['pedal'] = [{'type': e.get('type'), 'line': e.get('line'), 'sign': e.get('sign'),
                     'in_direction': anc_tag(e, 'direction')} for e in root.iter('pedal')]

    # octave-shift
    out['octave-shift'] = [{'type': e.get('type'), 'size': e.get('size'),
                            'in_direction': anc_tag(e, 'direction')} for e in root.iter('octave-shift')]

    # wedges: where do they land?
    out['wedge'] = [{'type': e.get('type'), 'niente': e.get('niente'),
                     'parent': par[e].tag,
                     'in_direction': anc_tag(e, 'direction'),
                     'in_notations': anc_tag(e, 'notations')} for e in root.iter('wedge')]

    # dashes / bracket direction spans
    out['dashes'] = [{'type': e.get('type')} for e in root.iter('dashes')]
    out['bracket'] = [{'type': e.get('type'), 'line-end': e.get('line-end')}
                      for e in root.iter('bracket')]

    # phantom other-articulation (D31 class)
    oa = list(root.iter('other-articulation'))
    out['other-articulation'] = {}
    for e in oa:
        t = (e.text or '').strip()
        out['other-articulation'][t] = out['other-articulation'].get(t, 0) + 1

    # note census: count notes and their written pitches (step+octave)
    notes = []
    for n in root.iter('note'):
        p = n.find('pitch')
        if p is not None:
            notes.append(p.findtext('step') + p.findtext('octave'))
    out['note_count'] = len(notes)
    out['written_pitches'] = notes
    return out

def main():
    results = {}
    for f in sorted(os.listdir(XMLDIR)):
        if not f.endswith('.xml'): continue
        results[f] = summarize(os.path.join(XMLDIR, f))
    print(json.dumps(results, indent=1))

if __name__ == '__main__':
    main()
