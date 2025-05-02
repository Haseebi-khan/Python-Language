import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv", encoding="latin-1")

print(df)

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



# df.fillna(0, inplace=True)
df['Measurements'].fillna(df["Measurements"].mean(), inplace=True)
df['Sensor_Reading'].fillna(df["Sensor_Reading"].mean(), inplace=True)
df['Measurement_to_SensorRatio'].fillna(df["Measurement_to_SensorRatio"].mean(), inplace=True)
df['Range_Meters'].fillna(df["Range_Meters"].mean(), inplace=True)


df.describe()



