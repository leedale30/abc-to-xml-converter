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
