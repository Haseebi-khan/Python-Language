import numpy as np

list2 = [6,5,3,3,2]
list3 = [43,45,34,23,12]

arr = np.array(list2)
arr2 = np.array(list3)


print(np.vstack((arr,arr2)), "\n\n\n") #-> Vertically Stack
print(np.hstack((arr, arr2))) #-> Horizentally Stack

