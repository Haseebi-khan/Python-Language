hours = input("Enter number of Hours: ")
rate = input("Enter Rate: ")

try:
    h = float(hours)
    r = float(rate)
    if h > 40:
        print("Overtime.")
        reg = h * r
        overTpay = (h - 40.0) * (r * 0.5)
        pay = overTpay + reg
        print("Pay : ", pay) 
    else:
        print("Regular.")
        pay = float(hours) * float(rate)
        print("Pay : ", pay)
except:
    print("Number is not entered correctly.")