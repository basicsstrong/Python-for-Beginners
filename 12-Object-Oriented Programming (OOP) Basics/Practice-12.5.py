import math

# Rectangle class
class Rectangle:
    def __init__(self, length, width):
        """
        Initializes the Rectangle object with length and width.
        
        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle (length * width).
        
        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width

# Circle class
class Circle:
    def __init__(self, radius):
        """
        Initializes the Circle object with the radius.
        
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle (π * radius^2).
        
        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

# Function to print area, demonstrating polymorphism
def print_area(shape):
    """
    Prints the area of any shape object (either Rectangle or Circle).
    
    Args:
        shape (object): A shape object (either Rectangle or Circle).
    """
    print(f"The area of the shape is: {shape.area()}")

# Create a Rectangle object
rectangle = Rectangle(5, 3)

# Create a Circle object
circle = Circle(4)

# Demonstrate polymorphism by passing different shape objects to print_area()
print_area(rectangle)  # Passing the Rectangle object
print_area(circle)     # Passing the Circle object
