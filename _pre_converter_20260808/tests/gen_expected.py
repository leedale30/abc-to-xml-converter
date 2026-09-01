#!/usr/bin/env python3
"""Regenerate tests/expected.json for the abc2xml conformance suite.

For every probe under tests/probes/<domain>/*.abc:
  - If the probe is listed in OVERRIDES below (a broken/missing feature), the
    override entry is written verbatim: it carries "xfail": "<bug-id>" and
    describes the DESIRED MusicXML output, which is expected to FAIL until the
    bug is fixed.
  - Otherwise the probe is converted NOW and a baseline snapshot of element
    counts is recorded (all tags except BLOCKLIST noise), plus a guard
    "other-articulation": 0 (the D31/D95 phantom-decoration detector).

After a FIX lands: remove the probe's OVERRIDES entry (or drop its "xfail")
and re-run this script -- the now-correct output becomes the guarded baseline.

Run:  python3 tests/gen_expected.py
"""

import json
import sys
import tempfile
from pathlib import Path

TESTS = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS))
from run_conformance import convert, load_root, discover_probes, EXPECTED  # noqa: E402

# Layout/metadata noise, plus tags polluted by known global bugs
# (CONF-structure-repeats-1 stamps <print><measure-numbering> into every
# measure of every conversion -- keep those out of working baselines so the
# fix does not mass-break the suite).
BLOCKLIST = {
    "score-partwise", "work", "work-title", "movement-title", "identification",
    "creator", "rights", "encoding", "software", "encoding-date", "supports",
    "defaults", "scaling", "millimeters", "tenths", "page-layout", "page-height",
    "page-width", "page-margins", "left-margin", "right-margin", "top-margin",
    "bottom-margin", "system-layout", "system-margins", "top-system-distance",
    "staff-layout", "staff-distance", "credit", "credit-words", "credit-type",
    "print", "measure-numbering", "miscellaneous", "miscellaneous-field",
}

# Keys deliberately dropped from specific working baselines because a planned
# fix will legitimately change them (feature has its own xfail probe instead).
EXCLUDE_KEYS = {
    # CONF-mechanics-3 (lyric elision) will add <elision> + an extra <text>
    # child; the elision feature is guarded by mechanics/lyrics_elision.abc.
    "mechanics/lyrics_multiverse.abc": {"text", "elision"},
}

# Extra hand-written assertions merged into auto baselines of WORKING probes.
EXTRA_KEYS = {
    "structure-repeats/barnumbers_header.abc": {"measure-numbering[text()='yes']": 4},
    "abcplus-extensions/p19_measurenumbering.abc": {"measure-numbering[text()='yes']": 4},
    "abcplus-extensions/p21_barnumbers.abc": {"measure-numbering[text()='yes']": 4},
    # grace/slash regression guards on the working halves of mixed probes
    "graces-arpeggios/p01_acciaccatura.abc": {"grace[@slash='yes']": 3},
    "lines/probe_octave_8va.abc": {"octave-shift[@type='down'][@size='8']": 1, "octave-shift[@type='stop']": 1},
    "lines/probe_octave_8vb.abc": {"octave-shift[@type='up'][@size='8']": 1, "octave-shift[@type='stop']": 1},
}

# ---------------------------------------------------------------------------
# DESIRED-behaviour entries for broken/missing features (all must FAIL today).
# ---------------------------------------------------------------------------
OVERRIDES = {
    # ---- lines ----
    "lines/probe_glissando_d31.abc": {
        "xfail": "CONF-lines-1",
        "note": "D31: bare !glissando! sprays <other-articulation> onto every later note and is never cleared",
        "counts": {"other-articulation": 0},
    },
    "lines/probe_wedge_niente.abc": {
        "xfail": "CONF-lines-2",
        "note": "no syntax reaches <wedge niente='yes'>; guessed tokens trigger the D31-class phantom spray",
        "counts": {"wedge[@niente='yes']": {"min": 1}, "other-articulation": 0},
    },
    "lines/probe_dashes_span.abc": {
        "xfail": "CONF-lines-3",
        "note": "no syntax reaches direction-type <dashes>",
        "counts": {"dashes": 2, "other-articulation": 0},
    },
    "lines/probe_bracket_span.abc": {
        "xfail": "CONF-lines-4",
        "note": "no syntax reaches direction-type <bracket>",
        "counts": {"bracket": 2, "other-articulation": 0},
    },
    # ---- ornaments ----
    "ornaments/p15_tilde_roll_d95.abc": {
        "xfail": "CONF-ornaments-1",
        "note": "D95: ~ (roll) emits phantom <other-articulation> per note forever; should be a real ornament element",
        "counts": {"other-articulation": 0, "ornaments": {"min": 1}},
    },
    "ornaments/p10_trem_single_4beam_slash.abc": {
        "xfail": "CONF-ornaments-3",
        "note": "!////! (4-beam single tremolo) unmapped; MusicXML allows tremolo marks 0-8",
        "counts": {"tremolo[@type='single']": 1, "other-articulation": 0},
    },
    "ornaments/p11_trem_single_trem4.abc": {
        "xfail": "CONF-ornaments-3",
        "note": "!trem4! unmapped",
        "counts": {"tremolo[@type='single']": 1, "other-articulation": 0},
    },
    # ---- articulations-breaths ----
    "articulations-breaths/probe_fermata_shapes.abc": {
        "xfail": "CONF-articulations-breaths-1",
        "note": "short/long fermata emit invalid shape= attribute; shape belongs in element text (angled/square)",
        "counts": {
            "fermata[text()='angled']": 1,
            "fermata[text()='square']": 1,
            "fermata[@shape='long']": 0,
            "fermata[@shape='short']": 0,
        },
    },
    "articulations-breaths/probe_fermata_inverted.abc": {
        "xfail": "CONF-articulations-breaths-2",
        "note": "!invertedfermata! unhandled -> phantom spray; should be <fermata type='inverted'>",
        "counts": {"fermata[@type='inverted']": 1, "other-articulation": 0},
    },
    "articulations-breaths/probe_breath_symbols.abc": {
        "xfail": "CONF-articulations-breaths-3",
        "note": "!breath(X)! symbol silently dropped; artMap path never extracts parenthesised content",
        "counts": {
            "breath-mark[text()='comma']": 1,
            "breath-mark[text()='tick']": 1,
            "breath-mark[text()='upbow']": 1,
            "breath-mark[text()='salzedo']": 1,
        },
    },
    # ---- graces-arpeggios ----
    "graces-arpeggios/p09_slash_run.abc": {
        "xfail": "CONF-graces-arpeggios-1",
        "note": "{/de} slashes only the first grace of the run; every note of a slashed run should carry slash='yes'",
        "counts": {"grace": 2, "grace[@slash='yes']": 2},
    },
    "graces-arpeggios/p07_arpeggio_direction.abc": {
        "xfail": "CONF-graces-arpeggios-2",
        "note": "no syntax for <arpeggiate direction='up|down'>; guessed tokens trigger phantom spray",
        "counts": {
            "arpeggiate[@direction='up']": 1,
            "arpeggiate[@direction='down']": 1,
            "other-articulation": 0,
        },
    },
    "graces-arpeggios/p08_non_arpeggiate.abc": {
        "xfail": "CONF-graces-arpeggios-3",
        "note": "no syntax for <non-arpeggiate>; bracket needs type=bottom on lowest and type=top on highest chord note",
        "counts": {
            "non-arpeggiate[@type='top']": 1,
            "non-arpeggiate[@type='bottom']": 1,
            "other-articulation": 0,
        },
    },
    "graces-arpeggios/p05_grace_after.abc": {
        "xfail": "CONF-graces-arpeggios-4",
        "note": "no grace-after syntax; trailing {d} should become <grace steal-time-previous> after the principal note",
        "counts": {"grace[@steal-time-previous]": {"min": 1}},
    },
    # ---- dynamics-directions-tempo ----
    "dynamics-directions-tempo/p07_metric_modulation.abc": {
        "xfail": "CONF-dynamics-directions-tempo-1",
        "note": "Q:1/4=3/8 mis-parsed as per-minute=3 (sound tempo 3.00!); should emit beat-unit = beat-unit metric modulation",
        "counts": {"beat-unit": 2, "per-minute": 0},
    },
    "dynamics-directions-tempo/p12_sound_directives.abc": {
        "xfail": "CONF-structure-repeats-3",
        "note": "[I:segno]-family sound directions have zero <direction-type> children -- schema-invalid MusicXML",
        "counts": {"sound": {"min": 5}, "direction-type": {"min": 5}},
    },
    # ---- structure-repeats ----
    "structure-repeats/barnumbers.abc": {
        "xfail": "CONF-structure-repeats-1",
        "note": "body-placed %%barnumbers takes effect one measure late (measure 1 emits 'none')",
        "counts": {
            "measure-numbering[text()='yes']": 4,
            "measure-numbering[text()='none']": 0,
        },
    },
    "abcplus-extensions/p20_measurenumbering_default.abc": {
        "xfail": "CONF-structure-repeats-1",
        "note": "with NO directive every measure still emits <measure-numbering>none</> (s.measureNumbering init to truthy 'no') -- hides bar numbers on every converted score",
        "counts": {"measure-numbering": 0},
    },
    "structure-repeats/anacrusis.abc": {
        "xfail": "CONF-structure-repeats-2",
        "note": "pickup bar not marked implicit='yes' -- every bar number off by one",
        "counts": {"measure[@implicit='yes']": 1},
    },
    "structure-repeats/dcds_directives.abc": {
        "xfail": "CONF-structure-repeats-3",
        "note": "%%segno/%%dacapo-family emit <direction> with no <direction-type> child -- schema-invalid",
        "counts": {"sound": {"min": 5}, "direction-type": {"min": 5}},
    },
    "structure-repeats/voltas_extra.abc": {
        "xfail": "CONF-structure-repeats-4",
        "note": "quoted volta text mangled: '-' replaced by ',' before the quoted-string check",
        "counts": {
            "ending[text()='4.-5.']": 1,
            "ending[@number='1,3']": {"min": 1},
            "repeat": {"min": 3},
        },
    },
    # ---- pitch-staff ----
    "pitch-staff/12_key_aeolian_ionian.abc": {
        "xfail": "CONF-pitch-staff-1",
        "note": "aeolian/ionian silently fall back to major (Aaeolian -> fifths=3!)",
        "counts": {
            "mode[text()='aeolian']": 1,
            "mode[text()='ionian']": 1,
            "fifths[text()='0']": 2,
        },
    },
    "pitch-staff/14_key_custom.abc": {
        "xfail": "CONF-pitch-staff-2",
        "note": "custom key sig emits malformed <key-octave number='5'/> (octave in number attr, empty text)",
        "counts": {"key-step": 2, "key-alter": 2, "key-octave[@number='5']": 0},
    },
    "pitch-staff/15_key_exp.abc": {
        "xfail": "CONF-pitch-staff-3",
        "note": "K:D exp: 'exp' ignored, D-major signature leaks through (4 key-steps instead of the 2 listed)",
        "counts": {"key-step": 2},
    },
    "pitch-staff/16_time_common_cut.abc": {
        "xfail": "CONF-pitch-staff-4",
        "note": "M:C / M:C| lose the symbol attribute (common/cut glyph)",
        "counts": {"time[@symbol='common']": 1, "time[@symbol='cut']": 1},
    },
    "pitch-staff/27_double_sharp.abc": {
        "xfail": "CONF-pitch-staff-5",
        "note": "^^ emits <accidental>sharp-sharp</> (two vertical sharps) instead of canonical double-sharp (x glyph)",
        "counts": {
            "accidental[text()='double-sharp']": 1,
            "accidental[text()='sharp-sharp']": 0,
        },
    },
    "pitch-staff/22_notehead_pitched.abc": {
        "xfail": "CONF-pitch-staff-6",
        "note": "no notehead syntax for pitched notes; guessed decorations trigger phantom spray",
        "counts": {"notehead": 3, "other-articulation": 0},
    },
    "pitch-staff/21_acc_microtone.abc": {
        "xfail": "CONF-pitch-staff-7",
        "note": "ABC 2.1 fractional accidentals rejected; microtone intent silently discarded",
        "counts": {"accidental": {"min": 3}},
    },
    "pitch-staff/03_clef_soprano_alto1.abc": {
        "xfail": "CONF-pitch-staff-8",
        "note": "standard clef names soprano/mezzosoprano unrecognised (house alto1/alto2 only)",
        "counts": {"clef": 2, "sign[text()='C']": 2},
    },
    "pitch-staff/09_clef_none.abc": {
        "xfail": "CONF-pitch-staff-9",
        "note": "clef=none accepted but emits nothing; MusicXML <sign>none</sign> unreachable",
        "counts": {"sign[text()='none']": 1},
    },
    # ---- mechanics ----
    "mechanics/tuplet_nested.abc": {
        "xfail": "CONF-mechanics-1",
        "note": "nested tuplet silently clobbers outer state and corrupts the measure (bar sums 440/480, no warning)",
        "counts": {"tuplet": 4, "time-modification": {"min": 4}},
    },
    "mechanics/beam_directive.abc": {
        "xfail": "CONF-mechanics-2",
        "note": "%%beam begin/end is an unreachable stub; beam control is only via note spacing",
        "counts": {"beam[text()='begin']": 3, "beam[text()='end']": 3},
    },
    "mechanics/lyrics_elision.abc": {
        "xfail": "CONF-mechanics-3",
        "note": "lyric elision ~ flattened to a space in one <text>; MusicXML <elision> unreachable",
        "counts": {"elision": 1, "lyric": 4},
    },
    # ---- abcplus-extensions ----
    "abcplus-extensions/p22_swing_mute.abc": {
        "xfail": "CONF-abcplus-extensions-1",
        "note": "%%mute captured by deco map 'mute'->stopped (brass hand-stop) instead of <sound mute='yes'>",
        "counts": {"sound[@swing='yes']": 1, "sound[@mute='yes']": {"min": 1}, "stopped": 0},
    },
    "abcplus-extensions/p22b_mute_only.abc": {
        "xfail": "CONF-abcplus-extensions-1",
        "note": "%%mute -> <technical><stopped> on the next note; documented <sound mute='yes'> never emitted",
        "counts": {"sound[@mute='yes']": {"min": 1}, "stopped": 0},
    },
    "abcplus-extensions/p08_midi_bank_forms.abc": {
        "xfail": "CONF-abcplus-extensions-2",
        "note": "%%midi-bank/vol/pan silently dropped in tune header (splitHeaderVoices only moves 'I:MIDI'); %%MIDI bank N has no regex at all",
        "counts": {"midi-bank": 2, "volume": {"min": 1}, "pan": {"min": 1}},
    },
    "abcplus-extensions/p17b_score_allbad.abc": {
        "xfail": "CONF-abcplus-extensions-3",
        "note": "%%score naming only nonexistent voices emits a <part> with no matching <score-part> -- schema-invalid",
        "counts": {"score-part": {"min": 1}},
    },
    "abcplus-extensions/p18_measurenb.abc": {
        "xfail": "CONF-abcplus-extensions-4",
        "note": "%%measurenb N renumbers one measure late and does not continue (1,2,3,25,5,6)",
        "counts": {"measure[@number='25']": 1, "measure[@number='26']": 1, "measure[@number='3']": 0},
    },
    "abcplus-extensions/p18b_measurenb_cont.abc": {
        "xfail": "CONF-abcplus-extensions-4",
        "note": "numbering falls back to the internal index right after the renumbered measure",
        "counts": {"measure[@number='27']": 1, "measure[@number='5']": 0},
    },
}


def main():
    probes = discover_probes()
    entries = {}
    with tempfile.TemporaryDirectory(prefix="abc2xml_gen_") as tmp:
        for probe in probes:
            rel = "%s/%s" % (probe.parent.name, probe.name)
            if rel in OVERRIDES:
                entries[rel] = OVERRIDES[rel]
                continue
            xml_path = convert(probe, tmp)
            root = load_root(xml_path)
            counts = {}
            for el in root.iter():
                tag = el.tag
                if tag in BLOCKLIST:
                    continue
                counts[tag] = counts.get(tag, 0) + 1
            for key in EXCLUDE_KEYS.get(rel, ()):  # keys a planned fix will change
                counts.pop(key, None)
            counts.setdefault("other-articulation", 0)  # phantom-deco guard
            counts.update(EXTRA_KEYS.get(rel, {}))
            entries[rel] = {"counts": dict(sorted(counts.items()))}
    unused = set(OVERRIDES) - {("%s/%s" % (p.parent.name, p.name)) for p in probes}
    if unused:
        print("WARNING: OVERRIDES entries with no probe file: %s" % sorted(unused))
    doc = {
        "_about": "Expectations for tests/run_conformance.py. Regenerate baselines with tests/gen_expected.py. "
                  "Entries with 'xfail' describe DESIRED behaviour of known bugs (see tests/README.md) and are expected to fail.",
        "probes": {k: entries[k] for k in sorted(entries)},
    }
    EXPECTED.write_text(json.dumps(doc, indent=1) + "\n")
    n_x = sum(1 for e in entries.values() if "xfail" in e)
    print("wrote %s: %d probes (%d baseline, %d xfail)" % (EXPECTED, len(entries), len(entries) - n_x, n_x))


if __name__ == "__main__":
    main()
