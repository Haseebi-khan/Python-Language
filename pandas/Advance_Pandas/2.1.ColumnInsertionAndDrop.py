
import pandas as pd
df = pd.read_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv", encoding="latin-1")


print(df)
df.info()


# Adding Column in data file

df["Range_Meters"] = df["Sensor_Reading"] * 100
print(df)


# Using Insert() method
# df.insert(location of column, "Column_Name", DATA)

df.insert(3,"Measurement_to_SensorRatio", (df['Measurements'] / df['Sensor_Reading']))

print(df)

df.to_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv", index=False)
print(df)



df.to_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv",)


df.drop(columns=["Unnamed: 0"], inplace=True)