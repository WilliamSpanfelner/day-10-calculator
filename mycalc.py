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
def calculate(n1, n2, func):
    return func(n1, n2)


def calculator():
    keep_calculating = True
    print(logo)

    num1 = float(input("What's the first number?: "))

    operator_string = ""
    for operator in operations:
        operator_string += operator + " "
    print(operator_string)

    while keep_calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        if num2 == 0 and operation_symbol == "/":
            print("Divisor must not be zero")
            num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        result = calculate(num1, num2, calculation_function)

        print(f"{num1} {operation_symbol} {num1} = {result}")

        should_continue = input(f"\nType 'y' to continue calculating with {result}, or type 'n' to start a new"
                                f"calculation.: \n")

        if should_continue == 'n':
            keep_calculating = False
            calculator()
        else:
            num1 = result


calculator()
