# Calculator
from art import logo
print(logo)
# Add
def add(n1, n2):
    return n1+n2
# Subtract
def subtract(n1, n2):
    return n1-n2
# Multiply
def multiply(n1, n2):
    return n1*n2
# Divide
def divide(n1, n2):
    return n1/n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def clculator():
    n1 = int(input("What's the first number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        n2 = int(input("What's the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")

        con = input(f"Type 'y' to continue calcuting with {answer}, or type 'n' to start a new calculation: ")
        if con == "y":
            n1 = answer
        else:
            should_continue = False
            clculator()

clculator()