# 5. Swap first 2 chars of 2 strings.
# Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'


string, string2 = "abc", "xyz"
new_string = ""
new_string2 = ""

j = 0

for i in range(3):
    if i < 2:
        new_string += string2[i]
        new_string2 += string[i]
    else:
        new_string += string[i]
        new_string2 += string2[i]

string = new_string
string2 = new_string2

print(string)
print(string2)
