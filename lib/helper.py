"""Implementing the helper functions in python."""

import requests

def curl(url):
    """
        url will be passed as parameter to the wget function
        if given url is valid, function will download the content from url
        downloaded content will be written into file index.html
    """
    try:
        response = requests.get(url)
        return response.text
    except:
        return "curl: unable to resolve host address " + url

def cat(text):
    """
        Implementing the cat command functionality by defining a function
    """
    lines = text.splitlines()
    for i in range(len(lines)):
        print(lines[i])

def tac(text):
    """
        Implementing the tac command functionality by defining a function
    """
    lines = text.splitlines()
    for i in range(len(lines)-1, -1, -1):
        print(lines[i])

def tail(text, n_lines=10):
    """
        Implementing the tail command functionality by defining a function
    """
    if text:
        lines = text.splitlines()
        lines = lines[-n_lines:]
        return "\n".join(lines)

def head(text, n_lines=10):
    """
        Implementing the head command functionality by defining a function
    """
    if text:
        lines = text.splitlines()
        lines = lines[:n_lines]
        return "\n".join(lines)

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
