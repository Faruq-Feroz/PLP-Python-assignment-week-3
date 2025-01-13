# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    """
    This function calculates the final price after applying a discount.
    If the discount percentage is 20% or higher, the discount is applied.
    Otherwise, it returns the original price.
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompt the user to enter the original price
original_price = float(input("Enter the original price of the item: "))

# Prompt the user to enter the discount percentage
discount_percentage = float(input("Enter the discount percentage: "))

# Call the calculate_discount function and store the result
final_price = calculate_discount(original_price, discount_percentage)

# Check if the discount was applied and print the result
if final_price < original_price:
    print(f"The final price after applying the discount is: {final_price:.2f}")
else:
    print(f"No discount was applied. The original price is: {original_price:.2f}")
