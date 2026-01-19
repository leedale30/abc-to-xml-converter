# ABC+ Converter Debug Report

**Title:** Symphony No. 5 (Wuxi Dream Variation)  
**Date:** 18/01/2026, 07:33:11

---

## ABC+ Input

```abc
X:1
T:Symphony No. 5 (Wuxi Dream Variation)
T:Trad. Chinese Arrangement (Full Orchestration)
C:Ludwig van Beethoven
C:Arr. by Antony Leedale
L:1/8
M:2/4
Q:1/4=56
%%score (Soprano) (Flute Oboe) (Horn_in_F Trombones Tuba) (Dizi Erhu) (Pipa Guzheng) (Violins_1 Violins_2 Violas Violoncellos Contrabasses) (Bass_Drum Aux_Percussion)
%%drummap BD   C2   36   % Bass Drum (Tanggu)
%%drummap CS   C#2  37   % Clapper/Woodblock
%%drummap CC   C#3  49   % Suspended Cymbal/Gong
K:Eb
% --- WOODWINDS ---
V:Flute nm="Flute" snm="Fl."
V:Oboe nm="Oboe" snm="Ob."
% --- BRASS ---
V:Horn_in_F nm="Horn in F" snm="Hrn."
V:Trombones nm="Trombones" snm="Tbn." clef=bass
V:Tuba nm="Tuba" snm="Tba." clef=bass
% --- CHINESE SOLOISTS ---
V:Soprano treble nm="Soprano" snm="Sop."
V:Dizi treble nm="Dizi" snm="Dz."
V:Erhu treble nm="Erhu" snm="Er."
V:Pipa treble nm="Pipa" snm="Pp."
V:Guzheng treble nm="Guzheng" snm="Gz."
% --- STRINGS ---
V:Violins_1 treble nm="Violins 1" snm="Vln.1"
V:Violins_2 treble nm="Violins 2" snm="Vln.2"
V:Violas alto nm="Violas" snm="Vla."
V:Violoncellos bass nm="Violoncellos" snm="Vc."
V:Contrabasses bass nm="Contrabasses" snm="Cb."
% --- PERCUSSION (SPLIT) ---
V:Bass_Drum perc nm="Bass Drum" snm="B.D."
V:Aux_Percussion perc nm="Aux Perc." snm="Aux."
%
% --- INTRO ---
V:Flute
!f! z G G G | !accent!E4 | !mp! z F F F | !accent!D4 | !mf! z G G G | c2 c2 | !cresc(start)! c4 | c2 z2 !cresc(end)! |
V:Oboe
!f! z G G G | !accent!E4 | !mp! z F F F | !accent!D4 | !mf! z G G G | E2 E2 | !cresc(start)! E4 | E2 z2 !cresc(end)! |
V:Horn_in_F
!f! z B B B | !accent!G4 | !mp! z _A _A _A | !accent!F4 | !mf! z B B B | G2 G2 | !cresc(start)! G4 | G2 z2 !cresc(end)! |
V:Trombones
!f! z E E E | !accent!B,4 | !mp! z D D D | !accent!B,4 | !mf! z E E E | C2 C2 | !cresc(start)! C4 | C2 z2 !cresc(end)! |
V:Tuba
!f! E,2 z2 | !accent!E,4 | !mp! B,,2 z2 | !accent!B,,4 | !mf! E,2 z2 | A,2 A,2 | !cresc(start)! A,4 | C,2 z2 !cresc(end)! |
V:Soprano
!f! z G G G | E4 | !mp! z F F F | D4 | !mf! z G G G | !cresc(start)! c2 c2 | c4 !cresc(end)! | z4 |
V:Dizi
!f! z (3g/a/b/ c' b | !accent!g4 | !mp! z (3f/g/a/ b a | !accent!f4 | !mf! z (3g/a/b/ c' d' | !trill!e'4 | !cresc(start)! (3e'd'c' (3d'c'b | !accent!c'2 z2 !cresc(end)! |
V:Erhu
!f! !downbow!z g g g | !accent!e4 | !mp! !downbow!z f f f | !accent!d4 | !mf! !downbow!z g g g | {g}c'2 {c}g2 | !cresc(start)! e2 c2 | !accent!G4 !cresc(end)! |
V:Pipa
!f! z [G,D] [G,D] [G,D] | !accent![C,G,c]4 | !mp! z [F,C] [F,C] [F,C] | !accent![B,,F,B,]4 | !mf! z [G,D] [G,D] [G,D] | !trill![C,G,c]4 | !cresc(start)! [C,G,c]2 [B,,G,d]2 | !accent![C,G,e]2 z2 !cresc(end)! |
V:Guzheng
!f! z2 (3G,B,E (3GEc | [C,G,c]4 | !mp! z2 (3F,A,D (3FAd | [B,,F,B,]4 | !mf! z2 (3G,B,D (3GBd | [C,G,c]2 G,2 | C,2 G,2 | [C,G,c]2 z2 |
V:Violins_1
!f! !downbow!z G G G | !accent!E4 | !mp! !downbow!z F F F | !accent!D4 | !mf! !downbow!z G G G | c2 c2 | !cresc(start)! c4 | c2 z2 !cresc(end)! |
V:Violins_2
!f! !downbow!z E E E | !accent!B,4 | !mp! !downbow!z D D D | !accent!B,4 | !mf! !downbow!z E E E | G2 G2 | !cresc(start)! G4 | E2 z2 !cresc(end)! |
V:Violas
!f! !downbow!z B, B, B, | !accent!G,4 | !mp! !downbow!z _A, _A, _A, | !accent!F,4 | !mf! !downbow!z B, B, B, | E2 E2 | !cresc(start)! C2 C2 | G,2 z2 !cresc(end)! |
V:Violoncellos
!f! E,2 z2 | !accent!E,4 | !mp! B,,2 z2 | !accent!B,,4 | !mf! E,2 z2 | C,2 C,2 | !cresc(start)! A,,2 A,,2 | C,2 z2 !cresc(end)! |
V:Contrabasses
!f! E,,2 z2 | !accent!E,,4 | !mp! B,,,2 z2 | !accent!B,,,4 | !mf! E,,2 z2 | C,,2 C,,2 | !cresc(start)! A,,,2 A,,,2 | C,,2 z2 !cresc(end)! |
V:Bass_Drum
!ff! C,,2 z2 | z4 | !p! C,,2 z2 | z4 | z4 | z4 | z4 | !f! C,,2 z2 |
V:Aux_Percussion
!ff! ^C3 z | !fermata!z4 | z4 | !fermata!z4 | !mf! ^C,,2 ^C,,2 | ^C,,2 ^C,,2 | ^C,,2 ^C,,2 | z4 |
%
% --- VERSE ---
V:Flute
z4 | z4 | z4 | z4 | !mf! z d d d | c2 B2 | G4 | z4 |
V:Oboe
z4 | z4 | z4 | z4 | !mf! z B B B | G2 F2 | E4 | z4 |
V:Horn_in_F
z4 | z4 | z4 | z4 | !mp! D4- | D4 | C4- | C4 |
V:Trombones
z4 | z4 | z4 | z4 | !mp! B,4- | B,4 | C4- | C4 |
V:Tuba
z4 | z4 | z4 | z4 | !mp! G,4- | G,4 | C,4- | C,4 |
V:Soprano
!mp! z A A A | G4 | z c c c | B4 | !mf! z d d d | c2 B2 | G4 | z4 |
V:Dizi
!mp! z A/c/ e c | !tenuto!d4 | z c/e/ g e | !tenuto!f4 | !mf! z f/a/ c' a | !trill!g2 !trill!f2 | (3gag (3fef | c2 z2 |
V:Erhu
!mp! !downbow!c'4 | {c'}b4 | !downbow!e'4 | {e'}d'4 | !mf! f'4 | {f'}e'2 {e'}d'2 | {c'}b4 | g4 |
V:Pipa
!mp! z [A,E] [A,E] [A,E] | [E,B,e] A,/E/ A,/E/ | z [C,G] [C,G] [C,G] | [G,Dg] D,/G,/ D,/G,/ | !mf! z [D,A] [D,A] [D,A] | [C,Gc] z [B,,G,B,] z | !trill![G,DG]4 | z4 |
V:Guzheng
!mp! A,,/E,/A,/C/ E/A/c/e/ | E,/B,/E/G/ B/e/g/b/ | C,/G,/C/E/ G/c/e/g/ | G,/D/G/B/ d/g/b/d'/ | !mf! D,/A,/D/F/ A/d/f/a/ | C,/G,/C/E/ B,,/F,/B,/D/ | G,,/D,/G,/B,/ D/G/B/d/ | D4 |
V:Violins_1
!mp! !pizz! c2 c2 | B2 z2 | e2 e2 | d2 z2 | !mf! !arco! f4 | e2 d2 | B4 | G4 |
V:Violins_2
!mp! !pizz! A,2 A,2 | G,2 z2 | C2 C2 | B,2 z2 | !mf! !arco! A4 | G2 F2 | G4 | E4 |
V:Violas
!mp! !pizz! E,2 E,2 | E,2 z2 | G,2 G,2 | G,2 z2 | !mf! !arco! D4 | C2 B,2 | D4 | C4 |
V:Violoncellos
!mp! !pizz! A,,2 z2 | E,2 z2 | C,2 z2 | G,2 z2 | !mf! !arco! D,4 | C,2 B,,2 | G,,4 | C,4 |
V:Contrabasses
!mp! !pizz! A,,2 z2 | E,,2 z2 | C,,2 z2 | G,,2 z2 | !mf! !arco! D,,4 | C,,2 B,,,2 | G,,,4 | C,,4 |
V:Bass_Drum
z4 | z4 | z4 | z4 | z4 | z4 | C,,2 z2 | z4 |
V:Aux_Percussion
!mp! ^C,,2 ^C,, ^C,, | ^C,,2 z2 | ^C,,2 ^C,, ^C,, | ^C,,2 z2 | !mf! ^C,,2 ^C,,2 | ^C,,2 ^C,,2 | z4 | z4 |
%
% --- LYRICAL ---
V:Flute
!p! c4 | B4 | A4 | G4 | !cresc(start)! F4 | F4 | E4- !cresc(end)! | E2 z2 |
V:Oboe
!p! G4 | G4 | F4 | E4 | !cresc(start)! D4 | C4 | B,4- !cresc(end)! | B,2 z2 |
V:Horn_in_F
!p! C4- | C4 | C4- | C4 | !cresc(start)! B,2 C2 | D2 F2 | E4- !cresc(end)! | E2 z2 |
V:Trombones
!p! G,4- | G,4 | A,4- | A,4 | !cresc(start)! F,4 | D,4 | E,4- !cresc(end)! | E,2 z2 |
V:Tuba
!p! C,4- | C,4 | F,4- | F,4 | !cresc(start)! B,,4 | B,,4 | E,4- !cresc(end)! | E,2 z2 |
V:Soprano
!p! E3 F | G3 E | F2 D2 | C4 | !cresc(start)! B,2 C2 | D2 F2 | E4- !cresc(end)! | E2 z2 |
V:Dizi
!p! (3gag (3fef | c2 B2 | A2 G2 | E4 | !cresc(start)! D2 E2 | F2 A2 | !trill!G4- !cresc(end)! | G2 z2 |
V:Erhu
!p! !downbow!G4 | {A}B4 | !downbow!A4 | G4 | !cresc(start)! F2 G2 | A2 B2 | {A}B4- !cresc(end)! | B2 z2 |
V:Pipa
!p! !trill![G,B,e]4 | !trill![G,B,e]4 | !trill![F,A,d]4 | !trill![E,G,c]4 | !cresc(start)! [D,F,B,]2 [D,F,B,]2 | [F,A,d]2 [F,A,d]2 | !trill![G,B,e]4- !cresc(end)! | [G,B,e]2 z2 |
V:Guzheng
!p! E,/B,/E/G/ B/e/g/b/ | E,/B,/E/G/ B/e/g/b/ | D,/A,/D/F/ A/d/f/a/ | C,/G,/C/E/ G/c/e/g/ | !cresc(start)! B,,/F,/B,/D/ F/B/d/f/ | D,/A,/D/F/ A/d/f/a/ | E,/B,/E/G/ B/e/g/b/ !cresc(end)! | B,2 E,2 |
V:Violins_1
!p! E2 z2 | E2 z2 | F2 z2 | E2 z2 | !cresc(start)! D4 | F4 | G4- !cresc(end)! | G2 z2 |
V:Violins_2
!p! B,2 z2 | B,2 z2 | D2 z2 | C2 z2 | !cresc(start)! B,4 | D4 | B,4- !cresc(end)! | B,2 z2 |
V:Violas
!p! G,2 z2 | G,2 z2 | A,2 z2 | G,2 z2 | !cresc(start)! F,4 | A,4 | G,4- !cresc(end)! | G,2 z2 |
V:Violoncellos
!p! E,4- | E,4 | D,4- | D,4 | !cresc(start)! B,,4 | B,,4 | E,4- !cresc(end)! | E,2 z2 |
V:Contrabasses
!p! E,,4- | E,,4 | F,,4- | F,,4 | !cresc(start)! B,,,4 | B,,,4 | E,,4- !cresc(end)! | E,,2 z2 |
V:Bass_Drum
z4 | z4 | z4 | z4 | z4 | z4 | !mf! C,,4 | z4 |
V:Aux_Percussion
z4 | z4 | z4 | z4 | z4 | z4 | z4 | z4 |
%
% --- BRIDGE ---
V:Flute
!mf! g2 b2 | f2 g2 | a2 f2 | g2 c'2 | b2 c'2 | _d'2 c'2 | b2 c'2 | b4 |
V:Oboe
!mf! e2 g2 | d2 e2 | f2 d2 | e2 g2 | f2 a2 | _d2 a2 | g2 a2 | f4 |
V:Horn_in_F
!mf! G4 | G4 | F4 | E4 | D4 | F4 | G4 | F4 |
V:Trombones
!mf! E4 | B,4 | D4 | C4 | B,4 | _D4 | D4 | B,4 |
V:Tuba
!mf! E,4 | G,4 | F,4 | C,4 | G,4 | _D,4 | G,4 | G,4 |
V:Soprano
!mf! B2 e2 | d2 e2 | f2 c2 | c2 B2 | B2 c2 | _d2 c2 | B2 c2 | B4 |
V:Dizi
!mf! B/d/e/g/ b/c'/b/g/ | d/f/a/c'/ b/c'/b/g/ | f/a/c'/e'/ d'/c'/b/a/ | g/b/d'/b/ a/g/f/e/ | d/f/b/d'/ c'/b/a/g/ | _d/f/b/d'/ c'/b/a/g/ | d/g/b/d'/ c'/b/a/g/ | !trill!b4 |
V:Erhu
!mf! g2 b2 | f2 g2 | a2 f2 | g2 d2 | d2 e2 | f2 e2 | d2 e2 | {e}d4 |
V:Pipa
[G,B,d] z [B,Eg] z | [B,Df] z [B,Eg] z | [A,Ca] z [F,A,f] z | [E,G,g] z [D,F,d] z | [D,F,d] z [E,G,e] z | [F,A,f] z [E,G,e] z | [D,F,d] z [E,G,e] z | !trill![D,F,B,]4 |
V:Guzheng
G,/E/G/B/ e/g/b/e'/ | F,/D/F/B/ d/f/b/d'/ | F,/C/F/A/ c/f/a/c'/ | E,/C/E/G/ c/e/g/c'/ | D,/B,/D/F/ B/d/f/b/ | _D,/B,/_D/F/ B/_d/f/b/ | D,/B,/D/F/ B/d/f/b/ | F,/B,/D/F/ B/d/f/b/ |
V:Violins_1
!mf! !tremolo! g4 | !tremolo! f4 | !tremolo! a4 | !tremolo! g4 | !tremolo! f4 | !tremolo! _d4 | !tremolo! d4 | !tremolo! d4 |
V:Violins_2
!mf! !tremolo! e4 | !tremolo! d4 | !tremolo! f4 | !tremolo! e4 | !tremolo! d4 | !tremolo! _d4 | !tremolo! B4 | !tremolo! B4 |
V:Violas
!mf! !tremolo! B4 | !tremolo! B4 | !tremolo! c4 | !tremolo! c4 | !tremolo! B4 | !tremolo! F4 | !tremolo! G4 | !tremolo! F4 |
V:Violoncellos
!mf! !accent!E, z !accent!G, z | !accent!B, z !accent!E z | !accent!F z !accent!A z | !accent!G z !accent!C z | !accent!B, z !accent!F z | !accent!_D z !accent!F z | !accent!G z !accent!B z | !accent!F4 |
V:Contrabasses
!mf! !pizz! E,2 z2 | G,2 z2 | F,2 z2 | C,2 z2 | G,2 z2 | _D,2 z2 | G,2 z2 | B,,4 |
V:Bass_Drum
z4 | z4 | z4 | z4 | z4 | z4 | z4 | !trill!C,,4 |
V:Aux_Percussion
^C,, c ^C,, c | ^C,, c ^C,, c | ^C,, c ^C,, c | ^C,, c ^C,, c | ^C,, c ^C,, c | ^C,, c ^C,, c | ^C,, c ^C,, c | z4 |
%
% --- CLIMAX ---
V:Flute
!f! e'4 | f'2 d'2 | e'4 | c'2 a2 | !ff! g2 a2 | b2 d'2 | c'4- | c'2 z2 |
V:Oboe
!f! g4 | a2 f2 | g4 | e2 c2 | !ff! b,2 c2 | d2 f2 | e4- | e2 z2 |
V:Horn_in_F
!f! e4 | f2 d2 | e4 | c2 A2 | !ff! G2 A2 | B2 d2 | c4- | c2 z2 |
V:Trombones
!f! c4 | d2 B,2 | C4 | A,2 F,2 | !ff! E,2 F,2 | G,2 B,2 | G,4- | G,2 z2 |
V:Tuba
!f! C,4 | D,2 G,,2 | C,4 | A,,2 F,,2 | !ff! E,,2 F,,2 | G,,2 G,,2 | C,4- | C,2 z2 |
V:Soprano
!f! e4 | f2 d2 | e4 | c2 A2 | !ff! G2 A2 | B2 d2 | c4- | c2 z2 |
V:Dizi
!f! e'2 c'2 | f'2 d'2 | e'2 g'2 | c'2 a2 | !ff! g2 a2 | b2 d'2 | !trill!c'4- | c'2 z2 |
V:Erhu
!f! {f}g'4 | {g'}a'2 f'2 | {f'}g'4 | {g'}e'2 c'2 | !ff! b2 c'2 | d'2 f'2 | {d'}e'4- | e'2 z2 |
V:Pipa
!trill![E,B,e]4 | !trill![D,A,d]4 | !trill![C,G,c]4 | !trill![A,,E,A,]4 | !ff! [E,B,e]2 [E,B,e]2 | [G,B,d]2 [G,B,d]2 | !trill![C,G,c]4- | [C,G,c]2 z2 |
V:Guzheng
E,/B,/E/G/ e/g/b/e'/ | D,/A,/D/F/ d/f/a/d'/ | C,/G,/C/E/ c/e/g/c'/ | A,,/E,/A,/C/ E/A/c/e/ | !ff! [E,B,e]2 [E,B,e]2 | [G,D g]2 [G,D g]2 | [C,G,c]4- | [C,G,c]2 z2 |
V:Violins_1
!f! g4 | a2 f2 | g4 | e2 c2 | !ff! B2 c2 | d2 f2 | e4- | e2 z2 |
V:Violins_2
!f! c4 | d2 A2 | c4 | G2 F2 | !ff! E2 F2 | G2 B2 | G4- | G2 z2 |
V:Violas
!f! G4 | A2 F2 | G4 | E2 C2 | !ff! B,2 C2 | D2 F2 | E4- | E2 z2 |
V:Violoncellos
!f! C,4 | D,2 D,2 | C,4 | A,,2 A,,2 | !ff! G,,2 A,,2 | B,,2 G,,2 | C,4- | C,2 z2 |
V:Contrabasses
!f! C,,4 | D,,2 D,,2 | C,,4 | A,,,2 A,,,2 | !ff! G,,,2 A,,,2 | B,,,2 G,,,2 | C,,4- | C,,2 z2 |
V:Bass_Drum
!ff! C,,2 z2 | C,,2 z2 | C,,2 z2 | C,,2 z2 | C,, ^C,, C,, ^C,, | C,, ^C,, C,, ^C,, | C,,2 z2 | z4 |
V:Aux_Percussion
z4 | z4 | z4 | z4 | z4 | z4 | ^C3 z | z4 |
%
% --- OUTRO ---
V:Flute
!p! z G G G | E4 | z F F F | D4 | C4- | C4- | C4- | C4 |]
V:Oboe
!p! z E E E | C4 | z D D D | B,4 | G,4- | G,4- | G,4- | G,4 |]
V:Horn_in_F
!p! z C C C | G,4 | z A, A, A, | F,4 | E,4- | E,4- | E,4- | E,4 |]
V:Trombones
!p! z C, C, C, | C,4 | z D, D, D, | G,,4 | C,4- | C,4- | C,4- | C,4 |]
V:Tuba
!p! C,2 z2 | G,,4 | B,,2 z2 | G,,4 | C,4- | C,4- | C,4- | C,4 |]
V:Soprano
!p! z G G G | E4 | z F F F | D4 | C4- | C4- | C4- | C4 |]
V:Dizi
!pp! z2 G2 | E4 | z2 F2 | D4 | C4- | C4- | C4- | C4 |]
V:Erhu
!p! !downbow!z g g g | {g}e4 | !downbow!z f f f | {f}d4 | G4- | G4- | G4- | G4 |]
V:Pipa
!pp! z2 [G,D]2 | !trill![C,G,c]4 | z2 [F,C]2 | !trill![B,,F,B,]4 | !trill![C,G,c]4- | [C,G,c]4- | [C,G,c]4- | !fermata![C,G,c]4 |]
V:Guzheng
!pp! z4 | [C,G,c]4 | z4 | [B,,F,B,]4 | [C,G,c]4- | [C,G,c]4- | [C,G,c]4- | !fermata![C,G,c]4 |]
V:Violins_1
!pp! z G G G | E4 | z F F F | D4 | C4- | C4- | C4- | !fermata!C4 |]
V:Violins_2
!pp! z E E E | C4 | z D D D | B,4 | G,4- | G,4- | G,4- | !fermata!G,4 |]
V:Violas
!pp! z C C C | G,4 | z A, A, A, | F,4 | E,4- | E,4- | E,4- | !fermata!E,4 |]
V:Violoncellos
!pp! !pizz! C,2 z2 | G,,4 | B,,2 z2 | G,,4 | !arco! C,4- | C,4- | C,4- | !fermata!C,4 |]
V:Contrabasses
!pp! !pizz! C,,2 z2 | G,,,4 | B,,,2 z2 | G,,,4 | !arco! C,,4- | C,,4- | C,,4- | !fermata!C,,4 |]
V:Bass_Drum
z4 | z4 | z4 | z4 | !fermata!C,,4 | z4 | z4 | z4 |]
V:Aux_Percussion
z4 | z4 | z4 | z4 | !fermata!^C3 z | z4 | z4 | z4 |]
%
%
```

---

## MusicXML Output

```xml
<?xml version='1.0' encoding='utf-8'?>
<?xml-model href="https://www.w3.org/2021/06/musicxml40/musicxml.xsd" type="application/xml" schematypens="http://www.w3.org/2001/XMLSchema"?>
<score-partwise>
  <work>
    <work-number>Trad. Chinese Arrangement (Full Orchestration)</work-number>
    <work-title>Symphony No. 5 (Wuxi Dream Variation)</work-title>
  </work>
  <identification>
    <creator type="composer">Ludwig van Beethoven
Arr. by Antony Leedale</creator>
    <encoding>
      <encoder>abc2xml version 239</encoder>
      <encoding-date>2026-01-18</encoding-date>
    </encoding>
  </identification>
  <part-list>
    <score-part id="PSoprano">
      <part-name>Soprano</part-name>
      <part-abbreviation>Sop.</part-abbreviation>
    </score-part>
    <score-part id="PFlute">
      <part-name>Flute</part-name>
      <part-abbreviation>Fl.</part-abbreviation>
    </score-part>
    <score-part id="PHorn_in_F">
      <part-name>Horn in F</part-name>
      <part-abbreviation>Hrn.</part-abbreviation>
    </score-part>
    <score-part id="PDizi">
      <part-name>Dizi</part-name>
      <part-abbreviation>Dz.</part-abbreviation>
    </score-part>
    <score-part id="PPipa">
      <part-name>Pipa</part-name>
      <part-abbreviation>Pp.</part-abbreviation>
    </score-part>
    <score-part id="PViolins_1">
      <part-name>Violins 1</part-name>
      <part-abbreviation>Vln.1</part-abbreviation>
    </score-part>
    <score-part id="PBass_Drum">
      <part-name>Bass Drum</part-name>
      <part-abbreviation>B.D.</part-abbreviation>
      <score-instrument id="IBass_Drum-X36">
        <instrument-name>Bass Drum</instrument-name>
      </score-instrument>
      <score-instrument id="IBass_Drum-X37">
        <instrument-name>Bass Drum</instrument-name>
      </score-instrument>
      <score-instrument id="IBass_Drum-X61">
        <instrument-name>Aux Perc.</instrument-name>
      </score-instrument>
      <score-instrument id="IBass_Drum-X72">
        <instrument-name>Aux Perc.</instrument-name>
      </score-instrument>
      <midi-instrument id="IBass_Drum-X36">
        <midi-channel>10</midi-channel>
        <midi-program>1</midi-program>
        <midi-unpitched>37</midi-unpitched>
      </midi-instrument>
      <midi-instrument id="IBass_Drum-X37">
        <midi-channel>10</midi-channel>
        <midi-program>1</midi-program>
        <midi-unpitched>38</midi-unpitched>
      </midi-instrument>
      <midi-instrument id="IBass_Drum-X61">
        <midi-channel>10</midi-channel>
        <midi-program>1</midi-program>
        <midi-unpitched>62</midi-unpitched>
      </midi-instrument>
      <midi-instrument id="IBass_Drum-X72">
        <midi-channel>10</midi-channel>
        <midi-program>1</midi-program>
        <midi-unpitched>73</midi-unpitched>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="PSoprano">
    <measure number="1">
      <attributes>
        <divisions>120</divisions>
        <key>
          <fifths>-3</fifths>
          <mode>major</mode>
        </key>
        <time>
          <beats>2</beats>
          <beat-type>4</beat-type>
        </time>
        <clef>
          <sign>G</sign>
          <line>2</line>
        </clef>
      </attributes>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="2">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="3">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="4">
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="5">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="6">
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="7">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
    </measure>
    <measure number="8">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="9">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="10">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="11">
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="12">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="13">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="14">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="15">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="16">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="17">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>180</duration>
        <voice>1</voice>
        <type>quarter</type>
        <dot />
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="18">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>180</duration>
        <voice>1</voice>
        <type>quarter</type>
        <dot />
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="19">
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="20">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="21">
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="22">
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="23">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="1" />
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
    </measure>
    <measure number="24">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="25">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="26">
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="27">
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="28">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="29">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="30">
      <note>
        <pitch>
          <step>D</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <accidental>flat</accidental>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="31">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="32">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="33">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="34">
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="35">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="36">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="37">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="38">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="39">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="1" />
        </notations>
      </note>
    </measure>
    <measure number="40">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="41">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="42">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="43">
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="44">
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="45">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
    </measure>
    <measure number="46">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
    </measure>
    <measure number="47">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="1" />
        </notations>
      </note>
    </measure>
    <measure number="48">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
    </measure>
  </part>
  <part id="PFlute">
    <measure number="1">
      <direction placement="above">
        <direction-type>
          <metronome>
            <beat-unit>quarter</beat-unit>
            <per-minute>56</per-minute>
          </metronome>
        </direction-type>
        <sound tempo="56.00" />
      </direction>
      <attributes>
        <divisions>120</divisions>
        <key>
          <fifths>-3</fifths>
          <mode>major</mode>
        </key>
        <time>
          <beats>2</beats>
          <beat-type>4</beat-type>
        </time>
      </attributes>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        <notations>
          <slur number="2" type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="2">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
    </measure>
    <measure number="3">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="4">
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
    </measure>
    <measure number="5">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="6">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="7">
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="8">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
    </measure>
    <measure number="9">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="10">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="11">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="12">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="13">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="14">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="15">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="16">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="17">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="18">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="19">
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="20">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="21">
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="22">
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="23">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="1" />
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="2" />
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
    </measure>
    <measure number="24">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <slur number="2" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="25">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="26">
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="27">
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="28">
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="29">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="30">
      <note>
        <pitch>
          <step>D</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <accidental>flat</accidental>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
        <accidental>flat</accidental>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="31">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="32">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="33">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="34">
      <note>
        <pitch>
          <step>F</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="35">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="36">
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="37">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="38">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="39">
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="1" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="2" />
        </notations>
      </note>
    </measure>
    <measure number="40">
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <slur number="2" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="41">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="42">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="43">
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="44">
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="45">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
    </measure>
    <measure number="46">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
    </measure>
    <measure number="47">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="1" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="2" />
        </notations>
      </note>
    </measure>
    <measure number="48">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
    </measure>
  </part>
  <part id="PHorn_in_F">
    <measure number="1">
      <attributes>
        <divisions>120</divisions>
        <key>
          <fifths>-3</fifths>
          <mode>major</mode>
        </key>
        <time>
          <beats>2</beats>
          <beat-type>4</beat-type>
        </time>
      </attributes>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        <notations>
          <slur number="2" type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
        <notations>
          <slur number="3" type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="2">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
    </measure>
    <measure number="3">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        <accidental>flat</accidental>
        </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        <accidental>flat</accidental>
        </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        <accidental>flat</accidental>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="4">
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
    </measure>
    <measure number="5">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="6">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="7">
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="8">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
    </measure>
    <measure number="9">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="10">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="11">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="12">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="13">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="1" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="2" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="3" />
        </notations>
      </note>
    </measure>
    <measure number="14">
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="15">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
          <slur number="1" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="2" />
          <slur number="2" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
          <slur number="3" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="16">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="17">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="2" />
          <slur number="2" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="3" />
        </notations>
      </note>
    </measure>
    <measure number="18">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="19">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="1" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="2" />
          <slur number="2" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="3" />
          <slur number="3" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="20">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="21">
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur number="2" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <slur number="3" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="22">
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="23">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="1" />
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="2" />
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="3" />
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
    </measure>
    <measure number="24">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <slur number="2" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>3</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
        <notations>
          <slur number="3" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="25">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="26">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="27">
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="28">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="29">
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="30">
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <accidental>flat</accidental>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <accidental>flat</accidental>
      </note>
    </measure>
    <measure number="31">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="32">
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="33">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="34">
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="35">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="36">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="37">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="38">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="39">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="1" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="2" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="3" />
        </notations>
      </note>
    </measure>
    <measure number="40">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <slur number="2" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>3</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
        <notations>
          <slur number="3" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="41">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="42">
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="43">
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="44">
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="45">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
    </measure>
    <measure number="46">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
    </measure>
    <measure number="47">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="1" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="2" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="3" />
        </notations>
      </note>
    </measure>
    <measure number="48">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
    </measure>
  </part>
  <part id="PDizi">
    <measure number="1">
      <attributes>
        <divisions>120</divisions>
        <key>
          <fifths>-3</fifths>
          <mode>major</mode>
        </key>
        <time>
          <beats>2</beats>
          <beat-type>4</beat-type>
        </time>
        <clef>
          <sign>G</sign>
          <line>2</line>
        </clef>
      </attributes>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>20</duration>
        <voice>1</voice>
        <type>16th</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>20</duration>
        <voice>1</voice>
        <type>16th</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>20</duration>
        <voice>1</voice>
        <type>16th</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        <notations>
          <slur number="2" type="stop" />
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="2">
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
    </measure>
    <measure number="3">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>20</duration>
        <voice>1</voice>
        <type>16th</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>20</duration>
        <voice>1</voice>
        <type>16th</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>20</duration>
        <voice>1</voice>
        <type>16th</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="4">
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
    </measure>
    <measure number="5">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>20</duration>
        <voice>1</voice>
        <type>16th</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>20</duration>
        <voice>1</voice>
        <type>16th</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>20</duration>
        <voice>1</voice>
        <type>16th</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="6">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <grace />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="7">
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="8">
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
    </measure>
    <measure number="9">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
    </measure>
    <measure number="10">
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <articulations>
            <tenuto />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="11">
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
    </measure>
    <measure number="12">
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <articulations>
            <tenuto />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="13">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>F</step>
          <octave>6</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="14">
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>F</step>
          <octave>6</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <grace />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="15">
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="16">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="17">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>1</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
    </measure>
    <measure number="18">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="19">
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
    </measure>
    <measure number="20">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="21">
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="22">
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="23">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="1" />
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="2" />
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
    </measure>
    <measure number="24">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <slur number="2" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="25">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="26">
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="27">
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="28">
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="29">
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="30">
      <note>
        <pitch>
          <step>D</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <accidental>flat</accidental>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="31">
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="32">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="33">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <grace />
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>6</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="34">
      <note>
        <pitch>
          <step>F</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>G</step>
          <octave>6</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="35">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>F</step>
          <octave>6</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>6</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="36">
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>G</step>
          <octave>6</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="37">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="38">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="39">
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="1" />
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="2" />
        </notations>
      </note>
    </measure>
    <measure number="40">
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <slur number="2" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="41">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <pp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="42">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="43">
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
    </measure>
    <measure number="44">
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <grace />
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="45">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
    </measure>
    <measure number="46">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
    </measure>
    <measure number="47">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="1" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="2" />
        </notations>
      </note>
    </measure>
    <measure number="48">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
    </measure>
  </part>
  <part id="PPipa">
    <measure number="1">
      <attributes>
        <divisions>120</divisions>
        <key>
          <fifths>-3</fifths>
          <mode>major</mode>
        </key>
        <time>
          <beats>2</beats>
          <beat-type>4</beat-type>
        </time>
        <clef>
          <sign>G</sign>
          <line>2</line>
        </clef>
      </attributes>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <slur number="6" type="stop" />
          <slur number="5" type="stop" />
          <slur number="4" type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="2">
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="3">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="4">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="5">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">begin</beam>
        <notations>
          <tuplet type="start" bracket="yes" />
        </notations>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>40</duration>
        <voice>2</voice>
        <type>eighth</type>
        <time-modification>
          <actual-notes>3</actual-notes>
          <normal-notes>2</normal-notes>
        </time-modification>
        <beam number="1">end</beam>
        <notations>
          <tuplet type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="6">
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="7">
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="8">
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="9">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="10">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <backup>
        <duration>180</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="11">
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="12">
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>1</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <backup>
        <duration>180</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="13">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="14">
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="15">
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>2</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="16">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="17">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="18">
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="19">
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="20">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="21">
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="22">
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="23">
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="2" />
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="1" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="3" />
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
    </measure>
    <measure number="24">
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="3" type="stop" />
          <slur number="2" type="stop" />
          <slur number="1" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="25">
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="26">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="27">
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="28">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="29">
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="30">
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <accidental>flat</accidental>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <accidental>flat</accidental>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <accidental>flat</accidental>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="31">
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="32">
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="33">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="34">
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="35">
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>6</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="36">
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">begin</beam>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">continue</beam>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>30</duration>
        <voice>2</voice>
        <type>16th</type>
        <beam number="1">end</beam>
      </note>
    </measure>
    <measure number="37">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="38">
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="39">
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="1" />
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="2" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="3" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="4" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="5" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="6" />
        </notations>
      </note>
    </measure>
    <measure number="40">
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="3" type="stop" />
          <slur number="2" type="stop" />
          <slur number="1" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <slur number="6" type="stop" />
          <slur number="5" type="stop" />
          <slur number="4" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="41">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <pp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="42">
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="43">
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="44">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="45">
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
    </measure>
    <measure number="46">
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
    </measure>
    <measure number="47">
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="1" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="2" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="3" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="4" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="5" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="6" />
        </notations>
      </note>
    </measure>
    <measure number="48">
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <fermata type="upright" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <fermata type="upright" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
    </measure>
  </part>
  <part id="PViolins_1">
    <measure number="1">
      <attributes>
        <divisions>120</divisions>
        <key>
          <fifths>-3</fifths>
          <mode>major</mode>
        </key>
        <time>
          <beats>2</beats>
          <beat-type>4</beat-type>
        </time>
        <clef>
          <sign>G</sign>
          <line>2</line>
        </clef>
      </attributes>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        <notations>
          <slur number="3" type="stop" />
          <slur number="2" type="stop" />
          <slur number="1" type="stop" />
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        <notations>
          <slur number="4" type="stop" />
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        <notations>
          <slur number="5" type="stop" />
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>4</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
        <notations>
          <slur number="6" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
        <notations>
          <slur number="7" type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="2">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
    </measure>
    <measure number="3">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        <accidental>flat</accidental>
        </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        <accidental>flat</accidental>
        </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        <accidental>flat</accidental>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>1</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="4">
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>1</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
    </measure>
    <measure number="5">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        <notations>
          <technical>
            <down-bow />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="6">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="7">
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>1</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>1</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="8">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
    </measure>
    <measure number="9">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <technical>
            <pizzicato />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <technical>
            <pizzicato />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
        <notations>
          <technical>
            <pizzicato />
          </technical>
        </notations>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
        <notations>
          <technical>
            <pizzicato />
          </technical>
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
        <notations>
          <technical>
            <pizzicato />
          </technical>
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="10">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="11">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="12">
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="13">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <technical>
            <arco />
          </technical>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <technical>
            <arco />
          </technical>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <technical>
            <arco />
          </technical>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
        <notations>
          <technical>
            <arco />
          </technical>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>D</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
        <notations>
          <technical>
            <arco />
          </technical>
        </notations>
      </note>
    </measure>
    <measure number="14">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>1</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="15">
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>1</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="16">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="17">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="6" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="7" />
        </notations>
      </note>
    </measure>
    <measure number="18">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>4</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>5</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="19">
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="6" />
          <slur number="6" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="7" />
          <slur number="7" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="20">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>4</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>5</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="21">
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
        <notations>
          <slur number="6" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <wedge type="crescendo" />
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>1</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
        <notations>
          <slur number="7" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="22">
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>1</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="23">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="1" />
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="4" />
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="5" />
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="6" />
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="7" />
        </notations>
      </note>
      <direction placement="below">
        <direction-type>
          <wedge type="stop" />
        </direction-type>
      </direction>
    </measure>
    <measure number="24">
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <slur number="4" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>3</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
        <notations>
          <slur number="5" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>4</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
        <notations>
          <slur number="6" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>5</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
        <notations>
          <slur number="7" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="25">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
        <notations>
          <technical>
            <pizzicato />
          </technical>
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="26">
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="27">
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="28">
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="29">
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="30">
      <note>
        <pitch>
          <step>D</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <accidental>flat</accidental>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <accidental>flat</accidental>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <accidental>flat</accidental>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
        <accidental>flat</accidental>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="31">
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>4</voice>
        <type>eighth</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="32">
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <ornaments>
            <tremolo />
          </ornaments>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
        <notations>
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="33">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="34">
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="35">
      <note>
        <pitch>
          <step>G</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="36">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>1</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>1</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="37">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>G</step>
          <octave>1</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>1</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="38">
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>1</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>1</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="39">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="1" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="4" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="5" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="6" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
        <notations>
          <slur type="start" number="7" />
        </notations>
      </note>
    </measure>
    <measure number="40">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
        <notations>
          <slur number="4" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>3</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>3</voice>
        <type>quarter</type>
        <notations>
          <slur number="5" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>4</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
        <notations>
          <slur number="6" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <tie type="stop" />
        <voice>5</voice>
        <type>quarter</type>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
        <notations>
          <slur number="7" type="stop" />
        </notations>
      </note>
    </measure>
    <measure number="41">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <pp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>G</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <pp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <pp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <rest />
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <pp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
        <notations>
          <technical>
            <pizzicato />
          </technical>
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <pp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
        <notations>
          <technical>
            <pizzicato />
          </technical>
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="42">
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>1</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="43">
      <note>
        <rest />
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>1</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <rest />
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
      </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        </note>
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>60</duration>
        <voice>3</voice>
        <type>eighth</type>
        </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>4</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>1</octave>
        </pitch>
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>5</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="44">
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>3</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>4</voice>
        <type>half</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>1</octave>
        </pitch>
        <duration>240</duration>
        <voice>5</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="45">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>4</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
          <technical>
            <arco />
          </technical>
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <tie type="start" />
        <voice>5</voice>
        <type>half</type>
        <notations>
          <tied type="start" />
          <technical>
            <arco />
          </technical>
        </notations>
      </note>
    </measure>
    <measure number="46">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>4</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <tie type="start" />
        <voice>5</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <tied type="start" />
        </notations>
      </note>
    </measure>
    <measure number="47">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="1" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="4" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="5" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>4</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="6" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>5</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <slur type="start" number="7" />
        </notations>
      </note>
    </measure>
    <measure number="48">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>1</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <fermata type="upright" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>2</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <fermata type="upright" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>3</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <fermata type="upright" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>4</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <fermata type="upright" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <pitch>
          <step>C</step>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <tie type="stop" />
        <voice>5</voice>
        <type>half</type>
        <notations>
          <tied type="stop" />
          <fermata type="upright" />
        </notations>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
    </measure>
  </part>
  <part id="PBass_Drum">
    <measure number="1">
      <attributes>
        <divisions>120</divisions>
        <time>
          <beats>2</beats>
          <beat-type>4</beat-type>
        </time>
        <clef>
          <sign>percussion</sign>
        </clef>
      </attributes>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <tie type="stop" />
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>quarter</type>
        <notehead>normal</notehead>
        <notations>
          <tied type="stop" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <slur number="1" type="stop" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>4</display-octave>
        </unpitched>
        <duration>180</duration>
        <instrument id="IBass_Drum-X61" />
        <voice>2</voice>
        <type>quarter</type>
        <dot />
        <notehead>x</notehead>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
    </measure>
    <measure number="2">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="3">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <p />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>quarter</type>
        <notehead>normal</notehead>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="4">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="5">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
    </measure>
    <measure number="6">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
    </measure>
    <measure number="7">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
    </measure>
    <measure number="8">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <f />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>quarter</type>
        <notehead>normal</notehead>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="9">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mp />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
    </measure>
    <measure number="10">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="11">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
    </measure>
    <measure number="12">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="13">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
    </measure>
    <measure number="14">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>quarter</type>
        <notehead>x</notehead>
      </note>
    </measure>
    <measure number="15">
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>quarter</type>
        <notehead>normal</notehead>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="16">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="17">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="18">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="19">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="20">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="21">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="22">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="23">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <mf />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>240</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>half</type>
        <notehead>normal</notehead>
      </note>
    </measure>
    <measure number="24">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="25">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
    </measure>
    <measure number="26">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
    </measure>
    <measure number="27">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
    </measure>
    <measure number="28">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
    </measure>
    <measure number="29">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
    </measure>
    <measure number="30">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
    </measure>
    <measure number="31">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>5</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X72" />
        <voice>2</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
    </measure>
    <measure number="32">
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>240</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>half</type>
        <notehead>normal</notehead>
        <notations>
          <ornaments>
            <trill-mark />
          </ornaments>
        </notations>
      </note>
    </measure>
    <measure number="33">
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>quarter</type>
        <notehead>normal</notehead>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="34">
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>quarter</type>
        <notehead>normal</notehead>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="35">
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>quarter</type>
        <notehead>normal</notehead>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="36">
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>quarter</type>
        <notehead>normal</notehead>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="37">
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>1</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>1</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
    </measure>
    <measure number="38">
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>1</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>eighth</type>
        <notehead>normal</notehead>
        </note>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>60</duration>
        <instrument id="IBass_Drum-X37" />
        <voice>1</voice>
        <type>eighth</type>
        <notehead>x</notehead>
        </note>
    </measure>
    <measure number="39">
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>120</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>quarter</type>
        <notehead>normal</notehead>
      </note>
      <note>
        <rest />
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>4</display-octave>
        </unpitched>
        <duration>180</duration>
        <instrument id="IBass_Drum-X61" />
        <voice>2</voice>
        <type>quarter</type>
        <dot />
        <notehead>x</notehead>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
    </measure>
    <measure number="40">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="41">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="42">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="43">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="44">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="45">
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>2</display-octave>
        </unpitched>
        <duration>240</duration>
        <instrument id="IBass_Drum-X36" />
        <voice>1</voice>
        <type>half</type>
        <notehead>normal</notehead>
        <notations>
          <fermata type="upright" />
        </notations>
      </note>
      <backup>
        <duration>240</duration>
      </backup>
      <note>
        <unpitched>
          <display-step>C</display-step>
          <display-octave>4</display-octave>
        </unpitched>
        <duration>180</duration>
        <instrument id="IBass_Drum-X61" />
        <voice>2</voice>
        <type>quarter</type>
        <dot />
        <notehead>x</notehead>
        <notations>
          <fermata type="upright" />
        </notations>
      </note>
      <note>
        <rest />
        <duration>60</duration>
        <voice>2</voice>
        <type>eighth</type>
      </note>
    </measure>
    <measure number="46">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="47">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
    </measure>
    <measure number="48">
      <note>
        <rest measure="yes" />
        <duration>240</duration>
        <voice>1</voice>
      </note>
      <barline location="right">
        <bar-style>light-heavy</bar-style>
      </barline>
    </measure>
  </part>
</score-partwise>

```

---

## Validation Log

```
-- decoded from utf-8
-- skipped header: (field X,1)
-- tie between different pitches: E0 converted to slur
-- tie between different pitches: c1 converted to slur
-- tie between different pitches: C0 converted to slur
-- tie between different pitches: B-1 converted to slur
-- tie between different pitches: e0 converted to slur
-- tie between different pitches: G-1 converted to slur
-- tie between different pitches: D0 converted to slur
-- tie between different pitches: C0 converted to slur
-- tie between different pitches: E0 converted to slur
-- tie between different pitches: c0 converted to slur
-- tie between different pitches: E-1 converted to slur
-- tie between different pitches: B-1 converted to slur
-- tie between different pitches: C0 converted to slur
-- tie between different pitches: G-1 converted to slur
-- tie between different pitches: A-1 converted to slur
-- tie between different pitches: E-1 converted to slur
-- tie between different pitches: G-1 converted to slur
-- tie between different pitches: C-1 converted to slur
-- tie between different pitches: G-1 converted to slur
-- tie between different pitches: C-1 converted to slur
-- tie between different pitches: F-1 converted to slur
-- tie between different pitches: E-1 converted to slur
-- tie between different pitches: C-1 converted to slur
-- tie between different pitches: C-1 converted to slur
-- tie between different pitches: E0 converted to slur
-- tie between different pitches: c0 converted to slur
-- tie between different pitches: C0 converted to slur
-- tie between different pitches: G0 converted to slur
-- tie between different pitches: c1 converted to slur
-- tie between different pitches: C0 converted to slur
-- tie between different pitches: B0 converted to slur
-- tie between different pitches: e1 converted to slur
-- tie between different pitches: G0 converted to slur
-- tie between different pitches: B-1 converted to slur
-- tie between different pitches: G-1 converted to slur
-- tie between different pitches: e0 converted to slur
-- tie between different pitches: C-1 converted to slur
-- tie between different pitches: G-1 converted to slur
-- tie between different pitches: c0 converted to slur
-- tie between different pitches: C-1 converted to slur
-- tie between different pitches: G-1 converted to slur
-- tie between different pitches: c0 converted to slur
-- Measure 1 has too many beats! (Found 3.00, expected 2.00)
-- Measure 3 has too many beats! (Found 3.00, expected 2.00)
-- Measure 5 has too many beats! (Found 3.00, expected 2.00)
-- tie between different pitches: C-1 converted to slur
-- tie between different pitches: G-1 converted to slur
-- tie between different pitches: c0 converted to slur
-- tie between different pitches: C-1 converted to slur
-- tie between different pitches: G-1 converted to slur
-- tie between different pitches: c0 converted to slur
-- tie between different pitches: G0 converted to slur
-- tie between different pitches: e0 converted to slur
-- tie between different pitches: C0 converted to slur
-- tie between different pitches: B-1 converted to slur
-- tie between different pitches: G0 converted to slur
-- tie between different pitches: G-1 converted to slur
-- tie between different pitches: G-1 converted to slur
-- tie between different pitches: E0 converted to slur
-- tie between different pitches: E-1 converted to slur
-- tie between different pitches: E-1 converted to slur
-- tie between different pitches: D-1 converted to slur
-- tie between different pitches: E-1 converted to slur
-- tie between different pitches: C-1 converted to slur
-- tie between different pitches: C-1 converted to slur
-- tie between different pitches: E-2 converted to slur
-- tie between different pitches: F-2 converted to slur
-- tie between different pitches: E-2 converted to slur
-- tie between different pitches: C-2 converted to slur
-- tie between different pitches: C-2 converted to slur
-- done in 0.39 secs

```
