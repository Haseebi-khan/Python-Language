import pandas as pd
import numpy as np


df = pd.read_csv(r"D:\Codes\Python\Python-Language\DataPreprocessing\nba.csv", encoding="utf-8")

# print(df.dtypes)
# print(df["Salary"].head(100))
# print(df["Salary"].max())

# Name         object
# Team         object
# Number      float64
# Position     object
# Age         float64
# Height       object
# Weight      float64
# College      object
# Salary      float64
# dtype: object

# print(df.isnull().sum())

# Name         1
# Team         1
# Number       1
# Position     1
# Age          1
# Height       1
# Weight       1
# College     85
# Salary      12
# dtype: int64

# 457            NaN             NaN     NaN      NaN   NaN    NaN     NaN   

# =================================
# first i gonna handle NAME obj.
# =================================



df.dropna(subset=['Name'], inplace=True)

# print(df['Name'].isnull().sum()) # 0

# print(df.isnull().sum())

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
# print(df.isnull().sum())

# print(df)

print(df["Salary"].max())  # 25000000.0
print(df["Salary"].min())  # 30888.0

# df['Salary'] = df['Salary'].replace((df['Salary'] > 250000), 250000)
# df['Salary'] = df['Salary'].replace((df['Salary'] < 30888), 30888)

df.loc[df['Salary'] > 2500000, 'Salary'] = 2500000
df.loc[df['Salary'] < 30888, 'Salary'] = 30888

# print(df['Salary'])



df.loc[df["College"].isnull(), "College"] = "Unknown"

# print(df.isnull().sum())
# Name         0
# Team         0
# Number       0
# Position     0
# Age          0
# Height       0
# Weight       0
# College      0
# Salary       0
# dtype: int64



# print(df.columns)
# Index(['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight',
#        'College', 'Salary'],
#       dtype='object')


df.sort_values(by=["Age", "Salary"], inplace=True, ascending=[False,False])

print(df.isnull().sum())

# Name         0
# Team         0
# Number       0
# Position     0
# Age          0
# Height       0
# Weight       0
# College      0
# Salary       0
# dtype: int64


df.to_csv(r"D:\Codes\Python\Python-Language\DataPreprocessing\nba.csv", index=False)


