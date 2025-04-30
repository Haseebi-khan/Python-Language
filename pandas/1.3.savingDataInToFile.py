import pandas as pd


data ={
    "Name": ["Haseeb", "Khan","Saed"],
    "Age" : [34,56,23],
    "City" : ["lhore", "karachi", "quetta"]  
}

df = pd.DataFrame(data)

df

# we are going to save it in CVS file

# if you dont want indexs like 0,1,2,in below output use index="false"
df.to_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\1.3.dataSets.csv", index=False)

df2.read_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\1.3.dataSets.csv")

#     Name	Age	City
# 0	Haseeb	34	lhore
# 1	Khan	56	karachi
# 2	Saed	23	quetta
