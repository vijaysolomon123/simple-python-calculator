def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return ("Cannot divide by 0")
    return x / y


operation_dict = {
    "add": add,
    "subtract": sub,
    "multiply": mul,
    "divide": div,
}

def main():
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")

        user_input = input(":")

        if user_input == "quit":
            break

        elif user_input in operation_dict:
             num1 = float(input("Enter the first number: "))
             num2 = float(input("Enter the second number: "))
             operation=operation_dict[user_input]
             result = operation(num1,num2)
             print("Result:", result)
        else:
             print("Invalid input")

main()