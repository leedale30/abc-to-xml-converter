#!/usr/bin/env python3
"""Permanent conformance suite for abc2xml (ABC+ -> MusicXML 4.0).

Converts every probe under tests/probes/<domain>/*.abc with abc2xml/abc2xml.py
and asserts element-count expectations from tests/expected.json.

Expectation semantics (attribute-order-independent, evaluated with xml.etree):
  - Each probe entry has a "counts" dict: {key: expectation}.
  - key syntax:      tag
                     parent/tag                (immediate-parent chain)
                     tag[@attr='value']        (attribute equality)
                     tag[@attr]                (attribute existence)
                     tag[text()='value']       (stripped text equality)
    Filters may be combined and applied to any path segment.
  - expectation:     int  -> exact count
                     {"min": n} / {"max": n} / both -> bounded count
  - Entries with "xfail": "<bug-id>" describe the DESIRED behaviour of a
    feature that is currently broken or missing.  They are expected to fail:
    the runner reports XFAIL and does NOT exit non-zero for them.  When a fix
    lands, the probe flips to XPASS -- remove the "xfail" marker (and refresh
    the counts with gen_expected.py) to lock the fix in as a guarded PASS.

Exit status: 1 only if a non-xfail probe fails or errors (a regression of a
working feature); 0 otherwise.

Usage:
  python3 tests/run_conformance.py               # full suite
  python3 tests/run_conformance.py --filter lines  # only probes whose relpath contains 'lines'
  python3 tests/run_conformance.py --verbose     # show per-key failures for XFAIL too
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
import xml.etree.ElementTree as ET

TESTS = Path(__file__).resolve().parent
ROOT = TESTS.parent
ABC2XML = ROOT / "abc2xml" / "abc2xml.py"
PROBES = TESTS / "probes"
EXPECTED = TESTS / "expected.json"

KEY_RE = re.compile(r"^([A-Za-z0-9_.\-]+)((?:\[[^\]]+\])*)$")
FILT_RE = re.compile(r"\[([^\]]+)\]")


def parse_part(part):
    m = KEY_RE.match(part)
    if not m:
        raise ValueError("bad key part: %r" % part)
    tag = m.group(1)
    conds = []
    for f in FILT_RE.findall(m.group(2)):
        am = re.match(r"^@([A-Za-z0-9_.:\-]+)='(.*)'$", f)
        if am:
            conds.append(("attr_eq", am.group(1), am.group(2)))
            continue
        ae = re.match(r"^@([A-Za-z0-9_.:\-]+)$", f)
        if ae:
            conds.append(("attr_has", ae.group(1), None))
            continue
        tm = re.match(r"^text\(\)='(.*)'$", f)
        if tm:
            conds.append(("text_eq", None, tm.group(1)))
            continue
        raise ValueError("bad filter %r in key part %r" % (f, part))
    return tag, conds


def elem_matches(el, tag, conds):
    if el.tag != tag:
        return False
    for kind, name, val in conds:
        if kind == "attr_eq":
            if el.get(name) != val:
                return False
        elif kind == "attr_has":
            if el.get(name) is None:
                return False
        elif kind == "text_eq":
            if (el.text or "").strip() != val:
                return False
    return True


def count_key(root, parent_of, key):
    parts = [parse_part(p) for p in key.split("/")]
    n = 0
    for el in root.iter():
        if not elem_matches(el, *parts[-1]):
            continue
        anc, ok = el, True
        for tag, conds in reversed(parts[:-1]):
            anc = parent_of.get(anc)
            if anc is None or not elem_matches(anc, tag, conds):
                ok = False
                break
        if ok:
            n += 1
    return n


def check_counts(root, counts):
    parent_of = {c: p for p in root.iter() for c in p}
    failures = []
    for key, want in sorted(counts.items()):
        got = count_key(root, parent_of, key)
        if isinstance(want, dict):
            lo, hi = want.get("min"), want.get("max")
            ok = (lo is None or got >= lo) and (hi is None or got <= hi)
            want_str = json.dumps(want)
        else:
            ok = got == want
            want_str = str(want)
        if not ok:
            failures.append("%s: expected %s, got %d" % (key, want_str, got))
    return failures


def load_root(xml_path):
    root = ET.parse(str(xml_path)).getroot()
    for el in root.iter():  # strip namespaces defensively
        if "}" in el.tag:
            el.tag = el.tag.split("}", 1)[1]
    return root


def convert(abc_path, outdir):
    r = subprocess.run(
        [sys.executable, str(ABC2XML), "-o", str(outdir), str(abc_path)],
        capture_output=True, text=True, timeout=120,
    )
    xml_path = Path(outdir) / (abc_path.stem + ".xml")
    if r.returncode != 0 or not xml_path.exists():
        raise RuntimeError(
            "abc2xml failed (rc=%d)\nstdout: %s\nstderr: %s"
            % (r.returncode, r.stdout.strip()[-800:], r.stderr.strip()[-800:])
        )
    return xml_path


def discover_probes():
    return sorted(
        p for p in PROBES.glob("*/*.abc") if p.is_file()
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--filter", default="", help="only run probes whose relative path contains this substring")
    ap.add_argument("--verbose", action="store_true", help="print per-key detail for XFAIL results too")
    args = ap.parse_args()

    if not ABC2XML.exists():
        print("FATAL: converter not found at %s" % ABC2XML)
        return 2
    if not EXPECTED.exists():
        print("FATAL: expectations file not found at %s" % EXPECTED)
        return 2

    expected = json.loads(EXPECTED.read_text())["probes"]

    results = {"PASS": 0, "FAIL": 0, "XFAIL": 0, "XPASS": 0, "NOEXP": 0}
    fail_lines = []
    xpass_lines = []

    with tempfile.TemporaryDirectory(prefix="abc2xml_conf_") as tmp:
        for probe in discover_probes():
            rel = "%s/%s" % (probe.parent.name, probe.name)
            if args.filter and args.filter not in rel:
                continue
            entry = expected.get(rel)
            if entry is None:
                results["NOEXP"] += 1
                print("NOEXP  %s  (no expectation recorded -- run gen_expected.py)" % rel)
                continue
            xfail = entry.get("xfail")
            try:
                xml_path = convert(probe, tmp)
                root = load_root(xml_path)
                failures = check_counts(root, entry.get("counts", {}))
            except Exception as e:  # conversion or parse error
                failures = ["conversion error: %s" % e]

            if not failures:
                if xfail:
                    results["XPASS"] += 1
                    xpass_lines.append(rel)
                    print("XPASS  %s  [%s]  (bug appears FIXED -- remove xfail to lock in)" % (rel, xfail))
                else:
                    results["PASS"] += 1
            else:
                if xfail:
                    results["XFAIL"] += 1
                    note = entry.get("note", "")
                    print("XFAIL  %s  [%s]%s" % (rel, xfail, ("  " + note) if note and args.verbose else ""))
                    if args.verbose:
                        for f in failures:
                            print("         - %s" % f)
                else:
                    results["FAIL"] += 1
                    fail_lines.append(rel)
                    print("FAIL   %s" % rel)
                    for f in failures:
                        print("         - %s" % f)

    total = sum(results.values())
    print()
    print("== conformance summary: %d probes | PASS %d  FAIL %d  XFAIL %d  XPASS %d  NOEXP %d =="
          % (total, results["PASS"], results["FAIL"], results["XFAIL"], results["XPASS"], results["NOEXP"]))
    if xpass_lines:
        print("XPASS (fixed bugs -- update expected.json):")
        for l in xpass_lines:
            print("  " + l)
    if fail_lines:
        print("REGRESSIONS of working features:")
        for l in fail_lines:
            print("  " + l)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
