"""
create a new variable file and read the contents of the file
and assign it to a variable "file" In order to read the contents
of the file we are making use of the
"""
import sys
from lib.helper import is_valid_file, cut


FLAG = True
nums = []
for argNum in range(1, len(sys.argv)):
    nums += sys.argv[argNum].split(",")

if ".tsv" in nums[-1]:
    FLAG = is_valid_file()
    nums.pop()


if '0' in nums:
    print("cut: fields are numbered from 1")
    FLAG = False

else:
    columns = []
    for i in nums[1:]:
        try:
            elem = int(i)
            columns.append(elem)
        except:
            FLAG = False
            print("cut: invalid field value "+i)
            break

if FLAG:
    try:
        file_pointer = open(sys.argv[-1], "r")
        TEXT = file_pointer.read()
    except:
        TEXT = sys.stdin.read()
    cut(TEXT, columns)
