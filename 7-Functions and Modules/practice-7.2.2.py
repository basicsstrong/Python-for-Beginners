import custom_module

def main():
    # Call the greet function
    custom_module.greet("Tech Enthusiast")

    # Calculate the area of a circle
    radius = float(input("Enter the radius of the circle: "))
    area = custom_module.calculate_area(radius)
    print(f"The area of the circle with radius {radius} is: {area:.2f}")

if __name__ == "__main__":
    main()
