import pandas as pd
# import numpy as np

df = pd.read_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv", encoding="latin-1")

print(df)

# =======================================================================
# =======================================================================
# =======================================================================

# df.dtype()
# df.shape
# df.dtype
# df.describe

# m = np.array(df["Measurements"])
# print(np.isnan(m).sum())
# # print(np.nan(m))
# m = np.nan_to_num(m, nan=(int(0)))
# print(m)
# max1 = np.max(m)
# min2 = np.min(m)
# print("Maximum Value is: ",max1)
# print("Minimum Value is: ",min2)
# m = np.nan_to_num(m, nan=(int(0)))
# m = np.nan_to_num(m, posinf=max1,neginf=min2)
# print(m)
# =======================================================================
# =======================================================================
# =======================================================================


##################     First Method     ##################


# .loc[] — Label-based indexer
# dataFrame or file.loc[RowIndex, "Column_Name"] = Value or Data
df.loc[ 4, "Measurements" ] =  0

print(df)


##################     Second Method     ##################
 
df["Range_Meters"] = df["Range_Meters"] - 100

print(df)

# OriginaldfToCheckChanges = pd.read_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv", encoding="latin-1")
 
# print(OriginaldfToCheckChanges)




# /////////////////////////////////////////////////////////////////
# //////////////////   Update Column Name /////////////////////////
# /////////////////////////////////////////////////////////////////


df.rename(columns={'B': 'Y'}, inplace=True)

