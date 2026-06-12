# Legacy helpers (archived from the old app folder)

These files were rescued from the earlier converter copy at
`~/ABC plus to MusicXML/abc-to-xml-converter` — a Jan 2026 clone of the same
GitHub repo (`leedale30/abc-to-xml-converter`) — before that folder was deleted
(2026-06-02) to avoid two confusing app copies. The canonical, newer converter
is **this** one (`~/COMPOSER/abc-to-xml-converter`, ~3 months ahead).

Kept for reference only — none are part of the current app:

- `abc_parse_music_FINAL.js`, `_FIX.js`, `_PUSH.js`, `_original.js`
  — old hand-edited variants of the abcjs music parser (the project now uses the
    `abcjs_fork` submodule). Related to grace-note handling.
- `apply_fix.py` — one-off patch script (a `letter_to_grace` edit).
- `fix_measures.py` — one-off: fix measure-count mismatches in `Galactic_Horizon.abc`.
- `normalize_measures.py` — one-off: pad all voices of `Galactic_Horizon.abc` to 220 bars.
- `split_perc.py` — utility: split a percussion voice.

Nothing else was unique to the old folder: all compositions already live under
`COMPOSER/COMPOSITIONS/...` (and `The_Titans_Arrival.mscz` was copied into its
composition folder), and the old clone had no unpushed git history.
