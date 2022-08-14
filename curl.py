"""The python code helps to read the command line input for curl method."""

import sys
# the import keyword imports the given pre-defined library sys
from lib.helper import curl
#the import keyword imports the given pre-defined libraries curl from lib.helper
URL = None
#The declared URL variable assigned with a value None
ARG_CNT = len(sys.argv) - 1
#Declaring ARG_CNT variable and assigning length of the command line argument as a value
if ARG_CNT != 1:
# Declaring if conditional block by comparing ARG_CNT variable's value       
    print('Usage: curl [URL]...')
    #If the condition satisfies or if we didn't provide URL as input during the execution time
    #the print function will display the above message

if ARG_CNT == 1:
 # Declaring if conditional block by comparing ARG_CNT variable's value
 # if we give URL as an input, this if block will be activate   
    URL = sys.argv[1]
    #The URL variable will get the value from commandline during the execution time
    if 'http' not in URL[:5]:
    # declaring a conditional block to check the given url is starting with http or not
        URL = "http://"+URL
        #If the url is not having http, we are concatinating the http to the URL variable
    print(curl(URL))
    #The print function will activate the linux curl command which takes url is an an argument

