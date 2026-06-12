#!/usr/bin/env python3
"""
Normalize all voices in Galactic_Horizon.abc to exactly 220 measures.
Each voice that has fewer bars gets padded with z8 rests at the end.
Each voice that has more bars gets truncated (removes excess from the end).
"""

import re

TARGET_MEASURES = 220

def count_bars(line):
    """Count measures in a voice line"""
    # Remove voice header
    content = re.sub(r'^\[V:[^\]]+\]\s*', '', line)
    # Count single bars
    bars = content.count('|')
    # || counts as one bar end
    double_bars = content.count('||')
    return bars - double_bars

def normalize_voice_line(line, target_bars):
    """Normalize a single voice line to have exactly target_bars measures"""
    match = re.match(r'(\[V:[^\]]+\])\s*', line)
    if not match:
        return line
    
    header = match.group(1)
    content = line[match.end():].strip()
    
    current_bars = count_bars(line)
    
    if current_bars == target_bars:
        return line  # Already correct
    
    # Remove trailing || and whitespace
    content = content.rstrip()
    if content.endswith('||'):
        content = content[:-2].rstrip()
        has_double_bar = True
    else:
        has_double_bar = True  # We'll add one
    
    # Split into measures
    measures = [m.strip() for m in content.split('|') if m.strip()]
    
    if len(measures) > target_bars:
        # Truncate
        measures = measures[:target_bars]
    elif len(measures) < target_bars:
        # Pad with rests
        while len(measures) < target_bars:
            measures.append('z8')
    
    # Reconstruct
    new_content = ' | '.join(measures) + ' ||'
    return f"{header} {new_content}\n"

def normalize_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # First pass: collect all voice lines and their total counts
    voice_totals = {}
    voice_lines = {}  # voice_name -> [(line_index, bar_count)]
    
    for i, line in enumerate(lines):
        match = re.match(r'\[V:(\w+)\]', line)
        if match:
            voice = match.group(1)
            bars = count_bars(line)
            if voice not in voice_totals:
                voice_totals[voice] = 0
                voice_lines[voice] = []
            voice_totals[voice] += bars
            voice_lines[voice].append((i, bars))
    
    print("Current voice totals:")
    for voice, total in sorted(voice_totals.items()):
        status = "OK" if total == TARGET_MEASURES else f"NEED {TARGET_MEASURES - total:+d}"
        print(f"  {voice}: {total} bars [{status}]")
    
    # Second pass: normalize voices that need fixing
    for voice, total in voice_totals.items():
        if total == TARGET_MEASURES:
            continue  # Already correct
        
        diff = TARGET_MEASURES - total
        vlines = voice_lines[voice]
        
        if diff > 0:
            # Need to add bars - add to LAST section only
            last_line_idx, last_bar_count = vlines[-1]
            lines[last_line_idx] = normalize_voice_line(
                lines[last_line_idx], 
                last_bar_count + diff
            )
            print(f"  Fixed {voice}: added {diff} rests to final section (line {last_line_idx + 1})")
        else:
            # Need to remove bars - remove from sections with excess z8 rests
            to_remove = abs(diff)
            for line_idx, _ in reversed(vlines):
                line = lines[line_idx]
                # Count trailing z8 rests
                content = line.rstrip().rstrip('|').rstrip()
                parts = content.split('|')
                trailing_rests = 0
                for p in reversed(parts):
                    if 'z8' in p.strip() and len(p.strip()) <= 4:
                        trailing_rests += 1
                    else:
                        break
                
                can_remove = min(trailing_rests, to_remove)
                if can_remove > 0:
                    # Remove trailing rests
                    new_bar_count = count_bars(line) - can_remove
                    lines[line_idx] = normalize_voice_line(lines[line_idx], new_bar_count)
                    to_remove -= can_remove
                    print(f"  Fixed {voice}: removed {can_remove} rests from line {line_idx + 1}")
                
                if to_remove <= 0:
                    break
            
            if to_remove > 0:
                print(f"  WARNING: Could not remove all excess bars for {voice}, {to_remove} remaining")
    
    with open(file_path, 'w') as f:
        f.writelines(lines)
    
    print("\nDone! Run validate_abc.py to verify.")

if __name__ == "__main__":
    normalize_file("COMPOSER/Galactic_Horizon.abc")
