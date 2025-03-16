# Function definition is here
def printme( str ):
    "This prints a passed string into this function"
    print (str)
    return;

# Now you can call the function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

def testfunction(arg):
    print ("ID inside the function:", id(arg))

var = "Hello"
print ("ID before passing:", id(var))
testfunction(var)
# ID before passing: 1667297083968
# ID inside the function: 1667297083968




def testfunction(arg):
    print ("ID inside the function:", id(arg))
    arg = arg + 1
    print ("new object after increment", arg, id(arg))

var=10
print ("ID before passing:", id(var))
testfunction(var)
print ("ID after passing:", id(var))
print ("value after function call", var)

# ID before passing: 140705612629192
# ID inside the function: 140705612629192
# new object after increment 11 140705612629224
# value after function call 10
# ///////////////////////////////////////////////////

def test_function(arg):
    print ("Inside function:",arg)
    print ("ID inside the function:", id(arg))
    arg=arg.append(100)
    print ("ID inside the function after append:", id(arg))

var = [10, 20, 30, 40]
print ("ID before passing:", id(var))
test_function(var)
print ("list after function call", var)
print ("ID after passing:", id(var))


def printinfo( name, age ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )


# //////////////////////////////////////////////////////


def printinfo( name, age = 35 ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )

# ////////////////////////////////////////////////////////

# Keyword-only arguments
# Those arguments that must be specified by their name while calling the function is known as Keyword-only arguments. They are defined by placing an asterisk ("*") in the function's parameter list before any keyword-only parameters. This type of argument can only be passed to a function as a keyword argument, not a positional argument.

# Example
# In the code below, we have defined a function with three keyword-only arguments. To call this method, we need to pass keyword arguments, otherwise, we will encounter an error.

def posFun(*, num1, num2, num3):
    print(num1 * num2 * num3)   

print("Evaluating keyword-only arguments: ")
posFun(num1=6, num2=8, num3=5) 

# ////////////////////////////////////////////////////////////

# List	    ✅ Yes	✅ Yes (modifies in place)	.append(), .pop()
# Integer	❌ No	❌ No (new object created)	x = x + 1
# String	❌ No	❌ No (new object created)	s = s + "abc"
# Tuple	    ❌ No	❌ No	(1, 2, 3)


def modify_var(x):
    x = x + 10  # Create a new object
    return x  # Return the new value

num = 5
num = modify_var(num)  # Reassign the returned value
print(num)  # Output: 15

# ////////////////////////////////////////////////////////////

# z=11 is passed as a keyword argument 
# (which is allowed because z comes after /).

def posFun(x, y, /, z):
    print(x + y + z)

print("Evaluating positional-only arguments: ")
posFun(33, 22, z=11) 

# //////////////////////////////////////////////////////////////////////

def posFun(*, num1, num2, num3):
    print(num1 * num2 * num3)

print("Evaluating keyword-only arguments: ")
posFun(num1=6, num2=8, num3=5) 

# //////////////////////////////////////////////////////////////////////

# Function definition is here
def print_info( arg1, *vartuple ):
    print(id("This prints a variable passed arguments"))
    print ("Output is: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return;

def print_info2( arg1, *vartuple ):
    print(id("This prints a variable passed arguments"))
    print ("Output is: ")
    print (arg1)
    for var in arg1:
        print (var)
    return;

# Now you can call printinfo function
something = [23,43,5,65,34]

print_info( 10 )
print_info( 70, 60, 50 )
print_info2( something )

# //////////////////////////////////////////////////////////////////////

def Sum(x,y):
    z = x + y
    return z
a,b, = 2,4
print("a = {}, b = {}, a + b = {}.".format(a,b, Sum(a,b)))

# //////////////////////////////////////////////////////////////////////

def myfunction(a: int, b: int):
   c = a+b
   return c
   
print (myfunction(10,20))
print (myfunction("Hello ", "Python"))

print ("Hello", "World", sep="-")