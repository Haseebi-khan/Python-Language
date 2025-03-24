# 8. Find longest word in a list.
# Write a Python function that takes a list of words and 
# return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

def findLongestWord(List):

    print(type(List))
    length = -1
    longestword = ""

    for word in List: 
        if len(word) > length:
            length = len(word)
            longestword = word
            
    return f"Longest List Word: {longestword} with the length: {length}."

List = ["haseeb", "za", "new", "Moremoereds"]
print ( findLongestWord(List))
