# BuiltIn function 


# np.nan          -> dettect missing Value
# np.nan_to_num() -> Replace missing Value with num 
# np.isinf()      -> infinate Value Dettection 

# nan mean not a Number

import numpy as np

list1 = [34,np.nan,76,np.nan,43]
list2 = [np.nan,10,20,30,np.nan]


arr = np.array(list1)
arr2 = np.array(list2)

print(np.isnan(arr))
print(np.isnan(arr2))


# we can not directly compare np.nan with np.nan
# like      if np.isnan == np.nan

