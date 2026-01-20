		var ii = 0;
		var inTie = false;
		while (ii < gra[1].length) {
			var acciaccatura = false;
			if (gra[1][ii] === '/') {
				acciaccatura = true;
				ii++;
			}
			var note = getCoreNote(gra[1], ii, {}, false);
			if (note !== null) {
				// The grace note durations should not be affected by the default length: they should be based on 1/16, so if that isn't the default, then multiply here.
				note.duration = note.duration / (multilineVars.default_length * 8);
				if (acciaccatura)
					note.acciaccatura = true;
				if (note.rest) {
					// don't allow rests inside gracenotes
					warn("Rests not allowed as grace notes '" + gra[1][ii] + "' while parsing grace note", line, i);
				} else
					gracenotes.push(note);

				if (inTie) {
					note.endTie = true;
					inTie = false;
				}
				if (note.startTie)
					inTie = true;

				ii  = note.endChar;
				delete note.endChar;

				if (note.end_beam) {
					note.endBeam = true;
					delete note.end_beam;
				}
			}
			else {
				// We shouldn't get anything but notes or a space here, so report an error
				if (gra[1][ii] === ' ') {
					if (gracenotes.length > 0)
						gracenotes[gracenotes.length-1].endBeam = true;
				} else
					warn("Unknown character '" + gra[1][ii] + "' while parsing grace note", line, i);
				ii++;
			}
		}
		if (gracenotes.length)
			return [gra[0], gracenotes];
	}
	return [ 0 ];
};

function letter_to_overlay(line, i) {
	if (line[i] === '&') {
		var start = i;
		while (line[i] && line[i] !== ':' && line[i] !== '|')
			i++;
		return [ i-start, line.substring(start+1, i) ];
	}
	return [ 0 ];
}

function durationOfMeasure(multilineVars) {
	// TODO-PER: This could be more complicated if one of the unusual measures is used.
	var meter = multilineVars.origMeter;
	if (!meter || meter.type !== 'specified')
		return 1;
	if (!meter.value || meter.value.length === 0)
		return 1;
	return parseInt(meter.value[0].num, 10) / parseInt(meter.value[0].den, 10);
}




var letter_to_accent = function(line, i) {
	var macro = multilineVars.macros[line[i]];

	if (macro !== undefined) {
		if (macro[0] === '!' || macro[0] === '+')
			macro = macro.substring(1);
		if (macro[macro.length-1] === '!' || macro[macro.length-1] === '+')
			macro = macro.substring(0, macro.length-1);
		if (legalAccents.includes(macro))
			return [ 1, macro ];
		else if (volumeDecorations.includes(macro)) {
			if (multilineVars.volumePosition === 'hidden')
				macro = "";
			return [1, macro];
		} else if (dynamicDecorations.includes(macro)) {
			if (multilineVars.dynamicPosition === 'hidden')
				macro = "";
			return [1, macro];
		} else {
			if (!multilineVars.ignoredDecorations.includes(macro))
				warn("Unknown macro: " + macro, line, i);
			return [1, '' ];
		}
	}
	switch (line[i])
	{
		case '.':
			if (line[i+1] === '(' || line[i+1] === '-') // a dot then open paren is a dotted slur; likewise dot dash is dotted tie.
				break;
			return [1, 'staccato'];
		case 'u':return [1, 'upbow'];
		case 'v':return [1, 'downbow'];
		case '~':return [1, 'irishroll'];
		case '!':
		case '+':
			var ret = tokenizer.getBrackettedSubstring(line, i, 5);
			// Be sure that the accent is recognizable.
			if (ret[1].length > 1 && (ret[1][0] === '^' || ret[1][0] ==='_'))
				ret[1] = ret[1].substring(1);	// TODO-PER: The test files have indicators forcing the ornament to the top or bottom, but that isn't in the standard. We'll just ignore them.
			if (legalAccents.includes(ret[1]))
				return ret;
			if (volumeDecorations.includes(ret[1])) {
				if (multilineVars.volumePosition === 'hidden' )
					ret[1] = '';
				return ret;
			}
			if (dynamicDecorations.includes(ret[1])) {
				if (multilineVars.dynamicPosition === 'hidden' )
					ret[1] = '';
				return ret;
			}

			var ind = accentPseudonyms.findIndex(function (acc) { return ret[1] === acc[0]})
			if (ind >= 0) {
				ret[1] = accentPseudonyms[ind][1];
				return ret;
			}

			ind = accentDynamicPseudonyms.findIndex(function (acc) { return ret[1] === acc[0]})
			if (ind >= 0) {
				ret[1] = accentDynamicPseudonyms[ind][1];
				if (multilineVars.dynamicPosition === 'hidden' )
					ret[1] = '';
				return ret;
			}

			// We didn't find the accent in the list, so consume the space, but don't return an accent.
			// Although it is possible that ! was used as a line break, so accept that.
			if (line[i] === '!' && (ret[0] === 1 || line[i+ret[0]-1] !== '!'))
				return [1, null ];
			warn("Unknown decoration: " + ret[1], line, i);
			ret[1] = "";
			return ret;
		case 'H':return [1, 'fermata'];
		case 'J':return [1, 'slide'];
		case 'L':return [1, 'accent'];
		case 'M':return [1, 'mordent'];
		case 'O':return[1, 'coda'];
		case 'P':return[1, 'pralltriller'];
		case 'R':return [1, 'roll'];
		case 'S':return [1, 'segno'];
		case 'T':return [1, 'trill'];
		case 't':return [1, 'trillh'];
		
	}
	return [0, 0];
};

var letter_to_spacer = function(line, i) {
	var start = i;
	while (tokenizer.isWhiteSpace(line[i]))
		i++;
	return [ i-start ];
};

// returns the class of the bar line
// the number of the repeat
// and the number of characters used up
// if 0 is returned, then the next element was not a bar line
var letter_to_bar = function(line, curr_pos) {
	var ret = tokenizer.getBarLine(line, curr_pos);
	if (ret.len === 0)
		return [0,""];
	if (ret.warn) {
		warn(ret.warn, line, curr_pos);
		return [ret.len,""];
	}

	// Now see if this is a repeated ending
	// A repeated ending is all of the characters 1,2,3,4,5,6,7,8,9,0,-, and comma
	// It can also optionally start with '[', which is ignored.
	// Also, it can have white space before the '['.
	for (var ws = 0; ws < line.length; ws++)
		if (line[curr_pos + ret.len + ws] !== ' ')
			break;
	var orig_bar_len = ret.len;
	if (line[curr_pos+ret.len+ws] === '[') {
		ret.len += ws + 1;
	}

	// It can also be a quoted string. It is unclear whether that construct requires '[', but it seems like it would. otherwise it would be confused with a regular chord.
	if (line[curr_pos+ret.len] === '"' && line[curr_pos+ret.len-1] === '[') {
		var ending = tokenizer.getBrackettedSubstring(line, curr_pos+ret.len, 5);
		return [ret.len+ending[0], ret.token, ending[1]];
	}
	var retRep = tokenizer.getTokenOf(line.substring(curr_pos+ret.len), "1234567890-,");
	if (retRep.len === 0 || retRep.token[0] === '-')
		return [orig_bar_len, ret.token];

	return [ret.len+retRep.len, ret.token, retRep.token];
};

var letter_to_open_slurs_and_triplets =  function(line, i) {
	// consume spaces, and look for all the open parens. If there is a number after the open paren,
	// that is a triplet. Otherwise that is a slur. Collect all the slurs and the first triplet.
	var ret = {};
	var start = i;
	if (line[i] === '.' && line[i+1] === '(') {
		ret.dottedSlur = true;
		i++;
	}
	while (line[i] === '(' || tokenizer.isWhiteSpace(line[i])) {
		if (line[i] === '(') {
			if (i+1 < line.length && (line[i+1] >= '2' && line[i+1] <= '9')) {
				if (ret.triplet !== undefined)
					warn("Can't nest triplets", line, i);
				else {
					ret.triplet = line[i+1] - '0';
					ret.tripletQ = tripletQ[ret.triplet];
					ret.num_notes = ret.triplet;
					if (i+2 < line.length && line[i+2] === ':') {
						// We are expecting "(p:q:r" or "(p:q" or "(p::r"
						// That is: "put p notes into the time of q for the next r notes"
						// if r is missing, then it is equal to p.
						// if q is missing, it is determined from this table:
						// (2 notes in the time of 3
						// (3 notes in the time of 2
						// (4 notes in the time of 3
						// (5 notes in the time of n | if time sig is (6/8, 9/8, 12/8), n=3, else n=2
						// (6 notes in the time of 2
						// (7 notes in the time of n
						// (8 notes in the time of 3
						// (9 notes in the time of n
						if (i+3 < line.length && line[i+3] === ':') {
							// The second number, 'q', is not present.
							if (i+4 < line.length && (line[i+4] >= '1' && line[i+4] <= '9')) {
								ret.num_notes = line[i+4] - '0';
								i += 3;
							} else
								warn("expected number after the two colons after the triplet to mark the duration", line, i);
						} else if (i+3 < line.length && (line[i+3] >= '1' && line[i+3] <= '9')) {
							ret.tripletQ = line[i+3] - '0';
							if (i+4 < line.length && line[i+4] === ':') {
								if (i+5 < line.length && (line[i+5] >= '1' && line[i+5] <= '9')) {
									ret.num_notes = line[i+5] - '0';
									i += 4;
								}
							} else {
								i += 2;
							}
						} else
							warn("expected number after the triplet to mark the duration", line, i);
					}
				}
				i++;
			}
			else {
				if (ret.startSlur === undefined)
					ret.startSlur = 1;
				else
					ret.startSlur++;
			}
		}
		i++;
	}
	ret.consumed = i-start;
	return ret;
};

MusicParser.prototype.startNewLine = function() {
	var params = { startChar: -1, endChar: -1};
	if (multilineVars.partForNextLine.title)
		params.part = multilineVars.partForNextLine;
	params.clef = multilineVars.currentVoice && multilineVars.staves[multilineVars.currentVoice.staffNum].clef !== undefined ? Object.assign({},multilineVars.staves[multilineVars.currentVoice.staffNum].clef) : Object.assign({},multilineVars.clef);
	var scoreTranspose = multilineVars.currentVoice ? multilineVars.currentVoice.scoreTranspose : 0;
	params.key = parseKeyVoice.standardKey(multilineVars.key.root+multilineVars.key.acc+multilineVars.key.mode, multilineVars.key.root, multilineVars.key.acc, scoreTranspose);
	params.key.mode = multilineVars.key.mode;
	if (multilineVars.key.impliedNaturals)
		params.key.impliedNaturals = multilineVars.key.impliedNaturals;
	if (multilineVars.key.explicitAccidentals) {
		for (var i = 0; i < multilineVars.key.explicitAccidentals.length; i++) {
			var found = false;
			for (var j = 0; j < params.key.accidentals.length; j++) {
				if (params.key.accidentals[j].note === multilineVars.key.explicitAccidentals[i].note) {
					// If the note is already in the list, override it with the new value
					params.key.accidentals[j].acc = multilineVars.key.explicitAccidentals[i].acc;
					found = true;
				}
			}
			if (!found)
				params.key.accidentals.push(multilineVars.key.explicitAccidentals[i]);
		}
	}
	multilineVars.targetKey = params.key;
	if (params.key.explicitAccidentals)
		delete params.key.explicitAccidentals;
	parseKeyVoice.addPosToKey(params.clef, params.key);
	if (multilineVars.meter !== null) {
		if (multilineVars.currentVoice) {
			multilineVars.staves.forEach(function(st) {
				st.meter = multilineVars.meter;
			});
			params.meter = multilineVars.staves[multilineVars.currentVoice.staffNum].meter;
			multilineVars.staves[multilineVars.currentVoice.staffNum].meter = null;
		} else
			params.meter = multilineVars.meter;
		multilineVars.meter = null;
	} else if (multilineVars.currentVoice && multilineVars.staves[multilineVars.currentVoice.staffNum].meter) {
		// Make sure that each voice gets the meter marking.
		params.meter = multilineVars.staves[multilineVars.currentVoice.staffNum].meter;
		multilineVars.staves[multilineVars.currentVoice.staffNum].meter = null;
	}
	if (multilineVars.currentVoice && multilineVars.currentVoice.name)
		params.name = multilineVars.currentVoice.name;
	if (multilineVars.vocalfont)
		params.vocalfont = multilineVars.vocalfont;
	if (multilineVars.tripletfont)
		params.tripletfont = multilineVars.tripletfont;
	if (multilineVars.gchordfont)
		params.gchordfont = multilineVars.gchordfont;
	if (multilineVars.style)
		params.style = multilineVars.style;
	if (multilineVars.currentVoice) {
		var staff = multilineVars.staves[multilineVars.currentVoice.staffNum];
		if (staff.brace) params.brace = staff.brace;
		if (staff.bracket) params.bracket = staff.bracket;
		if (staff.connectBarLines) params.connectBarLines = staff.connectBarLines;
		if (staff.name) params.name = staff.name[multilineVars.currentVoice.index];
		if (staff.subname) params.subname = staff.subname[multilineVars.currentVoice.index];
		if (multilineVars.currentVoice.stem)
			params.stem = multilineVars.currentVoice.stem;
		if (multilineVars.currentVoice.stafflines)
			params.stafflines = multilineVars.currentVoice.stafflines;
		if (multilineVars.currentVoice.staffscale)
			params.staffscale = multilineVars.currentVoice.staffscale;
		if (multilineVars.currentVoice.scale)
			params.scale = multilineVars.currentVoice.scale;
		if (multilineVars.currentVoice.color)
			params.color = multilineVars.currentVoice.color;
		if (multilineVars.currentVoice.style)
			params.style = multilineVars.currentVoice.style;
		if (multilineVars.currentVoice.transpose)
			params.clef.transpose = multilineVars.currentVoice.transpose;
		params.currentVoice = multilineVars.currentVoice
		var voices = Object.keys(multilineVars.voices)
		for (var mv = 0; mv < voices.length; mv++) {
			if (params.currentVoice.staffNum === multilineVars.voices[voices[mv]].staffNum && params.currentVoice.index === multilineVars.voices[voices[mv]].index)
				params.currentVoiceName = voices[mv]
		}
	}
	if (multilineVars.barNumbers === 0 && isFirstVoice() && multilineVars.currBarNumber !== 1)
		params.barNumber = multilineVars.currBarNumber;
	tuneBuilder.startNewLine(params);
	if (multilineVars.key.impliedNaturals)
		delete multilineVars.key.impliedNaturals;

	multilineVars.partForNextLine = {};
	if (multilineVars.tempoForNextLine.length === 4)
		tuneBuilder.appendElement(multilineVars.tempoForNextLine[0],multilineVars.tempoForNextLine[1],multilineVars.tempoForNextLine[2],multilineVars.tempoForNextLine[3]);
	multilineVars.tempoForNextLine = [];
}

// TODO-PER: make this a method in el.
var addEndBeam = function(el) {
	if (el.duration !== undefined && el.duration < 0.25)
		el.end_beam = true;
	return el;
};

var getCoreNote = function(line, index, el, canHaveBrokenRhythm) {
	//var el = { startChar: index };
	var isComplete = function(state) {
		return (state === 'octave' || state === 'duration' || state === 'Zduration' || state === 'broken_rhythm' || state === 'end_slur');
	};
	var dottedTie;
	if (line[index] === '.' && line[index+1] === '-') {
		dottedTie = true;
		index++;
	}
	var state = 'startSlur';
	var durationSetByPreviousNote = false;
	while (1) {
		switch(line[index]) {
			case '(':
				if (state === 'startSlur') {
					if (el.startSlur === undefined) el.startSlur = 1; else el.startSlur++;
				} else if (isComplete(state)) {el.endChar = index;return el;}
				else return null;
				break;
			case ')':
				if (isComplete(state)) {
					if (el.endSlur === undefined) el.endSlur = 1; else el.endSlur++;
				} else return null;
				break;
			case '^':
				if (state === 'startSlur') {el.accidental = 'sharp';state = 'sharp2';}
				else if (state === 'sharp2') {el.accidental = 'dblsharp';state = 'pitch';}
				else if (isComplete(state)) {el.endChar = index;return el;}
				else return null;
				break;
			case '_':
				if (state === 'startSlur') {el.accidental = 'flat';state = 'flat2';}
				else if (state === 'flat2') {el.accidental = 'dblflat';state = 'pitch';}
				else if (isComplete(state)) {el.endChar = index;return el;}
				else return null;
				break;
			case '=':
				if (state === 'startSlur') {el.accidental = 'natural';state = 'pitch';}
				else if (isComplete(state)) {el.endChar = index;return el;}
				else return null;
				break;
			case 'A':
			case 'B':
			case 'C':
			case 'D':
			case 'E':
			case 'F':
			case 'G':
			case 'a':
			case 'b':
			case 'c':
			case 'd':
			case 'e':
			case 'f':
			case 'g':
				if (state === 'startSlur' || state === 'sharp2' || state === 'flat2' || state === 'pitch') {
					el.pitch = pitches[line[index]];
					el.pitch += 7 * (multilineVars.currentVoice && multilineVars.currentVoice.octave !== undefined ? multilineVars.currentVoice.octave : multilineVars.octave);
					el.name = line[index];
					if (el.accidental)
						el.name = accMap[el.accidental] + el.name;
					transpose.note(multilineVars, el);
					state = 'octave';
					// At this point we have a valid note. The rest is optional. Set the duration in case we don't get one below
					if (canHaveBrokenRhythm && multilineVars.next_note_duration !== 0) {
						el.duration = multilineVars.default_length * multilineVars.next_note_duration;
						multilineVars.next_note_duration = 0;
						durationSetByPreviousNote = true;
					} else
						el.duration = multilineVars.default_length;
					// If the clef is percussion, there is probably some translation of the pitch to a particular drum kit item.
					if ((multilineVars.clef && multilineVars.clef.type === "perc") ||
						(multilineVars.currentVoice && multilineVars.currentVoice.clef === "perc")) {
						var key = line[index];
						if (el.accidental) {
							key = accMap[el.accidental] + key;
						}
						if (tune.formatting && tune.formatting.midi && tune.formatting.midi.drummap)
						el.midipitch = tune.formatting.midi.drummap[key];
					}
				} else if (isComplete(state)) {el.endChar = index;return el;}
				else return null;
				break;
			case ',':
				if (state === 'octave') {el.pitch -= 7; el.name += ','; }
				else if (isComplete(state)) {el.endChar = index;return el;}
				else return null;
				break;
			case '\'':
				if (state === 'octave') {el.pitch += 7; el.name += "'";  }
				else if (isComplete(state)) {el.endChar = index;return el;}
				else return null;
				break;
			case 'x':
			case 'X':
			case 'y':
			case 'z':
			case 'Z':
				if (state === 'startSlur') {
					el.rest = { type: rests[line[index]] };
					// There shouldn't be some of the properties that notes have. If some sneak in due to bad syntax in the abc file,
					// just nix them here.
					delete el.accidental;
					delete el.startSlur;
					delete el.startTie;
					delete el.endSlur;
					delete el.endTie;
					delete el.end_beam;
					delete el.grace_notes;
					// At this point we have a valid note. The rest is optional. Set the duration in case we don't get one below
					if (el.rest.type.indexOf('multimeasure') >= 0) {
						el.duration = tune.getBarLength();
						el.rest.text = 1;
						state = 'Zduration';
					} else {
						if (canHaveBrokenRhythm && multilineVars.next_note_duration !== 0) {
							el.duration = multilineVars.default_length * multilineVars.next_note_duration;
							multilineVars.next_note_duration = 0;
							durationSetByPreviousNote = true;
						} else
							el.duration = multilineVars.default_length;
						state = 'duration';
					}
				} else if (isComplete(state)) {el.endChar = index;return el;}
				else return null;
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
			case '0':
			case '/':
				if (state === 'octave' || state === 'duration') {
					var fraction = tokenizer.getFraction(line, index);
					//if (!durationSetByPreviousNote)
					el.duration = el.duration * fraction.value;
					// TODO-PER: We can test the returned duration here and give a warning if it isn't the one expected.
					el.endChar = fraction.index;
					while (fraction.index < line.length && (tokenizer.isWhiteSpace(line[fraction.index]) || line[fraction.index] === '-')) {
						if (line[fraction.index] === '-')
							el.startTie = {};
						else
							el = addEndBeam(el);
						fraction.index++;
					}
					index = fraction.index-1;
					state = 'broken_rhythm';
				} else if (state === 'sharp2') {
					el.accidental = 'quartersharp';state = 'pitch';
				} else if (state === 'flat2') {
					el.accidental = 'quarterflat';state = 'pitch';
				} else if (state === 'Zduration') {
					var num = tokenizer.getNumber(line, index);
					el.duration = num.num * tune.getBarLength();
					el.rest.text = num.num;
					el.endChar = num.index;
					return el;
				} else return null;
				break;
			case '-':
				if (state === 'startSlur') {
					// This is the first character, so it must have been meant for the previous note. Correct that here.
					tuneBuilder.addTieToLastNote(dottedTie);
					el.endTie = true;
				} else if (state === 'octave' || state === 'duration' || state === 'end_slur') {
					el.startTie = {};
					if (!durationSetByPreviousNote && canHaveBrokenRhythm)
						state = 'broken_rhythm';
					else {
						// Peek ahead to the next character. If it is a space, then we have an end beam.
						if (tokenizer.isWhiteSpace(line[index + 1]))
							addEndBeam(el);
						el.endChar = index+1;
						return el;
					}
				} else if (state === 'broken_rhythm') {el.endChar = index;return el;}
				else return null;
				break;
			case ' ':
			case '\t':
				if (isComplete(state)) {
					el.end_beam = true;
					// look ahead to see if there is a tie
					dottedTie = false;
					do {
						if (line[index] === '.' && line[index+1] === '-') {
							dottedTie = true;
							index++;
						}
						if (line[index] === '-') {
							el.startTie = {};
							if (dottedTie)
								el.startTie.style = "dotted";
						}
						index++;
					} while (index < line.length &&
						(tokenizer.isWhiteSpace(line[index]) || line[index] === '-') ||
						(line[index] === '.' && line[index+1] === '-'));
					el.endChar = index;
					if (!durationSetByPreviousNote && canHaveBrokenRhythm && (line[index] === '<' || line[index] === '>')) {	// TODO-PER: Don't need the test for < and >, but that makes the endChar work out for the regression test.
						index--;
						state = 'broken_rhythm';
					} else
						return el;
				}
				else return null;
				break;
			case '>':
			case '<':
				if (isComplete(state)) {
					if (canHaveBrokenRhythm) {
						var br2 = getBrokenRhythm(line, index);
						index += br2[0] - 1;	// index gets incremented below, so we'll let that happen
						multilineVars.next_note_duration = br2[2];
						el.duration = br2[1]*el.duration;
						state = 'end_slur';
					} else {
						el.endChar = index;
						return el;
					}
				} else
					return null;
				break;
			default:
				if (isComplete(state)) {
					el.endChar = index;
					return el;
				}
				return null;
		}
		index++;
		if (index === line.length) {
			if (isComplete(state)) {el.endChar = index;return el;}
			else return null;
		}
	}
	return null;
};

var getBrokenRhythm = function(line, index) {
	switch (line[index]) {
		case '>':
			if (index < line.length - 2 && line[index + 1] === '>' && line[index + 2] === '>')	// triple >>>
				return [3, 1.875, 0.125];
			else if (index < line.length - 1 && line[index + 1] === '>')	// double >>
				return [2, 1.75, 0.25];
			else
				return [1, 1.5, 0.5];
		case '<':
			if (index < line.length - 2 && line[index + 1] === '<' && line[index + 2] === '<')	// triple <<<
				return [3, 0.125, 1.875];
			else if (index < line.length - 1 && line[index + 1] === '<')	// double <<
				return [2, 0.25, 1.75];
			else
				return [1, 0.5, 1.5];
	}
	return null;
};

function isFirstVoice() {
	return multilineVars.currentVoice === undefined || (multilineVars.currentVoice.staffNum ===  0 && multilineVars.currentVoice.index ===  0);
}

module.exports = MusicParser;
