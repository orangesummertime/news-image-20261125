#!/usr/bin/env python3
"""news-image-20261125 entry: copy the front-page image to /output/entry.png.

Standard library only. No network, no randomness: the same bytes are
written on every run, so the program's two grading runs agree. The copy
is verified byte-for-byte before the program exits, so a partial write
can never pass as a finished entry. The source is validated as a whole
PNG first, so a corrupt or oversize image fails loudly here instead of
being copied to /output and failing the grading runs opaquely.
"""
import os
import shutil
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
PNG_IEND_TRAILER = bytes.fromhex("0000000049454e44ae426082")
MAX_IMAGE_BYTES = 1048576


def _validate_png(data):
    """Refuse a corrupt or oversize source before anything is copied.

    The competition requires a whole PNG of at most 1 MiB: a truncated
    source must fail loudly here instead of being copied to /output.
    """
    if len(data) > MAX_IMAGE_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("entry.png is not a PNG file")
    if not data.endswith(PNG_IEND_TRAILER):
        raise SystemExit("entry.png is truncated: missing IEND trailer")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    _validate_png(data)
    shutil.copyfile(src, dst)
    os.chmod(dst, 0o644)
    with open(src, "rb") as f:
        expected = f.read()
    with open(dst, "rb") as f:
        actual = f.read()
    if actual != expected:
        print(f"copy mismatch: {dst} differs from {src}", file=sys.stderr)
        raise SystemExit(1)
    print(f"wrote {dst} ({len(actual)} bytes, verified)", file=sys.stderr)


if __name__ == "__main__":
    main()
