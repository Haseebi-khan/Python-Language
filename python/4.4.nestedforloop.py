months = ["january", "febuary", "march"]
days = ["mon", "tue", "wed"]

for month in months:
    print("Month is: ", month)
    for day in days:
        print(month, " ", day)


i = 2
while(i < 25):
    j = 2
    while(j <= (i/j)):
        if not ( i % j ): break
        j = j + 1
    if (j > i/j) : print (i, " is prime")
    i = i + 1