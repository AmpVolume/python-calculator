# python-calculator
#Python-Calculator
# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract second number from first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide first number by second
def divide(a, b):
    # Check to avoid division by zero
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# Main calculator function with user interface
def calculator():
    print("Simple Python Calculator")
    while True:
        # Display menu options
        print("\nChoose operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Get user's choice
        choice = input("Enter choice (1-5): ")

        # Exit condition
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        # Validate input choice
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select 1-5.
