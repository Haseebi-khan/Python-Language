import numpy as np

list1 = [34,np.nan,76,np.nan,43]
list2 = [-np.inf,10,20,30,np.inf]


arr = np.array(list1)
arr2 = np.array(list2)

print(np.isnan(arr))


#nan_to_num(array ,nan=Value)


Value = 0
cleanned_Array = np.nan_to_num(arr, nan=Value) 

print(cleanned_Array)

# [False  True False  True False]
# [34.  0. 76.  0. 43.]


print(arr2)
# or
print(np.isinf(arr2))
# [ True False False False  True]
# [-inf  10.  20.  30.  inf]


cleanned_ArrayInf = np.nan_to_num(arr2, posinf = 1000, neginf = 1)

print(cleanned_ArrayInf)

# [   1.   10.   20.   30. 1000.]