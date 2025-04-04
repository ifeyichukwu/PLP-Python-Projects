# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.


def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        price = price - (price * (discount_percent/100))
        return f"The discounted amount is {price}"
    else:
        return f"The Original price was {price}"

price = int(input("What is the price that you have: "))
discount_percent = int(input("What is the percentage discount to be given: "))

discount = calculate_discount(price, discount_percent)
print(discount)