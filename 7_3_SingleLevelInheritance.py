class Car:
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped..")
    @staticmethod
    def move():
        print("car moveing..")
        
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
    

car = ToyotaCar("Grandi")
print(car.name)     
car.start()     
car.move()     
car.stop()     






class Person:
    def __init__(self, name):
        self.name = name
        print("Person")
    
    def show(self):
        print("Name: ",self.name)
        
class Employee(Person):
    def __init__(self, id):
        self.id = id
        print("Employee")
    
class Orginazation(Employee):
    def __init__(self,Orgname):
        self.Orgname = Orgname
        print("Orginazation")


org = Orginazation("SomePy")
        
    