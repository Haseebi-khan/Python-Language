class Student:
    def __init__(self, math, phy, chem, bio):
        self.math = math
        self.phy  = phy
        self.chem = chem
        self.bio  = bio
        
        # self.calculate_percentage()

    # def calculate_percentage(self):
    #     total = self.math + self.phy + self.chem + self.bio
    #     avg   = total / 4
    #     self.percentage = f"{avg}%"

    @property
    def percentage(self):
        total = self.math + self.phy + self.chem + self.bio
        avg = total / 4
        return f"{avg}%"

s = Student(45, 78, 67, 43)
print("Percentage:", s.percentage)


# =============================================================================================================


