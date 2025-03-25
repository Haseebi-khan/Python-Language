# 20. Reverse string if length is a multiple of 4.
# Write a Python function to reverse a string 
# if its length is a multiple of 4.

string = "PS DCodesPythonPython-Languages."
reverseString = ""
if (len(string) % 4) == 0:
    print(string[::-1])
    
def reverse_if_multiple_of_four(s):
    """Reverse the string if its length is a multiple of 4."""
    return s[::-1] if len(s) % 4 == 0 else s

# Example usage:
string = "PS DCodesPythonPython-Language"
print(reverse_if_multiple_of_four(string))


