"""Implementing the wc shell command in python."""

import sys

def wc(text):
    """
        will create a function of wc which takes text(i.e., content of the entire file)
        as a parameter
    """
    word_count = word_counts(text)
    char_count = char_counts(text)
    line_count = line_counts(text)
    byte_count = byte_counts(text)
    return [line_count, word_count, byte_count, char_count]

def word_counts(text):
    """
        returns the count of words a given file
    """
    list_of_words = text.split()
    return len(list_of_words)

def line_counts(text):
    """
        returns the count of lines a given file
    """
    list_of_lines = text.split("\n")
    return len(list_of_lines) - 1

def char_counts(text):
    """
        returns the count of character a given file
    """
    return len(text)

def byte_counts(text):
    """
        returns the count of bytes a given file
    """
    return len(text.encode('utf-8'))

def readfile(filename):
    """
        Reading the contents of a given file
    """
    try:
        file = open(filename)
        text = file.read()
        return text
    except FileNotFoundError:
        print("tail: cannot open", filename, "for reading: No such file or directory")


if __name__ == "__main__":
    TEXT = None
    ARG_CNT = len(sys.argv) - 1

    if ARG_CNT == 0:
        TEXT = sys.stdin.read()

    if ARG_CNT == 1:
        filename = sys.argv[1]
        TEXT = readfile(filename)

    response = wc(TEXT)
    print(" " + str(response[0]) + "  " + str(response[1]) + " " + str(response[2]))


