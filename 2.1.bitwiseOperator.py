a = 1 
b = 2
c = 5
d = 1

print("a & b = ", bin(a&b)) 
print("a & d = ", bin(a&d))
print("a | b = ", bin(a|b))

f = bin(a|b)

print(int(f,2))

print("a & b = ", a^d)

print("~b = ", ~b)

# if -2 == ~d:
#     print("-2 is ~b")

print(a<<2)     # 4 
print(b>>1)     # 1

# function convert int to binary and Vice verse
#it can also be convert to octal and hex
h = int("000100101",2)
print(h)
print(bin(h))
















