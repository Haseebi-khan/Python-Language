totalMarks = 100
obtainMarks = int(input("Enter Obtain marks: "))
result = ""

if obtainMarks > 75 and obtainMarks < totalMarks:
    result = "Passed with distinction        n"
elif obtainMarks < 33 and obtainMarks < totalMarks:
    result = "Failed."
else:
    result = "Pass."
print("You are ", result)


def checkDiscountRate(amount):
    if amount > 1000:
        return float(amount * 10 / 100)
    else:
        return float(0)


amount = int(input("Enter the Amount: "))
print("Current Amount is: ",amount - checkDiscountRate(amount))

def checkingDivisible(num):
    if num % 2 == 0:
        if num % 3 == 0:
            return("Number is Divisible by 2 and 3.")
        else:
            return("Number is Divisible by 2 and not 3")
    else:
        if num % 3 == 0:
            if num % 2 == 0:
                return("Number is Divisible by 3 and 2.")
            else :
                return("Number is Divisible by 3 and not 2.")

print(checkingDivisible(int(input("Enter the Number: "))))
