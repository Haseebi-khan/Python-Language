
import numpy as np

list2 = [6,5,3,3,2,43,45,34,23,12]
list3 = [43,45,34,23,12]

arr = np.array(list2)


"""
np.insert(Array, Index, Value, axis=None)
axis = 0 means Row vice addition.
axis = 1 means Coloun vice addition.
"""

newArr = np.insert(arr, 0, 2345)
 
print(newArr)

