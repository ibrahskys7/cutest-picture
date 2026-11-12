#!/usr/bin/env python3
"""Make the cutest picture (make.fun bounty cutest-picture-01).

Writes the bundled picture to /output/entry.png.

The picture -- a fluffy white kitten with big blue eyes sitting in a
basket of pastel flowers -- is stored in this repository as kitten.png.
This program copies it byte-for-byte to /output/entry.png, so every run
writes identical bytes. No network is used.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "kitten.png")
DST = "/output/entry.png"


def main() -> None:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote %s (%d bytes)" % (DST, os.path.getsize(DST)))


if __name__ == "__main__":
    main()
