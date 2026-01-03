class Person:
    # Class variable
    species = "Human"
    
    def __init__(self, name, age):
        self.name = name           # Instance variable
        self.age = age             # Instance variable

    # Instance Method: works on object (self) level
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

    # Class Method: works on class (cls) level
    @classmethod
    def describe_species(cls):
        return f"All persons are of species: {cls.species}"

    # Static Method: utility function, doesn't care about class or object
    @staticmethod
    def is_adult(age):
        return age >= 18
    
    
    
p = Person("Haseeb", 65)

print(p.introduce())             # Instance method
print(Person.describe_species())  # Class method
print(p.describe_species())       # Class method via object

print(Person.is_adult(1))      # Static method
print(p.is_adult(22))           # Static method via object



class Car:
    name = "Toyota"
    def __init__(self, name):
        Car.name = name


c = Car("GTR")

print(c.name)

class Employee:
    id = 324
    def __init__(self,id):
        self.__class__.id = id
    
    
e = Employee(2)
print(e.id)