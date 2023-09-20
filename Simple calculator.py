# Hello all I am Tharun Kumar Reddy Chitiki.
# Today I am writing this code to perform simple basic arithmetic operations as a  part of my task given duringmy internship at codsoft.

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main program loop
while True:
    print("\nSimple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "5":
        print("See You Soon...!")
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {result}")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"Result: {result}")
    else:
        print("Invalid choice. Please select a valid option.")
