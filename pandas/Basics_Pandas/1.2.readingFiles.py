import pandas as pd

# Reading CVS File:

# the encoding parameter tells Python how to interpret the byte data in the file as readable characters (text)

# Encoding	Description
# utf-8   	Most common and recommended. Supports all Unicode characters.
# latin-1 	Also known as ISO-8859-1. Good for Western European languages.
# utf-16  	Unicode encoding with 2 bytes per character. Sometimes used in Windows.
# cp1252  	Windows-1252. Similar to latin-1, common in Microsoft Office files.
# ascii   	Basic English only (A-Z, 0-9, symbols). Limited, avoid unless necessary.

df = pd.read_csv(r"D:\Codes\Python\Python-Language\DatasetPractice\sales_data_sample.csv", encoding="latin-1")

df.describe()
df.head()
# df.dtypes() seriers can be readed.
df.head(2823)
print(df)



# Reading xlsx File:

df2 = pd.read_excel(r"D:\Codes\Python\Python-Language\DatasetPractice\SampleSuperstore.xlsx", ) # engine="openpyxl
df2.head(2822)

# Reading gcsfs File:
#

# Reading json File:

df3= pd.read_json(r"D:\Codes\Python\Python-Language\DatasetPractice\sample_Data.json")
df3.head()



