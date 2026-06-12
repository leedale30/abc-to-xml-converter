#!/usr/bin/env python3
"""MusicXML → ABC+ Converter v1.0

Usage:
    python xml2abc.py input.musicxml                    # prints to stdout
    python xml2abc.py input.musicxml -o output.abc      # writes to file
    python xml2abc.py input.musicxml -o output.abc -t "My Title" -c "Composer"
"""

import xml.etree.ElementTree as ET
import argparse, sys, os, re

# ─── Constants ───────────────────────────────────────────────────────────────

NOTE_MAP = {
    ('C',0):'C',('D',0):'D',('E',0):'E',('F',0):'F',
    ('G',0):'G',('A',0):'A',('B',0):'B',
    ('C',1):'^C',('D',1):'^D',('E',1):'^E',('F',1):'^F',
    ('G',1):'^G',('A',1):'^A',('B',1):'^B',
    ('C',-1):'_C',('D',-1):'_D',('E',-1):'_E',('F',-1):'_F',
    ('G',-1):'_G',('A',-1):'_A',('B',-1):'_B',
    ('C',2):'^^C',('D',2):'^^D',('E',2):'^^E',('F',2):'^^F',
    ('G',2):'^^G',('A',2):'^^A',('B',2):'^^B',
    ('C',-2):'__C',('D',-2):'__D',('E',-2):'__E',('F',-2):'__F',
    ('G',-2):'__G',('A',-2):'__A',('B',-2):'__B',
}

FIFTHS_KEY = {
    -7:'Cb',-6:'Gb',-5:'Db',-4:'Ab',-3:'Eb',-2:'Bb',-1:'F',
    0:'C',1:'G',2:'D',3:'A',4:'E',5:'B',6:'F#',7:'C#'
}
FIFTHS_MINOR = {
    -7:'Ab',-6:'Eb',-5:'Bb',-4:'F',-3:'C',-2:'G',-1:'D',
    0:'A',1:'E',2:'B',3:'F#',4:'C#',5:'G#',6:'D#',7:'A#'
}

CLEF_MAP = {
    ('G','2'):'treble',('F','4'):'bass',('C','3'):'alto',('C','4'):'tenor',
    ('G',None):'treble',('F',None):'bass',('percussion',None):'perc',
}

KIND_MAP = {
    'major':'','minor':'m','dominant':'7','major-seventh':'maj7',
    'minor-seventh':'m7','diminished':'dim','augmented':'aug',
    'half-diminished':'m7b5','dominant-ninth':'9','major-minor':'mMaj7',
    'suspended-fourth':'sus4','suspended-second':'sus2',
    'diminished-seventh':'dim7','major-sixth':'6','minor-sixth':'m6',
    'dominant-11th':'11','major-ninth':'maj9','minor-ninth':'m9',
}

DYN_TAGS = {'ppp','pp','p','mp','mf','f','ff','fff','sfz','sfp','rfz','fp','sf','fz','n'}

ARTICULATION_MAP = {
    'staccato':'staccato','accent':'accent','tenuto':'tenuto',
    'strong-accent':'marcato','staccatissimo':'staccatissimo',
    'detached-legato':'tenuto','spiccato':'staccato',
}

ORNAMENT_MAP = {
    'trill-mark':'trill','mordent':'mordent','inverted-mordent':'uppermordent',
    'turn':'turn','delayed-turn':'turn','inverted-turn':'turn',
    'vertical-turn':'vertical-turn','shake':'shake','schleifer':'schleifer',
}

# ─── Pitch / Duration Helpers ────────────────────────────────────────────────

def pitch_to_abc(step, octave, alter=0):
    alter = int(float(alter)) if alter else 0
    base = NOTE_MAP.get((step, alter), step)
    o = int(octave)
    if o <= 3:
        note = base.upper() if len(base)==1 else base[:-1]+base[-1].upper()
        commas = 4 - o
        if commas > 0:
            note = note[:-1] + note[-1] + ',' * (commas - 1)
    elif o == 4:
        note = base
    else:
        note = base[:-1]+base[-1].lower() if len(base)>1 else base.lower()
        if o > 5:
            note += "'" * (o - 5)
    return note

def dur_to_abc(dur_type, dots=0):
    """Convert MusicXML type + dot count → ABC length modifier (relative to L:1/8)."""
    base_map = {'whole':8,'half':4,'quarter':2,'eighth':1,'16th':0.5,'32nd':0.25,'64th':0.125}
    val = base_map.get(dur_type, 1)
    for _ in range(dots):
        val *= 1.5
    if val == 1:
        return ''
    if val == int(val):
        return str(int(val))
    # fractional
    num = int(val * 8)
    den = 8
    while num % 2 == 0 and den % 2 == 0:
        num //= 2; den //= 2
    if den == 1:
        return str(num) if num != 1 else ''
    return f'{num}/{den}' if num != 1 else f'/{den}'

# ─── XML Helpers ─────────────────────────────────────────────────────────────

def txt(el, path, default=None):
    n = el.find(path)
    return n.text.strip() if n is not None and n.text else default

def attr(el, path, key, default=None):
    n = el.find(path)
    return n.get(key, default) if n is not None else default

# ─── Main Converter ──────────────────────────────────────────────────────────

def convert(xml_path, title_override=None, composer_override=None):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Strip namespace if present
    ns = ''
    m = re.match(r'\{(.+)\}', root.tag)
    if m:
        ns = m.group(0)
        for el in root.iter():
            el.tag = el.tag.replace(ns, '')

    # ── Metadata ──
    title = title_override or txt(root, './/work-title') or txt(root, './/movement-title') or 'Untitled'
    composer = composer_override or txt(root, './/creator[@type="composer"]') or ''

    # ── Part list ──
    parts_meta = {}
    for sp in root.findall('.//score-part'):
        pid = sp.get('id')
        name = txt(sp, 'part-name', 'Part')
        abbr = txt(sp, 'part-abbreviation', name[:4]+'.')
        midi_ch = attr(sp, './/midi-instrument/midi-channel', None)
        midi_prog = attr(sp, './/midi-instrument/midi-program', None)
        parts_meta[pid] = {'name':name,'abbrev':abbr,'clef':'treble','transpose':0}

    # ── Scan first measure for global attributes ──
    first_part = root.find('part')
    if first_part is None:
        return "% Error: no <part> found"
    first_m = first_part.find('measure')
    a = first_m.find('attributes') if first_m is not None else None

    divisions = int(txt(a, 'divisions', '1')) if a is not None else 1
    fifths = int(txt(a, './/fifths', '0')) if a is not None else 0
    mode = txt(a, './/mode', 'major') if a is not None else 'major'
    t_beats = txt(a, './/beats', '4') if a is not None else '4'
    t_type = txt(a, './/beat-type', '4') if a is not None else '4'

    tempo = '120'
    if first_m is not None:
        for d in first_m.findall('direction'):
            s = d.find('.//sound')
            if s is not None and s.get('tempo'):
                tempo = s.get('tempo'); break

    key_name = FIFTHS_KEY.get(fifths,'C') if mode != 'minor' else FIFTHS_MINOR.get(fifths,'A')+'m'

    # ── Detect clefs/transpositions per part ──
    for part_el in root.findall('part'):
        pid = part_el.get('id')
        if pid not in parts_meta:
            continue
        m1 = part_el.find('measure')
        aa = m1.find('attributes') if m1 is not None else None
        if aa is not None:
            clef = aa.find('.//clef')
            if clef is not None:
                s = txt(clef,'sign','G'); l = txt(clef,'line',None)
                parts_meta[pid]['clef'] = CLEF_MAP.get((s,l),'treble')
            tr = aa.find('.//transpose')
            if tr is not None:
                parts_meta[pid]['transpose'] = int(txt(tr,'chromatic','0'))

    # ── Build header ──
    pids = list(parts_meta.keys())
    out = []
    out.append('X:1')
    out.append(f'T:{title}')
    if composer:
        out.append(f'C:{composer}')
    out.append(f'M:{t_beats}/{t_type}')
    out.append('L:1/8')
    out.append(f'Q:1/4={int(float(tempo))}')
    score_str = ' | '.join(str(i+1) for i in range(len(pids)))
    out.append(f'%%score [{score_str}]')
    out.append(f'K:{key_name}')
    out.append('%')

    for i, pid in enumerate(pids):
        info = parts_meta[pid]
        v = f'V:{i+1} clef={info["clef"]}'
        if info['transpose'] != 0:
            v += f' transpose={info["transpose"]}'
        v += f' nm="{info["name"]}" snm="{info["abbrev"]}"'
        out.append(v)
    out.append('%')

    # ── Convert each part ──
    for pidx, pid in enumerate(pids):
        vnum = pidx + 1
        part_el = root.find(f".//part[@id='{pid}']")
        if part_el is None:
            continue
        measures = part_el.findall('measure')
        out.append(f'V:{vnum}')
        measure_lines = []

        for midx, meas in enumerate(measures):
            bar = []
            pending_dyn = ''

            # Check for mid-score attribute changes
            ma = meas.find('attributes')
            if ma is not None and midx > 0:
                new_fifths = txt(ma,'.//fifths')
                new_mode = txt(ma,'.//mode','major')
                if new_fifths is not None:
                    nf = int(new_fifths)
                    nk = FIFTHS_KEY.get(nf,'C') if new_mode!='minor' else FIFTHS_MINOR.get(nf,'A')+'m'
                    bar.append(f'[K:{nk}]')
                new_beats = txt(ma,'.//beats')
                new_bt = txt(ma,'.//beat-type')
                if new_beats and new_bt:
                    bar.append(f'[M:{new_beats}/{new_bt}]')

            for elem in meas:
                tag = elem.tag

                if tag == 'direction':
                    # Dynamics
                    dyn_el = elem.find('.//dynamics')
                    if dyn_el is not None:
                        for d in dyn_el:
                            if d.tag in DYN_TAGS:
                                pending_dyn = f'!{d.tag}!'
                    # Wedges (hairpins)
                    wedge = elem.find('.//wedge')
                    if wedge is not None:
                        wt = wedge.get('type','')
                        if wt == 'crescendo':
                            bar.append('!crescendo(!')
                        elif wt == 'diminuendo':
                            bar.append('!diminuendo(!')
                        elif wt == 'stop':
                            bar.append('!crescendo)!')
                    # Words / text
                    words = elem.find('.//words')
                    if words is not None and words.text:
                        t = words.text.strip()
                        if t:
                            placement = elem.get('placement','above')
                            prefix = '^' if placement == 'above' else '_'
                            bar.append(f'"{prefix}{t}"')
                    # Rehearsal
                    reh = elem.find('.//rehearsal')
                    if reh is not None and reh.text:
                        bar.append(f'"^[{reh.text.strip()}]"')
                    # Tempo changes mid-score
                    snd = elem.find('.//sound')
                    if snd is not None and snd.get('tempo') and midx > 0:
                        bar.append(f'[Q:1/4={int(float(snd.get("tempo")))}]')
                    # Segno / Coda
                    if elem.find('.//segno') is not None:
                        bar.append('!segno!')
                    if elem.find('.//coda') is not None:
                        bar.append('!coda!')

                elif tag == 'note':
                    rest = elem.find('rest')
                    chord_tag = elem.find('chord')
                    pitch = elem.find('pitch')
                    unpitched = elem.find('unpitched')
                    grace = elem.find('grace')
                    dur_type_el = elem.find('type')
                    dot_count = len(elem.findall('dot'))
                    tie = elem.find('tie')

                    dur_type = dur_type_el.text if dur_type_el is not None else 'quarter'

                    # Articulations
                    art_str = ''
                    notations = elem.find('notations')
                    if notations is not None:
                        arts = notations.find('articulations')
                        if arts is not None:
                            for a in arts:
                                mapped = ARTICULATION_MAP.get(a.tag)
                                if mapped:
                                    art_str += f'!{mapped}!'
                        # Ornaments
                        orns = notations.find('ornaments')
                        if orns is not None:
                            for o in orns:
                                mapped = ORNAMENT_MAP.get(o.tag)
                                if mapped:
                                    art_str += f'!{mapped}!'
                        # Fermata
                        if notations.find('fermata') is not None:
                            art_str += '!fermata!'
                        # Technical
                        tech = notations.find('technical')
                        if tech is not None:
                            if tech.find('up-bow') is not None:
                                art_str += '!upbow!'
                            if tech.find('down-bow') is not None:
                                art_str += '!downbow!'
                            if tech.find('snap-pizzicato') is not None:
                                art_str += '!snap!'
                        # Slurs
                        for sl in notations.findall('slur'):
                            if sl.get('type') == 'start':
                                bar.append('(')
                            # stop handled after note

                    # Grace notes
                    if grace is not None:
                        if pitch is not None:
                            s = txt(pitch,'step','C')
                            o = txt(pitch,'octave','4')
                            al = txt(pitch,'alter','0')
                            n = pitch_to_abc(s,o,al)
                            slash = grace.get('slash','no')
                            if slash == 'yes':
                                bar.append(f'{{/{n}}}')
                            else:
                                bar.append(f'{{{n}}}')
                        continue

                    abc_dur = dur_to_abc(dur_type, dot_count)

                    if rest is not None:
                        # Measure rest check
                        if rest.get('measure') == 'yes':
                            note_str = 'Z'
                        else:
                            note_str = f'z{abc_dur}'
                        if pending_dyn:
                            note_str = pending_dyn + note_str
                            pending_dyn = ''
                        if art_str:
                            note_str = art_str + note_str
                        bar.append(note_str)

                    elif pitch is not None:
                        s = txt(pitch,'step','C')
                        o = txt(pitch,'octave','4')
                        al = txt(pitch,'alter','0')
                        note_str = pitch_to_abc(s,o,al) + abc_dur

                        if tie is not None and tie.get('type') == 'start':
                            note_str += '-'

                        # Chord stacking
                        if chord_tag is not None and bar:
                            prev = bar[-1]
                            if prev.startswith('['):
                                bar[-1] = prev[:-1] + note_str + ']'
                            else:
                                bar[-1] = f'[{prev}{note_str}]'
                            # Handle slur stop
                            if notations is not None:
                                for sl in notations.findall('slur'):
                                    if sl.get('type') == 'stop':
                                        bar.append(')')
                            continue

                        prefixes = ''
                        if pending_dyn:
                            prefixes += pending_dyn
                            pending_dyn = ''
                        if art_str:
                            prefixes += art_str
                        note_str = prefixes + note_str
                        bar.append(note_str)

                    elif unpitched is not None:
                        # Percussion
                        ds = txt(unpitched,'display-step','C')
                        do = txt(unpitched,'display-octave','4')
                        note_str = pitch_to_abc(ds,do,0) + abc_dur
                        if chord_tag is not None and bar:
                            prev = bar[-1]
                            if prev.startswith('['):
                                bar[-1] = prev[:-1] + note_str + ']'
                            else:
                                bar[-1] = f'[{prev}{note_str}]'
                            continue
                        if pending_dyn:
                            note_str = pending_dyn + note_str
                            pending_dyn = ''
                        bar.append(note_str)

                    # Slur stop
                    if notations is not None:
                        for sl in notations.findall('slur'):
                            if sl.get('type') == 'stop':
                                bar.append(')')

                elif tag == 'harmony':
                    root_el = elem.find('root')
                    if root_el is not None:
                        rs = txt(root_el,'root-step','')
                        ra = txt(root_el,'root-alter')
                        cr = rs
                        if ra:
                            a = int(float(ra))
                            if a == 1: cr += '#'
                            elif a == -1: cr += 'b'
                            elif a == 2: cr += '##'
                            elif a == -2: cr += 'bb'
                        kind = txt(elem,'kind','')
                        suffix = KIND_MAP.get(kind, kind or '')
                        # Bass note
                        bass_el = elem.find('bass')
                        bass_str = ''
                        if bass_el is not None:
                            bs = txt(bass_el,'bass-step','')
                            ba = txt(bass_el,'bass-alter')
                            bass_str = '/' + bs
                            if ba:
                                ab = int(float(ba))
                                if ab == 1: bass_str += '#'
                                elif ab == -1: bass_str += 'b'
                        bar.append(f'"{cr}{suffix}{bass_str}"')

                elif tag == 'barline':
                    style = txt(elem,'bar-style','')
                    repeat = elem.find('repeat')
                    ending = elem.find('ending')
                    if repeat is not None:
                        d = repeat.get('direction','')
                        if d == 'forward':
                            bar.insert(0, '|:')
                        elif d == 'backward':
                            bar.append(':|')
                    elif style == 'light-heavy':
                        bar.append('|]')
                    elif style == 'light-light':
                        bar.append('||')
                    if ending is not None:
                        num = ending.get('number','1')
                        typ = ending.get('type','start')
                        if typ == 'start':
                            bar.append(f'[{num}')

            bar_str = ' '.join(bar)
            if not any(bar_str.endswith(x) for x in ['|]',':|','||']):
                bar_str += ' |'

            if (midx + 1) % 4 == 0:
                bar_str += f' %{midx+1}'

            measure_lines.append(bar_str)

        # Group 4 bars per line
        for i in range(0, len(measure_lines), 4):
            chunk = measure_lines[i:i+4]
            out.append(' '.join(chunk))
        out.append('%')

    return '\n'.join(out)

# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description='MusicXML → ABC+ Converter')
    p.add_argument('input', help='MusicXML file (.musicxml, .xml, .mxl)')
    p.add_argument('-o','--output', help='Output ABC+ file (default: stdout)')
    p.add_argument('-t','--title', help='Override title')
    p.add_argument('-c','--composer', help='Override composer')
    args = p.parse_args()

    if not os.path.exists(args.input):
        print(f'Error: {args.input} not found', file=sys.stderr)
        sys.exit(1)

    result = convert(args.input, args.title, args.composer)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f'✅ Written: {args.output}', file=sys.stderr)
    else:
        print(result)

if __name__ == '__main__':
    main()
