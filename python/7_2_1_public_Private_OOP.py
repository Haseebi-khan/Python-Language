

# # Bypasses private restriction
# # print(p._Person__status)

# # everything is public.
# class Account:
#     def __init__(self,account,name, accpas):
#         self.account = account
#         self.name = name
#         self.accpas = accpas
    
    
# account = Account(454,"Haseeb", "sdd3435")

# print("Name: ",account.name)
# print("Acc no: ",account.account)
# print("Pass:  ",account.accpas)


# print("====================================================")


# # some are private

# class Person:
#     def __init__(self, name, age, status, married):
#         self.name = name
#         self.age = age
#         self.__status = status
#         self.__married = married
        
#     def show(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#         self.__personalInfo()
    
#     def __personalInfo(self):
#         print("Status: ",self.__status)
#         print("Married",self.__married)

# p = Person("fdg",34,"alive",True)

# p.show()


class Person:
    
    company = ".co"
    
    def __init__(self,nickName:str, name: str, age: int, salary: int,
                 proffesion: str, address: str, company: str):
        # Public Attributes
        self.nickName = nickName
        
        # Private Attributes
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__proffesion = proffesion
        
        # Protected Attributes
        self._company = company
        self._addres = address
        
        
    def check(self):
        print("public Company: ", self.company)
        print("protected Company: ", self._company)

    @classmethod
    def changeCompany(cls,company):
        cls.company = company  
        
        
p1 = Person("hh", "Haseeb", 65, 324,"SWE","Nill", ".co" )

print(p1.nickName)
print(p1._addres)

Person.changeCompany("Hills.co")
# ===============================
p1.check()
# output
# public Company:  Hills.co
# protected Company:  .co
# ===============================
