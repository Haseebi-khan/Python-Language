# print("Hello World")

# x = 3
# if (x == 10):
#     print(x)
# else:
#     print("Nothing")

# # Works same as if - else if - else

# if(x == 10):
#     print("First Codition")
# elif(x == 3):
#     print("Second Codition")
# elif(x == 6):
#     print("Thrid Codition")

# if x<2:
#     print("Below 2")
# elif x>=2:
#     print("Two or more")
# else:
#     print("something else");

# x = 4
# if x<2:
#         print("Below 2")
# elif x<10:
#     print("Below 10")
# elif x<20:
#     print("Below 20")
# else:
#     print("something else");
    
    
#///////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////

# astr = 'Hello Bob'
# istr = int(astra)
# print('First', istr)
# astr = '123'
# istr = int(astra)
# print("Second", istr)

#///////////////////////////////////////////////////
#///////////////////////////////////////////////////

astr = 'Hello Bob'
try:
    istr = int(astra)
except: 
    istr = -1
    
print('First', istr)
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print("Second", istr)

ask = input("Enter the number: ")
try:
    num = int(ask)
except:
    num = -1
if num >= 0:
    print("number is: ", num)
else:
    print("Number is not Correctly Entered.")

temp = "5 degrees"
cel = 0
try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
except:
    print(cel)