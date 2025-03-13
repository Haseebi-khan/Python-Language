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