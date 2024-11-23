class EmployeeAccount:
    def __init__(self, name, salary):
        """
        Initializes the EmployeeAccount object with the name and salary attributes.
        
        Args:
            name (str): The name of the employee.
            salary (float): The salary of the employee, which is kept private.
        """
        self.name = name
        self.__salary = salary  # Private attribute

    def set_salary(self, new_salary):
        """
        Updates the salary of the employee. Ensures the new salary is a positive value.
        
        Args:
            new_salary (float): The new salary to update to.
        """
        if new_salary >= 0:
            self.__salary = new_salary
            print(f"Salary has been updated to {self.__salary}.")
        else:
            print("Invalid salary. Salary cannot be negative.")

    def get_salary(self):
        """
        Returns the current salary of the employee.
        """
        return self.__salary

# Create an EmployeeAccount object
employee = EmployeeAccount("John Doe", 50000)

# Get and print the current salary
print(f"Current salary: {employee.get_salary()}")

# Update the salary
employee.set_salary(60000)

# Get and print the updated salary
print(f"Updated salary: {employee.get_salary()}")
