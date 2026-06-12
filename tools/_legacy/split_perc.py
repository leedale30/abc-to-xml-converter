
import re

def split_perc(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    
    # 1. Update Header
    for line in lines:
        if line.startswith('%%score'):
            # Update score: replace (Perc) with (Perc1) (Perc2)
            new_line = line.replace('(Perc)', '(Perc1) (Perc2)')
            new_lines.append(new_line)
        elif line.startswith('V:Perc '):
            # Replace definition
            new_lines.append('V:Perc1 name="Snare/Cymbal" snm="SD" clef=bass\n')
            new_lines.append('V:Perc2 name="Bass Drum" snm="BD" clef=bass\n')
        elif line.startswith('%%midi program 22'):
            new_lines.append('%%midi program 22 49 % Percussion 1 (Snare/Cymbal)\n')
            new_lines.append('%%midi program 32 49 % Percussion 2 (Bass Drum)\n')
        elif line.startswith('[V:Perc]'):
            # Process content lines
            # Create SD line (Keep c, silence B)
            sd_line = line.replace('[V:Perc]', '[V:Perc1]')
            # Create BD line (Keep B, silence c)
            bd_line = line.replace('[V:Perc]', '[V:Perc2]')
            
            # Helper to silence notes
            def silence_notes(text, note_char):
                # Regex to match note (e.g. B, B2, B,,4 etc)
                # Note: pitch can have , or ' and duration digits and modifiers (!...!)
                # Simplification: Assume basic ABC for percussion here.
                # The file uses B2, c2, c8-!pp!
                # Note pattern: [^|\s(]*[NoteChar][^|\s)]*
                # We need to parse tokens carefully.
                
                tokens = re.split(r'(\s+|\|)', text)
                new_tokens = []
                for token in tokens:
                    if note_char in token and not token.startswith('[V:'): # Avoid header match
                        # Check if it's actually a note token
                        # Should start with note char or accidental
                        # Here we assume simple B/c per analysis.
                        
                        # Extract duration
                        duration_match = re.search(r'\d+', token)
                        duration = duration_match.group(0) if duration_match else ""
                        
                        # Replace with rest z + duration
                        # Handle ties (-) and dynamics (!..!)?
                        # If silencing, we remove dynamics and ties usually.
                        # Just z + duration.
                        new_token = 'z' + duration
                        new_tokens.append(new_token)
                    else:
                        new_tokens.append(token)
                return "".join(new_tokens)

            # Better regex replacement
            # Replace B... with z... in SD line
            # Regex: \bB[,']*(\d+)?(-)?(![^!]+!)?
            
            def replace_with_rest(match):
                dur = match.group(1) if match.group(1) else ""
                return "z" + dur

            # Silence B in SD (Perc1)
            # Match B followed by optionals (, or ') then digits
            # Ignore dynamics for now in rest (z doesn't need dynamics usually, but !p! z is valid)
            # Actually, let's just strip everything and put z[duration]
            sd_line = re.sub(r'\bB[,]*(\d+)?[-!a-zA-Z0-9()]*', replace_with_rest, sd_line)
            
            # Silence c in BD (Perc2)
            bd_line = re.sub(r'\bc[\']*(\d+)?[-!a-zA-Z0-9()]*', replace_with_rest, bd_line)

            new_lines.append(sd_line)
            new_lines.append(bd_line)
        else:
            new_lines.append(line)

    with open(file_path, 'w') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    split_perc("COMPOSER/Galactic_Horizon.abc")
