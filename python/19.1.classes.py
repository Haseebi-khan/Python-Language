# Concept        | Python (self)                                                        | C++ (this)
# Purpose        | Refers to the current object                                         | Refers to the current object
# Syntax         | Must write self manually as the first parameter in each method.      | this is automatically available inside class methods.
# Usage          | self.name = attribute                                                | this->name = attribute (or just name)
# Passed         | Python passes self automatically when calling a method.              | C++ passes this behind the scenes.
# Is it visible? | You must write self in Python.                                       | Optional in C++ (this-> is implied).

class Student:
    name = "Haseeb Khan"
    age = 30
    id = 10    
        

s1 = Student()
print("Name: ",s1.name)
print("Age: ",s1.age)
print("ID: ",s1.id)


class Car:
    name = "Null"
    color = "Blue"
    model = "2023"
    no_ = "unknown"
    
car1 = Car()
print(car1.name)
print(car1.color)
print(car1.no_)
print(car1.model)
    
    