x =5
print("Hello")

def lyrics_print():
    print("I m lambark, and i m okey.")
    print("I sleep all night and work all day.")

print("YO")
lyrics_print()
x+=2
print(x)


# Input from users
def fullname():
    fname = input("Enter your First name: ")
    lname = input("Ener your Last name: ")
    try:
        name = str(fname) + str(lname)
        print("Name: " ,name)
    except:
        print("Error in Name.")
    
big = max("hello world z.")
tiny = min("HelloWorld")

# Printing max, min character along with Fullname Function
# within Function

def checkingBoth():
    print(big)
    print(tiny)
    fullname()
    
    
# Printing the function
print(checkingBoth())
# funtion address
print(checkingBoth)
print(type(checkingBoth))

