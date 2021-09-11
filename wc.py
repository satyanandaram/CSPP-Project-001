"""Implementing the wc shell command in python."""

import sys

from lib.helper import wc, readfile

TEXT = None
ARG_CNT = len(sys.argv) - 1

if ARG_CNT == 0:
    TEXT = sys.stdin.read()

if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)

response = wc(TEXT)
print(" " + str(response[0]) + "  " + str(response[1]) + " " + str(response[2]))