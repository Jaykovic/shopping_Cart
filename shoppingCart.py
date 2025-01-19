def add_to_cart(item_name, price, *args, **kwargs):
    """
    Adds an item to the cart with optional discounts and details.

    Args:
        item_name (str): Name of the item.
        price (float): Price of the item.
        *args (float): Optional percentage discounts.
        **kwargs: Optional details about the item.

    Returns:
        dict: A dictionary containing the item name, final price, and details.
    """
    # Calculate the final price after applying all discounts
    final_price = price
    for discount in args:
        final_price *= (1 - discount / 100)

    # Return the processed item information
    return {
        "name": item_name,
        "final_price": round(final_price, 2),
        "details": kwargs
    }


def shopping_cart():
    """
    Simulates a shopping cart system where users can add items, apply discounts,
    and see a cart summary.
    """
    cart = []  # To store all items

    while True:
        # Get item name
        item_name = input("Enter item name (or 'done' to finish): ").strip()
        if item_name.lower() == "done":
            break

        # Get item price
        try:
            price = float(input("Enter item price: "))
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
            continue

        # Get discounts (optional)
        discounts = input("Enter discounts (if any, separated by spaces): ").strip()
        if discounts:
            discounts = [float(d) for d in discounts.split()]
        else:
            discounts = []

        # Get item details (optional)
        details_input = input("Enter item details (e.g., color=red size=large): ").strip()
        details = {}
        if details_input:
            for detail in details_input.split():
                key, value = detail.split("=")
                details[key] = value

        # Check for duplicates in the cart
        if any(item["name"] == item_name for item in cart):
            print(f"{item_name} is already in the cart. Skipping...")
            continue

        # Add the item to the cart
        item = add_to_cart(item_name, price, *discounts, **details)
        cart.append(item)
        print(f"Item added: {item_name} - Final Price: ${item['final_price']}")

    # Display cart summary
    print("\n--- Cart Summary ---")
    total_cost = 0
    for item in cart:
        details = ", ".join(f"{key}={value}" for key, value in item["details"].items())
        print(f"{item['name']} - ${item['final_price']} ({details})")
        total_cost += item["final_price"]
    print(f"Total Cost: ${round(total_cost, 2)}")


# Run the program
shopping_cart()
