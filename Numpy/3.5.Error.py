import numpy as np

matrix1 = np.array([[34,76,43], [34,93,23]]) # Shape(2,3)
vector = np.array([10,20]) # Shape(2)
# newArr = matrix1 + vector
 
# print(newArr)

# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# File d:\Codes\Python\Python-Language\Numpy\3.5.Error.py:7
#       3 matrix1 = np.array([[34,76,43], [34,93,23]]) # Shape(2,3)
#       5 vector = np.array([10,20]) # Shape(2)
# ----> 7 newArr = matrix1 + vector
#       9 print(newArr)

# ValueError: operands could not be broadcast together with shapes (2,3) (2,)
# ---------------------------------------------------------------------------
# solution
# ---------------------------------------------------------------------------
# use reshaping

matrix = matrix1.reshape(3,2)

print(matrix,"\n=====================================")



newArr = matrix + vector
print(newArr)

# [[34 76]
#  [43 34]
#  [93 23]] 
# =====================================
# it had added 10 and 20 in each row
# [[ 44  96]
#  [ 53  54]
#  [103  43]]


