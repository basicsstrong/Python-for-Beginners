def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    
    Returns:
        float: The area of the rectangle.
    """
    # Check if the inputs are valid (positive numbers)
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    
    # Calculate the area
    area = length * width

    # Return the calculated area
    return area

# Run the function as a script if executed directly
if __name__ == "__main__":
    # Prompt the user for input
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        
        # Call the function and display the result
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is: {area:.2f}")
    except ValueError as e:
        print(f"Error: {e}")