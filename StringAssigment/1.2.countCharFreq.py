# 2. Count character frequency in a string.
# Write a Python program to count the number of characters
# (character frequency) in a string.

# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

string = "google.com"

dic = {}

for i in string:
    count = 0
    for j in range(len(string)):
        if i == string[j]:
            count += 1
    dic[i] = count

print(dic)

