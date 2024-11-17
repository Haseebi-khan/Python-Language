string = "Haseeb Khan"

# String Sub 0 throgh 2
# Upto But not including

print(string[0:2])
print(string[0:])
print(string[:5])
print(string[0:20])
print(string[20:])
print(string[0:-1])
print(string[0:-1+1])
print(string[0:+1])
print(string[:])

name = string[0:6] + " " + " Khan "
print(name)

for letter in name:
    if letter == 'e':
        print(letter)

lowername = name.lower()
uppername = name.upper()
print("LowerName: ",lowername)
print("UpperName: ",uppername)

print(type(lowername),"\n\n\n")
# the DIR builtIn Key word show all the different method
# we can use it on data Type.
print(dir(uppername))



specific_letter = uppername.find("KHAN")
specific_letter2 = uppername.find("HASEEn")

print(specific_letter)
print(specific_letter2)

print("///////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////")

nstr = uppername.replace('HASEEB','kamel')
print("Old Upper: ",uppername)
print( "NSTR: " ,nstr)
uppername.replace('HASEEB','noman')
print("Old Upper: ",uppername)


uppername = uppername.replace('HASEEB','Rakeeb')
print("Old Upper: ",uppername)


print("///////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////")


nnstr = "      asdfgfgh        "
print(nnstr)
print(nnstr.lstrip())
print(nnstr.rstrip())
print(nnstr.strip())


nnstrn = "sadasdasd"
print(nnstrn.startswith('p'))
print(nnstrn.startswith('S'))
print(nnstrn.startswith('s'))

id_name_university = " haseeb khan hasenaskdl@umt.edu.pk 12:02:2022"
atpos = id_name_university.find('@')
print(atpos)
# how 
sspos = id_name_university.find(' ',atpos)
print(sspos)

host = id_name_university[atpos+1 : sspos]
print("Host of this domain is: ", host)



word = "bananana"
i = word.find("na")
print(i)