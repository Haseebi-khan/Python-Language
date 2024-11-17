fruit = "banana"
middleletter = fruit[2]
print(middleletter)

x=0
for letter in fruit:
    print("x: ",x, "   letter: ",letter)
    x+=1

count = 0
for letter in fruit:
    if letter == 'a':
        count +=1
print("count: ",count)