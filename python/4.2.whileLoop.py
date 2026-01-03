count=0
while count<5:
    count+=1
    print ("Iteration no. {}".format(count))

print ("End of while loop")



var = '0'
while var.isnumeric() == True:
    var = "test"
    if var.isnumeric() == True:
        print ("Your input", var)
print ("End of while loop")


var = None
while var != 1 : # This constructs an infinite loop
    var = int(input("Enter a number :"))
    print ("You entered: ", var)
print ("Good bye!")


count=0
while count<5:
    count+=1
    print ("Iteration no. {}".format(count))
else:
    print ("While loop over. Now in else block")
print ("End of while loop")


flag = 0
while (flag): print ("Given flag is really true!")
print ("Good bye!")

flag = 1
while (flag): 
    print ("Given flag is really true!")
    num = int(input("Enter 1 to stop Program."))
    if num == 2:
        break
print ("Good bye!")


# Python - Nested Loops

# while expression:
#    while expression:
#       statement(s)
#    statement(s)

i =0
while i < 10:
    print(i, end='')
    i += 1
    
    
i =10
while i > 0 :
    print(i, end='')
    i -= 1
    
    
    
# 1 4 9 16 25 36 49
    
i = 1
while i*i <= 100:
    print(i*i, end=' ')
    i += 1

    