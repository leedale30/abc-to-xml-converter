# ABC+ to MusicXML Feature Documentation

This document tracks all MusicXML features supported by the ABC+ Converter, including what's working, what's been recently added, and what's planned for future development.

---

## ✅ Fully Supported Features

### Core Notation

| ABC+ Syntax | MusicXML Element | Notes |
|-------------|------------------|-------|
| `C D E F` | `<note><pitch>` | Basic notes with pitch |
| `z`, `x` | `<rest>` | Visible and invisible rests |
| `Z` | `<rest measure="yes">` | Whole measure rest |
| `[CEG]` | `<chord>` | Chord notation |
| `C2`, `C/2`, `C3/2` | `<duration>`, `<type>` | Note durations |
| `^C`, `_C`, `=C` | `<accidental>` | Sharp, flat, natural |
| `C,`, `c'` | `<octave>` | Octave modifiers |

### Rhythm & Time

| ABC+ Syntax | MusicXML Element | Notes |
|-------------|------------------|-------|
| `M:4/4`, `M:6/8` | `<time>` | Time signatures |
| `L:1/8` | Unit length | Default note duration |
| `(3CDE` | `<tuplet>`, `<time-modification>` | Triplets and tuplets |
| `C>D`, `C<D` | Broken rhythm | Dotted/cut rhythm |
| `{cdc}` | `<grace>` | Grace notes |
| `{/c}` | `<grace slash="yes">` | Acciaccatura |

### Key & Clef

| ABC+ Syntax | MusicXML Element | Notes |
|-------------|------------------|-------|
| `K:C`, `K:Am` | `<key>` | Key signatures |
| `K:Cmix`, `K:Ddor` | `<key><mode>` | Modal keys |
| `K:clef=bass` | `<clef>` | Clef specification |
| `K:clef=alto` | `<clef><sign>C</sign>` | C clefs |
| `K:clef=perc` | `<clef><sign>percussion</sign>` | Percussion clef |
| `K:clef=tab` | `<clef><sign>TAB</sign>` | Tablature |

### Articulations

| ABC+ Syntax | MusicXML Element | Notes |
|-------------|------------------|-------|
| `!staccato!` or `.C` | `<staccato/>` | Staccato |
| `!accent!` | `<accent/>` | Accent |
| `!tenuto!` | `<tenuto/>` | Tenuto |
| `!marcato!` | `<strong-accent/>` | Marcato |
| `!fermata!` or `H` | `<fermata/>` | Fermata |
| `!upbow!` or `u` | `<up-bow/>` | Up bow |
| `!downbow!` or `v` | `<down-bow/>` | Down bow |
| `!breath!` | `<breath-mark/>` | Breath mark |
| `!snap!` | `<snap-pizzicato/>` | Snap pizzicato |

### Ornaments

| ABC+ Syntax | MusicXML Element | Notes |
|-------------|------------------|-------|
| `!trill!` or `T` | `<trill-mark/>` | Trill |
| `!trill(!`, `!trill)!` | `<wavy-line>` | Extended trill |
| `!mordent!` or `M` | `<mordent/>` | Lower mordent |
| `!uppermordent!` or `P` | `<inverted-mordent/>` | Upper mordent |
| `!turn!` | `<turn/>` | Turn |
| `!roll!` or `~` | `<trill-mark/>` | Roll |

### Dynamics

| ABC+ Syntax | MusicXML Element | Notes |
|-------------|------------------|-------|
| `!ppp!`, `!pp!`, `!p!` | `<dynamics><p/>` | Piano dynamics |
| `!mp!`, `!mf!` | `<dynamics><mp/>` | Mezzo dynamics |
| `!f!`, `!ff!`, `!fff!` | `<dynamics><f/>` | Forte dynamics |
| `!sfz!` | `<dynamics><sfz/>` | Sforzando |
| `!crescendo(!` | `<wedge type="crescendo">` | Hairpin crescendo |
| `!crescendo)!` | `<wedge type="stop">` | End crescendo |
| `!diminuendo(!` | `<wedge type="diminuendo">` | Hairpin diminuendo |

### Slurs & Ties

| ABC+ Syntax | MusicXML Element | Notes |
|-------------|------------------|-------|
| `(CDE)` | `<slur>` | Slurs |
| `C-C` | `<tie>`, `<tied>` | Ties |
| `.(CDE)` | `<slur line-type="dotted">` | Dotted slur |

### Barlines & Repeats

| ABC+ Syntax | MusicXML Element | Notes |
|-------------|------------------|-------|
| `|` | `<barline>` | Regular barline |
| `||` | `<barline><bar-style>light-light` | Double barline |
| `|]` | `<barline><bar-style>light-heavy` | Final barline |
| `|:`,`:|` | `<repeat>` | Repeat signs |
| `[1`, `[2` | `<ending>` | Volta brackets |
| `!segno!` | `<segno/>` | Segno sign |
| `!coda!` | `<coda/>` | Coda sign |
| `!D.S.!`, `!D.C.!` | `<words>` | Da Segno, Da Capo |

### Text & Directions

| ABC+ Syntax | MusicXML Element | Notes |
|-------------|------------------|-------|
| `"^text"` | `<words>` (above) | Text above staff |
| `"_text"` | `<words>` (below) | Text below staff |
| `"<text"` | `<words>` (left) | Text left |
| `">text"` | `<words>` (right) | Text right |
| `Q:1/4=120` | `<metronome>`, `<sound tempo>` | Tempo marking |

### Chord Symbols

| ABC+ Syntax | MusicXML Element | Notes |
|-------------|------------------|-------|
| `"C"`, `"Am"` | `<harmony><root>` | Basic chords |
| `"C7"`, `"Cmaj7"` | `<harmony><kind>` | Extended chords |
| `"C/E"` | `<harmony><bass>` | Slash chords |
| `"Cm7b5"` | `<harmony><degree>` | Altered chords |

### Lyrics

| ABC+ Syntax | MusicXML Element | Notes |
|-------------|------------------|-------|
| `w: lyr-ics` | `<lyric><syllabic>` | Lyrics with syllables |
| `w: word_` | `<extend>` | Melisma |
| Multiple `w:` lines | `<lyric number="N">` | Multiple verses |

### Multi-Voice & Staff

| ABC+ Syntax | MusicXML Element | Notes |
|-------------|------------------|-------|
| `V:1`, `V:2` | `<voice>` | Voice assignment |
| `%%score {1 2}` | Grand staff | Piano-style staves |
| `%%score [1 2]` | Bracket group | Orchestral grouping |
| Voice overlay `&` | `<backup>` | Overlapping voices |

### TAB & Percussion

| ABC+ Syntax | MusicXML Element | Notes |
|-------------|------------------|-------|
| `K:clef=tab` | TAB staff | Tablature notation |
| `!1!`-`!6!` | `<string>`, `<fret>` | String/fret numbers |
| `I:percmap` | `<unpitched>` | Percussion mapping |
| `%%drummap` | Drum notation | Custom drum maps |

---

## 🔧 Recently Implemented

### Update Checker (v1.0.0)

- **Feature**: Automatic GitHub release check on app startup
- **Files**: `app.py`, `templates/index.html`, `static/script.js`, `static/style.css`
- **Behavior**: Shows gold banner when new version available

### Debug Report Export

- **Feature**: Download combined ABC+, MusicXML, and logs as single `.md` file
- **Files**: `templates/index.html`, `static/script.js`
- **Button**: Bug icon (🐛) in MusicXML Output pane

---

## 🚧 Partially Supported

| Feature | Status | Notes |
|---------|--------|-------|
| `%%drummap` | ⚠️ Basic | Parses but limited note-head mapping |
| Multiple endings (3+) | ⚠️ Limited | 1st/2nd endings work, 3rd+ may have issues |
| Complex tuplets | ⚠️ Partial | Standard tuplets work, nested may not |
| Custom ABC+ directives | ⚠️ Via preprocessor | `%%dir`, `%%fx` → `<direction><words>` |

---

## ❌ Not Yet Supported

### High Priority

| Feature | MusicXML Element | ABC+ Syntax (Proposed) |
|---------|------------------|------------------------|
| Guitar chord diagrams | `<frame>` | `%%frame C x32010` |
| Figured bass | `<figured-bass>` | `"_6/4"` or `%%fb 6 4` |
| Page/system breaks | `<print new-page>` | `%%newpage`, `%%newline` |

### Medium Priority

| Feature | MusicXML Element | Notes |
|---------|------------------|-------|
| Swing playback | `<sound swing>` | Playback feature |
| Playback transposition | `<transpose>` | MIDI transposition |
| Multiple endings 3+ | `<ending number="3">` | Extend current system |

### Low Priority

| Feature | MusicXML Element | Notes |
|---------|------------------|-------|
| Image embedding | `<image>` | Rarely needed |
| Hyperlinks | `<link>` | Digital publishing |
| Bookmarks | `<bookmark>` | Navigation |
| Grouping | `<grouping>` | Analysis features |

---

## 📊 Coverage Summary

| Category | Supported | Total | Coverage |
|----------|-----------|-------|----------|
| Core Notation | 25 | 25 | 100% |
| Articulations | 12 | 15 | 80% |
| Ornaments | 8 | 10 | 80% |
| Dynamics | 10 | 10 | 100% |
| Barlines/Repeats | 10 | 12 | 83% |
| Text/Directions | 6 | 8 | 75% |
| Chord Symbols | 5 | 5 | 100% |
| Lyrics | 4 | 4 | 100% |
| Layout | 2 | 8 | 25% |
| **Overall** | ~82 | ~97 | **~85%** |

---

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-17 | Initial release, GitHub update checker, debug export |

---

## 📝 Contributing

To add a new feature:

1. Add ABC+ syntax parsing in `abc2xml/abc2xml.py`
2. Map to MusicXML element generation
3. Update this documentation
4. Test with sample ABC+ files
5. Rebuild app: `rm -rf build dist && python3 setup.py py2app`
