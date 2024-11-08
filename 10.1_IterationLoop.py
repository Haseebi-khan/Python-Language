n = 0
while n < 10:
    print(n+1)
    n += 1
print("Good")

while True:
    inp = input("Write done to end loop: >")
    if inp == 'done':
        print(inp)
        break
    elif inp == 'a':
        print("I m about to skip the current iteration.")
        continue
        print(a)
print("I m Done now.")

