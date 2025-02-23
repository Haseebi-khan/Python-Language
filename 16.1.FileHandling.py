# open() is used for open file
# it needs two or more parameter
# open(Filename   ,   Mode)
#  S = open(something.txt , read) 
# File name is S 
xfile = open('16.2.xfile.txt')
# count = 0
# for lines in xfile:
#     print(lines)
#     count +=1
# print("Total Lines: ",count)

# inp = xfile.read()
# print(len(inp))

print("==========================================")
print("==========================================")

# print(inp[ :20])
try:
    xfile = open('16.2.xfile.txt')
    print("File have opened.")
except:
    print("This file cannot be open.")
    # QUIT is the python silent built key.Quit all the program
    # without any Trace-Back
    quit()
print(xfile)
for lines in xfile:
    lines = lines.rstrip()
    if lines.startswith("RIYADH: "):
        print(lines)

