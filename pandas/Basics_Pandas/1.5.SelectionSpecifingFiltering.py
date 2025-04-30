# select specific column
# filtering rows
# combine multiple condition
# 
# square Brackets
# boolean condition
# 
# selecting columns:
        # a series    
        # data frames   
# 
# Column = df["column name"]
# Column = df["column name","Multiple Columns"]
# 
# filtering Rows
# 
# 
# based on single condition
# filter_row = df[df["Column Names"] operator Value]
# 
# based on Multi condition 
# filter_row = df[(df["Column Names"] operator Value) and more]


import pandas as pd
df = pd.read_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv", encoding="latin-1")


# This does not create a copy, but rather a view (or reference) to the "Measurements" column of the DataFrame. This means:
# If you modify measurements, it can affect the original df["Measurements"] column unless certain operations cause it to become a copy internally.

print(df.columns)

measurements = df["Measurements"]

print(measurements)

# 0      49.671415
# 1            inf
# 2      64.768854
# 3     152.302986
# 4           -inf
# 5     -23.413696
# 6     157.921282
# 7            NaN
# 8     -46.947439
# 9      54.256004
# 10           NaN
# 11    -46.572975
# 12     24.196227
# 13   -191.328024
# 14   -172.491783
# 15    -56.228753
# 16   -101.283112
# 17     31.424733
# 18    -90.802408
# 19           NaN
# Name: Measurements, dtype: float64




multiColumns = df[["ID","Measurements","Sensor_Reading"]]

print(multiColumns)

#     ID  Measurements  Sensor_Reading
# 0    1     49.671415           141.0
# 1    2           inf           160.0
# 2    3     64.768854            57.0
# 3    4    152.302986            84.0
# 4    5          -inf           130.0
# 5    6    -23.413696            99.0
# 6    7    157.921282           153.0
# 7    8           NaN           181.0
# 8    9    -46.947439            51.0
# 9   10     54.256004           183.0
# 10  11           NaN           103.0
# 11  12    -46.572975          -500.0

 
# Filtering Concepts:

low_mearement = df[df["Measurements"] < -100]
print(low_mearement)


#     ID  Measurements  Sensor_Reading Category Mixed_Info
# 4    5          -inf           130.0     BETA       10.0
# 13  14   -191.328024           103.0     BETA          7
# 14  15   -172.491783             NaN      NaN        NaN
# 16  17   -101.283112            63.0    Gamma          7




multiConditions = df[(df["Measurements"] < -100) & (df["Category"] == "Gamma")]

print(multiConditions)


# ID  Measurements  Sensor_Reading Category Mixed_Info
# 16  17   -101.283112            63.0    Gamma          7
