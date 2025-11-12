# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True


# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive).
y = 20
print(y > 50 and y < 101) # False

# Write an expression that checks if a number is NOT equal to 0 and greater than 10.
print(not(y==0 and y > 10)) # True

# Use chained comparison to check if 3 < 4 < 5.
z = 4
print(3 < z < 5) # True

# Challenge: Create a password rule using logical operators:
# Password must be at least 10 characters and have 1 digit
password = input("What is your password? ")
if len(password) >= 10 and any(char.isdigit() for char in password):
    print("Password is valid.")
else:
    print("Password is invalid. " \
    "It must be at least 10 characters long and contain at least one digit.")
