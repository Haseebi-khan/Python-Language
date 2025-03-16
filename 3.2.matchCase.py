value = int(input("Enter the value: "))

match value:
    case 0:
        print("Value is Zero.")
    case 4:
        print("Value is four.")
    case _ if value != 10:
        print("Value is  10")
    case _ if value != 5:
        print("Value is  5")
    case _:
        print("Nothing.")



def checkVowels(char):
    """Check if a character is a vowel.

    This function takes a single character as input and checks if it is a vowel (a, e, i, o, u).

    Args:
        char: The character to check.

    Returns:
        A string indicating whether the character is a vowel or a simple alphabet.
    """
    match char:
        case 'a' :
            return "Vowel Alphabet."
        case 'e' :
            return "Vowel Alphabet." 
        case 'i' :
            return "Vowel Alphabet." 
        case 'o' :
            return "Vowel Alphabet." 
        case 'u' :
            return "Vowel Alphabet." 
        case _ :
            return "Simple Alphabet." 

print(checkVowels(str(input("Enter the character: "))))
print(checkVowels.__doc__)
help(checkVowels)

def weekday(n):
    match n:
        case 1: 
            return "Monday"
        case 2: 
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7: 
            return "Sunday"
        case _:
            return "Invalid day number"

print(weekday(int(input("Enter the number till 7: "))))

def checkAccess(user):
    match user:
        case "admin" | "manager":
            return "Full access."
        case "user" | "customer" | "guest":
            return "Limited access."
        case _:
            return "No access."

print(checkAccess(str(input("Enter User name: "))))

