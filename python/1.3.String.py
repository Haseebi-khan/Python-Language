# string is IMMUTEABLE

string = str("Haseeb khan")
print(string)
print(string[2:5])
print(string[0:])
print(string[1])
print(string[0])
print(string*2)
print(string + "4")

# 1. Calculate string length.

# Write a Python program to calculate the length of a string.
# Click me to see the sample solution

string2 = str("abcdefg")
print(len(string2))


newString = 'the is String 1'
newString2 = "the is String 1"
newString3 = '''the is String 1'''


newString4 = "the is 'String' 1"
newString5 = '''the is "String" 1'''

# \n     it escape sequence characte

newString6 = newString3  + " " + newString5

print(newString6)



# ---------------------------------------------------------------------------

# Index Assignment is not allowed in python. such as 

newString[5] = "@"

print(newString)

# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# File d:\Codes\Python\Python-Language\1.3.String.py:17
#      13 print(newString6)
#      15 # Index Assignment is not allowed in python. such as 
# ---> 17 newString[5] = "@"
#      19 print(newString)

# TypeError: 'str' object does not support item assignmen

# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Both are same accessing till last character of the string. 
# ---------------------------------------------------------------------------

print(newString[5:])
print(newString[5:len(newString)])

# ---------------------------------------------------------------------------


newString = 'the is String 1.'
print(newString.endswith("."))


# ---------------------------------------------------------------------------
# it will not change the original string.
# ---------------------------------------------------------------------------
print(newString.capitalize())
print(newString)
 
# ---------------------------------------------------------------------------
# To change the original string.
# ----------------------------------------------------------------
newString = newString.capitalize()
print(newString)

newString.replace('i', 'e')
print(newString)

print(newString.replace('i', 'e'))

# ----------------------------------------------------------------
# find Func return the starting index of the word or character.
# ----------------------------------------------------------------
print(newString.find('st'))

# ----------------------------------------------------------------
# count Func counts the string of the sun string.
# ----------------------------------------------------------------

print(newString)
print(newString.count('i'))


name = input(str("Enter your name: "))
print(len(name))