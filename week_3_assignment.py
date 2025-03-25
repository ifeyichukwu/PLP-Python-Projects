

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