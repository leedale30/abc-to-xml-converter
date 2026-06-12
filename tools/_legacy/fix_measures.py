#!/usr/bin/env python3
"""
Fix measure count mismatches in Galactic_Horizon.abc
Target: 220 measures per voice (6 sections: 20+20+20+50+40+40+30=220)
Actually: I (20) + II (20) + III (30) + IV (50) + V (40) + VI (40) = 200? 
Let me calculate from the sections:
Section I: mm 1-20 = 20 bars
Section II: mm 21-40 = 20 bars  
Section III: mm 41-60 (Part 2) + mm 61-90 = 50 bars
Section IV: mm 91-140 = 50 bars
Section V: mm 141-180 = 40 bars
Section VI: mm 181-220 = 40 bars
Total: 20+20+50+50+40+40 = 220 bars
"""

import re

def count_bars(line):
    """Count bars (measures) in a voice line by counting | symbols"""
    # Remove the voice header
    content = re.sub(r'^\[V:[^\]]+\]\s*', '', line)
    # Count bar lines (|) but not double bars (||)
    # Each measure ends with | or ||
    bars = content.count('|')
    # || counts as one bar end, not two
    double_bars = content.count('||')
    # Correct: bars - double_bars gives us the actual measure count
    return bars - double_bars

def fix_voice_measures(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Voice target counts per section
    # If total is 222, we need to remove 2 bars
    # If total is 189, we need to add 31 bars
    
    fixes_needed = {
        'Picc': -2,    # 222 -> 220
        'Fl1': +31,    # 189 -> 220
        'Fl2': -1,     # 221 -> 220
        'Cl1': -9,     # 229 -> 220
        'Cl2': -8,     # 228 -> 220
        'Trb2': -10,   # 230 -> 220
        'Trb3': -10,   # 230 -> 220
    }
    
    new_lines = []
    for i, line in enumerate(lines):
        match = re.match(r'\[V:(\w+)\]', line)
        if match:
            voice = match.group(1)
            if voice in fixes_needed:
                fix = fixes_needed[voice]
                current_count = count_bars(line)
                print(f"Line {i+1}: {voice} has {current_count} bars, fix needed: {fix}")
                
                # For voices needing FEWER bars, remove trailing z8 rests
                if fix < 0:
                    # Find and remove extra z8 rests
                    parts = line.rstrip().rstrip('|').split('|')
                    # Find how many z8 rests at the end
                    trailing_rests = 0
                    for p in reversed(parts):
                        if 'z8' in p.strip() and len(p.strip()) <= 4:
                            trailing_rests += 1
                        else:
                            break
                    
                    if trailing_rests >= abs(fix):
                        # Remove the extra bars
                        new_parts = parts[:-abs(fix)]
                        new_line = '|'.join(new_parts) + ' ||\n'
                        new_lines.append(new_line)
                        print(f"  -> Fixed: removed {abs(fix)} trailing rests")
                        continue
                
                # For voices needing MORE bars, add z8 rests
                if fix > 0:
                    # Add rests before the final ||
                    base = line.rstrip().rstrip('|').rstrip()
                    if not base.endswith('|'):
                        base += ' |'
                    for _ in range(fix):
                        base += ' z8 |'
                    new_line = base + '|\n'
                    new_lines.append(new_line)
                    print(f"  -> Fixed: added {fix} rests")
                    continue
        
        new_lines.append(line)
    
    with open(file_path, 'w') as f:
        f.writelines(new_lines)
    
    print("Done!")

if __name__ == "__main__":
    fix_voice_measures("COMPOSER/Galactic_Horizon.abc")
