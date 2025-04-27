
pylist = [54,43,234,34,34,34] 
print(type(pylist))



import numpy as np
# same as C++ arraies such as one Dimensional array and two Dimensional array.
numpyArray = np.array([23,45,23,434,3,4,3,2,3,42])

print(type(numpyArray))

newArr = np.array(pylist)
print(type(newArr))

# type(shape, defualt value)

arr3 = np.array((10))  # size of array, Defualt Value.
# type(((arrayDimensionOne, arrayiemensionTwo)), defualt value).
arr4 = np.ones((2,2))
arr5 = np.zeros((3,2))
arr6 = np.full((2,1), -1)


print("array 1: ",arr3, "\n")
print("Array 4: ",arr4, "\n")
print("Array 5: ",arr5, "\n")
print("Array 6: ",arr6, "\n")

# /////////////////////////////// OutPut
# array 1:  10 

# Array 4:  [[1. 1.]
#  [1. 1.]] 

# Array 5:  [[0. 0.]
#  [0. 0.]
#  [0. 0.]] 

# Array 6:  [[-1]
#  [-1]]








# Sequensional Array

arr7 = np.arange(1,10,2)
arr7 

# array([1, 3, 5, 7, 9])


# create Identity Matrices
IDMatrice = np.eye(5)
print(IDMatrice)
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]