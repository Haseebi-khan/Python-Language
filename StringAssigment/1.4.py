# 4. Replace first char occurrences with $.
# Write a Python program to get a string from a given string 
# where all occurrences of its first char have been changed to '$', 
# except the first char itself.
 
# Sample String : 'restart'
# Expected Result : 'resta$t'

string = 'restart'
firstChar = string[0]
result = firstChar
for char in string[1:]:
    if char == firstChar:
        result += "$"
    else:
        result += char

print(result)


