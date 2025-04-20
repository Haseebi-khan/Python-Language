# 6.4.FileOtherMethods.py


with open("6.2.file1.txt", "r") as f:
    # Read the entire file into a string
    data = f.read()
    print("Data read from file:")
    print(data)
f.close()



# to remove the file
# import os
# os.remove("6.2.file1.txt")
# to remove the directory
os.rmdir("6.2.file1.txt")
# to remove the directory and all its contents
os.rmdir("6.2.file1.txt", recursive=True)



with open("6.3.file2.txt", "r+") as f:
    f.seek(0)
    data = f.read()
    print(data)
    f.seek(0)
    f.write("Moments pass, yet beauty stays,")
    f.write("In life's quiet, simple ways.")
    f.seek(0)
    f.write("\n")
    f.write("A world of wonder, vast and free,\n")
    f.write("A timeless gift for you and me.")

    f.seek(0)
    lines = f.read()
    print(lines)
    

f.close()


with open("6.3.file2.txt", "a+") as fileWriteSignOff:
    fileWriteSignOff.seek(0)
    data = fileWriteSignOff.read()
    print(type(data))
    print(data)
    
    fileWriteSignOff.write("\n")
    fileWriteSignOff.write("\n")
    fileWriteSignOff.write("\n")
    fileWriteSignOff.write("haseeb Khan ...@gmail.com")

    fileWriteSignOff.seek(0)
    data = fileWriteSignOff.read()
    print(data)

    fileWriteSignOff.close()
    
    
    
with open("6.3.file2.txt", "r+") as f:
    data = f.read()

new_data = data.replace("...","King")
print(new_data)

f.close()



def check_for_word(word):
    with open("6.3.file2.txt", "r") as f:
        data2 = f.readlines()
        print(type(data2))
        data3 = f.readline()
        print(type(data3))
        f.seek(0)
        data = f.read()
        print(type(data))
        
        if (data.find(word) != 1):
            print("found.")
        else:
            print("Not found.")
            
        f.close()

check_for_word()
    
# output =============================>     
# <class 'list'>
# <class 'str'>
# <class 'str'>
# found.
# output =============================>


def check_for_lines(word = "You"):
    data = True
    line_no = 1
    with open("6.3.file2.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1
    return -1 
            
check_for_lines()
# output =============================>
# 5
# output =============================>
