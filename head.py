"""Implementing the tail shell command in python."""

import sys
from lib.helper import head, readfile

TEXT = None
ARG_CNT = len(sys.argv)

if ARG_CNT > 2:
    print("Usage: head.py <file>")

if ARG_CNT == 1:
    TEXT = sys.stdin.read()

if ARG_CNT == 2:
    filename = sys.argv[1]
    TEXT = readfile(filename)

head(TEXT)
