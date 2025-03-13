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

var=[10, 20, 30, 40]
print ("ID before passing:", id(var))
test_function(var)
print ("list after function call", var)


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

