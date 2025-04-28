"""
np.delete(arr, index, axis = None)

flatten array
"""



import numpy as np

list2 = [6,5,3,3,2]
list3 = [43,45,34,23,12]

arr = np.array(list2)
arr2 = np.array(list3)

newArr = np.delete(arr, 0)
print(arr)
print(newArr)

# [6 5 3 3 2]
# [5 3 3 2]