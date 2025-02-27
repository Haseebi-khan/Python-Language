list = [203, "hasen" , 34.23, 'x']
print(type(list))

# news = int[45, 32 ]
# print(type(news))

for i in range(0,2,1):
    print(list[i])
print("\n")
    
for i in range(len(list)):
    print(list[i], end=' ')

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

obj = list(newList)
print(obj)

string = "Haseeb Khan"

liststr = list(string)

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