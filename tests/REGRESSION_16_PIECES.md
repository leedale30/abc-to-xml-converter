# Regression: 16 AOS_COMPOSER_TEST pieces vs patched abc2xml

Date: 2026-08-06
Converter under test: `COMPOSER/abc-to-xml-converter/abc2xml/abc2xml.py` (post-conformance patches; stock backup = `abc2xml.py.pre-conformance-2026-08-06`)
Method: each `<piece>.abc` converted with the patched converter into scratch
(`…/scratchpad/regress16/`, delivered files untouched), then compared against the
delivered `<piece>.musicxml` with `xml.etree` (element counts, attribute-order
independent — no regex verdicts). Comparison script: `…/scratchpad/regress16/compare.py`.

## Verdict

**16/16 pieces at full musical parity. Zero red flags.**

Parity checks that must match exactly, and did, for every piece:

- part count
- measure count per part
- pitched-note count per part
- per-part pitch multiset (step + alter + octave)

## Parity table

| # | Piece | Parts | Measures/part | Total measures | Pitched notes | Parity | Element diffs |
|---|-------|------:|--------------:|---------------:|--------------:|:------:|---------------|
| 1 | AOS1 baroque `concerto_grosso_in_d` | 6 | 118 | 708 | 2208 | PASS | +instrument-sound, +print/measure-numbering |
| 2 | AOS2 classical `symphony_in_g_mvt1` | 9 | 130 | 1170 | 3824 | PASS | +instrument-sound, +print/measure-numbering |
| 3 | AOS3 romantic `nocturne_in_e_flat` | 2 | 54 | 108 | 827 | PASS | +instrument-sound, +print/measure-numbering |
| 4 | AOS4 art song `the_lamplighter` | 3 | 80 | 240 | 889 | PASS | +instrument-sound, +print/measure-numbering |
| 5 | AOS4 choirs `frost_upon_the_pane` | 4 | 62 | 248 | 416 | PASS | +instrument-sound, +print/measure-numbering, **−213 phantom other-articulation** (D31 fix, see below) |
| 6 | AOS4 musical theatre `room` | 7 | 96 | 672 | 1717 | PASS | +instrument-sound, +print/measure-numbering |
| 7 | AOS4 popular song `run_it_back` | 6 | 116 | 696 | 1843 | PASS | none (delivered 2026-08-06, already patched-converter output) |
| 8 | AOS5 EDM `ultraviolet` | 7 | 129 | 903 | 3891 | PASS | +instrument-sound, +print/measure-numbering |
| 9 | AOS5 salsa `nueve_vidas` | 10 | 180 | 1800 | 4917 | PASS | +instrument-sound, +print/measure-numbering |
| 10 | AOS5 tango `sombra_de_almagro` | 7 | 112 | 784 | 3663 | PASS | +instrument-sound, +print/measure-numbering |
| 11 | AOS6 Arab takht `dulab_hijaz` | 6 | 96 | 576 | 1527 | PASS | +instrument-sound, +print/measure-numbering |
| 12 | AOS6 Hindustani `gat_in_yaman` | 4 | 34 | 136 | 460 | PASS | +instrument-sound, +print/measure-numbering |
| 13 | AOS6 silk-and-bamboo `liuyun_baban` | 6 | 60 | 360 | 1860 | PASS | none (delivered 2026-08-06, already patched-converter output) |
| 14 | AOS7 ballet `la_fontaine_dargent` | 12 | 192 | 2304 | 4176 | PASS | +instrument-sound, +print/measure-numbering |
| 15 | AOS7 film `terra_incognita` | 16 | 96 | 1536 | 3932 | PASS | +instrument-sound, +print/measure-numbering |
| 16 | AOS7 video game `vaultbreaker` | 11 | 152 | 1672 | 5224 | PASS | +instrument-sound, +print/measure-numbering |

"Measures/part" is identical across every part within each piece (verified per part, not just in aggregate).

## Element-level differences by class (all EXPECTED)

Only three diff classes appeared across the whole corpus:

### 1. `instrument-sound` (new emission — expected improvement)
Patched converter emits one `<instrument-sound>` per score-instrument (e.g.
`strings.violin`), delivered files had none. Counts: one per instrument, 2–19 per
piece depending on ensemble size.

### 2. `print` + `measure-numbering` (new emission — expected improvement)
Patched converter emits `<print><measure-numbering>yes</measure-numbering></print>`.
Delivered (stock) files had none. Note for review: it is emitted in **every measure
of every part** (e.g. 708 = 118 measures x 6 parts in the concerto; 2304 in the
ballet), where the MusicXML idiom only needs it once at the top of each part (it
persists until changed). Harmless and MuseScore-safe, but verbose — a candidate
polish item, not a regression.

### 3. `articulations` / `other-articulation` / `notations` (frost_upon_the_pane only — phantom removal, D31-class fix confirmed)
The ABC source contains exactly one `!mc!` and one `!mA,,!` (nonstandard
decorations, lines 143 and 110). The stock converter turned these into sticky
`<other-articulation>mc</other-articulation>` (148 copies) and
`<other-articulation>mA,,</other-articulation>` (65 copies) smeared onto every
subsequent note in those voices — exactly the D31 never-cleared bug. The patched
converter emits none of them. Legitimate notations are untouched: slur (24) and
fermata (4) counts are identical in both files.

No differences appeared in ties, wedges, sound, pedal, or divisions on this corpus —
those classes were byte-count identical between stock and patched output.

## Files

- Scratch conversions + comparison script + raw JSON:
  `/private/tmp/claude-501/-Users-antonyleedale-Documents-NEWEST-WEBSITE-JUNE26/79adbeff-652a-4f42-82fa-0c417190025d/scratchpad/regress16/`
- Delivered files were read only, never modified.
