numeber = int(input("Enter the number: "))

def recursion(value: int):
    if(value == 0 or value == 1):
        return 1
    return value * recursion(value - 1)
    
result = recursion(numeber)

print(result)


def Sum(num :int):
    if num == 0:
        return 0
    
    return num + Sum(num - 1)

print(Sum(int(input("Enter the number: "))))


def num(n :int):
    if n >= 10:
        return 0
    print(n)
    return num(n + 1)

print(num(int(input("Enter the number: "))))

def num(n :int):
    if n == 0:
        return -1
    if (n != -1):    #Just checking: if the function returns -1, does it actually return -1 or not?
        print(n)
    return num(n - 1)

print(num(int(input("Enter the number: "))))