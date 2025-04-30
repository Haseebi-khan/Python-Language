# Understanding the data set
# identifying the Problem
# planing next step


# Understand the Row and Handle the rows

import pandas as pd
df = pd.read_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv", encoding="latin-1")

print(df.head(10))
print(df.tail(10))

df.to_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv", index=False)

# Finding row and columns?
# What type of data?
# Missing places?

# info() method: 

    # number of Rows and Coloumn
    # name of Columns
    # int64 or float64 obj
    # non null counts
    # memory usage of data frame

print(df.info()) 
# ------------------------------------------------  
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 20 entries, 0 to 19
# Data columns (total 5 columns):
#  #   Column          Non-Null Count  Dtype  
# ------------------------------------------------
#  0   ID              20 non-null     int64  
#  1   Measurements    17 non-null     float64
#  2   Sensor_Reading  18 non-null     float64
#  3   Category        17 non-null     object 
#  4   Mixed_Info      16 non-null     object 
# dtypes: float64(2), int64(1), object(2)
# memory usage: 932.0+ bytes
# None
# ------------------------------------------------
print(df.describe())
# ------------------------------------------------
#              ID  Measurements  Sensor_Reading
# count  20.00000     17.000000       18.000000
# mean   10.50000           NaN      626.000000
# std     5.91608           NaN     2344.001205
# min     1.00000          -inf     -500.000000
# 25%     5.75000    -90.802408       63.250000
# 50%    10.50000    -23.413696      103.000000
# 75%    15.25000     54.256004      150.750000
# max    20.00000           inf     9999.000000
# ------------------------------------------------



# how much you are data is big 
# what are the names of the columns
# use Shape and columns


print(df.shape)
# (20, 5)

print(df.columns)
# Index(['ID', 'Measurements', 'Sensor_Reading', 'Category', 'Mixed_Info'], dtype='object')




