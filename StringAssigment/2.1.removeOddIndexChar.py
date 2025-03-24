# 11. Remove odd index chars from a string.
# Write a Python program to remove characters that
# have odd index values in a given string.

def rmOddIndexChar(string):
    newString = ""
    for i in range(0,(len(string)-1)):
        if i % 2 == 0:
            newString += string[i]
        
    return newString    

string = "Connected to Python"
print(rmOddIndexChar(string))