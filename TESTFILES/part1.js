var parseKeyVoice = require('./abc_parse_key_voice');
var transpose = require('./abc_transpose');

var tokenizer;
var warn;
var multilineVars;
var tune;
var tuneBuilder;
var header;

var {
  legalAccents,
  volumeDecorations,
  dynamicDecorations,
  accentPseudonyms,
  accentDynamicPseudonyms,
  nonDecorations,
  durations,
  pitches,
  rests,
  accMap,
  tripletQ
} = require('./abc_parse_settings')

var MusicParser = function(_tokenizer, _warn, _multilineVars, _tune, _tuneBuilder, _header) {
	tokenizer = _tokenizer;
	warn = _warn;
	multilineVars = _multilineVars;
	tune = _tune;
	tuneBuilder = _tuneBuilder;
	header = _header;
	this.lineContinuation = false;
}

//
// Parse line of music
//
// This is a stream of <(bar-marking|header|note-group)...> in any order, with optional spaces between each element
// core-note is <open-slur, accidental, pitch:required, octave, duration, close-slur&|tie> with no spaces within that
// chord is <open-bracket:required, core-note:required... close-bracket:required duration> with no spaces within that
// grace-notes is <open-brace:required, (open-slur|core-note:required|close-slur)..., close-brace:required> spaces are allowed
// note-group is <grace-notes, chord symbols&|decorations..., grace-notes, slur&|triplet, chord|core-note, end-slur|tie> spaces are allowed between items
// bar-marking is <ampersand> or <chord symbols&|decorations..., bar:required> spaces allowed
// header is <open-bracket:required, K|M|L|V:required, colon:required, field:required, close-bracket:required> spaces can occur between the colon, in the field, and before the close bracket
// header can also be the only thing on a line. This is true even if it is a continuation line. In this case the brackets are not required.
// a space is a back-tick, a space, or a tab. If it is a back-tick, then there is no end-beam.

// Line preprocessing: anything after a % is ignored (the double %% should have been taken care of before this)
// Then, all leading and trailing spaces are ignored.
// If there was a line continuation, the \n was replaced by a \r and the \ was replaced by a space. This allows the construct
// of having a header mid-line conceptually, but actually be at the start of the line. This is equivolent to putting the header in [ ].

// TODO-PER: How to handle ! for line break?
// TODO-PER: dots before bar, dots before slur
// TODO-PER: U: redefinable symbols.

// Ambiguous symbols:
// "[" can be the start of a chord, the start of a header element or part of a bar line.
// --- if it is immediately followed by "|", it is a bar line
// --- if it is immediately followed by K: L: M: V: it is a header (note: there are other headers mentioned in the standard, but I'm not sure how they would be used.)
// --- otherwise it is the beginning of a chord
// "(" can be the start of a slur or a triplet
// --- if it is followed by a number from 2-9, then it is a triplet
// --- otherwise it is a slur
// "]"
// --- if there is a chord open, then this is the close
// --- if it is after a [|, then it is an invisible bar line
// --- otherwise, it is par of a bar
// "." can be a bar modifier or a slur modifier, or a decoration
// --- if it comes immediately before a bar, it is a bar modifier
// --- if it comes immediately before a slur, it is a slur modifier
// --- otherwise it is a decoration for the next note.
// number:
// --- if it is after a bar, with no space, it is an ending marker
// --- if it is after a ( with no space, it is a triplet count
// --- if it is after a pitch or octave or slash, then it is a duration

// Unambiguous symbols (except inside quoted strings):
// vertical-bar, colon: part of a bar
// ABCDEFGabcdefg: pitch
// xyzZ: rest
// comma, prime: octave
// close-paren: end-slur
// hyphen: tie
// tilde, v, u, bang, plus, THLMPSO: decoration
// carat, underscore, equal: accidental
// ampersand: time reset
// open-curly, close-curly: grace notes
// double-quote: chord symbol
// less-than, greater-than, slash: duration
// back-tick, space, tab: space

var isInTie = function(multilineVars, overlayLevel, el) {
	if (multilineVars.inTie[overlayLevel] === undefined)
		return false;
	// If this is single voice music then the voice index isn't set, so we use the first voice.
	var voiceIndex = multilineVars.currentVoice ? multilineVars.currentVoice.staffNum * 100 + multilineVars.currentVoice.index : 0;
	if (multilineVars.inTie[overlayLevel][voiceIndex]) {
		if (el.pitches !== undefined || el.rest.type !== 'spacer')
			return true;
	}
	return false;
};

var el = { };
MusicParser.prototype.parseMusic = function(line) {
	header.resolveTempo();
	//multilineVars.havent_set_length = false;	// To late to set this now.
	multilineVars.is_in_header = false;	// We should have gotten a key header by now, but just in case, this is definitely out of the header.
	var i = 0;
	var startOfLine = multilineVars.iChar;
	// see if there is nothing but a comment on this line. If so, just ignore it. A full line comment is optional white space followed by %
	while (tokenizer.isWhiteSpace(line[i]) && i < line.length)
		i++;
	if (i === line.length || line[i] === '%')
		return;

	// Start with the standard staff, clef and key symbols on each line
	var delayStartNewLine = multilineVars.start_new_line;
	if (multilineVars.continueall === undefined)
		multilineVars.start_new_line = true;
	else
		multilineVars.start_new_line = false;
	var tripletNotesLeft = 0;

	// See if the line starts with a header field
	var retHeader = header.letter_to_body_header(line, i);
	if (retHeader[0] > 0) {
		i += retHeader[0];
		// fixes bug on this: c[V:2]d
		if (retHeader[1] === 'V')
			this.startNewLine();
			// delayStartNewLine = true;
		// TODO-PER: Handle inline headers
	}

	var overlayLevel = 0;
	while (i < line.length)
	{
		var startI = i;
		if (line[i] === '%')
			break;

		var retInlineHeader = header.letter_to_inline_header(line, i, delayStartNewLine);
		if (retInlineHeader[0] > 0) {
			i += retInlineHeader[0];
			//console.log("inline header", retInlineHeader)
			if (retInlineHeader[1] === 'V')
				delayStartNewLine = true; // fixes bug on this: c[V:2]d
			// TODO-PER: Handle inline headers
			//multilineVars.start_new_line = false;
		} else {
			// Wait until here to actually start the line because we know we're past the inline statements.
			if (!tuneBuilder.hasBeginMusic() || (delayStartNewLine && !this.lineContinuation)) {
				this.startNewLine();
				delayStartNewLine = false;
			}

			// We need to decide if the following characters are a bar-marking or a note-group.
			// Unfortunately, that is ambiguous. Both can contain chord symbols and decorations.
			// If there is a grace note either before or after the chord symbols and decorations, then it is definitely a note-group.
			// If there is a bar marker, it is definitely a bar-marking.
			// If there is either a core-note or chord, it is definitely a note-group.
			// So, loop while we find grace-notes, chords-symbols, or decorations. [It is an error to have more than one grace-note group in a row; the others can be multiple]
			// Then, if there is a grace-note, we know where to go.
			// Else see if we have a chord, core-note, slur, triplet, or bar.

			var ret;
			while (1) {
				ret = tokenizer.eatWhiteSpace(line, i);
				if (ret > 0) {
					i += ret;
				}
				if (i > 0 && line[i-1] === '\x12') {
					// there is one case where a line continuation isn't the same as being on the same line, and that is if the next character after it is a header.
					ret = header.letter_to_body_header(line, i);
					if (ret[0] > 0) {
						if (ret[1] === 'V')
							this.startNewLine(); // fixes bug on this: c\\nV:2]\\nd
						// TODO: insert header here
						i = ret[0];
						multilineVars.start_new_line = false;
					}
				}
				// gather all the grace notes, chord symbols and decorations
				ret = letter_to_spacer(line, i);
				if (ret[0] > 0) {
					i += ret[0];
				}

				ret = letter_to_chord(line, i);
				if (ret[0] > 0) {
					// There could be more than one chord here if they have different positions.
					// If two chords have the same position, then connect them with newline.
					if (!el.chord)
						el.chord = [];
					var chordName = tokenizer.translateString(ret[1]);
					chordName = chordName.replace(/;/g, "\n");
					var addedChord = false;
					for (var ci = 0; ci < el.chord.length; ci++) {
						if (el.chord[ci].position === ret[2]) {
							addedChord = true;
							el.chord[ci].name += "\n" + chordName;
						}
					}
					if (addedChord === false) {
						if (ret[2] === null && ret[3])
							el.chord.push({name: chordName, rel_position: ret[3]});
						else
							el.chord.push({name: chordName, position: ret[2]});
					}

					i += ret[0];
					var ii = tokenizer.skipWhiteSpace(line.substring(i));
					if (ii > 0)
						el.force_end_beam_last = true;
					i += ii;
				} else {
					if (nonDecorations.indexOf(line[i]) === -1)
						ret = letter_to_accent(line, i);
					else ret = [ 0 ];
					if (ret[0] > 0) {
						if (ret[1] === null) {
							if (i + 1 < line.length)
								this.startNewLine();	// There was a ! in the middle of the line. Start a new line if there is anything after it.
						} else if (ret[1].length > 0) {
							if (ret[1].indexOf("style=") === 0) {
								el.style = ret[1].substr(6);
							} else {
								if (el.decoration === undefined)
									el.decoration = [];
								if (ret[1] === 'beambr1')
									el.beambr = 1;
								else if (ret[1] === "beambr2")
									el.beambr = 2;
								else el.decoration.push(ret[1]);
							}
						}
						i += ret[0];
					} else {
						ret = letter_to_grace(line, i);
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
			}

			ret = letter_to_bar(line, i);
			if (ret[0] > 0) {
				// This is definitely a bar
				overlayLevel = 0;
				if (el.gracenotes !== undefined) {
					// Attach the grace note to an invisible note
					el.rest = { type: 'spacer' };
					el.duration = 0.125; // TODO-PER: I don't think the duration of this matters much, but figure out if it does.
					multilineVars.addFormattingOptions(el, tune.formatting, 'note');
					tuneBuilder.appendElement('note', startOfLine+i, startOfLine+i+ret[0], el);
					multilineVars.measureNotEmpty = true;
					el = {};
				}
				var bar = {type: ret[1]};
				if (bar.type.length === 0)
					warn("Unknown bar type", line, i);
				else {
					if (multilineVars.inEnding && bar.type !== 'bar_thin') {
						bar.endEnding = true;
						multilineVars.inEnding = false;
					}
					if (ret[2]) {
						bar.startEnding = ret[2];
						if (multilineVars.inEnding)
							bar.endEnding = true;
						multilineVars.inEnding = true;
						if (ret[1] === "bar_right_repeat") {
							// restore the tie and slur state from the start repeat
							multilineVars.restoreStartEndingHoldOvers();
						} else {
							// save inTie, inTieChord
							multilineVars.duplicateStartEndingHoldOvers();
						}
					}
					if (el.decoration !== undefined)
						bar.decoration = el.decoration;
					if (el.chord !== undefined)
						bar.chord = el.chord;
					if (bar.startEnding && multilineVars.barFirstEndingNum === undefined)
						multilineVars.barFirstEndingNum = multilineVars.currBarNumber;
					else if (bar.startEnding && bar.endEnding && multilineVars.barFirstEndingNum)
						multilineVars.currBarNumber = multilineVars.barFirstEndingNum;
					else if (bar.endEnding)
						multilineVars.barFirstEndingNum = undefined;
					if (bar.type !== 'bar_invisible' && multilineVars.measureNotEmpty) {
						if (isFirstVoice()) {
							multilineVars.currBarNumber++;
							if (multilineVars.barNumbers && multilineVars.currBarNumber % multilineVars.barNumbers === 0)
								bar.barNumber = multilineVars.currBarNumber;
						}
					}
					multilineVars.addFormattingOptions(el, tune.formatting, 'bar');
					tuneBuilder.appendElement('bar', startOfLine+startI, startOfLine+i+ret[0], bar);
					multilineVars.measureNotEmpty = false;
					el = {};
				}
				i += ret[0];
			} else if (line[i] === '&') {	// backtrack to beginning of measure
				ret = letter_to_overlay(line, i);
				if (ret[0] > 0) {
					tuneBuilder.appendElement('overlay', startOfLine, startOfLine+1, {});
					i += 1;
					overlayLevel++;
				}

			} else {
				// This is definitely a note group
				//
				// Look for as many open slurs and triplets as there are. (Note: only the first triplet is valid.)
				ret = letter_to_open_slurs_and_triplets(line, i);
				if (ret.consumed > 0) {
					if (ret.startSlur !== undefined)
						el.startSlur = ret.startSlur;
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
				}

				// handle chords.
				if (line[i] === '[') {
					var chordStartChar = i;
					i++;
					var chordDuration = null;
					var rememberEndBeam = false;

					var done = false;
					while (!done) {
						var accent = letter_to_accent(line, i);
						if (accent[0] > 0) {
							i += accent[0];
						}

						var chordNote = getCoreNote(line, i, {}, false);
						if (chordNote !== null && chordNote.pitch !== undefined) {
							if (accent[0] > 0) { // If we found a decoration above, it modifies the entire chord. "style" is handled below.
								if (accent[1].indexOf("style=") !== 0) {
									if (el.decoration === undefined)
										el.decoration = [];
									el.decoration.push(accent[1]);
								}
							}
							if (chordNote.end_beam) {
								el.end_beam = true;
								delete chordNote.end_beam;
							}
							if (el.pitches === undefined) {
								el.duration = chordNote.duration;
								el.pitches = [ chordNote ];
							} else	// Just ignore the note lengths of all but the first note. The standard isn't clear here, but this seems less confusing.
								el.pitches.push(chordNote);
							delete chordNote.duration;
							if (accent[0] > 0) { // If we found a style above, it modifies the individual pitch, not the entire chord.
								if (accent[1].indexOf("style=") === 0) {
									el.pitches[el.pitches.length-1].style = accent[1].substr(6);
								}
							}

							if (multilineVars.inTieChord[el.pitches.length]) {
								chordNote.endTie = true;
								multilineVars.inTieChord[el.pitches.length] = undefined;
							}
							if (chordNote.startTie)
								multilineVars.inTieChord[el.pitches.length] = true;

							i  = chordNote.endChar;
							delete chordNote.endChar;
						} else if (line[i] === ' ') {
							// Spaces are not allowed in chords, but we can recover from it by ignoring it.
							warn("Spaces are not allowed in chords", line, i);
							i++;
						} else {
							if (i < line.length && line[i] === ']') {
								// consume the close bracket
								i++;

								if (multilineVars.next_note_duration !== 0) {
									el.duration = el.duration * multilineVars.next_note_duration;
									multilineVars.next_note_duration = 0;
								}

								if (isInTie(multilineVars,  overlayLevel, el)) {
									el.pitches.forEach(function(pitch) { pitch.endTie = true; });
									setIsInTie(multilineVars,  overlayLevel, false);
								}

								if (tripletNotesLeft > 0 && !(el.rest && el.rest.type === "spacer")) {
									tripletNotesLeft--;
									if (tripletNotesLeft === 0) {
										el.endTriplet = true;
									}
								}

								var postChordDone = false;
								while (i < line.length && !postChordDone) {
									switch (line[i]) {
										case ' ':
										case '\t':
											addEndBeam(el);
											break;
										case ')':
											if (el.endSlur === undefined) el.endSlur = 1; else el.endSlur++;
											break;
										case '-':
											el.pitches.forEach(function(pitch) { pitch.startTie = {}; });
											setIsInTie(multilineVars,  overlayLevel, true);
											break;
										case '>':
										case '<':
											var br2 = getBrokenRhythm(line, i);
											i += br2[0] - 1;	// index gets incremented below, so we'll let that happen
											multilineVars.next_note_duration = br2[2];
											if (chordDuration)
												chordDuration = chordDuration * br2[1];
											else
												chordDuration = br2[1];
											break;
										case '1':
										case '2':
										case '3':
										case '4':
										case '5':
										case '6':
										case '7':
										case '8':
										case '9':
										case '/':
											var fraction = tokenizer.getFraction(line, i);
											chordDuration = fraction.value;
											i = fraction.index;
											var ch = line[i]
											if (ch === ' ')
												rememberEndBeam = true;
											if (ch === '-' || ch === ')' || ch === ' ' || ch === '<' || ch === '>')
												i--; // Subtracting one because one is automatically added below
											else
												postChordDone = true;
											break;
										case '0':
											chordDuration = 0;
											break;
										default:
											postChordDone = true;
											break;
									}
									if (!postChordDone) {
										i++;
									}
								}
							} else
								warn("Expected ']' to end the chords", line, i);

							if (el.pitches !== undefined) {
								if (chordDuration !== null) {
									el.duration = el.duration * chordDuration;
									if (rememberEndBeam)
										addEndBeam(el);
								}

								multilineVars.addFormattingOptions(el, tune.formatting, 'note');
								tuneBuilder.appendElement('note', startOfLine+startI, startOfLine+i, el);
								multilineVars.measureNotEmpty = true;
								el = {};
							}
							done = true;
						}
					}

				} else {
					// Single pitch
					var el2 = {};
					var core = getCoreNote(line, i, el2, true);
					if (el2.endTie !== undefined) setIsInTie(multilineVars,  overlayLevel, true);
					if (core !== null) {
						if (core.pitch !== undefined) {
							el.pitches = [ { } ];
							// TODO-PER: straighten this out so there is not so much copying: getCoreNote shouldn't change e'
							if (core.accidental !== undefined) el.pitches[0].accidental = core.accidental;
							el.pitches[0].pitch = core.pitch;
							el.pitches[0].name = core.name;
							if (core.midipitch || core.midipitch === 0)
								el.pitches[0].midipitch = core.midipitch;
							if (core.endSlur !== undefined) el.pitches[0].endSlur = core.endSlur;
							if (core.endTie !== undefined) el.pitches[0].endTie = core.endTie;
							if (core.startSlur !== undefined) el.pitches[0].startSlur = core.startSlur;
							if (el.startSlur !== undefined) el.pitches[0].startSlur = el.startSlur;
							if (el.dottedSlur !== undefined) el.pitches[0].dottedSlur = true;
							if (core.startTie !== undefined) el.pitches[0].startTie = core.startTie;
							if (el.startTie !== undefined) el.pitches[0].startTie = el.startTie;
						} else {
							el.rest = core.rest;
							if (core.rest.type === 'multimeasure' && isFirstVoice())
								multilineVars.currBarNumber += core.rest.text - 1 // The minus one is because the measure with the rest is already counted once normally.
							if (core.endSlur !== undefined) el.endSlur = core.endSlur;
							if (core.endTie !== undefined) el.rest.endTie = core.endTie;
							if (core.startSlur !== undefined) el.startSlur = core.startSlur;
							if (core.startTie !== undefined) el.rest.startTie = core.startTie;
							if (el.startTie !== undefined) el.rest.startTie = el.startTie;
						}

						if (core.chord !== undefined) el.chord = core.chord;
						if (core.duration !== undefined) el.duration = core.duration;
						if (core.decoration !== undefined) el.decoration = core.decoration;
						if (core.graceNotes !== undefined) el.graceNotes = core.graceNotes;
						delete el.startSlur;
						delete el.dottedSlur;
						if (isInTie(multilineVars,  overlayLevel, el)) {
							if (el.pitches !== undefined) {
								el.pitches[0].endTie = true;
							} else if (el.rest.type !== 'spacer') {
								el.rest.endTie = true;
							}
							setIsInTie(multilineVars,  overlayLevel, false);
						}
						if (core.startTie || el.startTie)
							setIsInTie(multilineVars,  overlayLevel, true);
						i  = core.endChar;

						if (tripletNotesLeft > 0 && !(core.rest && core.rest.type === "spacer")) {
							tripletNotesLeft--;
							if (tripletNotesLeft === 0) {
								el.endTriplet = true;
							}
						}

						if (core.end_beam)
							addEndBeam(el);

						// If there is a whole rest, then it should be the duration of the measure, not it's own duration. We need to special case it.
						// If the time signature length is greater than 4/4, though, then a whole rest has no special treatment.
						if (el.rest && el.rest.type === 'rest' && el.duration === 1 && durationOfMeasure(multilineVars) <= 1) {
							el.rest.type = 'whole';

							el.duration = durationOfMeasure(multilineVars);
						}

						// Create a warning if this is not a displayable duration.
						// The first item on a line is a regular note value, each item after that represents a dot placed after the previous note.
						// Only durations less than a whole note are tested because whole note durations have some tricky rules.

						if (el.duration < 1 && durations.indexOf(el.duration) === -1 && el.duration !== 0) {
							if (!el.rest || el.rest.type !== 'spacer')
								warn("Duration not representable: " + line.substring(startI, i), line, i);
						}

						multilineVars.addFormattingOptions(el, tune.formatting, 'note');
						var succeeded = tuneBuilder.appendElement('note', startOfLine+startI, startOfLine+i, el);
						if (!succeeded) {
							this.startNewLine()
							tuneBuilder.appendElement('note', startOfLine+startI, startOfLine+i, el);
						}
						multilineVars.measureNotEmpty = true;
						el = {};
					}
				}

				if (i === startI) {	// don't know what this is, so ignore it.
					if (line[i] !== ' ' && line[i] !== '`')
						warn("Unknown character ignored", line, i);
					i++;
				}
			}
		}
	}
	this.lineContinuation = line.indexOf('\x12') >= 0 || (retHeader[0] > 0)
	if (!this.lineContinuation) { el = { } }
};

var setIsInTie =function(multilineVars, overlayLevel, value) {
	// If this is single voice music then the voice index isn't set, so we use the first voice.
	var voiceIndex = multilineVars.currentVoice ? multilineVars.currentVoice.staffNum * 100 + multilineVars.currentVoice.index : 0;
	if (multilineVars.inTie[overlayLevel] === undefined)
		multilineVars.inTie[overlayLevel] = [];
	multilineVars.inTie[overlayLevel][voiceIndex] = value;
};

var letter_to_chord = function(line, i) {
	if (line[i] === '"')
	{
		var chord = tokenizer.getBrackettedSubstring(line, i, 5);
		if (!chord[2])
			warn("Missing the closing quote while parsing the chord symbol", line , i);
		// If it starts with ^, then the chord appears above.
		// If it starts with _ then the chord appears below.
		// (note that the 2.0 draft standard defines them as not chords, but annotations and also defines @.)
		if (chord[0] > 0 && chord[1].length > 0 && chord[1][0] === '^') {
			chord[1] = chord[1].substring(1);
			chord[2] = 'above';
		} else if (chord[0] > 0 && chord[1].length > 0 && chord[1][0] === '_') {
			chord[1] = chord[1].substring(1);
			chord[2] = 'below';
		} else if (chord[0] > 0 && chord[1].length > 0 && chord[1][0] === '<') {
			chord[1] = chord[1].substring(1);
			chord[2] = 'left';
		} else if (chord[0] > 0 && chord[1].length > 0 && chord[1][0] === '>') {
			chord[1] = chord[1].substring(1);
			chord[2] = 'right';
		} else if (chord[0] > 0 && chord[1].length > 0 && chord[1][0] === '@') {
		      // @-15,5.7		
		      chord[1] = chord[1].substring(1);
		      var x = tokenizer.getFloat(chord[1]);
		      if (x.digits === 0){
			warn("Missing first position in absolutely positioned annotation.", line, i);
			chord[1] = chord[1].replace("@","");
			chord[2] = 'above';
			return chord;
		      }
		      chord[1] = chord[1].substring(x.digits);
		      if (chord[1][0] !== ','){
			warn("Missing comma absolutely positioned annotation.", line, i);
			chord[1] = chord[1].replace("@","");
			chord[2] = 'above';
			return chord;
		      }
		      chord[1] = chord[1].substring(1);
		      var y = tokenizer.getFloat(chord[1]);
		      if (y.digits === 0){
			warn("Missing second position in absolutely positioned annotation.", line, i);
			chord[1] = chord[1].replace("@","");
			chord[2] = 'above';
			return chord;
		      }
		      chord[1] = chord[1].substring(y.digits);
		      var ws = tokenizer.skipWhiteSpace(chord[1]);
		      chord[1] = chord[1].substring(ws);
		      chord[2] = null;
		      chord[3] = {
			x: x.value,
			y: y.value
		      };	
		} else {
			if (multilineVars.freegchord !== true) {
				chord[1] = chord[1].replace(/([ABCDEFG0-9])b/g, "$1♭");
				chord[1] = chord[1].replace(/([ABCDEFG0-9])#/g, "$1♯");
				chord[1] = chord[1].replace(/^([ABCDEFG])([♯♭]?)o([^A-Za-z])/g, "$1$2°$3");
				chord[1] = chord[1].replace(/^([ABCDEFG])([♯♭]?)o$/g, "$1$2°");
				chord[1] = chord[1].replace(/^([ABCDEFG])([♯♭]?)0([^A-Za-z])/g, "$1$2ø$3");
				chord[1] = chord[1].replace(/^([ABCDEFG])([♯♭]?)\^([^A-Za-z])/g, "$1$2∆$3");
			}
			chord[2] = 'default';
			chord[1] = transpose.chordName(multilineVars, chord[1]);
		}
		return chord;
	}
	return [0, ""];
};

var letter_to_grace =  function(line, i) {
	// Grace notes are an array of: startslur, note, endslur, space; where note is accidental, pitch, duration
	if (line[i] === '{') {
		// fetch the gracenotes string and consume that into the array
		var gra = tokenizer.getBrackettedSubstring(line, i, 1, '}');
		if (!gra[2])
			warn("Missing the closing '}' while parsing grace note", line, i);
		// If there is a slur after the grace construction, then move it to the last note inside the grace construction
		if (line[i+gra[0]] === ')') {
			gra[0]++;
			gra[1] += ')';
		}

		var gracenotes = [];
