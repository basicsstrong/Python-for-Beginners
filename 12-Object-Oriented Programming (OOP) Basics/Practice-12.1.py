# Define the Car class
class Car:
    def __init__(self, make, model, year):
        """
        Initializes the attributes of the Car object.
        
        Args:
            make (str): The make of the car (e.g., "Toyota").
            model (str): The model of the car (e.g., "Corolla").
            year (int): The year the car was made (e.g., 2020).
        """
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """
        Prints out the car's make, model, and year.
        """
        print(f"Car Info: {self.year} {self.make} {self.model}")

# Create an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Call the display_info method on the my_car object
my_car.display_info()
