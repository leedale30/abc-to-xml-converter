Machine‑readable (for your vibe coder / ABC generator)

Musically meaningful (so the creative AI composer understands why and how to use each command)

So here is exactly that:
A compact, coder‑friendly table where each ABC+ command has:

Function (what the code does)

Musical meaning (why a composer would choose it)

MusicXML target (what it becomes in notation software)

This is the version you can feed directly into a rule‑based system and an algorithmic composer.

🎼 ABC+ Command Dictionary for Algorithmic Composition & Code Parsing
Machine‑friendly + musically meaningful + MusicXML‑aligned

1. Articulations
These modify the attack or shape of a note.

ABC+ Function (Coder) Musical Meaning (Composer) MusicXML
!staccato! Mark note as short Light, detached playing 
!tenuto! Mark note as held Smooth, full‑value emphasis 
!accent! Add accent Strong attack 
!marcato! Add strong accent Very forceful attack 
!pizz! Set technique=pizz Plucked string sound 
!arco! Set technique=arco Return to bowing 
!mute! Set technique=mute Softer, filtered tone 
!open! Set technique=open Open string/brass 
!harmonic! Set technique=harmonic Flute‑like overtone 
2. Dynamics
These affect loudness and expressive shape.

ABC+ Function Musical Meaning MusicXML
!p! dynamic=p Soft 
!mp! dynamic=mp Moderately soft 
!mf! dynamic=mf Moderately loud 
!f! dynamic=f Loud 
!ff! dynamic=ff Very loud 
!subito-p! sudden dynamic drop Dramatic soft entry 

+ subito text
!subito-f! sudden dynamic rise Dramatic loud entry + subito text
!cresc(start)! start crescendo Gradually louder 
!cresc(end)! end crescendo End of swell 
!dim(start)! start diminuendo Gradually softer 
!dim(end)! end diminuendo End of fade 

3. Placement / Positioning
These tell the engraving engine where to place text/dynamics.

ABC+ Function Musical Meaning MusicXML
!p@above! place dynamic above Emphasize conductor visibility placement="above"
!f@below! place dynamic below Useful for lower staves placement="below"
!text("sul G")@above! text above Technique instruction 
!text("dolce")@x=10,y=20! absolute offset Fine engraving control 
4. Slurs
These define phrasing and legato.

ABC+ Function Musical Meaning MusicXML
(1slur-start start slur #1 Begin phrase 
(1slur-end end slur #1 End phrase 
(2slur-start nested slur Sub‑phrase 
(2slur-end end nested End sub‑phrase 
5. Beam Grouping
Controls rhythmic grouping.

ABC+ Function Musical Meaning MusicXML
%%beam begin force beam start Group notes visually begin
%%beam end force beam end End grouping end
6. Tuplets
Defines irregular rhythmic groups.

ABC+ Function Musical Meaning MusicXML
(3:2 tuplet-start start tuplet 3 notes in time of 2 
tuplet-end end tuplet End grouping 
7. Layout & Engraving
These affect visual structure, not sound.

ABC+ Function Musical Meaning MusicXML
%%system-break new system New line of music 
%%page-break new page Page turn 
%%staff-spacing N staff distance Vertical spacing 
%%measure-numbering on show bar numbers Conductor clarity 
%%hide-rests hide rests Cue notation none
%%cue-size on small notes Cue notes 
%%transpose N transposition Instrument transposition 
8. Instrument Metadata
Helps the composer AI choose appropriate timbres.

ABC+ Function Musical Meaning MusicXML
%%instrument V1 violin set instrument Choose timbre 
%%midi-program V1 41 GM program Playback sound 
%%sound V1 strings.violin sound ID Detailed timbre 
9. Percussion Mapping
Defines drum kit layout.

ABC+ Function Musical Meaning MusicXML
%%perc V3 hi-hat x map hi‑hat Cymbal sound 
%%perc V3 snare o map snare Drum sound 
%%perc V3 kick o map kick Bass drum 
10. Lyrics Enhancements
For vocal phrasing.

ABC+ Function Musical Meaning MusicXML
_melisma-start start melisma One syllable over many notes 
_melisma-end end melisma End of melisma 
"IPA:[tʃaː]" IPA text Accurate phonetics 
~ elision Two syllables sung as one 
11. Expressive Text
These guide musical character.

ABC+ Function Musical Meaning MusicXML
!dolce! expressive text Sweetly 
!espressivo! expressive text With expression 
!rit.! tempo text Slow down 
!text("sul G")! technique text Play on G string 
