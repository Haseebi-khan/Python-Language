
import numpy as np

list2 = [6,5,3,3,2,43,45,34,23,12]
list3 = [43,45,34,23,12]

arr = np.array(list2)



newArr = np.append(arr, list2)
print(newArr)

# [ 6  5  3  3  2 43 45 34 23 12  6  5  3  3  2 43 45 34 23 12]
