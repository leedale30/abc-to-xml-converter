# Antigravity Project Rules

## Agentic Skills Setup

- This project uses a global library of agentic skills.
- The master library is stored at `~/antigravity-skills`.
- To enable these skills in any new project, create the `.agent` directory and symlink the master library:

  ```bash
  mkdir -p .agent && ln -s ~/antigravity-skills .agent/skills
  ```

## Development Standards

- Always refer to relevant skills in `~/antigravity-skills` (linked via `.agent/skills`) for domain-specific expertise.
- Follow the guidelines in `senior-fullstack` and `javascript-mastery` for all code changes.

## ABC+ Authoring Rules — MusicXML / MuseScore Compatibility

### Rule: never let a breath mark (or articulation) attach to a grace note
abc2xml applies a decoration to the **next note event**. A `!breath!` written at a phrase/bar end immediately before a pickup **grace** note (e.g. `... e2) !breath!|({f}...`) is therefore attached to that grace, producing a `<breath-mark/>` *inside* a `<grace>` `<note>` in the output.

- The output is **valid MusicXML** — Dorico imports it without complaint — **but MuseScore 4's importer segfaults** on a grace note carrying a breath-mark.
- Grace notes on their own import fine (even many per bar); breath marks on their own import fine. **Only the combination on the same note crashes.**

**Do:** ensure a real note or rest separates a `!breath!` from a following grace. Place the breath where it lands on a real note or a rest (`!breath!z2` is safe), or omit it. Never write `note) !breath!|({grace}`.

**Check (must print `0`):**
```bash
awk '/<note>/{g=b=0}/<grace/{g=1}/breath-mark/{b=1}/<\/note>/{if(g&&b)c++}END{print c+0}' out.musicxml
```

*Discovered 2026-06-02 while preparing a 58-stave orchestral score (The Fire-Bringer). Minimal reproducer + passing twin in that project's `grace_test/` (`06_grace_plus_breath_CRASHES` vs `02_grace_full`).*
