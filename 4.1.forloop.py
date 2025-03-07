definition = """
Python for Loop with Range Objects
Python's built-in range() function returns an iterator object that streams a sequence of numbers. This object contains integers from start to stop, separated by step parameter. You can run a for loop with range as well.
Syntax
"""
total_vowels = 0
for char in definition:
    if char in 'aeiou':
        total_vowels += 1
print("Total Vowels in text: ", total_vowels)






numbers = [34,54,67,21,78,97,45,44,80,19]

print("Numbers: ",end="")

for number in numbers:
    print(number, end=" ")
print("\nNumbers which are divisible by 2")

for number in numbers:
    if number % 2 == 0:
        print(number, end=" ")

print("\nNumbers which are not divisible by 2")
for number in numbers:
    if number % 2 == 1:
        print(number, end=" ")


for number in range(0,9,1):
    print(number, end=" ")
print()
for number in range(5,10):
    print(number, end=" ")
print()
for number in range(10):
    print(number, end=" ")
print()

numbers = {10: "Ten", 20 : "twenty", 30 : "Thirty", 40 : "Forty"}

for x in numbers:
    print(x, " : ", numbers[x])






# //////////////////////////////////////////////////////////////////
#For loop to iterate between 10 to 20
for num in range(10, 20):  
   #For loop to iterate on the factors 
   for i in range(2,num): 
      #If statement to determine the first factor
      if num%i == 0:      
         #To calculate the second factor
         j=num/i          
         print ("%d equals %d * %d" % (num,i,j))
         #To move to the next number
         break 
      else:                  
         print (num, "is a prime number")
         break