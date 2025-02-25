day = 12
month = "May"
year = '2024'


print("Day Address: ", id(day))
print("Month Address: ", id(month))
print("Year Address: ", id(year))



counter = int(1)
mile = float(3.4)
miles = float(345345345.44543534)
name = str("Haseeb")
name2 = str('Khan')

print("Counter type: ",type(counter))
print("mile type: ",type(mile)) 
print("miles type: ",type(miles)) 
print("name type: ",type(name)) 
print("name2 type: ",type(name2)) 


# #############################################################

# Multiple varible assigment name

a = 10
print(a)
b = a
print(b)
c = b
print(c)
c = a
print(c)
c=id(a)
a = b = c
x,y,z = 10, 30.2,"Sting Variable"
print(c)

c = 66
print(a,b,c)
print(x,y,z)




a = b = c = 20
a is b is c
print(id(a), id(b), id(c))
print(a, b, c)

b =10
print(id(a), id(b), id(c))
print(a, b, c)



