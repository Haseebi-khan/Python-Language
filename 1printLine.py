print("Hello World!\n")
print(" ||||")
print("*haseb")

print('What is your name?')
name = input()
print(name)

x = input('Enter a number: ')
print(type(x))

x = int(input('Enter a number: '))
print(type(x))

x = 5
print('The number is ' + str(x))


# Its terminal Query for compiling Python code and runing it.
# python3 main.py



# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1:])  # Prints all elements starting from index 1

# Print out last element from areas
print(areas[-1])  # Prints the last element (9.50)

# Print out the area of the living room
print(areas[5])   # Prints the area of the living room (20.0)



# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Assume hallway, kitchen, and living room are downstairs
# Use slicing to create downstairs
downstairs = areas[:6]  # Slice from start to index 6 (exclusive)

# Assume bedroom and bathroom are upstairs
# Use slicing to create upstairs
upstairs = areas[6:]  # Slice from index 6 to the end

# Print out downstairs and upstairs
print("Downstairs:", downstairs)
print("Upstairs:", upstairs)


house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Access the room name
print(house[4][0])  # Output: bathroom

# Access the room area
print(house[4][1])  # Output: 9.50


house = {
    "hallway": 11.25,
    "kitchen": 18.0,
    "living room": 20.0,
    "bedroom": 10.75,
    "bathroom": 9.50
}

# Access the room area
print(house["bathroom"])  # Output: 9.50



# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create an explicit copy of areas
areas_copy = areas.copy()

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)


# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))  # Output: <class 'list'>

# Print out length of var1
print(len(var1))   # Output: 4

# Convert var2 to an integer: out2
out2 = int(var2)
print(out2)        # Output: 1


# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))  # Output: <class 'list'>

# Print out length of var1
print(len(var1))   # Output: 4

# Convert var2 to an integer: out2
out2 = int(var2)
print(out2)        # Output: 1



# Define the lists
first = [1, 3, 5]
second = [2, 4, 6]

# Merge the contents of first and second into a new list: full
full = first + second

# Sort full in descending order
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)



# String to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print("Original place:", place)
print("place_up:", place_up)

# Print out the number of o's in place
print("Number of o's in place:", place.count('o'))



# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))  # Output: 2

# Print out how often 9.50 appears in areas
print(areas.count(9.50))  # Output: 1



# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(7.5)  # poolhouse size
areas.append(12.0)  # garage size

# Print out areas
print("Before reversing:")
print(areas)

# Reverse the order of the elements in areas
areas.reverse()

# Print out areas
print("\nAfter reversing:")
print(areas)
