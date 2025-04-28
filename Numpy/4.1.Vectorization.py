import numpy as np

list1 = [34,76,43]
list2 = [10,20,30]

result = [x + y for x, y in zip(list1, list2)]
print(result)

# [44, 96, 73]

# vectorized Approuch


arr = np.array(list1)
arr2 = np.array(list2)

result2 = arr + arr2
multiple = arr * 2

print(result2)

# [44, 96, 73]
# [44 96 73]



print(multiple)


# [ 68 152  86]