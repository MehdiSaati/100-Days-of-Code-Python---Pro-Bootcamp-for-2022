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

n1 = int(input("What's the first number: "))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from line aboe: ")
n2 = int(input("What's the second number: "))
calculation_function = operations[operation_symbol]
answer = calculation_function(n1, n2)
print(f"{n1} {operation_symbol} {n2} = {answer}")
 