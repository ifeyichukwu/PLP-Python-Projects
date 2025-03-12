#Simple calculator that performs mathematical operations based on user input.

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

def sum_of_numbers(num1, num2):
    result = num1 + num2
    return result

sum_result = sum_of_numbers(num1, num2)
print(f"The result of your summation is: {sum_result}")
