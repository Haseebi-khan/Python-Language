# Sorting data in 1 column

# sort_values()

import pandas as pd

data = {
    
    "name":["Haseeb", "Khan", "Numan", "sadhksa"],
    "age": [43,17,34,23],
    "salary": [2000,5555,3333,8888]
}


df = pd.DataFrame(data)
df

# name	age	salary
# 0	Haseeb	43	2000
# 1	Khan	17	5555
# 2	Numan	34	3333
# 3	sadhksa	23	8888


df.sort_values(by="salary", inplace=True, ascending=True)
df

# 	name	age	salary
# 0	Haseeb	43	2000
# 2	Numan	34	3333
# 1	Khan	17	5555
# 3	sadhksa	23	8888


# 	name	age	salary
# 0	Haseeb	43	2000
# 2	Numan	34	3333
# 3	sadhksa	23	8888
# 1	Khan	17	5555


# =========================================================
                # Targeting Multi-Columns
# =========================================================

df.sort_values(by=["age", "salary"], inplace=True, ascending=[True, False])
df                                                          

# 	name	age	salary
# 1	Khan	17	5555
# 3	sadhksa	23	8888
# 2	Numan	34	3333
# 0	Haseeb	43	2000

# =========================================================




