# ABC+ Feature Showcase Checklist

## 1. Playback & State

- [x] `%%swing` (Swing feel interpretation)
- [x] `%%mute` (Voice/Part muting)
- [x] **[NEW]** `%%whistle-tab on` (Tin Whistle Fingering Diagrams)
- [ ] `%%dir` (Directional metadata)
- [ ] `%%mood` / `%%style` (Mood and Style metadata)

## 2. Layout & Engraving

- [x] `%%vskip` (Vertical spacing control)
- [x] `%%sep` (Musical section separators/lines)
- [x] **[NEW]** `%%lyrics-above` (Global placement for lyrics)
- [x] `%%measurenumbering` (Custom measure numbering placement/visibility)
- [x] `@above` / `@below` (Explicit placement for any decoration or text)
- [x] `!text("...")@placement` (Rich text annotations)

## 3. Advanced Symbols

- [x] Figured Bass (`!fb "..."!`)
- [x] Guitar Chord Frames (`!frame "..."!`)
- [x] Parameterized Decorations (e.g., `fingering(1)`, `fret(5)`)
- [x] Complex Dynamics (`subito-p`, `!cresc(start)!` with hairpins)
- [x] Rehearsal Marks (`!marker "A"!`)

## 4. Multi-voice & Orchestration

- [x] Score grouping (`%%score`)
- [x] MIDI program shifts per voice
- [x] Staff descriptors (name, shortname)
- [x] Part-specific metadata
