# ABC+ to MusicXML Feature Documentation

This document tracks all MusicXML features supported by the ABC+ Converter.

---

## ✅ Fully Supported Features

### Core Notation

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `C D E F` | `<note><pitch>` | Basic notes with pitch |
| `z`, `x` | `<rest>` | Visible and invisible rests |
| `Z` | `<rest measure="yes">` | Whole measure rest |
| `[CEG]` | `<chord>` | Chord notation |
| `C2`, `C/2`, `C3/2` | `<duration>`, `<type>` | Note durations |
| `^C`, `_C`, `=C` | `<accidental>` | Sharp, flat, natural |
| `C,`, `c'` | `<octave>` | Octave modifiers |

### Rhythm & Time

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `M:4/4`, `M:6/8` | `<time>` | Time signatures |
| `L:1/8` | Unit length | Default note duration |
| `(3CDE` | `<tuplet>`, `<time-modification>` | Triplets and tuplets |
| `C>D`, `C<D` | Broken rhythm | Dotted/cut rhythm |
| `{cdc}` | `<grace>` | Grace notes |
| `{/c}` | `<grace slash="yes">` | Acciaccatura |

### Key & Clef

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `K:C`, `K:Am` | `<key>` | Key signatures |
| `K:Cmix`, `K:Ddor` | `<key><mode>` | Modal keys |
| `K:clef=bass` | `<clef>` | Clef specification |
| `K:clef=alto` | `<clef><sign>C</sign>` | C clefs |
| `K:clef=perc` | `<clef><sign>percussion</sign>` | Percussion clef |
| `K:clef=tab` | `<clef><sign>TAB</sign>` | Tablature |

### Articulations

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `!staccato!` or `.C` | `<staccato/>` | Staccato |
| `!accent!` | `<accent/>` | Accent |
| `!tenuto!` | `<tenuto/>` | Tenuto |
| `!marcato!` | `<strong-accent/>` | Marcato |
| `!fermata!` or `H` | `<fermata/>` | Fermata |
| `!upbow!` or `u` | `<up-bow/>` | Up bow |
| `!downbow!` or `v` | `<down-bow/>` | Down bow |
| `!breath!` | `<breath-mark/>` | Breath mark |
| `!snap!` | `<snap-pizzicato/>` | Snap pizzicato |
| `!staccatissimo!` | `<staccatissimo/>` | Staccatissimo |
| `!caesura!` | `<caesura/>` | Caesura |

### Ornaments

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `!trill!` or `T` | `<trill-mark/>` | Trill |
| `!trill(!`, `!trill)!` | `<wavy-line>` | Extended trill |
| `!mordent!` or `M` | `<mordent/>` | Lower mordent |
| `!uppermordent!` or `P` | `<inverted-mordent/>` | Upper mordent |
| `!turn!` | `<turn/>` | Turn |
| `!vertical-turn!` | `<vertical-turn/>` | Vertical turn |
| `!shake!` | `<shake/>` | Shake |
| `!schleifer!` | `<schleifer/>` | Schleifer |
| `!haydn!` | `<haydn/>` | Haydn ornament |

### Dynamics

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `!ppp!`, `!pp!`, `!p!` | `<dynamics>` | Piano dynamics |
| `!mp!`, `!mf!` | `<dynamics>` | Mezzo dynamics |
| `!f!`, `!ff!`, `!fff!` | `<dynamics>` | Forte dynamics |
| `!sfz!`, `!rfz!`, `!n!` | `<dynamics>` | Special dynamics |
| `!sfzp!`, `!rf!` | `<dynamics>` | Complex dynamics |
| `!crescendo(!` | `<wedge type="crescendo">` | Hairpin crescendo |

### Slurs & Ties

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `(CDE)` | `<slur>` | Slurs |
| `C-C` | `<tie>`, `<tied>` | Ties |
| `.(CDE)` | `<slur line-type="dotted">` | Dotted slur |

### Pedal & Octave Lines

Real, playback-capable spanners — attach the decoration to the next note (no space). Do **not**
use `"^Ped."`/`"^8va"` text annotations: they are cosmetic `<words>` only and do not play back.

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `!ped!` / `!ped-up!` | `<pedal line="no" sign="yes">` | Sustain pedal, asterisk style (`Ped.` … `✶`) |
| `!ped(!` / `!ped)!` | `<pedal line="yes" sign="no">` | Sustain pedal, line/bracket style |
| `!ped-change!` | `<pedal type="change" line="yes">` | Re-pedal (lift-and-recatch) notch inside a pedal line |
| `!8va!` / `!8va)!` | `<octave-shift>` | Octave line (also `!8vb!` `!15ma!` `!15mb!` `!22ma!` `!22mb!`); close with `)` |
| `!gliss(!` / `!gliss)!` | `<glissando>` | Glissando slide (spell `gliss`, not `glissando`) |

### Barlines & Repeats

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `|` | `<barline>` | Regular barline |
| `||` | `<barline>` | Double barline |
| `|]` | `<barline>` | Final barline |
| `|:`,`:|` | `<repeat>` | Repeat signs |
| `[1`, `[2` | `<ending>` | Volta brackets |
| `!segno!` | `<segno/>` | Segno sign |
| `!coda!` | `<coda/>` | Coda sign |

### Text & Directions

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `"^text"` | `<words>` | Text above staff |
| `"_text"` | `<words>` | Text below staff |
| `Q:1/4=120` | `<metronome>` | Tempo marking |
| `%%marker A` | `<rehearsal>` | Rehearsal mark |

### Chord Symbols

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `"C"`, `"Am"` | `<harmony>` | Basic chords |
| `"C/E"` | `<harmony><bass>` | Slash chords |
| `%%frame C x32010` | `<frame>` | Guitar chord diagrams |
| `%%fb 6 4` | `<figured-bass>` | Figured bass notation |

### Layout & Formatting

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `%%newpage` | `<print new-page="yes">` | Start new page |
| `%%newline` | `<print new-system="yes">` | Start new system |
| `%%vskip 20` | `<system-distance>` | Vertical spacing |
| `%%sep` | `<system-dividers>` | Horizontal separator |
| `%%measurenumbering yes` | `<measure-numbering>` | Toggle bar numbers |

### Playback Controls

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `%%swing` | `<sound swing="yes"/>` | Swing playback |
| `%%mute` | `<sound mute="yes"/>` | Instrument muting |

### TAB & Percussion

| ABC+ Syntax | MusicXML Element | Notes |
| :--- | :--- | :--- |
| `K:clef=tab` | TAB staff | Tablature notation |
| `!1!`-`!6!` | `<string>`, `<fret>` | String/fret numbers |
| `I:percmap` | `<unpitched>` | Percussion mapping |

---

## 📊 Coverage Summary

| Category | Supported | Total | Coverage |
| :--- | :--- | :--- | :--- |
| Core Notation | 25 | 25 | 100% |
| Articulations | 15 | 15 | 100% |
| Ornaments | 10 | 10 | 100% |
| Dynamics | 12 | 12 | 100% |
| Barlines/Repeats| 12 | 12 | 100% |
| Text/Directions | 8 | 8 | 100% |
| Chord Symbols | 7 | 7 | 100% |
| Lyrics | 4 | 4 | 100% |
| Layout | 8 | 8 | 100% |
| **Overall** | ~101 | ~101 | **~92%** |

---

## 📝 version History

| Version | Date | Changes |
| :--- | :--- | :--- |
| 1.4.4 | 2026-07-16 | **Filenames containing glob metacharacters are no longer silently dropped.** Input paths were always passed through `glob()`, so a real file whose name contains `[` `]` `?` `*` — e.g. `Bossa Nova [Mark]/x.abc`, where `[Mark]` is read as a character class — matched nothing and abc2xml exited with "none of the input files exist". An existing literal path now wins; globbing still applies to genuine patterns. |
| 1.4.3 | 2026-07-16 | **Hairpin fix (silent data loss).** Every wedge *start* was emitted as `<wedge type="stop">`, so all crescendos/diminuendos were dead — scores showed and played no hairpins at all, with no warning. The start/stop test was `if ')' in d or 'end' in d`, and `end` is a substring of cresc**end**o / diminu**end**o / decresc**end**o, so `!crescendo(!`, `!diminuendo(!` and the bare `!crescendo!` / `!diminuendo!` / `!decrescendo!` forms all became stops. (The `!<(!` / `!>(!` forms were unaffected — hence the bug hid.) Replaced the substring guesswork with explicit token sets; all 25 `wedgeMap` tokens now map correctly. Regression test: `TESTFILES/test_wedge_hairpins.abc`. See `TROUBLESHOOTING.md`. |
| 1.4.2 | 2026-06-12 | New directives: `%%tempofont <font>` (font-family on tempo words/metronome) and `%%barnumbers <0|1|yes|no>` (alias for measure numbering). Ported from in-progress work recovered from a secondary clone. Spec submodule removed — the ABC+ spec lives in its own repo (github.com/leedale30/abc-plus-spec). |
| 1.3.3 | 2026-06-03 | MuseScore-compat: `addInstrumentSounds()` emits `<instrument-sound>` for every part (mapped from the part name) so MuseScore/others recognise instruments instead of falling back to generic "MS Basic" sounds. Matches Dorico's output. |
| 1.3.2 | 2026-06-02 | MuseScore-compat: `fixGraceBreaths()` relocates breath-marks off grace notes (prevents a MuseScore 4 import crash; output stays valid MusicXML, Dorico-confirmed). Regression test: `TESTFILES/test_grace_breath_musescore.abc`. See `TROUBLESHOOTING.md` / `.agent/rules.md`. |
| 1.3.1 | 2026-01-20 | Fixed audio synthesis (offline support) and visual sync |
| 1.3.0 | 2026-01-20 | Added ABCJS audio synthesis and OpenSheetMusicDisplay rendering |
| 1.2.0 | 2026-01-17 | Added playback and layout controls |
| 1.0.0 | 2026-01-17 | Initial release |
