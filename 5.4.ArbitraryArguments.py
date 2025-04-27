

# sum of numbers
def add(*args):
   s=0
   for x in args:
      s=s+x
   return s
result = add(10,20,30,40)
print (result)

result = add(1,2,3)
print (result)

# Accepts any number of arguments as a tuple.
def calculate(*args):
    total = sum(args)
    
    
    print("Args length: ",len(args))
    return (total/len(args))

new_result = calculate(10, 20, 30, 40)

print(new_result)
    
    
# =================================================================================
# An argument prefixed with a single asterisk * for arbitrary positional arguments.
# An argument prefixed with two asterisks ** for arbitrary keyword arguments.
# =================================================================================

# =====================
# *args → Tuple
# =====================
def addition(*args):
   
   for value in args:
      print(value, end=" ")

   return sum(args)

add_result = addition(34,45,56,76,43,23,43)

print("=",add_result)



# =====================
# **kwargs → Dictionary
# =====================
def addition(**args):
   
   print(type(args))  
    
   for key in args:
      print(key, end=" ")
    
   return sum(args.values())

add_result = addition(data1 = 34,data2 = 45,data3 = 43,data4 = 23)

print("=",add_result)



def percent(math, sci, **optional):
   print ("maths:", math)
   print ("sci:", sci)
   s=math+sci
   for k,v in optional.items():
      print ("{} : {}".format(k,v))
      s=s+v
   return s/(len(optional)+2)

result=percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)
print ("percentage:", result)