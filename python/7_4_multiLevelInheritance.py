
class A:
    varA = "A"

class B: 
    varB = "B"
    
class C(A,B):
    varC = "C"
    
c = C()
print(c.varA)
print(c.varB)
print(c.varC)






# Super Method

class Staff:
    def __init__(self, name):
        self.name = name
        print("Person")
    
    def show(self):
        print("Name: ",self.name)
        
class Employee():
    def __init__(self, id):
        self.id = id
        print("Employee")
    
class Orginazation(Staff,Employee):
    def __init__(self,Orgname, name, id):
        self.Orgname = Orgname
        print("Orginazation")
        
        super().__init__(name)
        Employee.__init__(self,id)
        
        
o = Orginazation("SomePy", "nobody",34)

print(o.name)
print(o.id)
print(o.Orgname)