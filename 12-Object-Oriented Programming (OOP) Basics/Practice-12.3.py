# Base class Person
class Person:
    def __init__(self, name, age):
        """
        Initializes the Person object with name and age attributes.
        
        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age
    
    def introduce(self):
        """
        Prints a general introduction for the Person.
        """
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Subclass Employee that inherits from Person
class Employee(Person):
    def __init__(self, name, age, position):
        """
        Initializes the Employee object with name, age, and position attributes.
        
        Args:
            name (str): The name of the employee.
            age (int): The age of the employee.
            position (str): The job position of the employee.
        """
        # Call the constructor of the base class Person
        super().__init__(name, age)
        self.position = position
    
    def introduce(self):
        """
        Overrides the introduce method to provide a personalized introduction
        with the employee's name, age, and position.
        """
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I work as a {self.position}.")

# Create an Employee object
employee = Employee("Alexa", 30, "Software Engineer")

# Call the introduce method on the employee object
employee.introduce()
