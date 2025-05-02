import pandas as pd
# import numpy as np

df = pd.read_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\practice_dataset.csv", encoding="latin-1")

print(df)

df.drop( columns = df["someThing"], inplace = True)

print(df)