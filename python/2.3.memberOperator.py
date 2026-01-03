string = "Haseeb Khan"

a = "Khan" 
b = "h"
c = "beesaH"

print(a, " in string is :", "yes" if a in string else "not")
print(b, " in string is :", "yes" if b in string else "not")
print(c, " in string is :", "yes" if c in string else "not")
print(c, " in string is :", "yes" if c not in string else "not")


listOfNumbers = [10,20,30,40,50, "Haseeb Khan"]
d = 10
e = 90
f = None
g = 50
i = "s"


print(a , "in string is: ", a in listOfNumbers)
print(a , "in string is: ", a in listOfNumbers[5])
print(b , "in string is: ", b in listOfNumbers)
print(c , "in string is: ", c in listOfNumbers)
print(d , "in string is: ", d in listOfNumbers)
print(e , "in string is: ", e in listOfNumbers)
print(f , "in string is: ", f in listOfNumbers)
print(g , "in string is: ", g not in listOfNumbers)
print(i , "in string is: ", i not in listOfNumbers)




var = (10,20,30,40)
j = 10
k = 20
print ((j,k), "in", var, ":", (j,k) in var)
var = ((10,20),30,40)
j = 10
k = 20
print ((j,k), "in", var, ":", (j,k) in var)
print((var[0])[1])
