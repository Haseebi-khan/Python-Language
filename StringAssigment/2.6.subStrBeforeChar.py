# 19. Get substring before a specific character.
# Write a Python program to get the last part of a string
# before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python


string = "remote: Resolving deltas: 100% (2/2), completed with 2 local objects."
newString = string.split(",")
subString = newString[1]
print(subString)
