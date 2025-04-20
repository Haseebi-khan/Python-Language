

# Traceback (most recent call last):
#   File "d:\Codes\Python\Python-Language\6.5.FileHandlingPractice.py", line 7, in <module>
#     with open("6.5.FileHandlingPractice.py", "r+") as f:
#          ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: '6.5.FileHandlingPractice.py'
# PS D:\Codes\Python>


# 1,3,56,44,45,434,465,23,4,32,54,65,23,54,65,

list = []
with open("6.5.file.txt", "r+") as f:

    nums = f.read()
    integers = ""
    for i in range(len(nums)):
        if nums[i] == ',':
            # print(integers)
            list.append(int(integers))
            integers = ""
        else:
            integers += nums[i]
    f.close()  
      
print(list)
print(type(list[0]))


# [1, 3, 56, 44, 45, 434, 465, 23, 4, 32, 54, 65, 23, 54, 65]
# <class 'int'>




with open("6.5.file.txt", "r+") as f:
    data = f.read()
    listn = data.split(",")
    print(listn)
    print(type(listn))
    
    listn.pop()
    
    for i in range(len(listn)):
        listn[i] = int(listn[i])
        print(type(listn[i]))