import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv", encoding="latin-1")

df

# NaN (not a number.)
# None (for object data)

# isnull()  
# true - NaN is missing 
# false - value is present


print(df.isnull())
print(df.isnull().sum())

# ==================================================================================

# ID                            0
# Measurements                  3
# Sensor_Reading                2
# Measurement_to_SensorRatio    5
# Category                      3
# Mixed_Info                    4
# Range_Meters                  2
# dtype: int64

# ==================================================================================

# ==================================================================================
                        # Droping Missing Values OR Outliers
# ==================================================================================

# if axis mean row or column
#if axis is Zero means ROW
#if axis is One means column
# ==================================================================================

# df.dropna(axis= 0, inplace=True)
# print(df.isnull().sum())
# print(df)

# ==================================================================================


df.replace([np.inf, -np.inf], np.nan, inplace=True)

print(df['Measurements'].mean())

for col in ["ID","Measurements"]:
    meanValue = df[col].mean()
    df[col] = df[col].fillna(meanValue)
    

df["Category"] = df["Category"].fillna(df["Category"].mode()[0])

df["Category"] = df["Category"].str.capitalize()

df


print(df['Mixed_Info'].unique())

maping = {'nine' : 9, 'True': 1, 'FIVE': 5, 'False': 0}

df['Mixed_Info'] = df['Mixed_Info'].replace(maping)

# =====================================================================
# TypeError: can only concatenate str (not "int") to str
# =====================================================================

df['Mixed_Info'] = pd.to_numeric(df['Mixed_Info'], errors='ignore')

df['Mixed_Info'] = df['Mixed_Info'].fillna(df['Mixed_Info'].mean())

df

df.describe()
df.shape
print(df.dtypes)
# =====================================================================

ID                              int64
Measurements                  float64
Sensor_Reading                float64
Measurement_to_SensorRatio    float64
Category                       object
Mixed_Info                    float64
Range_Meters                  float64
dtype: object

# =====================================================================

df.to_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv", index=False)





updated_DF = pd.read_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv", encoding="latin-1")
 

updated_DF