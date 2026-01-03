# ===============================================
# Using Keyword-Only argument
# ===============================================

def intr(amt,*, rate):
   
   val = amt*rate/100
   return val
   
interest = intr(1000, rate=10)
print(interest)

# def intr(amt, *, rate):
#    val = amt * rate / 100
#    return val
   
# interest = intr(1000, 10)
# print(interest)


# ===============================================
# 1 positional argument but 2 were given
# ===============================================

# Positional Arguments
def intr(amt, rate):
   val = amt * rate / 100
   return val
   
interest = intr(1000, 10)
print(interest)


# Positional-Only Arguments
def myfunction(x, /, y, *, z):
   print (x, y, z)
   
myfunction(10, y=20, z=30)
myfunction(10, 20, z=30)
