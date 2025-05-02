
# combaining data frame vertically or Horizentally


import pandas as pd
import numpy as np

# pd.concat([df1,df2], axis=0, ignore_index=True)

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
print("Row vice:")
df_concate = pd.concat([firstYearData, secYearData], ignore_index=True)
print(df_concate)

print("Column vice:")
df_concate = pd.concat([firstYearData, secYearData], axis=1,ignore_index=True)
print(df_concate)