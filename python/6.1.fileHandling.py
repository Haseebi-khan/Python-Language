# # mode = "r" for read, "w" for write, "a" for append, "x" for exclusive creation
# # "r+" for read and write, "w+" for write and read, "a+" for append and read
# # objectOfFile = open("FileName.txt", "mode")  # By default, it opens in read mode
# # objectOfFile = open("FileName.txt", "r")  # By default, it opens in read mode
# # objectOfFile = open("FileName.txt", "w")  # Opens in write mode, creates a new file if it doesn't exist



# # "r" mode: Opens a file for reading. The file pointer is placed at the beginning of the file.
# # "w" mode: Opens a file for writing. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
# # "a" mode: Opens a file for appending. The file pointer is placed at the end of the file if it exists. If the file does not exist, it creates a new file.
# # "x" mode: Opens a file for exclusive creation. If the file already exists, the operation fails.
# # "r+" mode: Opens a file for both reading and writing. The file pointer is placed at the beginning of the file.
# # "w+" mode: Opens a file for both writing and reading. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
# # "a+" mode: Opens a file for both appending and reading. The file pointer is placed at the end of the file if it exists. If the file does not exist, it creates a new file.
# # "b" mode: Opens a file in binary mode. This is used for non-text files like images or audio files.
# # "t" mode: Opens a file in text mode. This is the default mode and is used for text files.
# # "U" mode: Universal newline mode. This is used to read files with different newline conventions (e.g., \n, \r\n, \r). This mode is deprecated in Python 3.
# # 

# import os

# f = open("6.2.file1.txt", "r")

# data = f.read()
# print(data)
# data2 = f.read(10)
# print(data2)
# f.close()




# file1 = open("6.2.file1.txt", "r")

# file1.seek(6) 
# line1 = file1.readline()
# print(line1, end='')
# line2 = file1.readline()
# print(line2)
# file1.seek(0)
# line3 = file1.readline()
# print(line3, end='')
# file1.close()

file1 = open("6.2.file1.txt", "r")
lines = file1.readlines()
print("Total lines in file:", len(lines))

if len(lines) >= 5:
    print("The fifth line is: ->", lines[4].strip(), "<-")
else:
    print("The file has less than 5 lines.")

file1.close()

# Output==================================================================>
# PS D:\Codes\Python\Python-Language> & "C:/Program Files/Python313/python.exe" d:/Codes/Python/Python-Language/6.1.fileHandling.py
# Total lines in file: 9
# The fifth line is: ->  <-
# Total lines in file: 9
# PS D:\Codes\Python\Python-Language> 
# ==================================================================>




file1 = open("6.2.file1.txt", "r")
lines = file1.readlines()
print("Total lines in file:", len(lines))
file1.close()