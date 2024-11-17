rork = 0
print("Before",rork)
for thing in [3,5,6,3,8,55,3]:
    rork += 1
    print(rork, " ", thing)
print("After", rork) 
print("\n\n")

found = False
for value in [45,34,54,2,2,1,43,4]:
    if value == 2222 :
        found = True
        print("value: ",value)
print(found)

largest = -1
small = None
arr = [34,3435,32,32,121]

for num in arr:
    if small is None:
        small = num
    if num > largest:
        largest = num
    if num < small:
        small = num
print("Largest Number: ",largest)
print("smallest Number: ",small)
# print(34 in arr)


a =0
b = 0.0  
print(a is  b)
