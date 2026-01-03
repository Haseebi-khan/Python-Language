
# class Keyboard2:
#     keyCount = 20   # class variable (shared)

#     def __init__(self, keyCount: int = 20):
#         self.keyCount = keyCount   # instance variable

#     def incKey(self):
#         self.keyCount += 1   # increment instance key count

#     @staticmethod
#     def showCount():
#         print("Total Keys (default class value):", Keyboard2.keyCount)


# # Create a list of objects
# k = [Keyboard2() for _ in range(6)]  # 6 keyboard objects

# # Increment keys for first 3 objects
# for obj in k[0:3]:
#     obj.incKey()

# # Call static method from first object
# k[0].showCount()

# # Print instance values
# print("Object 0 keys:", k[0].keyCount)
# print("Object 1 keys:", k[1].keyCount)
# print("Object 5 keys:", k[5].keyCount)


class Student:
    
    grade = 10
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def get_data(self):
        print("Name: ", self.name, ", Age: ", self.age,", Grade: ", self.grade)
    
    @classmethod
    def update_grade(cls, grade):
        cls.grade = grade
        
    @staticmethod
    def check_age(age):
        if age > 10:
            print("Above 10")
        else:
            print("Below 10")
        
        
s1 = Student("abc",34)
s2 = Student("xyz",45)

Student.update_grade(20)

s1.get_data()
s2.get_data()

    
    
    
        