# 7. Replace 'not'...'poor' with 'good'.
# Write a Python program to find the first appearance of 
# the substrings 'not' and 'poor' in a given string. 
# If 'not' follows 'poor', replace the whole 'not'...'poor' 
# substring with 'good'. Return the resulting string.

# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def ReplacingString(string):
    
    wordsList = string.split()
    notFound = False
    poorFound = False
    
    for i, word in enumerate(wordsList):
        if word == 'not':
            notIndex = i
            notFound = True
        if notFound and word.lower() == 'poor':
            poorIndex = i
            poorFound = True
            break
        
    if notFound and poorFound and notIndex < poorIndex :
        resultWords = wordsList[:notIndex] + ['good'] + wordsList[poorIndex+1:]
        result = " ".join(resultWords)
    else:
        result = string 
        
    return result + "!"
    
result =  ReplacingString("The lyrics is not that poor")

print(result)
