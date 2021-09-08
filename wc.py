import sys,os

def wc(file_data):
    """will create a function of wc which takes file_data(i.e., content of the entire file) 
    as a parameter"""
    word_count = word_counts(file_data)
    char_count = char_counts(file_data)
    line_count = line_counts(file_data)
    byte_count = byte_counts(file_data)
    return(line_count,word_count, byte_count,char_count)

def word_counts(file_data): 
    list_of_words = file_data.split()
    return len(list_of_words)

def line_counts(file_data):
    list_of_lines = file_data.split("\n")
    return len(list_of_lines) - 1

def char_counts(file_data):
    return len(file_data)

def byte_counts(s):
    return len(s.encode('utf-8'))

if len(sys.argv) == 1:
    value = sys.stdin.read()
    for i in wc(value)[:3]:
        print(i,end=" ")
    print()
else:
    try:
        open_file = open(sys.argv[1],'r')    
        for i in wc(open_file.read())[:3]:
            print(i,end=" ")
        print(sys.argv[1])
    except FileNotFoundError:
        print("wc: No such file or directory")
