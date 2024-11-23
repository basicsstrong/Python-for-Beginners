def validate_age(age):
    """
    Validates if the given age is valid for signing up on a website.
    The age must be at least 18.
    
    Args:
        age (int): The age of the user.
    
    Raises:
        ValueError: If the age is less than 18.
    """
    if age < 18:
        raise ValueError("You must be at least 18 to sign up!")
    else:
        print("Age is valid. You can sign up!")

# Example usage
if __name__ == "__main__":
    try:
        user_age = int(input("Enter your age: "))
        validate_age(user_age)
    except ValueError as e:
        print("Error:", e)
