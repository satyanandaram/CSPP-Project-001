"""Implementing the tail shell command in python."""

import sys
from lib.helper import tail, readfile

TEXT = None
ARG_CNT = len(sys.argv) - 1

if ARG_CNT == 0:
    TEXT = sys.stdin.read()

if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)

if ARG_CNT > 1:
    print("Usage: tail.py <file>")

print(tail(TEXT))
