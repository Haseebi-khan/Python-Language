import numpy as np
import pandas as pd

data = {
    "Time": [1,2,3,4,5,6,7],
    "values": [54,65,None,67,45,43,None]
} 

df = pd.DataFrame(data)

# before

df

# Time	values
# 0	1	54.0
# 1	2	65.0
# 2	3	NaN
# 3	4	67.0
# 4	5	45.0
# 5	6	43.0
# 6	7	NaN

df['values'] = df['values'].interpolate(method="linear")

# after

df 

# Time	values
# 0	1	54.0
# 1	2	65.0
# 2	3	66.0
# 3	4	67.0
# 4	5	45.0
# 5	6	43.0
# 6	7	43.0