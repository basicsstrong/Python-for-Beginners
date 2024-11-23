import math

def main():
    """
    A program to calculate the square root and factorial of a number using the math module.
    """
    print("Welcome to the Math Operations Program!")
    
    try:
        # Prompt the user to input a number
        number = int(input("Enter a non-negative integer: "))

        # Validate input
        if number < 0:
            print("Error: Factorial and square root are undefined for negative numbers.")
            return

        # Calculate square root
        sqrt_result = math.sqrt(number)
        
        # Calculate factorial
        factorial_result = math.factorial(number)
        
        # Display the results
        print("\n--- Results ---")
        print(f"Square root of {number}: {sqrt_result:.2f}")
        print(f"Factorial of {number}: {factorial_result}")

    except ValueError:
        print("Error: Please enter a valid non-negative integer.")

if __name__ == "__main__":
    main()
