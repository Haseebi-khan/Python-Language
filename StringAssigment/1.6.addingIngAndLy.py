# 6. Add ing or ly to a string.
# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing', add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


string  = input("Enter the string: ")

if len(string) < 3:
    result = string
else:
    if string[-3] == 'i' and string[-2] == 'n' and string[-1] == 'g':
        result = string + "ly"
    else:
        result = string + "ing"

print(result)
