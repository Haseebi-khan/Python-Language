a = None
print(a)
# none
a = 0
print(bool(a))
# flase
a = 1
print(bool(a))
#true
a = 2
print(bool(a))
# true

a = -2
print("-2: ",bool(a))

a = True
print(a)
# true
a = False
print(a)
# false

a = 2
b = 4
print(bool(a==b))
# false

print(a==b)
# false

a = None
print(bool(a))
# false

a = ()
print(bool(a))
# false

a = 0.0
print(bool(a))
# false

a = 10
print(bool(a))
# true


x = None

print("x = ", x)
print("type of x = ", type(x))

print("Conversion to integer data type")
a = int(1)     # a will be 1
b = int(2.2)   # b will be 2
c = int(float("3.3"))  # convert "3.3" to float 3.3, then to int 3
# c = int("3.3")   # c will be 3

print (a)
print (b)
print (c)

print("Conversion to floating point number")
a = float(1)     # a will be 1.0
b = float(2.2)   # b will be 2.2
c = float("3.3") # c will be 3.3

print (a)
print (b)
print (c)

print("Conversion to string")
a = str(1)     # a will be "1" 
b = str(2.2)   # b will be "2.2"
c = str("3.3") # c will be "3.3"

print (a)
print (b)
print (c)


a = int(1)     # a will be 1
b = int(2.2)   # b will be 2
c = int(float("3.3"))   # c will be 3
print (a)
print (b)
print (c)