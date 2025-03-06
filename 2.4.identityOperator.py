var = (10,20,30,40)
j = 10
k = 20
# print ((j,k), "in", var, ":", (j,k) in var)
var = ((10,20),30,40)
j = 10
k = 20
# print ((j,k), "in", var, ":", (j,k) in var)
# print((var[0])[1])

var2 = list(var)

print(var is var2)

var3  = var2

var3.insert(0,(23, "Haseeb"))

print(var2 is var3)
print(var2) 
print(var3)

del var3[0]
 
print(var2)
print(var3)
