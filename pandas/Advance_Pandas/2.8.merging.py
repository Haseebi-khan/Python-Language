
# newdf.merge(df1, df2, on="Column_Name", how="type of join")

# how = inner, outter, left, right

import pandas as pd
import numpy as np

firstYearData = pd.DataFrame({
    "stdID": [1,2,3,4,5],
    "name":["Haseeb", "Khan", "Numan", "sadhksa", "more"],
    "age": [43,17,17,17,45],
    "marks":[540, 455, 333, 234,400]
})

secYearData = pd.DataFrame({
    "stdID": [1,3,4],
    "name":["Haseeb", "Numan", "sadhksa"],
    "age": [44,18,18],
    "marks":[501, 233, 532]
})

batch_1092 = pd.merge(firstYearData, secYearData, on="stdID", how="inner")



# print(batch_1092)

# it will print each sum and create new column 
# batch_1092["total marks"] = batch_1092["marks_x"] + batch_1092["marks_y"] 

# print(batch_1092)


#    stdID   name_x  age_x  marks_x   name_y  age_y  marks_y
# 0      1   Haseeb     43      540   Haseeb     44      501
# 1      3    Numan     17      333    Numan     18      233
# 2      4  sadhksa     17      234  sadhksa     18      532
#    stdID   name_x  age_x  marks_x   name_y  age_y  marks_y  total marks
# 0      1   Haseeb     43      540   Haseeb     44      501         1041
# 1      3    Numan     17      333    Numan     18      233          566
# 2      4  sadhksa     17      234  sadhksa     18      532          766






# ===============================================================================================
batch_1092 = pd.merge(firstYearData, secYearData, on="name", how="left")
print(batch_1092)
# ===============================================================================================
                                            # OutPut
# ===============================================================================================
#    stdID_x     name  age_x  marks_x  stdID_y  age_y  marks_y
# 0        1   Haseeb     43      540      1.0   44.0    501.0
# 1        2     Khan     17      455      NaN    NaN      NaN
# 2        3    Numan     17      333      3.0   18.0    233.0
# 3        4  sadhksa     17      234      4.0   18.0    532.0
# 4        5     more     45      400      NaN    NaN      NaN
# ===============================================================================================



# ===============================================================================================
batch_1092 = pd.merge(firstYearData, secYearData, on="name", how="right")
print(batch_1092)
# ===============================================================================================
                                            # OutPut
# ===============================================================================================
#    stdID_x     name  age_x  marks_x  stdID_y  age_y  marks_y
# 0        1   Haseeb     43      540        1     44      501
# 1        3    Numan     17      333        3     18      233
# 2        4  sadhksa     17      234        4     18      532