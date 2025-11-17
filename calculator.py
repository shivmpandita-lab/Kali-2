def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def main():
    print("Simple Addition and Subtraction Calculator")
    choice = input("Type + for addition, - for subtraction: ").strip()
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice == '+':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '-':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    else:
        print("Invalid operation. Please choose + or -.")

if __name__ == "__main__":
    main()
    def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def get_number(prompt):
    """Safely get a number from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")

def main():
    print("=== Simple Calculator ===")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "3":
            print("Exiting... Goodbye!")
            break

        if choice not in ["1", "2"]:
            print("❌ Invalid choice. Please try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = add(num1, num2)
            print(f"✔ Result: {num1} + {num2} = {result}")

        elif choice == "2":
            result = subtract(num1, num2)
            print(f"✔ Result: {num1} - {num2} = {result}")

if __name__ == "__main__":
    main()
    
