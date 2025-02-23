# Body Mass Index Program
import numpy as np

height = [61.33, 73.32, 56.53, 80.0, 78.44]
weight = [56.34, 71.45, 83.45, 75.5, 65.33]

np_h = np.array(height) * 0.0254
np_w = np.array(weight) * 0.453592

bmi = np_w / np_h ** 2

print(bmi)



import numpy as np

# Assuming weight_lb and height_in lists are already defined.
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])



import numpy as np

# Assuming baseball is a predefined list of lists (each inner list could represent a player’s stats).
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)



import numpy as np

# Assuming baseball is a predefined list of lists
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49])  # Index 49 corresponds to the 50th row

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]
print(np_weight_lb)

# Print out height of 124th player
# Assuming height is in the first column (index 0)
print(np_baseball[123, 0])  # Index 123 corresponds to the 124th row



import numpy as np

# Assuming baseball and updated are predefined lists/arrays
np_baseball = np.array(baseball)
updated = np.array(updated)

# Print out the addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion (for height in meters, weight in kg, and age unchanged)
conversion = np.array([0.0254, 0.453592, 1])

# Print out the product of np_baseball and conversion
print(np_baseball * conversion)
