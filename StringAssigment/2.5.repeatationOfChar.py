# 17. Repeat last 2 chars of a string 4 times.
# Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

def repeatOfLastChar(string, time = 4):
    lastChars = string[-2] + string[-1]
    newString = ""
    for i in range(0,time):
        newString += lastChars
    print(newString)
    
    pass

repeatOfLastChar("python")
repeatOfLastChar("Exercises")
