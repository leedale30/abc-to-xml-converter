# ABC+ Converter Debug Report

**Title:** Guitar Solo  
**Date:** 18/01/2026, 06:43:37

---

## ABC+ Input

```abc
X:1
T:Guitar Solo
%%linked-tab 1
M:4/4
K:C
V:1 name="Lead Guitar"
C2 E2 G2 c2 | e8 |
```

---

## MusicXML Output

```xml
<?xml version='1.0' encoding='utf-8'?>
<?xml-model href="https://www.w3.org/2021/06/musicxml40/musicxml.xsd" type="application/xml" schematypens="http://www.w3.org/2001/XMLSchema"?>
<score-partwise>
  <work>
    <work-title>Guitar Solo</work-title>
  </work>
  <identification>
    <encoding>
      <encoder>abc2xml version 239</encoder>
      <encoding-date>2026-01-18</encoding-date>
    </encoding>
  </identification>
  <part-list>
    <score-part id="P1">
      <part-name>Lead Guitar</part-name>
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
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
      <note>
        <pitch>
          <step>E</step>
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
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>120</duration>
        <voice>1</voice>
        <type>quarter</type>
      </note>
    </measure>
    <measure number="2">
      <note>
        <pitch>
          <step>E</step>
          <octave>5</octave>
        </pitch>
        <duration>480</duration>
        <voice>1</voice>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>

```

---

## Validation Log

```
-- decoded from utf-8
-- skipped header: (field X,1)
-- skipped I-field: linked-tab 1
-- done in 0.00 secs

```
