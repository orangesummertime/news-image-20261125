#!/usr/bin/env python3
"""news-image-20261125 entry: copy the front-page image to /output/entry.png.

Standard library only. No network, no randomness: the same bytes are
written on every run, so the program's two grading runs agree. The copy
is verified byte-for-byte before the program exits, so a partial write
can never pass as a finished entry.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
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
