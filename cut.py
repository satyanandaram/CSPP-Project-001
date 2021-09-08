import sys
# create a new variable file and read the contents of the file and assign it to a variable "file"
# In order to read the  contents of the file we are making use of the 

def cut(fileContent, cols, delim="\t"):
    lst = fileContent.split("\n")
    for i in lst:
        for j in cols:
            if int(j) > len(i.split(delim)):
                continue
            print(i.split(delim)[int(j)-1],end=delim)
        print()


def isValidFile():
    try:
        file= open(sys.argv[-1], "r")
        file.close()
        return True
    except:
        print("cut: "+sys.argv[-1]+": No such file or directory")
        return False


flag=True
nums=[]
for argNum in range(1,len(sys.argv)):
    nums += sys.argv[argNum].split(",")

if ".tsv" in nums[-1]:
    flag = isValidFile()
    nums.pop()


if '0' in nums:
    print("cut: fields are numbered from 1")
    flag = False

else:
    columns = []
    for i in nums[1:]:
        try:
            elem = int(i)
            columns.append(elem)
        except:
            flag = False
            print("cut: invalid field value "+i)
            break

if (flag):
    try:
        file = open(sys.argv[-1], "r")
        fileContent = file.read()
    except:
        fileContent = sys.stdin.read()
    cut(fileContent,columns)
