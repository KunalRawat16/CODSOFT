def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y. Raise an error if y is zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def display_menu():
    """Display the available operations for the calculator."""
    print("\nSimple Calculator")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    """Main function to run the calculator."""
    while True:
        display_menu()
        choice = input("Enter choice (1-5): ")

        if choice in {'1', '2', '3', '4'}:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            try:
                if choice == '1':
                    result = add(num1, num2)
                    print(f"The result of {num1} + {num2} is {result}.")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"The result of {num1} - {num2} is {result}.")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"The result of {num1} * {num2} is {result}.")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"The result of {num1} / {num2} is {result}.")
            except ValueError as e:
                print(e)
        
        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
