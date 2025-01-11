import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculation(n1, n2, operation):
    return operations[operation](n1, n2)

def continue_calculation(result, next_num, operation):
    return operations[operation](result, next_num)

while True:
    os.system('cls')
    first_number = float(input("What's the first number?:"))
    operation = input("Pick an operation:")
    second_number = float(input("What's the second number?:"))
    result = float(calculation(first_number, second_number, operation))
    decision = ""
    while decision != "y" and decision != "n":
        decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        while decision == "y":
            operation = input("Pick an operation:")
            next_number = float(input("What's the next number?:"))
            result = float(continue_calculation(result, next_number, operation))
            decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        

        

