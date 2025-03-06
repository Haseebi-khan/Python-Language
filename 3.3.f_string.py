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