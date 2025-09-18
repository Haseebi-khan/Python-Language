class Person:
    name = "bbb"
    name2 = "ccc"
    
    def changeName(self,name):
        self.name = name
        
    # method to change class vars value.
    def change(self,name, name2):
        self.__class__.name = name
        self.__class__.name2 = name2
        
    @classmethod
    def changeing(cls, name1,name2,name3):
        
        print(f"{Person.name} var is going to play with {name1}")
        cls.name = name1
        print(f"{cls.name2} var is going to play with {name2}")
        cls.name2 = name2
        print(f"{cls.name} var is going to play with {name3}")
        cls.name = name3
        
       
p = Person()

print("=======================================")
p.changeName("aaa")
print(p.name)
print(Person.name)
print(Person.name2)


print("=======================================")
p.change("xyz", "abc")
p.changeName("def")
print(p.name)
print(Person.name)
print(Person.name2)

print("=======================================")

p.changeing("abc", "def", "ghi")

print("=======================================")

