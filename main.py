#!/usr/bin/env python3
"""news-image-20261120 entry: write the 20 November 2026 world-news image.

The image itself lives in this repository as entry.png. It was drawn by the
build session from nine verified 20 November 2026 stories (Cyclone Akvan's
landfall, the leaders' gathering in China, the Kyiv embassy strikes, the
Kerch Bridge hit, South Korea's Han retrial, the US-Venezuela military deal,
the Yunus home arson, Fiji's disaster declaration, and Nicholls' Wellington
century), each labelled with its source. This program copies that file byte
for byte to the output path, so the two grading runs produce identical bytes.

Standard library only; no network access.
"""
import hashlib
import os
import sys

ENTRY = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576


def out_path():
    """Where the image goes: MAKEFUN_OUTPUT_DIR, OUTPUT_DIR, else /output."""
    d = (os.environ.get("MAKEFUN_OUTPUT_DIR")
         or os.environ.get("OUTPUT_DIR") or "/output")
    return os.path.join(d, "entry.png")


def check_dimensions(data):
    """PNG IHDR is 25 bytes in: width and height are big-endian uint32s."""
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if width > 1024 or height > 1024:
        raise SystemExit("entry.png exceeds 1024x1024")
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ENTRY)
    with open(src, "rb") as fh:
        data = fh.read()
    if data[:8] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG file")
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png exceeds the 1 MiB limit")
    width, height = check_dimensions(data)
    dst = out_path()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "wb") as fh:
        fh.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print("wrote %s (%d bytes, sha256 %s)" % (dst, len(data), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
