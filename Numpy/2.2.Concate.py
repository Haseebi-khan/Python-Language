
import numpy as np

list2 = [6,5,3,3,2]
list3 = [43,45,34,23,12]

arr = np.array(list2)
arr2 = np.array(list3)

newArr = np.concatenate((arr, arr2), axis = 0)

print(newArr)


# [ 6  5  3  3  2 43 45 34 23 12]


"""
np.concate(as tuple(arr1,arr2,), axis = None)

axis = 0 -> vertically stacking
axis = 0 -> Horizental stacking

"""