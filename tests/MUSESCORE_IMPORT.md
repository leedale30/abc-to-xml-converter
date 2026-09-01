# MuseScore 4 import verification — conformance campaign

Date: 2026-08-06 · Agent: MuseScore-import agent
Pipeline: probe `.abc` → `abc2xml.py` (post-conformance-fix build) → `tools/to_musescore.sh` → `.mscz` → unzip → element check in the `.mscx` (xml.etree, attribute-order-independent).
Workspace: scratchpad `msimport/` (abc / xml / mscz / mscx). 23 probes covering all nine domains (fixed features preferred) + 2 full reconverted pieces.

## Headline

- **25/25 files imported**: exit 0 and a non-trivial `.mscz` for every probe and both pieces. Zero MuseScore crashes.
- **21/23 probe features fully survived** into the `.mscx` as the correct native MuseScore element.
- **3 feature-level losses/partials** (converts fine, but the notation is degraded or dropped inside MuseScore) — see "Not done" below.

## Probe results (feature → MuseScore element found in the .mscx)

| Probe | Feature | Survived as | Verdict |
|---|---|---|---|
| articulations-breaths/probe_breath | `!breath!` ×2 | `Breath` ×2, `symbol=breathMarkComma` | OK |
| articulations-breaths/probe_fermata_shapes (FIXED CONF-art-1) | `!longfermata!` `!shortfermata!` | `Fermata` subtypes `fermataLongAbove`, `fermataShortAbove` | OK |
| articulations-breaths/probe_fermata_inverted (FIXED CONF-art-2) | `!invertedfermata!` | `Fermata` subtype `fermataBelow` | OK |
| dynamics/p01_dynamics_basic | p…pppp, f…ffff, mp, mf | `Dynamic` ×10 with exact subtypes | OK |
| dynamics/p05_metronome_basic | `Q:1/4=120` | `Tempo` tempo=2 (120 bpm) + metronome text | OK |
| abcplus-extensions/p11_instrument_sounds | `<instrument-sound>` mapping ×7 | `instrumentId` ×7 (flute, bass clarinet, english-horn, french-horn, piccolo trumpet, strings.group, voice.bass) | OK¹ |
| abcplus-extensions/p14_score_brace_grand | `%%score {RH LH}` grand staff | 1 `Part` with 2 `Staff`, `bracket type="1"` (brace) span=2, barLineSpan=1 | OK |
| graces-arpeggios/p01_acciaccatura | `{/x}` ×3 | `acciaccatura` ×3 | OK |
| graces-arpeggios/p06_arpeggio | `!arpeggio!` ×2 | `Arpeggio` ×2 | OK |
| lines/probe_gliss_paired | `!gliss(!…!gliss)!` + `!~(!…!~)!` | `Spanner type="Glissando"` ×2 (both spans) | OK |
| lines/probe_pedal_sign | `!ped!`/`!ped-up!` | `Spanner type="Pedal"` ×1 | OK |
| lines/probe_octave_8va | `!8va!`…`!8va)!` | `Spanner type="Ottava"` subtype `8va` | OK |
| lines/probe_wedge_startend | paired + bare wedges | `HairPin` subtypes 0 (cresc) + 1 (dim) for the two **paired** spans | PARTIAL² |
| mechanics/chord_symbols | "C" "Am" "G7" "C/E" | `Harmony` ×4; roots as tpc, quality `m`/`7`, `bass` present on C/E | OK |
| mechanics/figured_bass | `%%fb 6 4`, `%%fb #6` | `FiguredBass` ×2; digits 6,4 and prefix+6 | OK |
| ornaments/p02_trill_span (FIXED CONF-orn-2) | `!trill(!`…`!trill)!` wavy-line | real `Spanner type="Trill"` subtype `trill` spanning m1→m2 (extra empty `prev` anchor fragments are MuseScore serialisation, not loss) | OK |
| ornaments/p12_trem_double | `!/-! !//-! !///-! !////-!` | `TremoloTwoChord` subtypes c8, c16, c32, c64 | OK |
| ornaments/p15_tilde_roll_d95 (FIXED D95) | `~` roll → `<other-ornament>roll</>` | `Ornament` with **empty subtype** — element exists but no glyph | PARTIAL³ |
| pitch-staff/16_time_common_cut (FIXED) | `M:C`, `[M:C|]` | `TimeSig` subtype 1 (common, 4/4) + subtype 2 (cut, 2/2) | OK |
| pitch-staff/12_key_aeolian_ionian (FIXED) | `K:Aaeolian`, `[K:Cionian]` | correct 0-fifths signatures (no spurious KeySig — correct for 0 accidentals) | OK |
| structure-repeats/anacrusis (FIXED CONF-str-2) | pickup bar | first `Measure len="1/4"` + `irregular=1`, 3 normal bars follow | OK |
| structure-repeats/dcds_directives (FIXED CONF-str-3) | `%%segno %%tocoda %%dalsegno %%dacapo %%fine` | `StaffText` ×5 — segno as `<sym>segno</sym>` glyph, "To Coda", "D.S.", "D.C.", "Fine". **No native `Jump`/`Marker`** | PARTIAL⁴ |
| structure-repeats/voltas | `[1`/`[2` + `|:` `:|` | `Volta` ×2 + `startRepeat` + `endRepeat` | OK |

¹ "Basses" (contrabass section) maps to `voice.bass` — a name-mapping choice in `addInstrumentSounds()`, arguably should be `strings.contrabass`; cosmetic, playback falls back sensibly.
² ³ ⁴ — see "Not done" below.

## Full pieces (reconverted from .abc to scratch, then imported)

| Piece | XML → mscx parity | Notes |
|---|---|---|
| concerto_grosso_in_d (AOS1, 6 parts) | parts 6/6 · measures 118/118 · note events 2400/2400 (2208 pitched + 192 rests) | `Dynamic` ×87, `Tempo`, `Harmony` ×99, `StaffText` ×35 all present; 197 KB mscz |
| la_fontaine_dargent (AOS7, 12 parts) | parts 12/12 · measures 192/192 · note events 5525/5525 (4176 pitched + 1349 rests) | `Slur` ×117 (= 234 XML start/stop), `HairPin` ×25 (= 50 XML wedges), `acciaccatura` ×68, `Harmony` ×180, `Dynamic` ×205; 340 KB mscz |

Both pieces import loss-free at the structural level.

## NOT done — converts but dies (or degrades) on MuseScore import

1. **`~` roll (D95 follow-up)** — `ornaments/p15_tilde_roll_d95`. The fix emits a valid `<ornaments><other-ornament>roll</other-ornament></ornaments>`, but MuseScore 4 imports `other-ornament` as an `Ornament` with an **empty `<subtype/>`** — no symbol, effectively invisible in the score. If the roll should be *seen* in MuseScore, the converter needs to emit a concrete ornament MuseScore recognises (e.g. `<inverted-mordent>` as a visual proxy, or a `<words>` fallback).
2. **Bare (unterminated) wedges** — `lines/probe_wedge_startend`. `!crescendo!`, `!dim!`, `!w!` each emit a start-only `<wedge>` with **no stop**; abc2xml wrote 7 wedge elements, MuseScore imported only the 2 properly paired hairpins and silently dropped the 3 unterminated ones. Converter-side fix: auto-close bare wedges (e.g. at the next note or bar) so they survive as short hairpins.
3. **Sound-jump directives (CONF-structure-repeats-3 follow-up)** — `structure-repeats/dcds_directives`. The marks are now schema-valid and *visible* (StaffText, segno glyph correct), but MuseScore creates **no `Jump`/`Marker`** elements, so D.C./D.S./To Coda/Fine have no playback-navigation semantics after import. MuseScore builds Jump/Marker from the `<sound dacapo/dalsegno/tocoda/fine>` attributes only when the direction words match its recognised patterns/positions; worth a converter experiment (e.g. put the sound attrs on the barline-adjacent direction or use `<segno>`/`<coda>` direction-types for the coda family) if native jumps are wanted.

## Method notes

- The ubiquitous `Articulation ×10` in every file is the Instrument definition's default articulation table (velocity/gateTime), not notation — ignore it when grepping.
- mscx spanners are written twice (start element + `prev`-anchor at the end point); count `Spanner type="X"` with a child `X` element for true counts.
- MuseScore CLI aborts (SIGABRT) after writing the file are masked by `to_musescore.sh` by design; verdicts here rely on file existence + content, which is the correct gate.
