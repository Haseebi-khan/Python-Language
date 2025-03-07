letter = "Hey! my name is {} and I m from {}."
letter3 = "Hey! my name is {} and I m from {}."
letter2 = "Hey! my name is {1} and I m from {0}."
country = "pakistan"
name = "Haseeb"

print(letter.format(name,country))
print(letter2.format(country,name))
print(letter3.format(name,country))


# using F sting concepts
country = "pakistan"
name = "Haseeb"

msg = "My name is {name} and I m from {country}"
msg2 = f"My name is {name} and I m from {country}"
print(msg)
print(msg2)

txt = "For only {price:.2f} $dollers."
print(txt.format(price = 34.6756657))

price = 49.099999
txt = "For only {price:.2f} $dollers."
print(txt)


price = 49.099999
txt = f"For only {price:.2f} $dollers."
print(txt)

print(type(f"{2*3}"))


def greeting(details):
    match details:
        case [time, name]:
            return f'Good {time} {name}!'
        case [time, *names]:
            msg = ""
            for name in names:
                msg += f'Good {time} {name}!\n'
            # print("I m inside function: ",end=' ', msg)
            return msg

print (greeting(["Morning", "Khan"]))
print (greeting(["Afternoon","Guest"]))
print (greeting(["Evening", "haseeb", "khan", "rida"]))





def result(mark):
    match mark:
        case [name, marks] if marks > 33 and marks < 100 :
            return  f"{name} passed exam, securing {marks}."
        case [name, marks] if marks < 33 or marks > 100 :
            return  f"{name} failed exam, securing {marks}."

print(result(["Haseeb",55]))
print(result(["Haseeb",-23]))
print(result(["Haseeb",12]))
print(result(["Haseeb",200]))


def intr(details):
   match details:
      case [amt, duration] if amt < 10000:
         return amt * 10 * duration / 100
      case [amt, duration] if amt >= 10000:
         return amt * 15 * duration / 100
     
print ("Interest = ", intr([5000,5]))
print ("Interest = ", intr([15000,3]))