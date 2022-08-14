lst = ["a", "b", 1, 2] 
# declaring a lst list variable, lists can have mixed types
print(lst[1]) # Indexing - Prints "b"

s = "" # declaring empty string variable
for i in range(len(lst)):
#declaring for looping control statement with range function
# The range function generates values with in the range of parameter value	
    s = s + str(lst[i])
	#Accessing list value using indexing then concatinating value to string variable
print(s)
#prints string variable value as output
