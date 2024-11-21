string = "lahore is shut down due to smog"
nstr = string.split()
print(string)
print(nstr)


nstring = "apple;banna;organ;peach"
nsss = nstring.split()
print(nsss)
nsss = nstring.split(";")
print(nsss)

nnnnn = "From haseeb.khan@umt.edu.pk Sat 23,03,2024 09:43:33 2024"
bbb = nnnnn.split()
email = bbb[1]
pieces = email.split("@")
host = pieces[1]
print(host)


words = "His e-mail is q-lar@freecodecamp.org"
pieces = words.split()
parts = pieces[3].split("-")
n = parts[1]
print(n)
