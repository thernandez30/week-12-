# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

#2d lists- lists inside of a list

# fruits =     ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats =      ["chicken", "fish", "turkey"]

# groceries= ["fruits", "vegetables", "meats"]

# print(groceries)
# #groceries at index 0 is fruits, 1 is vegetables, and 2 is meats
# print(groceries[0])
# #gorceries at row 0, column 1 is orange
# print(groceries[0][1])
# #groceries at row 1, column 2 is potatoes
# print(groceries[1][2])
# #groceries at row 2, column 2 is turkey
# print(groceries[2][2])
# #groceries at row 2, column 1 is fish
# print(groceries[2][1])

groceries = [["apple", "orange", "banana", "coconut"], ["celery", "carrots", "potatoes"], ["chicken", "fish", "turkey"]]

for collection in groceries:
    for food in collection: 
        print(food, end =" ")
print()

num_pad = ((1, 2, 3), (4, 5, 6), (7, 8 ,9), ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

# Print the first list.

# Print the second item from the third list.

# Use a list comprehension to extract the last item from each sub-list.

# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
