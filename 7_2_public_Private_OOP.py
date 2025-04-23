

# Bypasses private restriction
# print(p._Person__status)

# everything is public.
class Account:
    def __init__(self,account,name, accpas):
        self.account = account
        self.name = name
        self.accpas = accpas
    
    
account = Account(454,"Haseeb", "sdd3435")

print("Name: ",account.name)
print("Acc no: ",account.account)
print("Pass:  ",account.accpas)


print("====================================================")


# some are private

class Person:
    def __init__(self, name, age, status, married):
        self.name = name
        self.age = age
        self.__status = status
        self.__married = married
        
    def show(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        self.__personalInfo()
    
    def __personalInfo(self):
        print("Status: ",self.__status)
        print("Married",self.__married)

p = Person("fdg",34,"alive",True)

p.show()


