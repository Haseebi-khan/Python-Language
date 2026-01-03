string = "Haseeb"
print (string)
tobytes = string.encode('utf-8')
print (tobytes)
string = tobytes.decode('utf-8')
print (string)

# print(memoryview(string))

a =10
b=20

a,b=b,a #values of a and b swapped. a becomes 10, b becomes 21

print(a, "   ", b)