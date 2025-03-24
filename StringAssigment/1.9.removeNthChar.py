# 9. Remove nth character from a string.
# Write a Python program to remove the nth index character from a nonempty string.

def removeNthChar(nth: int, string: str):
    nthChar = string[nth]
    newStr = ""
    for i in range(0,len(string),1):
        if i == nth:
            continue
        newStr += string[i]
    
    return newStr
string = "MyNameIsHaseebKhan"
print("Original String: ",string)
print("Updated String: ", removeNthChar(8, string))
