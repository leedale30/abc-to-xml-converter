# ABC+ Converter Debug Report

**Title:** ABC+ Jazz & Continuo Fusion  
**Date:** 18/01/2026, 05:45:39

---

## ABC+ Input

```abc
X:3
T:ABC+ Jazz & Continuo Fusion
C:Antony Leedale
M:4/4
L:1/8
Q:1/4=140
K:Bb
%%swing 67
%%score (1 2) 3
%
V:1 name="Trumpet" short="Tpt." clef=treble
V:2 name="Piano" short="Pno." clef=treble
V:3 name="Bass" short="Bs." clef=bass
%
% --- Swing & Mute Demo ---
V:1
!marker "JAZZ"! !ff! !accent! f2 !staccato! d2 !accent! f2 !staccato! d2 | !mordent! c2 B2 G2 F2 |
V:2
!text("comping")@above! z2 [D,F,A,C]2 z2 [D,F,A,C]2 | z2 [_E,G,B,D]2 z2 [E,G,B,D]2 |
V:3
!text("walking")@below! B,,2 D,2 F,2 G,2 | _A,2 G,2 F,2 E,2 |
%
%%sep 0.5cm
%
% --- Continuo & Mute ---
V:1
!text("mosaiced out")@above!
%%mute
z8 | z8 |
V:2
!text("organ continuo")@above! !frame "Bb 1,3,3,3,1,x"! [B,DF]4 !frame "Eb 3,4,3,1,x,x"! [_EGB]4 | !frame "F7 1,1,2,1,3,1"! [FAC_e]8 |
V:3
!text("figured bass active")@below!
!fb "7"! B,,4 E,4 | !fb "4 3"! F,,8 |]

```

---

## MusicXML Output

```xml
<?xml version='1.0' encoding='utf-8'?>
<?xml-model href="https://www.w3.org/2021/06/musicxml40/musicxml.xsd" type="application/xml" schematypens="http://www.w3.org/2001/XMLSchema"?>
<score-partwise>
  <work>
    <work-title>ABC+ Jazz &amp; Continuo Fusion</work-title>
  </work>
  <identification>
    <creator type="composer">Antony Leedale</creator>
    <encoding>
      <encoder>abc2xml version 239</encoder>
      <encoding-date>2026-01-18</encoding-date>
    </encoding>
  </identification>
  <part-list>
    <score-part id="P1">
      <part-name>Trumpet</part-name>
    </score-part>
    <score-part id="P3">
      <part-name>Bass</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <direction placement="above">
        <direction-type>
          <metronome>
            <beat-unit>quarter</beat-unit>
            <per-minute>140</per-minute>
          </metronome>
        </direction-type>
        <sound tempo="140.00" />
      </direction>
      <attributes>
        <divisions>120</divisions>
        <key>
          <fifths>-2</fifths>
          <mode>major</mode>
        </key>
        <time>
          <beats>4</beats>
          <beat-type>4</beat-type>
        </time>
        <clef>
          <sign>G</sign>
          <line>2</line>
        </clef>
      </attributes>
      <direction placement="above">
        <direction-type>
          <rehearsal>"JAZZ"</rehearsal>
        </direction-type>
      </direction>
      <direction placement="below">
        <direction-type>
          <dynamics>
            <ff />
          </dynamics>
        </direction-type>
      </direction>
      <note>
        <pitch>
          <step>F</step>
          <octave>5</octave>
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
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <articulations>
            <staccato />
          </articulations>
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
          <articulations>
            <accent />
          </articulations>
        </notations>
      </note>
      <note>
        <pitch>
          <step>D</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <articulations>
            <staccato />
          </articulations>
        </notations>
      </note>
      <backup>
        <duration>480</duration>
      </backup>
      <direction placement="above">
        <direction-type>
          <words>comping</words>
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
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
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
      <note>
        <pitch>
          <step>D</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
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
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="2">
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <notations>
          <ornaments>
            <mordent />
          </ornaments>
        </notations>
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
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <backup>
        <duration>480</duration>
      </backup>
      <note>
        <rest />
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
        <accidental>flat</accidental>
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
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>120</duration>
        <voice>2</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="3">
      <direction placement="above">
        <direction-type>
          <words>mosaiced out</words>
        </direction-type>
      </direction>
      <note>
        <rest measure="yes" />
        <duration>480</duration>
        <voice>1</voice>
        <notations>
          <technical>
            <stopped />
          </technical>
        </notations>
      </note>
      <backup>
        <duration>480</duration>
      </backup>
      <direction placement="above">
        <direction-type>
          <words>organ continuo</words>
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
      <note>
        <chord />
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
        <accidental>flat</accidental>
      </note>
      <note>
        <chord />
        <pitch>
          <step>G</step>
          <octave>4</octave>
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
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>2</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="4">
      <note>
        <rest measure="yes" />
        <duration>480</duration>
        <voice>1</voice>
      </note>
      <backup>
        <duration>480</duration>
      </backup>
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>480</duration>
        <voice>2</voice>
        <type>whole</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>A</step>
          <octave>4</octave>
        </pitch>
        <duration>480</duration>
        <voice>2</voice>
        <type>whole</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>480</duration>
        <voice>2</voice>
        <type>whole</type>
      </note>
      <note>
        <chord />
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>5</octave>
        </pitch>
        <duration>480</duration>
        <voice>2</voice>
        <type>whole</type>
        <accidental>flat</accidental>
      </note>
    </measure>
  </part>
  <part id="P3">
    <measure number="1">
      <attributes>
        <divisions>120</divisions>
        <key>
          <fifths>-2</fifths>
          <mode>major</mode>
        </key>
        <time>
          <beats>4</beats>
          <beat-type>4</beat-type>
        </time>
        <clef>
          <sign>F</sign>
          <line>4</line>
        </clef>
      </attributes>
      <direction placement="below">
        <direction-type>
          <words>walking</words>
        </direction-type>
      </direction>
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
        <pitch>
          <step>D</step>
          <octave>3</octave>
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
        <pitch>
          <step>G</step>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="2">
      <note>
        <pitch>
          <step>A</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
        <accidental>flat</accidental>
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
        <pitch>
          <step>F</step>
          <octave>3</octave>
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
    </measure>
    <measure number="3">
      <direction placement="below">
        <direction-type>
          <words>figured bass active</words>
        </direction-type>
      </direction>
      <figured-bass>
        <figure>
          <figure-number>7</figure-number>
        </figure>
      </figured-bass>
      <direction placement="above">
          <direction-type>
            <other-direction print-object="no">separator</other-direction>
          </direction-type>
        </direction>
        <note>
        <pitch>
          <step>B</step>
          <alter>-1</alter>
          <octave>2</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <alter>-1</alter>
          <octave>3</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="4">
      <figured-bass>
        <figure>
          <figure-number>4</figure-number>
        </figure>
        <figure>
          <figure-number>3</figure-number>
        </figure>
      </figured-bass>
      <note>
        <pitch>
          <step>F</step>
          <octave>2</octave>
        </pitch>
        <duration>480</duration>
        <voice>1</voice>
        <type>whole</type>
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
-- skipped header: (field X,3)
-- done in 0.01 secs

```
