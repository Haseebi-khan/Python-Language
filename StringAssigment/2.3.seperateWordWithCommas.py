# 14. Sort distinct words in comma-separated input.
# Write a Python program that accepts a comma-separated sequence
# of words as input and 
# prints the distinct words in sorted form (alphanumerically).

# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white, red

# ================================================================

colors_str = "red, white, black, red, green, black"

colors = colors_str.split(', ')

sortedColors = ""

for color in colors:
    for i in range(68, 68+26):
        if ord(colors[0]) == i:
            sortedColors += color + ", "
            break
    
print(sortedColors)

# ===================================================================

a = 'a'

intofa = ord(a)

print(intofa)
    
# ===============================================================
colors_str = "red, white, black, red, green, black"

colors = colors_str.split(', ')

# Get distinct words and sort them
colors = sorted(list(set(colors)))

sortedColors = ""
for color in colors:
    sortedColors += color + ", "

# Remove the trailing comma and space
sortedColors = sortedColors.rstrip(', ')

print(sortedColors)

# ==============================================================



char = 'A'
ascii_value = ord(char)
print(ascii_value)  # 65

ascii_value = 65
char = chr(ascii_value)
print(char)  # 'A'
