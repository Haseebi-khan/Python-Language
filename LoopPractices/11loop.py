# Write a while loop that simulates a countdown from 10, 
# printing each number, and then prints "Blast off!".

countdown = 10
while countdown != 0:
    print(countdown)
    countdown -= 1
    if countdown == 0:
        print("Blast off!")
