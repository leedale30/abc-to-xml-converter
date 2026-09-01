# abc2xml conformance suite

Permanent regression + fix-loop harness for `abc2xml/abc2xml.py` (ABC+ -> MusicXML 4.0),
built from the nine-domain feature census of 2026-08-06.

## Run

```bash
python3 tests/run_conformance.py              # full suite (157 probes)
python3 tests/run_conformance.py --filter lines   # one domain / one probe
python3 tests/run_conformance.py --verbose    # per-key detail for XFAILs too
```

Result classes:

| class | meaning | affects exit code |
|-------|---------|-------------------|
| PASS  | working feature, output matches baseline | no |
| FAIL  | **regression of a working feature** | **exit 1** |
| XFAIL | known bug/missing feature (entry has `"xfail": "<bug-id>"`), fails as expected | no |
| XPASS | an xfail probe now passes — the bug appears fixed | no (but act on it) |
| NOEXP | probe has no expectation entry | no |

Baseline at suite creation: **PASS 116, FAIL 0, XFAIL 41, XPASS 0** (157 probes).
The runner's failure path is proven: poisoning an expectation produces FAIL + exit 1.

## Files

- `run_conformance.py` — the runner. Converts every `tests/probes/<domain>/*.abc`,
  parses the XML with `xml.etree`, and counts elements attribute-order-independently.
  Count keys support `parent/tag`, `[@attr='v']`, `[@attr]`, `[text()='v']`; expected
  values are exact ints or `{"min":n}` / `{"max":n}`.
- `expected.json` — one entry per probe. Working probes carry a snapshot of element
  counts (layout noise and the polluted `<print>/<measure-numbering>` tags excluded)
  plus an `"other-articulation": 0` guard — the D31/D95 phantom-decoration detector.
  Bug probes carry `"xfail"` + the **desired** counts.
- `gen_expected.py` — regenerates `expected.json`. Holds the xfail OVERRIDES table.
- `probes/<domain>/` — 157 tiny self-contained probes (census-built; three added by
  the suite builder: `graces-arpeggios/p09_slash_run.abc`,
  `mechanics/lyrics_elision.abc`, `pitch-staff/27_double_sharp.abc`).
  Census artefacts (`findings.json`, `inspect_*.py`, `out*/`, `xml/`, `mscz/`) are
  not read by the runner.

## After fixing a bug

1. Run the suite: the fixed probe(s) report **XPASS**.
2. Delete the probe's entry from `OVERRIDES` in `gen_expected.py` (or drop `"xfail"`).
3. `python3 tests/gen_expected.py` — the now-correct output becomes the guarded baseline.
4. Re-run; confirm PASS and no new FAILs.

## Bug register (one line per id)

Broken (working syntax, wrong/invalid output) — fix these first:

- **CONF-lines-1 (= D31)** — bare `!glissando!` (any unknown decoration): emits `<other-articulation>` AND re-queues the token, stamping every later note forever; generic mechanism at doNotations else-branch + staffDecos re-append (`probes/lines/probe_glissando_d31.abc`).
- **CONF-ornaments-1 (= D95)** — `~` roll: phantom `<other-articulation>roll</>` per note, never a real ornament element (`ornaments/p15_tilde_roll_d95.abc`).
- **CONF-structure-repeats-1** — `s.measureNumbering` init to truthy `'no'`: EVERY measure of EVERY conversion emits `<measure-numbering>none</>`, hiding bar numbers estate-wide; body-placed `%%barnumbers` also one measure late (`structure-repeats/barnumbers.abc`, `abcplus-extensions/p20_measurenumbering_default.abc`).
- **CONF-ornaments-2** — `!trill(!/!trill)!` spans: invalid `trill-mark@type=start`, no `<wavy-line>` stop ever (`ornaments/p02_trill_span.abc`, `p03_wavy_line_direct.abc`).
- **CONF-articulations-breaths-1** — short/long fermata emit invalid `shape=` attribute; shape belongs in element text angled/square (`articulations-breaths/probe_fermata_shapes.abc`).
- **CONF-articulations-breaths-2** — `!invertedfermata!` unhandled -> D31-class spray; should be `<fermata type="inverted">` (`probe_fermata_inverted.abc`).
- **CONF-structure-repeats-2** — anacrusis not marked `implicit="yes"`: every bar number off by one (`structure-repeats/anacrusis.abc`).
- **CONF-structure-repeats-3** — `%%segno`/`[I:segno]`-family sound directions have zero `<direction-type>` children: schema-invalid MusicXML (`structure-repeats/dcds_directives.abc`, `dynamics-directions-tempo/p12_sound_directives.abc`).
- **CONF-pitch-staff-4** — `M:C` / `M:C|` lose `symbol="common|cut"` (`pitch-staff/16_time_common_cut.abc`).
- **CONF-pitch-staff-1** — `K:Aaeolian` -> fifths=3 major (sharpened pitches!); ionian also unmapped (`12_key_aeolian_ionian.abc`).
- **CONF-pitch-staff-3** — `K:D exp` ignored: full D-major signature leaks through (`15_key_exp.abc`).
- **CONF-pitch-staff-2** — custom key sig emits malformed `<key-octave number="5"/>` (`14_key_custom.abc`).
- **CONF-pitch-staff-5** — `^^` -> `sharp-sharp` instead of canonical `double-sharp` (`27_double_sharp.abc`).
- **CONF-mechanics-1** — nested tuplet silently clobbers outer tuplet and corrupts the measure, no warning (`mechanics/tuplet_nested.abc`).
- **CONF-dynamics-directions-tempo-1** — `Q:1/4=3/8` mis-parsed: per-minute=3, `<sound tempo="3.00">` (near-frozen playback, silent); should be a metric-modulation beat-unit pair (`p07_metric_modulation.abc`).
- **CONF-abcplus-extensions-1** — `%%mute` hijacked by deco map `mute->stopped` (brass hand-stop); documented `<sound mute="yes">` unreachable (`p22_swing_mute.abc`, `p22b_mute_only.abc`).
- **CONF-abcplus-extensions-2** — `%%midi-bank/vol/pan` silently dropped in tune header; `%%MIDI bank N` has no regex at all (`p08_midi_bank_forms.abc`).
- **CONF-graces-arpeggios-1** — `{/de}` slashes only the first grace of the run (`p09_slash_run.abc`).
- **CONF-structure-repeats-4** — quoted volta text mangled: `-` -> `,` before the quoted-string check (`voltas_extra.abc`).
- **CONF-abcplus-extensions-3** — `%%score` naming only nonexistent voices: `<part>` with no `<score-part>`, schema-invalid (`p17b_score_allbad.abc`).
- **CONF-abcplus-extensions-4** — `%%measurenb N` renumbers one measure late and never continues (`p18_measurenb.abc`, `p18b_measurenb_cont.abc`).

Missing (no syntax reaches the MusicXML element), ranked by musical value for the education estate:

- **CONF-graces-arpeggios-2** — `<arpeggiate direction="up|down">` (`p07_arpeggio_direction.abc`); proposal `!arpeggioup!`/`!arpeggiodown!`.
- **CONF-graces-arpeggios-3** — `<non-arpeggiate>` bracket (`p08_non_arpeggiate.abc`); proposal `!nonarpeggio!` -> type=bottom on lowest + type=top on highest chord note.
- **CONF-articulations-breaths-3** — breath-mark/caesura symbols (comma/tick/upbow/salzedo; caesura shapes): artMap path never extracts `!breath(X)!` parenthesised content (`probe_breath_symbols.abc`).
- **CONF-pitch-staff-6** — noteheads on pitched notes (x, diamond, slash, triangle, none, circle-x); proposal `!head=x!` family (`22_notehead_pitched.abc`).
- **CONF-lines-2** — niente hairpins `<wedge niente="yes">`; proposal `!dim-niente(!` / `!cresc-niente(!` (`probe_wedge_niente.abc`).
- **CONF-ornaments-3** — single-note tremolo 4+ beams (`!////!`, `!trem4!`..`trem8`) (`p10`, `p11`).
- **CONF-graces-arpeggios-4** — grace-after (`<grace steal-time-previous>`); proposal `c{<d}` (`p05_grace_after.abc`).
- **CONF-pitch-staff-7** — ABC 2.1 microtone accidentals `^/C` `_/D` `^3/2E` -> quarter-sharp family (`21_acc_microtone.abc`).
- **CONF-pitch-staff-8** — standard clef names `soprano`/`mezzosoprano` (`03_clef_soprano_alto1.abc`).
- **CONF-pitch-staff-9** — `clef=none` -> `<sign>none</sign>` (`09_clef_none.abc`).
- **CONF-lines-3** — `<dashes>` span; proposal `!dashes(!`/`!dashes)!` (`probe_dashes_span.abc`).
- **CONF-lines-4** — direction-type `<bracket>` span; proposal `!bracket(!`/`!bracket)!` (`probe_bracket_span.abc`).
- **CONF-mechanics-2** — `%%beam begin/end` is an unreachable stub (`beam_directive.abc`).
- **CONF-mechanics-3** — lyric `<elision>` (ABC `oh~my`) (`lyrics_elision.abc`).
- **CONF-structure-repeats-5** — bar-styles dashed/heavy/tick unreachable; proposal one-shot `%%barline dashed|heavy|tick` (no probe yet — add one with the chosen syntax when implementing).

Census-noted but not registered (documentation/watch items): `%%score {V1 V2}` both-named
brace silently NOT a grand staff (use `{* ...}`), frame-frets hardcoded to 4, `vel:` maps to
sound/@dynamics percent not raw MIDI velocity, secondary beam levels always `number="1"`,
linked-tab string/fret gated on undocumented `-f` flag, unknown `Q:"text"` snaps sound tempo
to 120, several working features undocumented in FEATURES.md (`!courtesy!`, `!arpeggio!`,
`vel:`, `%%harp`, `%%accordion`, `%%measurenb`).
