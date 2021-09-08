"""Implementing the tail shell command in python."""

import sys
from lib.helper import tail, readfile

TEXT = None
ARG_CNT = len(sys.argv)

if ARG_CNT > 2:
    print("Usage: tail.py <file>")

if ARG_CNT == 1:
    TEXT = sys.stdin.read()

if ARG_CNT == 2:
    filename = sys.argv[1]
    TEXT = readfile(filename)

print(tail(TEXT))
