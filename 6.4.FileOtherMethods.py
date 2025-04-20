# 6.4.FileOtherMethods.py


with open("6.2.file1.txt", "r") as f:
    # Read the entire file into a string
    data = f.read()
    print("Data read from file:")
    print(data)
f.close()



# to remove the file
import os
os.remove("6.2.file1.txt")
# to remove the directory
os.rmdir("6.2.file1.txt")
# to remove the directory and all its contents
os.rmdir("6.2.file1.txt", recursive=True)