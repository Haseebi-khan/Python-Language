


import pandas as pd
df = pd.read_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv", encoding="latin-1")


print(df)
df.info()


# Column Insertion in data file

df["Range_Meters"] = df["Sensor_Reading"] * 100
print(df)
