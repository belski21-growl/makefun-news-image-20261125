"""Ship the pinned newspaper picture for news-image-20261125 (v8).

The repository carries one picture, entry.png, next to this file.
This runner is the only way the picture reaches the grader: it
checks the bundled file against a pinned fingerprint first, then
copies it into the output directory and checks the copy again.
Anything that is not byte-for-byte the v8 picture is refused,
and a bundled file that matches an earlier shipped round is
named by that round so a stale checkout explains itself.

The v8 picture itself is unchanged from the first v8 build.
Two slots were re-reported for this round (the Ras Tanura
refinery claim in slot #6 and the Australia LGBTQ-veterans
apology in slot #14), the region bar still totals 34 stories,
and only the fingerprint below moved with the new bytes.

Standard library only, no network, no secrets, deterministic
output: the bytes written are the repository bytes, so two runs
in two different directories produce identical files. Running
with --verify-only performs every check and prints the same
summary without writing anything. License: MIT. """

import os, sys
from argparse import ArgumentParser
from collections import namedtuple
from hashlib import sha256
from pathlib import Path
from shutil import copyfile

# Exit codes the shell sees.
OK = 0
FAIL = 1

# The bundled picture's name, and the name it keeps in the output dir.
FILE_NAME = "entry.png"

# Gate the picture must satisfy: 1024 by 1024, at most a mebibyte.
WANT_WIDTH = 1024
WANT_HEIGHT = 1024
SIZE_LIMIT = 1024 * 1024

# Fingerprint of the v8 picture - this runner ships exactly these bytes.
EXPECTED_BYTES = 324007
EXPECTED_DIGEST = "5fd850f8bcd788081b3dfc36466e25ae5ee7ddc1ef5f93ab298d2e0a41ce934a"

# Pictures shipped in earlier rounds, keyed by (size, sha256), so a
# stale bundled file can be named by its round when it is refused.
STALE = {
    (325798, "4967825d8cf7ba7e29f8f7815c8fc2cda0fc26af27f94cd4d0b705e78b689a7a"): "v6",
    (322851, "8e07008437dd49cc8e494b0b493e496faddae40da4a3d9f5a233802864285a97"): "v5",
    (272076, "4edbd9944d3a228978d479f762b8c0c4c55667575fd5311fa9d51e703c5c64ed"): "v4",
    (276540, "df4a30ca10053c6005b37b0c2a82dbddd0d1699f2f7f50f8f857df5fab136f6c"): "v3",
    (270327, "30b59778c802cccfe743db3e40263e668636f418f9e8d037b47537c928759ae2"): "v2",
    (263286, "0639ce21ed82f2df9019d1a5b47dc49ec503a492adb0d90966c35d888e842577"): "v1",
}

# Bytes pulled per read while hashing.
CHUNK = 64 * 1024

# Magic bytes opening the two picture formats the gate accepts.
PNG_HEAD = b"\x89PNG\r\n\x1a\n"
JPEG_HEAD = b"\xff\xd8\xff"

# One measured picture: byte count, sha256 hex, format, pixel size.
Scan = namedtuple("Scan", "nbytes digest kind width height")


class GateError(Exception):
    """A gate check failed; the message is the error line to print."""


def sniff(head):
    """Name the picture format from its opening bytes, or ""."""
    found = ""
    if head.startswith(PNG_HEAD):
        found = "PNG"
    elif head.startswith(JPEG_HEAD):
        found = "JPEG"
    return found


def png_size(head):
    """Width and height from a PNG IHDR chunk, or nothing."""
    if len(head) < 33 or head[:8] != PNG_HEAD:
        return
    if head[12:16] != b"IHDR":
        return
    w = int.from_bytes(head[16:20], "big")
    h = int.from_bytes(head[20:24], "big")
    return w, h


def jpeg_size(head):
    """Width and height from a JPEG's first start-of-frame marker.

    Steps through the marker segments from the start of the file:
    standalone markers are stepped over, segments carrying a length
    are jumped whole, and the first frame marker gives the size.
    Baseline, extended-sequential and progressive frames all count. """
    if len(head) < 4 or head[:2] != JPEG_HEAD[:2]:
        return
    i = 2
    while i + 9 <= len(head):
        if head[i] == 0xFF:
            code = head[i + 1]
            if code in (0xC0, 0xC1, 0xC2):
                return (int.from_bytes(head[i + 7:i + 9], "big"),
                        int.from_bytes(head[i + 5:i + 7], "big"))
            if code in (0xD8, 0xD9, 0x01) or 0xD0 <= code <= 0xD7:
                i += 2
            else:
                i += 2 + int.from_bytes(head[i + 2:i + 4], "big")
        if head[i] != 0xFF:
            i += 1
    return


def measure(head):
    """Format plus (width, height) for a picture header sample."""
    kind = sniff(head)
    if not kind:
        raise GateError("bundled picture opens with neither PNG nor JPEG magic")
    if kind == "PNG":
        wh = png_size(head)
    else:
        wh = jpeg_size(head)
    if wh is None:
        raise GateError("picture header gives no readable dimensions")
    return kind, wh


def hash_file(path):
    """Hash and measure one file in a single streaming pass.

    The first chunk read doubles as the header sample, so format
    and dimensions come from bytes already in hand. """
    hasher = sha256()
    n = 0
    head = b""
    try:
        with open(path, "rb") as fh:
            while (block := fh.read(CHUNK)):
                if not head:
                    head = block
                hasher.update(block)
                n += len(block)
    except OSError as err:
        raise GateError("cannot read %s (%s)" % (path, err)) from err
    if n == 0:
        raise GateError("bundled picture is empty")
    kind, wh = measure(head)
    return Scan(n, hasher.hexdigest(), kind, wh[0], wh[1])


def stale_tag(scan):
    """Round label if this scan is an earlier shipped picture."""
    return STALE.get((scan.nbytes, scan.digest))


def check_scan(scan):
    """Reject any scan that is not the pinned v8 picture, exactly."""
    if (scan.width, scan.height) != (WANT_WIDTH, WANT_HEIGHT):
        raise GateError("picture is %dx%d, gate wants %dx%d"
                        % (scan.width, scan.height, WANT_WIDTH, WANT_HEIGHT))
    if scan.nbytes > SIZE_LIMIT:
        raise GateError("picture is %d bytes, over the 1 MiB cap" % scan.nbytes)
    if scan.nbytes != EXPECTED_BYTES or scan.digest != EXPECTED_DIGEST:
        tag = stale_tag(scan)
        if tag:
            raise GateError("bundled picture is the old %s ship (%d bytes, sha256 %s); "
                            "this runner only accepts pinned v8 (%d bytes, sha256 %s)"
                            % (tag, scan.nbytes, scan.digest,
                               EXPECTED_BYTES, EXPECTED_DIGEST))
        raise GateError("bundled picture fingerprint does not match pinned v8 "
                        "(%d bytes, sha256 %s)"
                        % (EXPECTED_BYTES, EXPECTED_DIGEST))


def output_dir():
    """Where the grader wants the picture, or /output by default."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return chosen if chosen else "/output"


def report(scan, shipped):
    """Print the check summary for a scanned picture."""
    print("entry.png - %d bytes, %s, %dx%d"
          % (scan.nbytes, scan.kind, scan.width, scan.height))
    print("sha256 %s" % scan.digest)
    if shipped:
        print("copy verified: size, sha256, magic and dimensions all match the pinned v8 picture")
    if not shipped:
        print("verify-only: fingerprint matches pinned v8, nothing written")


def parse_cli(argv):
    """Command line: the only flag is --verify-only."""
    parser = ArgumentParser(
        prog="main.py",
        description="Ship the pinned v8 entry.png into the output directory.")
    parser.add_argument("--verify-only", action="store_true", help="only check the bundled picture, do not copy it")
    parsed = parser.parse_args(argv)
    return parsed


def main(argv=None):
    """Check the bundled picture, then copy it unless --verify-only.

    Returns 0 on success and 1 on any failure, with the reason on
    stderr. The copy is hashed again after it is written and must
    agree with the bundled picture on every field before the run
    is reported as verified. """
    opts = parse_cli(argv)
    here = Path(__file__).resolve().parent
    bundled = here / FILE_NAME
    try:
        scan = hash_file(bundled)
        check_scan(scan)
    except GateError as err:
        print("error: %s" % err, file=sys.stderr)
        return FAIL
    if opts.verify_only:
        report(scan, shipped=False)
        return OK
    dest = Path(output_dir())
    dest.mkdir(parents=True, exist_ok=True)
    target = dest / FILE_NAME
    copyfile(bundled, target)
    try:
        again = hash_file(target)
    except GateError as err:
        print("error: written copy unreadable: %s" % err, file=sys.stderr)
        return FAIL
    if again != scan:
        print("error: written copy differs from the bundled picture", file=sys.stderr)
        return FAIL
    report(again, shipped=True)
    return OK


if __name__ == "__main__":
    raise SystemExit(main())
