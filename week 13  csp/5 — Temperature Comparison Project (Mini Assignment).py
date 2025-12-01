# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.
# # Prints whether it’s cold, warm, or hot using comparison operators.
temp = int(input("What is the temperature today?"))
if temp >= -10 and temp <= 50: 
    print("Ahhh! It's cold!")
elif temp >= 51 and temp <= 70:
    print("it's warm outside.")
elif temp >= 71 and temp <= 110:
    print("It's hot!")
else:
    print("Extreme temperature warning!")
# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:
