# List is MUTABLE 

list3333 = [203, "hasen" , 34.23, 'x']
print(type(list3333))

# news = int[45, 32 ]
# print(type(news))

for i in range(0,2,1):
    print(list3333[i])
print("\n")
    
for i in range(len(list3333)):
    print(list3333[i], end=' ')

nelist = bytearray([65,77,85,98,86])

bytesobj = bytes(nelist)

print(bytesobj)

size = 5
value = 16
representing_bytesofmeme = bytes([value] * size)

print(representing_bytesofmeme)

import array
arr = array.array('i', [1, 2, 3, 4, 5])
view = memoryview(arr)
print(view)
id(view)

newList = ["Hello World!", 45]

# obj = list(newList)
# print(obj)

string = "Haseeb Khan"

liststr = list3333(string)

print(liststr)

del liststr[6]
print(liststr)

newTuple = tuple(string)

print(newTuple, "\n\n")
# del newTuple[6]

# print(newTuple)

list1 = list(newTuple)

del list1[6]

newTuple = tuple(list1)

print(newTuple)


string = "Khan"
tobytes = string.encode('utf-16')
print (tobytes)
string = tobytes.decode('utf-16')
print (string)
string = "\u20B9"
print (string)
tobytes = string.encode('utf-16')
print (tobytes)
string = tobytes.decode('utf-16')
print (string)





# ---------------------------------------------------------------------------

newList = [34, 56.45 , "Khan", '33']

newList.append('newString')
newList.append('99')
newList.append('299')
print(newList)
# newList.sort()
# print(newList)

newList.sort(key=str)
print("After sorting:", newList)

# ---------------------------------------------------------------------------
# Understanding how these value are sorting.
# ---------------------------------------------------------------------------
# [34, 56.45, 'Khan', '33', 'newString', '99', '299']
# After sorting: ['299', '33', 34, 56.45, '99', 'Khan', 'newString']
# ---------------------------------------------------------------------------

newList.sort(key=str,reverse=True)
print(newList)

for i in newList:
    print(type(i))

newList.append(34)
print(newList)

# ---------------------------------------------------------------------------
# we can pop value using list index.
# ---------------------------------------------------------------------------

# --------------------------------------------------------------------------
# newList.pop(34)
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# File d:\Codes\Python\Python-Language\1.4.ListTruple.py:1
# ----> 1 newList.pop(34)

# IndexError: pop index out of range
# --------------------------------------------------------------------------


tup = ("string")
print(type(tup))
# --------------------------------------------------------------------------
# <class 'str'>
# --------------------------------------------------------------------------

# comma is using must within tuple otherwise it will become string as you can seen in above code
new_tup = ("string",)
print(type(new_tup))
# --------------------------------------------------------------------------
# <class 'tuple'>
# --------------------------------------------------------------------------

# Tuple have two most used func which is tuple.index and tuple.count 

# ///////////////////////////////////////////////////////////////////////////////////////////////////
# QUESTION  1
# ///////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////

oldPlaList = ['r', 'a', 'c', 'e', 'c', 'a', 'r']

pallist = list(reversed(oldPlaList))  # This works if the built-in 'list' is intact
print("pallist:", pallist)
i = 0
pal = True
for char in oldPlaList:
    if char == pallist[i]:
        i += 1
    else:
        pal = False
        break

del pallist

if pal == False:
    print("Not palindrome.")
else:
    print("palindrome")
# ////////////////////////////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////////////////////////////
# QUESTION 2
# ///////////////////////////////////////////////////////////////////////////////////////////////////
movies = []
movie1 = movies.append(input(str("Enter the First movie name: ")))
movie2 = movies.append(input(str("Enter the second movie name: ")))
movie3 = movies.append(input(str("Enter the thrid movie name: ")))
print(movies)

# ////////////////////////////////////////////////////////////////////////////////////////////////
