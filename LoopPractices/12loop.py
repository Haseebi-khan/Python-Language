# Write a while loop to find 
# the first power of 2 greater than 1000.

num = 1
power = 0

while num <= 1000:
    power += 1
    num = 2 ** power   
    print(num)
    
print("\nlast : ",num)



