"""
📝 Discount Calculator Assignment
Author: Oluwalayomi Jesuloluwa

This program defines a function `calculate_discount` that applies a discount
to a given price if the discount percentage is 20% or higher. Otherwise,
it returns the original price.

Steps:
1. Define the calculate_discount function.
2. Prompt the user for the original price and discount percentage.
3. Apply the discount if eligible.
4. Print the final price.
"""

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after discount if discount is 20% or higher,
               otherwise the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


# --- Main program ---
# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"Discount applied! Final price: ${final_price:.2f}")
else:
    print(f"No discount applied. Final price: ${final_price:.2f}")
