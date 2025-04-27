"""
np.split()
equal


np.hsplit()
np.vsplit()

"""


import numpy as np

list2 = [6,5,3,4,3,2]
list3 = [43,45,34,23,12]

arr = np.array(list2)
arr2 = np.array(list3)



# Function      	Behavior
# np.split()     	Strict equal splits only. ❌ Error if not divisible.
# np.array_split()	Allows unequal splits. ✅

print(np.array_split(arr2, 2))

newSplit = np.split(arr, 2)
print(newSplit)