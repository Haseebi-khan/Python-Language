import numpy as np

list2 = [6,5,3,3,2]
list3 = [43,45,34,23,12]

arr = np.array([list2,list3])

print("Before: ",arr, "\n\n")

newArr = np.delete(arr, 1, axis=0)
print("After: ",newArr)


# Before:  [[ 6  5  3  3  2]
#          [43 45 34 23 12]] 

# After:  [[6 5 3 3 2]]