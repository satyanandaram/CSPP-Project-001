"""Implementing the wc shell command in python."""

import sys
# The import keyword imports the given pre-defined library sys
def wc(text):
    """
        will create a function of wc which takes text(i.e., content of the entire file)
        as a parameter
    """
    word_count = word_counts(text)
    #declaring word_count variable which gets the value from word_count user defined function
    char_count = char_counts(text)
    #declaring char_count variable which gets value from char_count user defined function
    line_count = line_counts(text)
    #declaring line_count variable which gets value from line_count user defined function
    byte_count = byte_counts(text)
    #declaring byte_count variable which gets values from byte_counts user defined function
    return [line_count, word_count, byte_count, char_count]
    #the current function returns the list of values

def word_counts(text):
    """
        returns the count of words a given file
    """
    list_of_words = text.split()
    #declaring list_of_words variable which gets list of words from text.split() predefined function
    #The split function will split the words based on delimeter. The default delimeter is space for given text
    return len(list_of_words)
    #returns the length of the list of words.

def line_counts(text):
    """
        returns the count of lines a given file
    """
    list_of_lines = text.split("\n")
    #declaring list_of_lines variable. 
    #The text.split() function is having a delimeter ("\n")
    #The text will be split into lines
    return len(list_of_lines) - 1
    # returns the length of list of lines
def char_counts(text):
    """
        returns the count of character a given file
    """
    return len(text)
    # returns the length of the text

def byte_counts(text):
    """
        returns the count of bytes a given file
    """
    return len(text.encode('utf-8'))
    #returns the length of the unicode bytes

def readfile(filename):
    """
        Reading the contents of a given file
    """
    try: 
# Declaring a try block to handle the abnormal situations like not getting file as an input
        file = open(filename)
        #declaring file variable which knows the file path and able to open the file
        text = file.read()
        #declaring a text variable which can able to get the text from the read function
        return text
        # returns the text 
    except FileNotFoundError:
        print("tail: cannot open", filename, "for reading: No such file or directory")
        #if any exception occured, this except block will be executes and program won't be terminate

if __name__ == "__main__":
# Declaring if conditional block. 
#Its a main function
    TEXT = None
    #The declared TEXT variable assigned with a value None
    ARG_CNT = len(sys.argv) - 1
#Declaring ARG_CNT variable and assigning length of the command line argument as a value
    if ARG_CNT == 0:
        # declaring nested if conditional block by comparing ARG_CNT variable's value
        TEXT = sys.stdin.read()
        #Assigning system's input value to TEXT Variable 
    if ARG_CNT == 1:
    # Declaring if conditional block by comparing ARG_CNT variable's value  
        filename = sys.argv[1]
        #Assigning commandline argument value to filename variable. 
        #The filename variable will contains the given file path
        TEXT = readfile(filename)
        #The TEXT variable will get the data through readfile function which takes file name as an argument.
    response = wc(TEXT)
    #declaring a list variable named response which gets data from the wc function defined in this file. 
    print(" " + str(response[0]) + "  " + str(response[1]) + " " + str(response[2]) + " " +str(response[3]))
    # printing desired output from the response variable


