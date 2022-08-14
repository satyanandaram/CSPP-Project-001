"""Implementing the tail shell command in python."""

import sys
# The import keyword imports the given pre-defined library sys
from lib.helper import tail, readfile
#the import keyword imports the given pre-defined libraries head, readfile from lib.helper
TEXT = None
#The declared TEXT variable assigned with a value None
ARG_CNT = len(sys.argv) - 1
#Declaring ARG_CNT variable and assigning length of the command line argument as a value
if ARG_CNT == 0:
    # declaring if conditional block by comparing ARG_CNT variable's value
    TEXT = sys.stdin.read()
    #Assigning system's input value to TEXT Variable 
if ARG_CNT == 1:
    # Declaring if conditional block by comparing ARG_CNT variable's value
    filename = sys.argv[1]
    #Assigning commandline argument value to filename variable. 
    #The filename variable will contains the given file path
    TEXT = readfile(filename)
#The TEXT variable will get the data through readfile function which takes file name as an argument.
if ARG_CNT > 1:
    #Declaring if conditional block by comparing ARG_CNT variable's value
    print("Usage: tail.py <file>")
#If the condition satisfies or if we didn't provide file name as input during the execution time
    #the program will prints the above error message
print(tail(TEXT))
# The print function will activate the head command and pass the TEXT to head command which belongs to the linux shell
# The print function will print the last 10 lines from given file as an argument
