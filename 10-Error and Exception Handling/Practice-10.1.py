def divide_by_input():
    """
    Prompts the user for a number and divides 10 by that number.
    Handles both ZeroDivisionError and ValueError exceptions.
    """
    try:
        # Prompt the user for input and convert it to a number
        user_input = input("Enter a number: ")
        number = float(user_input)  # Convert input to a float
        
        # Divide 10 by the number
        result = 10 / number
        print(f"10 divided by {number} is {result}")
    
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")
    
    except ValueError:
        print("Error: Please enter a valid number!")

# Example usage
if __name__ == "__main__":
    divide_by_input()

"""

The order of the except blocks matters because Python checks them sequentially from top to bottom. Here’s why ZeroDivisionError is caught first, followed by ValueError in your case:

In Python, the try block executes the code, and if an exception occurs, Python looks for the first matching except block. The exception handling mechanism works like this:

First, it checks if the exception matches the first except block.
If it doesn’t match, Python continues checking the next except block and so on.


Why catch ZeroDivisionError first?
When a user inputs 0, the operation 10 / 0 triggers a ZeroDivisionError.
Once ZeroDivisionError occurs, Python jumps directly to the corresponding except block and ignores the remaining blocks (in this case, ValueError), since it has already handled the exception.

Why catch ValueError after ZeroDivisionError?
A ValueError happens when the user inputs something that can’t be converted to a number (like letters or symbols).
The ValueError will not be triggered unless the input is something that can't be converted into a number.
Only after checking for ZeroDivisionError (if there was no zero division) will Python check for any ValueError.

Does the order matter here?
Yes! You must always catch specific exceptions before general exceptions.

For example, if you swapped the order (catching ValueError before ZeroDivisionError), it would cause issues because a ZeroDivisionError would never be caught: Python would first think the input is invalid (ValueError) and handle it without even checking for division by zero.
Key Rule:
Specific exceptions (like ZeroDivisionError) should be caught before more general exceptions (like ValueError), so that more specific problems are addressed first.
General exceptions (like ValueError) are meant to catch a wide range of errors, but they should be placed last.


"""
