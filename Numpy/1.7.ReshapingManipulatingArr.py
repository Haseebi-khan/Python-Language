

# reshaping means Converting 1d array into 2d or 3d array.
# it doesnt create copy, it only return veiw of the array.




import numpy as np

list2 = [6,5,3,3,2,4,3,45,34,23,43,12]
list3 = [43,45,34,23,12]

arr = np.array(list2)


_2dimensionalArr = arr.reshape(3,4)
print(_2dimensionalArr)


# [[ 6  5  3  3]
#  [ 2  4  3 45]
#  [34 23 43 12]]