# ABC+ Converter Debug Report

**Title:** Simple Guitar Chords Demo  
**Date:** 18/01/2026, 05:57:32

---

## ABC+ Input

```abc
X:1
T:Simple Guitar Chords Demo
M:4/4
L:1/4
K:C
%%frame C x,3,2,0,1,0
%%frame G 3,2,0,0,0,3
%%frame Am x,0,2,2,1,0
%%frame F 1,3,3,2,1,1
%
!frame C! C2 E2 | !frame G! G2 B2 | !frame Am! A2 c2 | !frame F! F2 A2 |]

```

---

## MusicXML Output

```xml
<?xml version='1.0' encoding='utf-8'?>
<?xml-model href="https://www.w3.org/2021/06/musicxml40/musicxml.xsd" type="application/xml" schematypens="http://www.w3.org/2001/XMLSchema"?>
<score-partwise>
  <work>
    <work-title>Simple Guitar Chords Demo</work-title>
  </work>
  <identification>
    <encoding>
      <encoder>abc2xml version 239</encoder>
      <encoding-date>2026-01-18</encoding-date>
    </encoding>
  </identification>
  <part-list>
    <score-part id="P1">
      <part-name />
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>120</divisions>
        <key>
          <fifths>0</fifths>
          <mode>major</mode>
        </key>
        <time>
          <beats>4</beats>
          <beat-type>4</beat-type>
        </time>
      </attributes>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
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
      </note>
      <note>
        <pitch>
          <step>B</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
    </measure>
    <measure number="3">
      <note>
        <pitch>
          <step>A</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
      </note>
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
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
      </note>
      <note>
        <pitch>
          <step>A</step>
          <octave>4</octave>
        </pitch>
        <duration>240</duration>
        <voice>1</voice>
        <type>half</type>
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
-- done in 0.01 secs

```
