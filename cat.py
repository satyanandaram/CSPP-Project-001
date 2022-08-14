"""Implementing the cat shell command in python."""

import sys
# the import keyword imports the given pre-defined library sys
from lib.helper import cat, readfile
#the import keyword imports the given pre-defined libraries cat, readfile from lib.helper
TEXT = None
#The declared TEXT variable assigned with a value None
ARG_CNT = len(sys.argv) - 1
#Declaring ARG_CNT variable and assigning length of the command line argument as a value
if ARG_CNT == 0:
#declaring if conditional block by comparing ARG_CNT variable's value
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
    print(sys.argv[0], "doesn't handle more than one argument")
    #If the condition satisfies or if we didn't provide file name as input during the execution time
    #the program will prints the above error message
print(cat(TEXT))
# The print function will activate the cat command and pass the TEXT to cat command which belongs to the linux shell 
