# The **raw_input()** function works similar to **input()** function. 
# Here only point is that this function was available in Python 2.7, 
# and it has been renamed to **input()** in Python 3.6

# To make these two lines appear in the same line, 
# define **end** parameter in the first print() function and 
# set it to a whitespace string " ".

name = "Haseeb Khan"
city = "Lahore"

print("Hello, ", name)
print("I m from ", city)



surname = input("Enter your surname: ")
address = input("Enter your address: ")
age = int(input("Enter your Age: ", ))
print(surname)
print(address)
print(age)

amount = float(input("Enter the amount: "))
rate = float(input("Enter the rate: "))

interest = amount * rate / 100
print("Amount: ", amount, " Interest: ", interest)

print("My Name is Khan.")
print("My Name is Khan.", end=" " "Good to see you here,")
print(" ok, and your address.")
print("NONE.")
