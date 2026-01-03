for letter in 'Python':
    if letter != 'h':
        pass
        # print ('This is pass block')
        print ('Current Letter :', letter)
print ("Good bye!")


# while True: pass
# Ellipses  
def func1():
    # Alternative to pass
    print("above Ellipses")
    pass
    # asdas
    ...      
    print("below Ellipses")

# Works on same line too
def func2(): ...          
    # Does nothing if called
func1()                  
func2()        