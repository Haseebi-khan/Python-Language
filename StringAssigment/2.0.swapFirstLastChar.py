# 10. Swap first and last chars of a string.
# Write a Python program to change a given string to a newly string where the first 
# and last chars have been exchanged.

def swapFirstAndLastChar(string):
    newString = string[-1]
    for char in string:
        if char == string[-1]:
            newString += string[0]
        else:
            newString += char
    
    return newString

string = "HaseebKhan"

print("Swaped String: ", swapFirstAndLastChar(string))

