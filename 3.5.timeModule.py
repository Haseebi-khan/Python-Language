import time

currentTime = time.strftime("%H : %M : %S")

print(type(currentTime))

print(currentTime)

hour = int(time.strftime("%H"))

if hour > 0 and hour < 13 :
    print("Good Morning.")
else:
    print("Good Afternoon.")















