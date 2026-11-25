"""news-image-20261125 entry program (v6).

Copies the pre-built newspaper image (entry.png, 1024x1024) to the
output directory as entry.png, verifying integrity (size, SHA-256 and
image magic bytes) before and after the copy.

v6: Goldfish-r5 micro-fix. Of the v5 tally, #30 Blanche-Nvidia FAILED
(presser Tue 24 Nov; BBC published 2026-11-24T21:45:46Z) and #19 Guam
El Nino was grey-leaning-fail (substance 18-24 Nov); both replaced
with primary-verified 25 Nov stories (#30 German GDP +0.1% in Q3 /
Reuters 2026-11-25T07:01:40Z; #19 Japan services inflation +4.2% /
Reuters, slug 2026-11-25). Region bar rebalanced to APAC 23, AMERICAS
2, EUROPE 6, MIDDLE EAST 1, AFRICA 2 (= 34); #15 headline softened
("first in 5 months" dropped — not in the AJP body); map pins 9-10 /
4-5 widened so their labels fit; footer exclusions updated with the
v6 research (Blanche, Guam, UN femicide brief, Sarkozy-Bruni trial
order, N. Korea Christians report). Numbers strip untouched (no
figure came from #19/#30). This program pins the v6 fingerprint
(EXPECTED_SHA256 / EXPECTED_SIZE) and refuses to ship any other
bytes, so a stale v5 image can never be submitted by mistake.

Deterministic: the output bytes are exactly the repository bytes, so
both grader runs write identical files. Standard library only, no
network access, no environment secrets.

SPDX-License-Identifier: MIT
"""

import hashlib
import os
import shutil
import sys

# Magic bytes for the two image formats the gate accepts.
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"

# Entry image shipped in this repository, next to this file.
SOURCE_NAME = "entry.png"

# Output file name required by the competition.
OUTPUT_NAME = "entry.png"

# The gate requires a 1024x1024 image (<=1 MiB). The entry image must
# match exactly; a wrong-size image is rejected here, never shipped.
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024

# v6 pinned fingerprint (entry.png rebuilt 25 Nov 2026 ~07:35 UTC after the
# Goldfish-r5 micro-fix). Any other bytes are rejected.
EXPECTED_SIZE = 325798
EXPECTED_SHA256 = "4967825d8cf7ba7e29f8f7815c8fc2cda0fc26af27f94cd4d0b705e78b689a7a"

# Known stale fingerprints: (size, sha256, version). If the source image
# matches one of these, the error names the stale version explicitly so a
# wrong-version image is never silently shipped as v6.
PREVIOUS_FINGERPRINTS = (
    (322851,
     "8e07008437dd49cc8e494b0b493e496faddae40da4a3d9f5a233802864285a97",
     "v5"),
    (272076,
     "4edbd9944d3a228978d479f762b8c0c4c55667575fd5311fa9d51e703c5c64ed",
     "v4"),
    (276540,
     "df4a30ca10053c6005b37b0c2a82dbddd0d1699f2f7f50f8f857df5fab136f6c",
     "v3"),
    (270327,
     "30b59778c802cccfe743db3e40263e668636f418f9e8d037b47537c928759ae2",
     "v2"),
    (263286,
     "0639ce21ed82f2df9019d1a5b47dc49ec503a492adb0d90966c35d888e842577",
     "v1"),
)


def _jpeg_dimensions(path):
    """Return (width, height) from a JPEG's first SOF segment, else None."""
    with open(path, "rb") as handle:
        data = handle.read(65536)
    if len(data) < 4 or data[:2] != JPEG_MAGIC[:2]:
        return None
    pos = 2
    while pos + 9 < len(data):
        if data[pos] != 0xFF:
            pos += 1
            continue
        marker = data[pos + 1]
        if marker in (0xC0, 0xC1, 0xC2):  # SOF0/1/2: height(2) width(2)
            height = int.from_bytes(data[pos + 5:pos + 7], "big")
            width = int.from_bytes(data[pos + 7:pos + 9], "big")
            return width, height
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        seg_len = int.from_bytes(data[pos + 2:pos + 4], "big")
        pos += 2 + seg_len
    return None


def _png_dimensions(path):
    """Return (width, height) from a PNG IHDR chunk, else None."""
    with open(path, "rb") as handle:
        head = handle.read(33)
    if len(head) < 33 or not head.startswith(PNG_MAGIC):
        return None
    if head[12:16] != b"IHDR":
        return None
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    return width, height


def _dimensions(path):
    """Return (width, height) for a PNG or JPEG file, else None."""
    dims = _png_dimensions(path)
    if dims is not None:
        return dims
    return _jpeg_dimensions(path)


def _fingerprint(path):
    """Return (size_in_bytes, sha256_hexdigest, magic_ok) for a file."""
    digest = hashlib.sha256()
    size = 0
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(65536)
            if not chunk:
                break
            size += len(chunk)
            digest.update(chunk)
    with open(path, "rb") as handle:
        head = handle.read(8)
    magic_ok = head.startswith(PNG_MAGIC) or head.startswith(JPEG_MAGIC)
    return size, digest.hexdigest(), magic_ok


def _output_dir():
    """Grader output dir: MAKEFUN_OUTPUT_DIR, else /output, else ./out."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main(argv=None):
    verify_only = argv is not None and "--verify-only" in argv
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    out_dir = _output_dir()
    if not verify_only:
        os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, OUTPUT_NAME)

    src_size, src_sha, src_magic = _fingerprint(source)
    if src_size == 0:
        print("error: source image is empty", file=sys.stderr)
        return 1
    if src_size > 1048576:
        print("error: source image exceeds 1 MiB", file=sys.stderr)
        return 1
    if not src_magic:
        print("error: source is not a PNG or JPEG", file=sys.stderr)
        return 1
    src_dims = _dimensions(source)
    if src_dims is None:
        print("error: cannot read source image dimensions", file=sys.stderr)
        return 1
    if src_dims != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        print("error: source is %dx%d, expected %dx%d" % (
            src_dims[0], src_dims[1], EXPECTED_WIDTH, EXPECTED_HEIGHT),
            file=sys.stderr)
        return 1
    if src_size != EXPECTED_SIZE or src_sha != EXPECTED_SHA256:
        for old_size, old_sha, old_ver in PREVIOUS_FINGERPRINTS:
            if src_size == old_size and src_sha == old_sha:
                print("error: source is stale %s (%d bytes sha256 %s); "
                      "expected v6 %d bytes sha256 %s"
                      % (old_ver, old_size, old_sha,
                         EXPECTED_SIZE, EXPECTED_SHA256), file=sys.stderr)
                return 1
        print("error: source fingerprint mismatch: expected v6 %d bytes "
              "sha256 %s" % (EXPECTED_SIZE, EXPECTED_SHA256), file=sys.stderr)
        return 1

    if verify_only:
        print("entry.png: %d bytes" % src_size)
        print("sha256: %s" % src_sha)
        print("dimensions: %dx%d" % src_dims)
        print("fingerprint: matches pinned v6 (size + sha256)")
        print("verified: size + sha256 + magic + dimensions OK (no copy)")
        return 0

    shutil.copyfile(source, target)

    dst_size, dst_sha, dst_magic = _fingerprint(target)
    if (dst_size, dst_sha, dst_magic) != (src_size, src_sha, src_magic):
        print("error: output does not match source", file=sys.stderr)
        return 1
    dst_dims = _dimensions(target)
    if dst_dims != src_dims:
        print("error: output dimensions changed", file=sys.stderr)
        return 1

    with open(target, "rb") as handle:
        is_png = handle.read(4) == PNG_MAGIC[:4]
    print("entry.png: %d bytes" % dst_size)
    print("sha256: %s" % dst_sha)
    print("format: %s" % ("PNG" if is_png else "JPEG"))
    print("dimensions: %dx%d" % dst_dims)
    print("verified: size + sha256 + magic + dimensions match source")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
