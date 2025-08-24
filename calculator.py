# Simple Calculator

# Functions for operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# Menu for user
print("Choose Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from user
choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Check user choice
if choice == "1":
    print("Answer =", add(num1, num2))
elif choice == "2":
    print("Answer =", subtract(num1, num2))
elif choice == "3":
    print("Answer =", multiply(num1, num2))
elif choice == "4":
    print("Answer =", divide(num1, num2))
else:
    print("Invalid choice")
