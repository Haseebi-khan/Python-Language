# Simple calculator.
def calculator(x,y):
    inp = input("Enter operation: ")
    if inp == '+':
        suma = x + y
        print("Sum is: ",suma)
    elif inp == '*':
        mul = x * y
        print("Multiple is: ",mul)
        
    elif inp == '-':
        sub = x - y
        print("Minus is: ",sub)
    elif inp == '/':
        div = x / y
        print("Div is: ",div)
    else:
        print("Enter coorect Operation.")
    
calculator(input("Enter first num: "),input("Enter Sec num: "))

# simple func
def nameFunc():
    name = input("Enter your name: ")
    return name

print("Your name is: ",nameFunc())


first_number = int(input('Type the first number: ')) ;\
second_number = int(input('Type the second number: ')) ;\
print("The sum is: ", first_number + second_number)

