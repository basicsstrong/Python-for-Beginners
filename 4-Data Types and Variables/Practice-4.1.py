def main():
    """
    Collects user's name, age, and height, and prints a personalized message.
    """
    # Prompt the user for their name
    name = input("Enter your name: ")

    # Prompt the user for their age (convert to integer)
    age = int(input("Enter your age: "))

    # Prompt the user for their height in centimeters (convert to float)
    height = float(input("Enter your height in centimeters: "))

    # Print a personalized message
    print("\n--- Personalized Message ---")
    print(f"Hello, {name}!")
    print(f"You are {age} years old and {height:.1f} cm tall.")
    
    # Provide an additional fun fact based on the information
    years_until_100 = 100 - age
    print(f"Did you know? You'll turn 100 in {years_until_100} years!")

if __name__ == "__main__":
    main()
