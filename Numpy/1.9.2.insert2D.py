
import numpy as np

list2 = [6,5,3,3,2]
list3 = [43,45,34,23,12]

arr = np.array([list2,list3])

# Now inserting a new row (must match columns)
new_row = [3, 1, 0, 0, 0]

newArr = np.insert(arr, 1, list3, axis=0)

print(newArr)

# [[ 6  5  3  3  2]
#  [43 45 34 23 12]
#  [43 45 34 23 12]]


