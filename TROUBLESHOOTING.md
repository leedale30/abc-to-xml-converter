# Fixing "ModuleNotFoundError: No module named 'pyparsing'" Error

## Problem

When running the ABC to MusicXML converter, conversions fail with:

```
ModuleNotFoundError: No module named 'pyparsing'
```

This happens even when `pyparsing` is installed in the virtual environment.

## Root Cause

The `app.py` was using a hardcoded `python3` command in the subprocess call:

```python
result = subprocess.run(
    ['python3', CONVERTER_SCRIPT, temp_abc_path],  # ❌ Uses system Python
    ...
)
```

This invokes the **system Python** instead of the **virtual environment's Python**, so packages installed in `.venv` (like `pyparsing`) are not available.

## Solution

Replace `'python3'` with `sys.executable`, which always points to the Python interpreter currently running the Flask app:

```python
result = subprocess.run(
    [sys.executable, CONVERTER_SCRIPT, temp_abc_path],  # ✅ Uses venv Python
    ...
)
```

## Quick Fix Steps

1. **Open `app.py`**
2. **Find line ~139** containing `['python3', CONVERTER_SCRIPT, ...]`
3. **Replace `'python3'` with `sys.executable`**
4. **Restart the Flask server**

## Verification

After applying the fix, conversions should complete successfully without the `pyparsing` import error.

---

*Fixed: 2026-01-16*

---

# MuseScore 4 crashes on import (grace note + breath mark)

## Problem

A `.musicxml` file from the converter is valid and converts with **no error**, but **MuseScore 4 crashes (segfaults) on import** — no file is produced and the process aborts. The *same file opens correctly in Dorico*.

## Root Cause

abc2xml applies a decoration to the **next note event**. When a `!breath!` is written at a phrase/bar end immediately before a pickup **grace** note:

```
... A3 A e2 e2) !breath!|({f}!tenuto!e3 ...
```

the breath is deferred onto the following grace note, emitting a `<breath-mark/>` *inside* a `<grace>` `<note>`:

```xml
<note>
  <grace />
  <pitch>...</pitch>
  <notations><articulations><breath-mark /></articulations></notations>
</note>
```

A breath-mark on a zero-duration grace is nonsensical, and **MuseScore 4's importer crashes on it**. Grace notes alone import fine (even 32 in a bar); breath marks alone import fine; **only the combination on one note triggers the crash.** Dorico tolerates it (relocating the breath to a rest), which confirms the MusicXML is valid and the fault is MuseScore's.

## Solution

Keep breath marks off grace notes in the ABC source: ensure a real note or rest separates a `!breath!` from a following grace, or drop that breath. A breath before a rest (`!breath!z2`) is safe; `note) !breath!|({grace}` is not.

## Verification

No `<note>` in the output should contain both `<grace/>` and `<breath-mark>`:

```bash
awk '/<note>/{g=b=0}/<grace/{g=1}/breath-mark/{b=1}/<\/note>/{if(g&&b)c++}END{print c+0}' out.musicxml   # must print 0
```

---

*Documented: 2026-06-02*

---

# MuseScore imports parts as generic / "MS Basic" sounds (instruments not recognised)

## Problem

After importing a converted `.musicxml`, MuseScore shows "MS Basic" (or a generic sound) for
most parts instead of the real instruments. Only a few whose `<part-name>` happens to match
MuseScore's instrument list exactly (e.g. "Piccolo", "English Horn") are recognised. Opening the
file in Dorico, re-saving as MusicXML, then opening *that* in MuseScore works fine.

## Root Cause

MuseScore maps a part to a playback instrument primarily via the MusicXML **`<instrument-sound>`**
id inside `<score-instrument>` (e.g. `wind.flutes.flute`, `brass.trumpet.bflat`, `strings.violin`).
abc2xml did not emit `<instrument-sound>` at all — and emitted no `<score-instrument>` for melodic
parts — so MuseScore could only name-match and fell back to a generic sound. Dorico writes an
`<instrument-sound>` for every part, which is why a Dorico round-trip "fixes" recognition.

## Solution

`addInstrumentSounds()` (called at the end of `parse()`) adds an `<instrument-sound>` to every
part, mapped from the part name via a standard-sound table (`_INSTRUMENT_SOUNDS`), creating a
`<score-instrument>` when the part has none. The table is scanned most-specific-first (so
"bass clarinet" beats "clarinet", "piccolo trumpet" beats "trumpet", and a bare "bass" → voice
fallback comes last). Result matches Dorico: Flute → `wind.flutes.flute`, Cimbasso →
`brass.cimbasso`, Mark Tree → `metal.bells.bell-tree`, voices → `voice.*`, strings → `strings.*`.

Note: orchestral string **sections** named in the plural ("Violins 1", "Violas", …) are mapped by
MuseScore to its string-section sound `strings.group` — this is MuseScore's own behaviour and is
identical for Dorico's export; solo strings ("Solo Viola") map to the specific instrument.

## Verification

Every `<score-part>` should contain an `<instrument-sound>`:

```bash
grep -c '<instrument-sound>' out.musicxml   # == number of parts
```

---

*Documented: 2026-06-03*

---

# MuseScore 4 crashes on import (tuplet duration rounding, divisions=2520)

## Problem

A score using explicit-ratio tuplets — e.g. `(4:3:4` over `L:1/16` sixteenths — converts with
**no error**, but **MuseScore 4 crashes on import** (crash reporter fires, no output file).
One isolated tuplet group in a bar may survive; a bar full of them, or many such bars, crashes.

## Root Cause

abc2xml used `divisions = 2520` (2^3 x 3^2 x 5 x 7) per quarter note — chosen for 5/7/9-tuplets,
but **not divisible enough for q=3 ratios on sixteenth notes**. A `(4:3` tuplet sixteenth is
`630 * 3/4 = 472.5` divisions, and `mkNote` floor-divides (`dvs * tmden // tmnum`) → 472.
Each group loses 2 divisions, measures come up short, and MuseScore 4's importer crashes on the
inconsistent measure lengths. (Dotted-eighth-span 4:3 groups are idiomatic in polyrhythmic
piano writing, so this hit every bar of a 4-against-3 mesh.)

## Solution

`divisions` raised to **5040** (2^4 x 3^2 x 5 x 7) in `abc2xml.py` (`reset()`), making every
common tuplet duration integral: 4:3 sixteenth = 945, 5:4 = 1008, 9:8 = 1120, 3:2 = 1680.
The unused-factor reducer at output time shrinks the numbers back down where possible.

## Verification

```bash
python3 abc2xml/abc2xml.py -o /tmp TESTFILES/test_ratio_tuplet_divisions.abc
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" -o /tmp/t.mscz /tmp/test_ratio_tuplet_divisions.xml
ls /tmp/t.mscz   # must exist
```

---

*Fixed: 2026-06-12*

---

# MuseScore 4 shows a wrong default 120 tempo (tempo-word annotation, no BPM)

## Problem

A score plays back at a wrong **120 BPM** at section starts even though the `Q:` / metronome
marks are correct. Inspecting the `.mscz` shows extra `<Tempo>` objects of 2.0 QPS (120 BPM)
sitting next to the real ones — and sometimes mid-section (e.g. a stray 120 inside a 90-BPM
Agitato). The `.musicxml` is correct (one `<sound tempo>` per real change).

## Root Cause

Tempo *text* written as a standalone annotation separate from the metronome —
`[Q:1/4=60] "^Poco piu mosso"` — makes abc2xml emit **two** directions: a `<metronome>`/
`<sound tempo>` (the real BPM) and a bare `<words>Poco piu mosso</words>`. MuseScore 4's
importer recognises Italian tempo terms (`Lento`, `Presto`, `Vivace`, `piu mosso`,
`largamente`, …) in `<words>` and creates a Tempo for them; with no BPM on that direction it
**defaults to 120**. A purely descriptive term that happens to be a tempo word (e.g.
`largamente` used as an expression, with no tempo change) creates a stray 120 all on its own.

## Solution

Unify the term and the BPM into one direction using ABC's tempo-with-string syntax, so there is
only one tempo object (carrying the real BPM):

```
Q:"Lento misterioso" 1/4=40           % header
[Q:"Poco piu mosso" 1/4=60]           % inline, replaces  [Q:1/4=60] "^Poco piu mosso"
```

For a tempo *word used as expression only* (no tempo change), reword to a non-tempo term
(`largamente` → `sonoro`, `ben cantato`, …) so MuseScore does not invent a tempo.

## Verification

```bash
# unzip the .mscz and count Tempo objects — must equal the number of real tempo changes
python3 - <<'PY'
import re,glob
mscx=open(glob.glob('*.mscx')[0]).read()
print(len(re.findall(r'<tempo>([0-9.]+)</tempo>', mscx)), "tempo marks; BPMs:",
      [round(float(t)*60,1) for t in re.findall(r'<tempo>([0-9.]+)</tempo>', mscx)])
PY
```

---

*Fixed: 2026-06-13*

---

# Pedal (or octave line) doesn't play back — written as text instead of a decoration

## Problem

A score shows `Ped.` / `✶` (or `8va`) markings but the sustain pedal (or octave transposition)
has **no effect on playback** in MuseScore.

## Root Cause

The marking was written as a **text annotation** — `"^Ped."`, `"_Ped."`, `"_*"`, `"^8va"` —
which abc2xml emits as a cosmetic `<words>` element. It is **not** a `<pedal>` / `<octave-shift>`,
so nothing plays. (MuseScore may also misread a tempo-like word from such text.)

## Solution

Use the real decorations, attached to the next note with **no space**:

| Want | Write | Emits |
| --- | --- | --- |
| Pedal, asterisk style (`Ped.` … `✶`) | `!ped!` … `!ped-up!` | `<pedal line="no" sign="yes">` |
| Pedal, line/bracket style | `!ped(!` … `!ped)!` | `<pedal line="yes" sign="no">` |
| Re-pedal (lift + recatch) | `!ped-change!` (inside a `!ped(!`…`!ped)!` line) | `<pedal type="change">` |
| Octave up/down | `!8va!`…`!8va)!`, `!8vb!`, `!15ma!`, … | `<octave-shift>` |

For continuous **re-pedalling**, use ONE `!ped(!`…`!ped)!` line with `!ped-change!` at each
harmony change — a run of bare `!ped!` signs merges into a single held pedal in MuseScore.
`tools/abc_audit.py` flags pedal/octave written as text.

## Verification

```bash
python3 abc2xml/abc2xml.py -o /tmp TESTFILES/test_pedal_styles.abc
grep -c '<pedal' /tmp/test_pedal_styles.xml      # must be > 0 (real pedal directions)
```

---

*Fixed: 2026-06-13*

---

# Hairpins never appear (all `<wedge>` elements are `type="stop"`)

## Problem

Crescendos and diminuendos written with the word forms are silently dropped. The score
converts without error, but MuseScore shows **no hairpins** and plays no dynamic swell:

```abc
!crescendo(!C D E F!crescendo)!      % -> no hairpin at all
!diminuendo(!G A B c!diminuendo)!    % -> no hairpin at all
```

Diagnose by counting wedge types — starts must balance stops:

```bash
python3 abc2xml/abc2xml.py score.abc | grep -o 'wedge type="[a-z]*"' | sort | uniq -c
#   BAD:  26 wedge type="stop"          <- zero starts, every hairpin dead
#   GOOD:  9 wedge type="crescendo"
#          4 wedge type="diminuendo"
#         13 wedge type="stop"
```

## Root Cause

The wedge start/stop test was a substring match:

```python
if ')' in d or 'end' in d: type = 'stop'      # checked FIRST
```

`end` is a substring of cresc**end**o, diminu**end**o and decresc**end**o. So the *opening*
tokens matched the stop test and every hairpin start became a stop. Affected tokens:
`crescendo(`, `diminuendo(`, and the bare `crescendo` / `diminuendo` / `decrescendo`.

The `!<(!` / `!<)!` / `!>(!` / `!>)!` symbol forms contain no "end" and always worked — which
is why the bug went unnoticed: whichever form you happened to use decided whether your
dynamics existed.

## Solution

Fixed in **1.4.3** — the substring guesswork is replaced by explicit token sets covering all
25 `wedgeMap` entries. Both the word forms and the symbol forms now work.

## Verification

```bash
python3 abc2xml/abc2xml.py TESTFILES/test_wedge_hairpins.abc | grep -o 'wedge type="[a-z]*"'
# expect: 4x crescendo, 4x diminuendo, 8x stop — strictly alternating start,stop
```

If you have scores authored before 1.4.3, re-convert them: their hairpins were never in the
MusicXML, so any `.mscz`/audio rendered from them is missing its dynamics.
