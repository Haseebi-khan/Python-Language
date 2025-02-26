dic = {}
dic1 = {1:'one', 2:'two'}
dic[4]="This can be new Thing."
dic["three"] = "This can also be new Thing."

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values
print("\n\n")
print (dic.keys()) # Prints all the values
print (dic.values()) # Prints all the values
print("\n\n")

print(dic)


# set = {[34,23,"dfd",34], 12, 3.3, (45,33)}
# print(set)

# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# File d:\Codes\Python\Python-Language\1.5.Dictionary .py:1
# ----> 1 set = {[34,23,"dfd",34], 12, 3.3, (45,33)}
#       2 print(set)

# TypeError: unhashable type: 'list'

set = {4,3,2,"Python code" , 4+4j}
print(set)
print(type(set))
