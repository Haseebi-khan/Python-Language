a = 0b0101
print("a: ", a, "type: ", type(a))
b = int("0b010011",2)
print("b: ", b, "type: ", type(b))
c = bin(a)
print("c: ", c, "type: ", type(c))
d = int(c,2)
print("d: ", d, "type: ", type(d))


e = int(input("Enter Number: "),2)
print(e)
e = int(input("Enter Number: "),8)
print(e)
e = int(input("Enter Number: "),16)
print(e)
e = int(input("Enter Number: "),32)
print(e)



# e = int(input("Enter Number: "),128)
# print(e)
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# File d:\Codes\Python\Python-Language\2.7. number.py:1
# ----> 1 e = int(input("Enter Number: "),128)
#       2 print(e)

# ValueError: int() base must be >= 2 and <= 36, or 0