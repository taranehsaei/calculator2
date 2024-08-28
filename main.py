import math

# Define the basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Define some advanced operations
def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Square root of a negative number."
    return math.sqrt(x)

def logarithm(x):
    if x <= 0:
        return "Error! Logarithm of a non-positive number."
    return math.log(x)

def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number."
    return math.factorial(int(x))

# The main calculator function
def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiate")
        print("6. Square Root")
        print("7. Logarithm")
        print("8. Factorial")
        print("9. Exit")
        
        choice = input("Enter choice (1-9): ")

        if choice == '9':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            elif choice == '5':
                print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter the number: "))
            print(f"√{num} = {square_root(num)}")

        elif choice == '7':
            num = float(input("Enter the number: "))
            print(f"log({num}) = {logarithm(num)}")

        elif choice == '8':
            num = int(input("Enter a non-negative integer: "))
            print(f"{num}! = {factorial(num)}")

        else:
            print("Invalid input. Please select a valid operation.")

if __name__ == "__main__":
    calculator()
