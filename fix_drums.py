import re

def fix_measure(msre):
    # Remove leading/trailing whitespace
    m = msre.strip()
    if not m: return msre
    
    # Check if it looks like a drum measure with the issue
    # Pattern: starts with C,,2
    # We strip decorations temporarily for checking
    clean_m = re.sub(r'![^!]+!', '', m).strip()
    
    if clean_m.startswith("C,,2"):
        # Split into tokens (notes/chords)
        # Note: Chords [A B] count as one token.
        # Simple split by space might work if spacing is standard.
        # But [^C,,^F,,] has no spaces inside.
        tokens = clean_m.split()
        
        # We expect 1 (quarter) + 7 (eighths) = 8 tokens
        # We want 1 + 6 = 7 tokens
        if len(tokens) == 8:
            # Reconstruct the measure using original 'm' to keep decorations if any?
            # Actually the drum lines don't have decorations on the notes usually, except start.
            # But wait, there might be 'fill' text.
            
            # Let's find the LAST token in the original string and remove it.
            # We can find the last space and cut.
            # But we must be careful about trailing spaces or invisible chars.
            
            # Splitting the original string 'm' by space
            parts = m.split()
            # If parts match the count (some parts might be decorations)
            
            # Let's assume the decoration is attached to the first note or separate.
            # tokens count was on clean_m.
            
            # If clean_m has 8 notes, we remove the last one.
            # finding the last note in 'm'.
            last_space = m.rfind(' ')
            if last_space != -1:
                return m[:last_space] + ' ' # Remove last token
            
    return msre

with open('untitled3.abc', 'r') as f:
    lines = f.readlines()

new_lines = []
fixed_count = 0

for line in lines:
    # Only process lines that look like drum notes (checking for C,,2)
    if "C,,2" in line and "|" in line:
        # Split by |
        # Note: ABC bars can be | or || or [| etc.
        # But this file uses |
        
        # Split carefully to preserve delimiters?
        # Simpler: Split by '|'
        parts = line.split('|')
        new_parts = []
        for i, p in enumerate(parts):
            # The last part usually is empty or newline if line ends with |
            if i == len(parts) - 1 and p.strip() == "":
                new_parts.append(p)
                continue
            
            # Fix the measure
            new_p = fix_measure(p)
            if new_p != p:
                fixed_count += 1
            new_parts.append(new_p)
        
        new_line = "|".join(new_parts)
        new_lines.append(new_line)
    else:
        new_lines.append(line)

with open('untitled3.abc', 'w') as f:
    f.writelines(new_lines)

print(f"Fixed {fixed_count} measures.")
