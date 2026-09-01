#!/usr/bin/env python3
"""Census inspector for ornament probes: per-note notations content, attribute-order-independent."""
import sys, glob, os
import xml.etree.ElementTree as ET

def describe(el):
    attrs = ' '.join('%s=%s' % (k, v) for k, v in sorted(el.attrib.items()))
    txt = (el.text or '').strip()
    out = el.tag
    if attrs: out += '[' + attrs + ']'
    if txt: out += '="%s"' % txt
    return out

def main(xmldir):
    for path in sorted(glob.glob(os.path.join(xmldir, '*.xml'))):
        print('##', os.path.basename(path))
        tree = ET.parse(path)
        root = tree.getroot()
        ni = 0
        for part in root.iter('part'):
            for meas in part.iter('measure'):
                for note in meas.iter('note'):
                    ni += 1
                    pitch = note.find('pitch')
                    if pitch is not None:
                        p = pitch.findtext('step', '') + pitch.findtext('octave', '')
                    else:
                        p = 'rest'
                    dur = note.findtext('duration', '-')
                    ntype = note.findtext('type', '-')
                    tmod = note.find('time-modification')
                    tm = ''
                    if tmod is not None:
                        tm = ' tmod=%s:%s' % (tmod.findtext('actual-notes'), tmod.findtext('normal-notes'))
                    items = []
                    for nots in note.findall('notations'):
                        for child in nots:
                            if child.tag in ('ornaments', 'articulations', 'technical'):
                                for sub in child:
                                    items.append(child.tag + '/' + describe(sub))
                            else:
                                items.append(describe(child))
                    line = '  n%02d %-5s dur=%-5s type=%-8s%s' % (ni, p, dur, ntype, tm)
                    if items: line += ' | ' + ' ; '.join(items)
                    print(line)
        print()

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'xml')
