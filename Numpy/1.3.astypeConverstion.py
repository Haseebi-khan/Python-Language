# ////////////////////////////////////////////////////////////////////////////
# Through this method we can change string Data of number and then convert it into requrid Data Type.
# ////////////////////////////////////////////////////////////////////////////

import numpy as np

list2 =[6,5,3,3,2]
list3 =[43,45,34,23,12]

arr = np.array(list2)
print(arr.dtype)

# int64

floateArr = arr.astype(float)

print(floateArr.dtype)
print(floateArr)
