def calculate_total_cost(quantity, price_per_unit):
    """
    Calculate the total cost with a 10% discount.

    Parameters:
        quantity (int): The number of items purchased.
        price_per_unit (float): The price of a single item.

    Returns:
        float: The total cost after applying the discount.
    """
    # Calculate the initial total cost
    total_cost = quantity * price_per_unit

    # Apply a 10% discount
    discount = total_cost * 0.10
    total_cost_after_discount = total_cost - discount

    return total_cost_after_discount


def main():
    """
    Collect user input for quantity and price, calculate total cost, 
    and display the result with a 10% discount.
    """
    print("Welcome to the Total Cost Calculator!")

    try:
        # Prompt user for the quantity of items
        quantity = int(input("Enter the quantity of items: "))

        # Prompt user for the price per unit
        price_per_unit = float(input("Enter the price per unit: "))

        # Validate that the inputs are positive
        if quantity <= 0 or price_per_unit <= 0:
            print("Error: Quantity and price must be positive values.")
            return

        # Calculate the total cost
        total_cost = calculate_total_cost(quantity, price_per_unit)

        # Display the result
        print("\n--- Receipt ---")
        print(f"Quantity: {quantity}")
        print(f"Price per unit: ${price_per_unit:.2f}")
        print(f"Total cost after 10% discount: ${total_cost:.2f}")

    except ValueError:
        print("Error: Please enter valid numeric inputs for quantity and price.")

if __name__ == "__main__":
    main()
