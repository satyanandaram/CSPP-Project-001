"""
    The python code helps to read the command line input for curl method.
"""

import sys
from lib.helper import curl

URL = None
ARG_CNT = len(sys.argv) - 1

if ARG_CNT != 1:
    print('Usage: curl [URL]...')

if ARG_CNT == 1:
    URL = sys.argv[1]
    if 'http' not in URL[:5]:
        URL = "http://"+URL
    print(curl(URL))
