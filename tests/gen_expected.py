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

!! DO NOT RUN THIS SCRIPT BLIND -- MEASURED 2026-08-08 !!
OVERRIDES still carries entries for ELEVEN bug ids that are already FIXED, and an
entry always wins over the live conversion.  Running this script as it stands takes
the suite from 19 xfail to 31 and silently re-marks these twelve PASSING probes as
known-broken:

    CONF-lines-1                lines/probe_glissando_d31.abc
    CONF-ornaments-1            ornaments/p15_tilde_roll_d95.abc
    CONF-articulations-breaths-1  articulations-breaths/probe_fermata_shapes.abc
    CONF-articulations-breaths-2  articulations-breaths/probe_fermata_inverted.abc
    CONF-structure-repeats-1    structure-repeats/barnumbers.abc
                                abcplus-extensions/p20_measurenumbering_default.abc
    CONF-structure-repeats-2    structure-repeats/anacrusis.abc
    CONF-structure-repeats-3    dynamics-directions-tempo/p12_sound_directives.abc
    CONF-pitch-staff-1..4       pitch-staff/{12_key_aeolian_ionian,14_key_custom,
                                15_key_exp,16_time_common_cut}.abc

The suite still exits 0 afterwards (xfail does not fail the build), so the loss is
SILENT.  This trap was hit and reverted once before (see FIXLOG.md, CONF-ornaments-2)
and again on 2026-08-08.  Clear the stale OVERRIDES entries first, or diff the
regenerated expected.json against the previous one and confirm no probe gained an
"xfail".  Attribute- and text-level guards survive regeneration only if they are
listed in EXTRA_KEYS below -- a plain tag census cannot see them.

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
    # 'yes' is not in the MusicXML measure-numbering enum (none|measure|system) — Dorico
    # refused every converted file. Fixed 2026-08-29: 'yes'-style inputs map to 'system'
    # (what MuseScore's lenient importer had been rendering anyway). The ='yes' zero-guards
    # keep a regeneration from ever re-blessing the invalid value.
    "structure-repeats/barnumbers_header.abc": {"measure-numbering[text()='system']": 4, "measure-numbering[text()='yes']": 0},
    "abcplus-extensions/p19_measurenumbering.abc": {"measure-numbering[text()='system']": 4, "measure-numbering[text()='yes']": 0},
    "abcplus-extensions/p21_barnumbers.abc": {"measure-numbering[text()='system']": 4, "measure-numbering[text()='yes']": 0},
    # grace/slash regression guards on the working halves of mixed probes
    "graces-arpeggios/p01_acciaccatura.abc": {"grace[@slash='yes']": 3},
    "lines/probe_octave_8va.abc": {"octave-shift[@type='down'][@size='8']": 1, "octave-shift[@type='stop']": 1},
    "lines/probe_octave_8vb.abc": {"octave-shift[@type='up'][@size='8']": 1, "octave-shift[@type='stop']": 1},
    # ---- ANTONY_DECISIONS item 16, fixed 2026-08-08 (see FIXLOG.md) ----
    # A plain tag census cannot see any of these; without them a regeneration would
    # quietly UNGUARD all six fixes while still reporting a green suite.
    "structure-repeats/voltas_extra.abc": {         # volta-33 sentinel
        "ending[text()='4.-5.']": 1, "ending[@number='1,3']": {"min": 1},
        "ending[@number='33']": 0, "ending[@number='']": 2,
        "ending[@type='start']": 3, "ending[@type='stop']": 3,
    },
    "structure-repeats/dcds_directives.abc": {      # %%tocoda target attribute
        "sound[@tocoda='TheCoda']": 1, "sound[@coda]": 0,
        "sound[@segno='TheSegno']": 1, "sound[@dalsegno='TheSegno']": 1,
        "sound[@dacapo='yes']": 1, "sound[@fine='yes']": 1,
    },
    "dynamics-directions-tempo/p07_metric_modulation.abc": {
        "beat-unit": 2, "per-minute": 0, "beat-unit-dot": 1, "metronome": 1,
        "sound[@tempo='180.00']": 1, "sound[@tempo='3.00']": 0,
    },
    "dynamics-directions-tempo/p07b_metric_modulation_after_tempo.abc": {
        "beat-unit": 3, "per-minute": 1,
        "sound[@tempo='90.00']": 1, "sound[@tempo='60.00']": 1,
    },
    "abcplus-extensions/p22_swing_mute.abc":  {"sound[@swing='yes']": 1, "sound[@mute='yes']": 1, "stopped": 0},
    "abcplus-extensions/p22b_mute_only.abc":  {"sound[@mute='yes']": 1, "stopped": 0},
    "abcplus-extensions/p22c_handstop_vs_mute.abc": {
        "sound[@mute='yes']": 1, "sound[@mute='no']": 1, "stopped": 1,
    },
    "ornaments/p10_trem_single_4beam_slash.abc": {"tremolo[@type='single']": 1, "tremolo[text()='4']": 1, "ornaments/tremolo": 1},
    "ornaments/p11_trem_single_trem4.abc":      {"tremolo[@type='single']": 1, "tremolo[text()='4']": 1, "ornaments/tremolo": 1},
    "ornaments/p12_trem_single_range.abc": dict(
        [("tremolo[@type='single']", 8), ("tremolo[@type='start']", 1), ("tremolo[@type='stop']", 1)] +
        [("tremolo[text()='%d']" % i, 3 if i == 4 else 1) for i in range(1, 9)]),
    "abcplus-extensions/p08_midi_bank_forms.abc": {
        "midi-bank": 2, "midi-bank[text()='2']": 1, "midi-bank[text()='3']": 1,
        "volume": 1, "pan": 1, "midi-program": 2,
    },
    # ---- guards migrated 2026-08-29 from OVERRIDES entries whose bugs were found fixed ----
    # (12 stale xfail rows were re-listed by a regeneration and reported XPASS; an XPASS
    # cannot exit 1, so leaving them would UNGUARD the fixes. Attr/text keys and the
    # blocklisted measure-numbering tag are invisible to the auto census, hence hand-held.)
    "articulations-breaths/probe_fermata_shapes.abc": {   # was CONF-articulations-breaths-1
        "fermata[text()='angled']": 1, "fermata[text()='square']": 1,
        "fermata[@shape='long']": 0, "fermata[@shape='short']": 0,
    },
    "articulations-breaths/probe_fermata_inverted.abc": { # was CONF-articulations-breaths-2
        "fermata[@type='inverted']": 1,
    },
    "structure-repeats/barnumbers.abc": {                 # was CONF-structure-repeats-1 (body-placed)
        "measure-numbering[text()='system']": 4,
        "measure-numbering[text()='none']": 0,
        "measure-numbering[text()='yes']": 0,
    },
    "abcplus-extensions/p20_measurenumbering_default.abc": { # was CONF-structure-repeats-1 (no directive)
        "measure-numbering": 0,
    },
    "structure-repeats/anacrusis.abc": {                  # was CONF-structure-repeats-2
        "measure[@implicit='yes']": 1,
    },
    "pitch-staff/12_key_aeolian_ionian.abc": {            # was CONF-pitch-staff-1
        "mode[text()='aeolian']": 1, "mode[text()='ionian']": 1, "fifths[text()='0']": 2,
    },
    "pitch-staff/14_key_custom.abc": {                    # was CONF-pitch-staff-2
        "key-octave[@number='5']": 0,
    },
    "pitch-staff/16_time_common_cut.abc": {               # was CONF-pitch-staff-4
        "time[@symbol='common']": 1, "time[@symbol='cut']": 1,
    },
}

# ---------------------------------------------------------------------------
# DESIRED-behaviour entries for broken/missing features (all must FAIL today).
# ---------------------------------------------------------------------------
OVERRIDES = {
    # ---- lines ----
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
    # ---- articulations-breaths ----
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
    # ---- pitch-staff ----
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
