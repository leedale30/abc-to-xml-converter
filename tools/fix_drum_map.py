import re
import sys

def fix_drum_map(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    drum_map = {}
    new_lines = []

    # 1. Parse %%drummap directives
    # Format: %%drummap LABEL PITCH MIDI
    # We want to map LABEL -> PITCH
    # Note: PITCH might be in ABC notation like ^F,, or c'
    
    map_regex = re.compile(r'^%%\s*drummap\s+(\w+)\s+([^\s]+)\s+')
    
    for line in lines:
        match = map_regex.match(line)
        if match:
            bg_label = match.group(1)
            bg_pitch = match.group(2)
            drum_map[bg_label] = bg_pitch
            # We keep the line (maybe comment it out?) or just leave it.
            # abc2xml skips it anyway.
            # But let's verify if abc2xml crashes on it. Log said "skipped I-field".
            new_lines.append(line)
        else:
            new_lines.append(line)

    print(f"Found drum map: {drum_map}")

    # 2. Substitute in Voice lines
    # We only want to substitute if the label matches a token.
    # But tokens in ABC are tricky. "BD2" -> "BD" is the content.
    # We need to sort keys by length (longest first) to avoid partial matches if any.
    
    sorted_labels = sorted(drum_map.keys(), key=len, reverse=True)
    
    final_lines = []
    
    for line in new_lines:
        # Heuristic: Only modify lines that look like music or V: lines?
        # Actually just modify everything that isn't a header?
        # Header lines start with Letter:
        if re.match(r'^[A-Z]:', line) or line.startswith('%%'):
            final_lines.append(line)
            continue
            
        # Music line.
        # Replace occurrences.
        # Use regex to ensure we match the label prefixing a duration?
        # e.g. BD2 -> C2.
        # But BD might be just BD.
        # Also need to be careful not to replace things inside strings or comments.
        
        # Simple string replace might be dangerous if label is "A" or "B" (valid notes).
        # The user's labels are BD, SN, CH, OH, CC, RC, JB.
        # These are 2-letter codes. Unlikely to conflict with A-G unless "CC" conflicts with C.
        # "CC" -> "C#3".
        # If we have "CC2", replacing keys "CC" -> "C#3" results in "C#32".
        # "C#3" is a pitch? No, C#3 is probably "C#" octave 3?
        # Wait, the user's map says: %%drummap CC   C#3  49
        # "C#3" in ABC?
        # Standard ABC pitches are C, C,, c c' etc.
        # "C#3" looks like scientific pitch notation or something `abcm2ps` allows.
        # If `abc2xml` supports it, great.
        # If not, we might need to verify what `abc2xml` expects.
        # `abc2xml` expects standard ABC pitch.
        # Let's check one: `%%drummap BD C2 36`.
        # C2 is a pitch "C" at octave 2? Or C duration 2?
        # In %%drummap syntax, it usually means Pitch.
        # If the user used "C2" as the pitch, that might mean C at some octave.
        # But wait, looking at the map:
        # BD -> C2
        # SN -> D2
        # CH -> F#2
        # JB -> c'
        
        # "C2" in standard ABC usually means Note C, length 2.
        # BUT here it is the PITCH DEFINITION.
        # If I replace "BD" with "C2", then "BD2" becomes "C22".
        # That means Note C, length 2 * 2 = 4?
        # That would change the rhythm!
        
        # Inspecting input.abc again:
        # %%drummap BD   C2   36
        # Does "C2" mean the pitch C,,? Or C,,,?
        # Midi 36 is C2 (or C1 depending on standard). Low C.
        # In ABC, C is Middle C (usually). C, is lower. C,, is 36.
        # So "C2" might be a specific notation the user uses for "Low C".
        # OR, maybe they copied this valid map from somewhere else.
        
        # If I blindly replace, I risk "C22".
        # Let's look at JB -> c'.
        # JB2 becomes c'2. That is valid ABC.
        
        # What about BD -> C2?
        # BD2 -> C22.
        # If C2 is "Note C length 2", then C22 is "Note C length 22".
        # This is definitely wrong rhythmically.
        
        # HYPOTHESIS: The user's drum map is defining Pitch using a syntax `abc2xml` might not like, or simply they mean "Note C, octave 2" (which is incorrect ABC syntax, should be C,,).
        # However, verifying `conversion.log` line 4: `**misplaced symbol: 2`
        # This happens on `JB2`?
        # No, `JB` is mapped to `c'`. `c'` is valid.
        # But `BD` is mapped to `C2`.
        # `SN` mapped to `D2`.
        
        # If I replace BD with C2, we get C22.
        # If I replace SN with D2, we get D22.
        
        # Wait. "Measure 28 has too many beats! (Found 5.00, expected 4.00)"
        # Last measure: `CC2 JB2 BD4`.
        # CC -> C#3. JB -> c'. BD -> C2.
        # Replaced: `C#32 c'2 C24`.
        # C#32 -> C# duration 32? (Huge).
        # c'2 -> duration 2.
        # C24 -> C duration 24.
        # Total duration = 32 + 2 + 24 = 58.
        # That can't be right.
        
        # CONCLUSION: The user's drum map values (C2, D2, F#2) are likely "Note name + Octave Number" (Scientific Pitch).
        # Standard ABC does NOT use numbers for octaves (it uses commas and apostrophes).
        # `abc2xml` (and standard ABC) needs `C,,` for C2, `D,,` for D2.
        # `c'` is correct (Middle C + octave).
        
        # So I need to map their Scientific Pitch to ABC Pitch.
        # C2 -> C,,
        # D2 -> D,,
        # F#2 -> ^F,,
        # A#2 -> ^A,,
        # C#3 -> ^C,
        # D#3 -> ^D,
        # c' -> c' (already ABC).
        
        # I will bake this translation into my script.
        
        newline = line
        for label, raw_pitch in drum_map.items():
            # Convert raw_pitch to ABC pitch if necessary
            abc_pitch = raw_pitch
            if raw_pitch == "C2": abc_pitch = "C,,"
            elif raw_pitch == "D2": abc_pitch = "D,,"
            elif raw_pitch == "F#2": abc_pitch = "^F,,"
            elif raw_pitch == "A#2": abc_pitch = "^A,,"
            elif raw_pitch == "C#3": abc_pitch = "^C,"
            elif raw_pitch == "D#3": abc_pitch = "^D,"
            
            # Replace Label with abc_pitch
            # We assume Label is followed by nothing or a number.
            newline = newline.replace(label, abc_pitch)
            
        final_lines.append(newline)

    with open(filename, 'w') as f:
        f.writelines(final_lines)
    
    print("Fixed drum directives.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fix_drum_map(sys.argv[1])
