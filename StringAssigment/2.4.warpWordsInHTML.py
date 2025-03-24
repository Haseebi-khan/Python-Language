# 15. Wrap word(s) in HTML tags.
# Write a Python function to create an HTML string 
# with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def add_tags(tag, string):
    HTMLString = ""
    HTMLString += "<" + tag + ">" + string + "</" + tag + ">"
    
    return HTMLString

print(add_tags("i" , "Python"))