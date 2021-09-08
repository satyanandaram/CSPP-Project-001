"""
    The python code helps to read the command line input for curl method.
"""

import sys
from lib.helper import curl

if len(sys.argv) != 2:
    print('Usage: curl [URL]...')

if len(sys.argv) == 2:
    url = sys.argv[1]
    if 'http' not in url[:5]:
        url = "http://"+url
    print(curl(url))
