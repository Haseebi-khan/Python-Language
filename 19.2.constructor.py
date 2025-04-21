# Concept        | Python (self)                                                        | C++ (this)
# Purpose        | Refers to the current object                                         | Refers to the current object
# Syntax         | Must write self manually as the first parameter in each method.      | this is automatically available inside class methods.
# Usage          | self.name = attribute                                                | this->name = attribute (or just name)
# Passed         | Python passes self automatically when calling a method.              | C++ passes this behind the scenes.
# Is it visible? | You must write self in Python.                                       | Optional in C++ (this-> is implied).


# self word is not fix in constructor,you can named like currentObj or currentInstance etc.

class Person:

    def __init__(self ,name: str, age: int):
        self.name = name
        self.age = age
        
p = Person("Haseeb", 55)

print(p)

class Company:
    comName = "SomePy"        # class attributes 
    comManager = "Unknown"
    def __init__(self, manager ,age: int, name: str = "" ):
        self.CEO = Person(name,age)    # Obj Attributes
        self.comManager = manager  # Obj attr > Class attr


c = Company( "Pyhtonfile", age=34, name="Khan")
print(c.comName)
print(c.comManager)

print(c.CEO.name)
print(c.CEO.age)

