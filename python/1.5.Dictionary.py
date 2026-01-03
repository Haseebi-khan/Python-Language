# Dictionary is unordered, dic are mutable and dont allow duplicate keys.
# but dictionary key are immutable.


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



dic = {}
dic['name'] = "Haseeb Khan"
dic["age"] = 21
dic[1] = "0344543534345"

print(dic)

dic[1] = 4334

print(dic)
 
# Nested Dictionary is also possible.

nestedDic = {
    "name" : "haseeb khan",
    "age" : 32,
    "grades" : {
        "PF" : 65, 'english' : 56, "math" : {
            "calculus 1" : 77, 'calculus 2' : 98,
            "calculus 3" : 50, "Linear Algibra": 78
        }, "OPP" : 45
    }
}  

print(nestedDic.keys())
print(nestedDic["grades"].keys())


print(nestedDic.values())
print(nestedDic["grades"].values())

print(len(nestedDic["grades"]))

print(nestedDic.items())

nestedDicKeyList = list(nestedDic.keys())
# ////////////////////////////////////////////////////////////////////
# Keys of the nestedDic will be store in to list.abs 
# ///////////////////////////////////////////////////////////////////////////////

print(nestedDicKeyList)
print(type(nestedDicKeyList))

# ///////////////////////////////////////////////////////////////////////////////



# ///////////////////////////////////////////////////////////////////////////////
# we can also use nestedDic.get("Key of dicionary")
# ///////////////////////////////////////////////////////////////////////////////
print(nestedDic.get("sadkj"))     # -> None
print(nestedDic["dfs"])           # ->Error


print(nestedDic["grades"]['math'])
print(nestedDic["grades"]['math']["calculus 1"])

nestedDic["grades"]['math'] = {"cal" : 88}
print(nestedDic["grades"]['math'])

# ///////////////////////////////////////////////////////////////////////////////
# we can also use Update key word to push key and value into dictionary/.
# ///////////////////////////////////////////////////////////////////////////////
#  it also work to merge the dictionaries
nestedDic.update({"name" : "Haseeb Ullah", "current" : "Student"})

newDix = {"hobby" : "Football"}

nestedDic.update(newDix)

print(nestedDic.items())
# ///////////////////////////////////////////////////////////////////////////////



# ///////////////////////////////////////////////////////////////////////////////
# Question
# ///////////////////////////////////////////////////////////////////////////////
dictionary = {
    "table" : ["a small furniure.", "List & Fact and figures."],
    "cat" : "a small animal."
}

print(dictionary)
# ///////////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////////
# Question
# ///////////////////////////////////////////////////////////////////////////////

subject = {"python", "java", "C++", "C", "js", "python"}

print(len(subject))

# ///////////////////////////////////////////////////////////////////////////////
