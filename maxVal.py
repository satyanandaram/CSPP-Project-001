def findMaxVal(lst):
    max=0
    for i in range(len(lst)):
        if(max<lst[i]):
            max=lst[i]
    #print ("Maximum Value: ",max)
    return max
arr=[1,2,3,4,5,2,7,1]
print(findMaxVal(arr))
#prints 7 as output