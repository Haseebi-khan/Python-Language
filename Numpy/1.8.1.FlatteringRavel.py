
import numpy as np

list2 = [6,5,3,3,2]
list3 = [43,45,34,23,12]

arr = np.array([list2,list3])

# ravel -> veiw
# flatten -> copy

print("Just Shows Veiw",arr.ravel(),"\n\n\n\n")
print("Create Copy of npArr" ,arr.flatten())
print("Create Copy of npArr with Tpye" ,type(arr.flatten()))


# ////////////////////  OUTPUT /////////////////////
# Just Shows Veiw [ 6  5  3  3  2 43 45 34 23 12] 
# Create Copy of npArr [ 6  5  3  3  2 43 45 34 23 12]
# Create Copy of npArr with Tpye <class 'numpy.ndarray'>
# ////////////////////  OUTPUT /////////////////////