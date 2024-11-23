# Import the math library
import math

# Prompt the user for a number
number = float(input("Enter a number: "))

# Calculate the square root of the number
square_root = math.sqrt(number)

# Calculate the sine and cosine of the number
sine_value = math.sin(number)
cosine_value = math.cos(number)

# Print the results
print(f"The square root of {number} is: {square_root}")
print(f"The sine of {number} (in radians) is: {sine_value}")
print(f"The cosine of {number} (in radians) is: {cosine_value}")
