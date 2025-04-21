# @Static Methods: dont use self parametter (work at class level)
# @Static Methods: dont use self parametter (work at class level)



class Employee:

    def __init__(self, name: str, id: int, age: int):
        self.name = name
        self.age = age
        self.Id = id
    
    @staticmethod
    def showIdInfo(emp_id: int):
        print(emp_id)

    def empInfo(self):
        print(self.name)
        print(self.age)
        self.showIdInfo(self.Id)
        # print(name)  # NameError: name 'name' is not defined
        
    
e = Employee("Nobody", 34, 23)

e.empInfo()