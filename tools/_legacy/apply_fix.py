
import sys

# The fix we want to apply
TARGET = """						ret = letter_to_grace(line, i);
						// TODO-PER: Be sure there aren't already grace notes defined. That is an error.
						if (ret[0] > 0) {
							el.gracenotes = ret[1];
							i += ret[0];
						} else
							break;
					}
				}
			}"""

REPLACEMENT = """						ret = letter_to_grace(line, i);
						// TODO-PER: Be sure there aren't already grace notes defined. That is an error.
						if (ret[0] > 0) {
							el.gracenotes = ret[1];
							i += ret[0];
						} else {
							ret = letter_to_open_slurs_and_triplets(line, i);
							if (ret.consumed > 0) {
								if (ret.startSlur !== undefined)
									el.startSlur = (el.startSlur || 0) + ret.startSlur;
								if (ret.dottedSlur)
									el.dottedSlur = true;
								if (ret.triplet !== undefined) {
									if (tripletNotesLeft > 0)
										warn("Can't nest triplets", line, i);
									else {
										el.startTriplet = ret.triplet;
										el.tripletMultiplier = ret.tripletQ / ret.triplet;
										el.tripletR = ret.num_notes;
										tripletNotesLeft = ret.num_notes === undefined ? ret.triplet : ret.num_notes;
									}
								}
								i += ret.consumed;
							} else
								break;
						}
					}
				}
			}"""

def main():
    with open('abc_parse_music_original.js', 'r') as f:
        content = f.read()
    
    if TARGET in content:
        new_content = content.replace(TARGET, REPLACEMENT)
        with open('abc_parse_music_FINAL.js', 'w') as f:
            f.write(new_content)
        print("FIX_APPLIED_SUCCESSFULLY")
    else:
        # Try with different indentations or small variations if needed
        # But based on my view_file, it should match perfectly.
        print("TARGET_NOT_FOUND")

if __name__ == '__main__':
    main()
