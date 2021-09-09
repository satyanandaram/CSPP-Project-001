import sys,os

from lib.helper import wc

if len(sys.argv) == 1:
    value = sys.stdin.read()
    for i in wc(value)[:3]:
        print(i,end=" ")
    print()
else:
    try:
        open_file = open(sys.argv[1],'r')    
        for i in wc(open_file.read())[:3]:
            print(i, end=" ")
        print(sys.argv[1])
    except FileNotFoundError:
        print("wc: No such file or directory")
