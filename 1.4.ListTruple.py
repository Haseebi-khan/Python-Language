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