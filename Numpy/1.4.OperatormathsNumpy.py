#    within class
    # def __add__(self, num2):
    #     newReal = self.real + num2.real
    #     newImage = self.image + num2.image
    #     return Complex(newReal, newImage)


import numpy as np

list2 =[6,5,3,3,2]
list3 =[43,45,34,23,12]

arr = np.array(list2)

print(arr + 5)
print(arr * 2)
print(arr ** 2)
print(arr / 2)


