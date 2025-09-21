# 6.	Use a for loop to count how many even 
# numbers are in a given list.

list = [2,3,4,6,7,8,5,8,5,4,3]
count = 0

for i in list:
    if i % 2 == 0:
        count += 1

print(count)