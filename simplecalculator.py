def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x / y

def calculator():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("Select operation:")
    print("1. Addition") 
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter choice (1/2/3/4): ")

    if operation == '1':
        print(f"The result is: {add(num1, num2)}")
    elif operation == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif operation == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif operation == '4':
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input. Please choose a valid operation.")

if __name__ == "__main__":
    calculator()
