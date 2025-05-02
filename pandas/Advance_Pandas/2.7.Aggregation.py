import pandas as pd
import numpy as np

data = {
    "name":["Haseeb", "Khan", "Numan", "sadhksa", "more"],
    "age": [43,17,17,17,45],
    "salary": [2000,5555,3333,8888,1111]
}

# Aggregation means numerical statistics
df = pd.DataFrame(data)

print("Salary Mean: ",df['salary'].mean())  # 32.4


# Aggregation by group columns

grouped = df.groupby("age")["salary"].mean()

print(grouped)

# it will create unique obj of age, then for each obj calculate the mean,

#   which shows how much 17 old employees are getting paid. soon on  
















