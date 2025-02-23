fruit= [
    "organ", "something", "blahblah", "apple"
] 

for item in fruit:
    if item == "blahblah":
        continue
    else:
        print(item)

friends = ["A","B","C","D"]
for i in range(len(friends)):
    friend = friends[i]
    print("Hi ", friend)
     
    
F_F = friends + fruit

print(F_F)
print(type(F_F))
# the DIR builtIn Key word show all the different method
# we can use it on data Type.
print(dir(F_F))


stuff = list()
stuff.append('Book')
stuff.append(99)
stuff.append("cookies")
print(stuff)
fruit.sort()
print(fruit)


num = [4,2,34,2,45,564,23,78,34,76,341,32,34,45,6,3,2,2,35,7678,67]

print("Length: ",len(num))
print("Max: ",max(num))
print("Min: ",min(num))
print("Sum: ",sum(num))
print("Average: ",sum(num)/len(num))

