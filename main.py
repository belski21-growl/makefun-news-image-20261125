"""news-image-20261125 entry program (v10).

Ships the rebuilt full-day newspaper image (entry.png, 1024x1024
JPEG) to the grader output directory, checking the image before and
after the copy so only the exact v10 bytes can ever be submitted.

v10: one Goldfish-r8 micro-fix round over v9 (49 clean + 1 grey,
0 failed; verdict LAYAK LANJUT BELUM LAYAK SUBMIT). Same 50 stories,
10 regions, 20 fields, 3 illustrated heroes, 12 illustrated
secondary panels, UTC timeline, 6-number strip, numbered world map
and DATE CHECK footer — compiled ~23:35 UTC 25 Nov 2026, so the
whole day is covered: US tariffs on 14 economies, the Kospi -6.2%
chip rout, Shenzhou-24 docking with Pakistan's first astronaut,
the Cairo tanker fire, Hodeidah, Hormuz, the UK price cap, the
Bangladesh wage, the Bogor mine, Samara, Phala Phala and the rest.
Every story was verified against its primary outlet as first
reported Wednesday 25 November 2026; the known 24-November traps
(Huawei verdict, WHO Ebola evacuation, UN femicide brief, Tube
strike, Kyiv aid ask, Odesa strike) are listed as exclusions in the
image footer and in build-log.md. What v10 changes, and only this:
the region bar (all 10 counts now read in full), the hero-3 Earth
art (no longer spills onto the JIUQUAN kicker), the #10 "100 M" art
label (moved clear of the number chip), and the #48 headline (now
explicitly attributed to the rights group). Nothing else — no story,
number, date or layout element was touched.

This program pins the v10 fingerprint (EXPECTED_BYTES /
EXPECTED_DIGEST) and refuses to ship anything else: a stale v9 (or
older) image is named as stale in the error, never shipped as v10.

Deterministic: the output bytes are exactly the repository bytes,
so repeated grader runs write identical files. Standard library
only, no network access, no environment secrets.

SPDX-License-Identifier: MIT
"""

import hashlib
import os
import shutil
import sys

JPEG_SOI = b"\xff\xd8"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
WANT_WIDTH = 1024
WANT_HEIGHT = 1024

SOURCE_FILE = "entry.png"
DEST_FILE = "entry.png"

# v10 pinned fingerprint (entry.png re-rendered 26 Nov 2026 ~00:22 UTC
# from /tmp/gen_ni25_v10.py: Goldfish-r8 micro-fix — region bar
# rebalanced + two-pass labels, hero-3 Earth cap clamped, #10 "100 M"
# label moved, #48 headline attributed. Same 50 stories, 10 regions,
# 20 fields as v9; only those four fixes changed any pixel).
EXPECTED_BYTES = 363276
EXPECTED_DIGEST = (
    "6fdefdbfc15e83535d8c33dedec40b699199323dce1284ab46be308d536b5fb0"
)

# Stale fingerprints, oldest first: (size, sha256, version). A source
# image matching one of these is reported as that stale version.
STALE = (
    (263286,
     "0639ce21ed82f2df9019d1a5b47dc49ec503a492adb0d90966c35d888e842577",
     "v1"),
    (270327,
     "30b59778c802cccfe743db3e40263e668636f418f9e8d037b47537c928759ae2",
     "v2"),
    (276540,
     "df4a30ca10053c6005b37b0c2a82dbddd0d1699f2f7f50f8f857df5fab136f6c",
     "v3"),
    (272076,
     "4edbd9944d3a228978d479f762b8c0c4c55667575fd5311fa9d51e703c5c64ed",
     "v4"),
    (322851,
     "8e07008437dd49cc8e494b0b493e496faddae40da4a3d9f5a233802864285a97",
     "v5"),
    (325798,
     "4967825d8cf7ba7e29f8f7815c8fc2cda0fc26af27f94cd4d0b705e78b689a7a",
     "v6"),
    (324007,
     "5fd850f8bcd788081b3dfc36466e25ae5ee7ddc1ef5f93ab298d2e0a41ce934a",
     "v8"),
    (362993,
     "cc7b54f82d65b2817443430c8b64e671444d522cda5e6b8eb46ca31981bfb841",
     "v9"),
)


class GateError(Exception):
    """A v10 gate failure: message already names the version."""


def _head(path, limit=65536):
    with open(path, "rb") as handle:
        return handle.read(limit)


def _jpeg_size(blob):
    """(width, height) from the first SOF marker in a JPEG head."""
    if blob[:2] != JPEG_SOI:
        return None
    cursor = 2
    while cursor + 9 <= len(blob):
        if blob[cursor] != 0xFF:
            cursor += 1
            continue
        marker = blob[cursor + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            height = int.from_bytes(blob[cursor + 5:cursor + 7], "big")
            width = int.from_bytes(blob[cursor + 7:cursor + 9], "big")
            return width, height
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            cursor += 2
            continue
        span = int.from_bytes(blob[cursor + 2:cursor + 4], "big")
        cursor += 2 + span
    return None


def _png_size(blob):
    """(width, height) from a PNG IHDR chunk."""
    if not blob.startswith(PNG_SIGNATURE) or len(blob) < 33:
        return None
    if blob[12:16] != b"IHDR":
        return None
    width = int.from_bytes(blob[16:20], "big")
    height = int.from_bytes(blob[20:24], "big")
    return width, height


def inspect_image(path):
    """Return a dict describing the file at path.

    Keys: size (bytes), digest (sha256 hex), kind ("JPEG"/"PNG"/None),
    dimensions ((w, h) or None).
    """
    digest = hashlib.sha256()
    size = 0
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(65536)
            if not chunk:
                break
            size += len(chunk)
            digest.update(chunk)
    blob = _head(path)
    if blob.startswith(PNG_SIGNATURE):
        kind = "PNG"
    elif blob[:3] == b"\xff\xd8\xff":
        kind = "JPEG"
    else:
        kind = None
    dims = _png_size(blob) if kind == "PNG" else _jpeg_size(blob)
    return {"size": size, "digest": digest.hexdigest(),
            "kind": kind, "dimensions": dims}


def _fail(message):
    raise GateError("v10 error: " + message)


def gate_source(path):
    """Inspect the source image and enforce every v10 gate.

    Returns the inspection dict on success; raises GateError with a
    v9-named message on any failure.
    """
    if not os.path.isfile(path):
        _fail("source image missing: %s" % path)
    report = inspect_image(path)
    if report["size"] == 0:
        _fail("source image is empty")
    if report["size"] > MAX_BYTES:
        _fail("source image is %d bytes, over the 1 MiB limit"
              % report["size"])
    if report["kind"] is None:
        _fail("source is neither PNG nor JPEG (bad magic bytes)")
    if report["dimensions"] is None:
        _fail("cannot read dimensions from source image")
    if report["dimensions"] != (WANT_WIDTH, WANT_HEIGHT):
        _fail("source is %dx%d, expected %dx%d"
              % (report["dimensions"][0], report["dimensions"][1],
                 WANT_WIDTH, WANT_HEIGHT))
    if (report["size"], report["digest"]) != (EXPECTED_BYTES,
                                              EXPECTED_DIGEST):
        for old_size, old_digest, old_ver in STALE:
            if (report["size"], report["digest"]) == (old_size, old_digest):
                # v10: the v9 stale case names the fix it lacks, so a
                # v9 image is never mistaken for a fixed v10 image.
                extra = (" — v9 lacks the Goldfish-r8 fixes (region "
                         "bar counts, hero-3 kicker, #10 label, #48 "
                         "attribution)") if old_ver == "v9" else ""
                _fail("source is stale %s (%d bytes, sha256 %s)%s; "
                      "expected v10 %d bytes, sha256 %s"
                      % (old_ver, old_size, old_digest, extra,
                         EXPECTED_BYTES, EXPECTED_DIGEST))
        _fail("source fingerprint mismatch: expected v10 %d bytes, "
              "sha256 %s" % (EXPECTED_BYTES, EXPECTED_DIGEST))
    return report


def _out_dir():
    """Grader output dir: MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def _print_report(report, copied):
    print("entry.png: %d bytes" % report["size"])
    print("sha256: %s" % report["digest"])
    print("format: %s" % report["kind"])
    print("dimensions: %dx%d" % report["dimensions"])
    print("version: v10 (Goldfish-r8 micro-fix: region bar + hero-3 "
          "kicker + #10 label + #48 attribution)")
    print("fingerprint: matches pinned v10 (size + sha256)")
    if copied:
        print("verified: size + sha256 + magic + dimensions match source")
    else:
        print("verified: size + sha256 + magic + dimensions OK (no copy)")


def run(argv):
    verify_only = "--verify-only" in argv
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_FILE)
    report = gate_source(source)
    if verify_only:
        _print_report(report, copied=False)
        return 0
    out_dir = _out_dir()
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, DEST_FILE)
    shutil.copyfile(source, target)
    after = inspect_image(target)
    if (after["size"], after["digest"], after["kind"],
            after["dimensions"]) != (report["size"], report["digest"],
                                     report["kind"],
                                     report["dimensions"]):
        _fail("output does not match source after copy")
    _print_report(after, copied=True)
    return 0


def main(argv=None):
    try:
        return run(list(sys.argv[1:] if argv is None else argv))
    except GateError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except OSError as exc:
        print("v10 error: %s" % exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
