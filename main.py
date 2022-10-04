# Calculator
from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# calculate(n1, n2, func) is considered a higher-order function since it takes another function as an argument
def calculator(n1, n2, func):
    return func(n1, n2)


print(logo)
result = calculator(2, 3, divide)
print(f"2 / 3 = {result}")

# def calculate():
#     keep_calculating = True
#     print(logo)
#     num1 = float(input("What's the first number?: "))
#
#     for operator in operations:
#         print(operator)
#
#     while keep_calculating:
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("What's the next number?: "))
#
#         calculation_function = operations[operation_symbol]
#         answer = calculation_function(num1, num2)
#
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
#
# should_continue = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start a new
# calculation.: \n")
#
#         if should_continue == 'n':
#             keep_calculating = False
#             calculate()
#         else:
#             num1 = answer

# calculate()

# operation_symbol = input("Pick an operation: ")
# num3 = int(input("What's the next number?: "))

# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(first_answer, num3)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
